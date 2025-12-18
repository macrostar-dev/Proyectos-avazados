import shutil
from pathlib import Path
from datetime import datetime

# Carpeta base = padre de Principal_Code → Uadmin
BASE_DIR = Path(__file__).resolve().parent.parent
CARPETA_TRABAJO = BASE_DIR   # Trabajamos directo en Uadmin

def copiar_archivo_con_fecha(palabra_buscar: str):
    """
    Busca un archivo en la carpeta Uadmin (BASE_DIR) que contenga 'palabra_buscar'
    en el nombre y crea una COPIA en la misma carpeta con la fecha de hoy.

    - Fecha lógica: día/mes/año (DD/MM/YYYY)
    - En el nombre del archivo se usa: DD-MM-YYYY (sin '/')
    """

    palabra_buscar = palabra_buscar.lower().strip()

    if not CARPETA_TRABAJO.exists():
        raise FileNotFoundError(f"❌ La carpeta base no existe: {CARPETA_TRABAJO}")

    # 1. Buscar archivo que contenga la palabra clave en Uadmin
    archivo_encontrado = next(
        (
            f for f in CARPETA_TRABAJO.iterdir()
            if f.is_file() and palabra_buscar in f.name.lower()
        ),
        None
    )

    if not archivo_encontrado:
        print(f"❌ No se encontró ningún archivo que contenga: '{palabra_buscar}' en {CARPETA_TRABAJO}")
        return

    print(f"📄 Archivo encontrado: {archivo_encontrado.name}")

    # 2. Obtener fecha (día/mes/año) y versión segura para nombre de archivo
    fecha_hoy = datetime.now().strftime("%d/%m/%Y")   # formato que pediste
    fecha_para_nombre = fecha_hoy.replace("/", "-")   # para el nombre del archivo

    # 3. Armar nombre nuevo usando f-string
    nuevo_nombre = f"{archivo_encontrado.stem} {fecha_para_nombre}{archivo_encontrado.suffix}"
    ruta_copia = CARPETA_TRABAJO / nuevo_nombre

    # 4. Crear copia en la MISMA carpeta (Uadmin)
    shutil.copy2(archivo_encontrado, ruta_copia)
    print(f"📑 Copia creada como: {ruta_copia.name}")
    print(f"🗓 Fecha usada (lógica): {fecha_hoy}")

    return ruta_copia

# ==========================
# EJECUCIÓN DIRECTA (ejemplo)
# ==========================

