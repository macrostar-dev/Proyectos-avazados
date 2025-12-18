import shutil
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
CARPETA_REPORTES = BASE_DIR / "Reportes"

def importar_archivo_por_rango(nombre_rango, solo_ultimo=True):
    """
    Busca en Descargas un archivo cuyo nombre CONTENGA la palabra clave.
    Luego copia el archivo a /Reportes y elimina el archivo original.
    """

    carpeta_descargas = Path.home() / "Downloads"
    CARPETA_REPORTES.mkdir(parents=True, exist_ok=True)

    palabra = nombre_rango.lower()

    # Archivos filtrados
    archivos = [
        f for f in carpeta_descargas.iterdir()
        if f.is_file() and palabra in f.name.lower()
    ]

    if not archivos:
        return []

    # Tomar solo el archivo más reciente si solo_ultimo=True
    if solo_ultimo:
        archivos = [max(archivos, key=lambda x: x.stat().st_mtime)]

    rutas_finales = []

    for archivo in archivos:
        destino = CARPETA_REPORTES / archivo.name

        # Copiar a Reportes
        shutil.copy2(str(archivo), str(destino))

        # Eliminar el archivo original
        archivo.unlink()

        rutas_finales.append(destino)

    return rutas_finales


# Ejemplo de uso:
ruta = importar_archivo_por_rango("Desamparados")
print(ruta)
