import shutil
from pathlib import Path

# Carpeta base = padre de Principal_Code → Uadmin
BASE_DIR = Path(__file__).resolve().parent.parent
CARPETA = BASE_DIR / "Reportes"

def procesar_archivo(palabra_buscar: str, nuevo_nombre: str) -> None:
    palabra_buscar = palabra_buscar.lower().strip()

    if not CARPETA.exists():
        raise FileNotFoundError(f"❌ La carpeta de reportes no existe: {CARPETA}")

    # 1. Buscar archivo que contenga la palabra clave
    archivo_encontrado = next(
        (
            f for f in CARPETA.iterdir()
            if f.is_file() and palabra_buscar in f.name.lower()
        ),
        None
    )

    if not archivo_encontrado:
        print(f"❌ No se encontró ningún archivo que contenga: '{palabra_buscar}'")
        return

    print(f"📄 Archivo encontrado: {archivo_encontrado.name}")

    # 2. Renombrar archivo original (mismo folder)
    ruta_renombrada = CARPETA / nuevo_nombre
    archivo_encontrado.rename(ruta_renombrada)
    print(f"✔ Renombrado a: {ruta_renombrada.name}")

    # 3. Preparar ruta del Excel final
    ruta_excel = CARPETA / f"{nuevo_nombre}.xlsx"

    # 🗑 Eliminar Excel previo si existe **ANTES DEL CONVERTOR**
    if ruta_excel.exists():
        ruta_excel.unlink()
        print(f"🗑 Eliminado Excel anterior: {ruta_excel.name}")

    # 4. Crear copia con extensión .xlsx (convertor)
    shutil.copy2(ruta_renombrada, ruta_excel)
    print(f"📑 Copia creada como: {ruta_excel.name}")

    # 5. Eliminar archivo renombrado (el temporal)
    ruta_renombrada.unlink()
    print(f"🗑 Eliminado archivo temporal: {ruta_renombrada.name}")

    print("✔ Proceso terminado. Solo queda el archivo Excel final.")

# ==========================
# EJECUCIÓN DIRECTA
# ==========================


