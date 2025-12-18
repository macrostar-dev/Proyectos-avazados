from reubicador import *
from filler import generar_reporte_ko_misma_carpeta
from conversor import procesar_archivo
from login import login_automatico
import time
from correo import enviar_correo_con_adjuntos
from notification import enviar_mensaje
from archivo_diario import copiar_archivo_con_fecha
from eliminador import *
from actualizador_anual import actualizacion_anual

actualizacion_anual()

login_automatico(
    url_login="link de inicio de sesion",
    usuario_texto="correo de acceso",
    password_texto="Contrasena",
    url_destino="url de acceso una parte de la web",
    url_destino2="url de acceso a un parte de la web"
)

for f in (BASE_DIR / "Reportes").glob("*"): f.unlink()
time.sleep(30)

importar_archivo_por_rango("Nombre del documento a transformar")
importar_archivo_por_rango("Nombre del documento a transformar")

procesar_archivo('Palabra a buscar en un rango', 'Nuevo nombre asignado')
procesar_archivo('Palabra a buscar en un rango', 'Nuevo nombre asignado')

generar_reporte_ko_misma_carpeta(
    archivo_origen="Reportes/(Archivo a rellenar).xlsx",
    archivo_destino="(Archivo de destino).xlsx",
    hoja_destino="(Hoja de destino)",
)
generar_reporte_ko_misma_carpeta(
    archivo_origen="Reportes/(Archivo a rellenar).xlsx",
    archivo_destino="(Archivo de destino).xlsx",
    hoja_destino="(Hoja de destino)",
)

documento=copiar_archivo_con_fecha("Documento al que se le va a asignar fecha")

enviar_correo_con_adjuntos(
    destinatario="correo de destino",
    asunto="Asunto",
    cuerpo="...",
    ruta_archivo=Path(__file__).resolve().parent.parent / f'{documento}',
    cc=["correos a notificar"]
)

eliminar_archivo_por_palabra(palabra_buscar=fecha_del_documento)
enviar_mensaje()