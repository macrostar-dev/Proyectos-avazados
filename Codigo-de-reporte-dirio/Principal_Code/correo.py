import smtplib
from email.message import EmailMessage
import mimetypes
from pathlib import Path

SMTP_SERVER = "smtp.office365.com"
SMTP_PORT = 587
USER = "example@mail.com" #Cambiar por el correo que enviara el correo
PASSWORD = "passwonrd" #Cambiar por la contaseña de acceso



def enviar_correo_con_adjuntos(destinatario, asunto, cuerpo, ruta_archivo, cc=None):
    """
    Envía correo con adjunto y CC opcional.
    - destinatario: string o lista
    - cc: string o lista (opcional)
    """

    msg = EmailMessage()
    msg["From"] = USER

    # Permitir uno o varios destinatarios
    if isinstance(destinatario, list):
        msg["To"] = ", ".join(destinatario)
    else:
        msg["To"] = destinatario

    # Permitir uno o varios CC
    if cc:
        if isinstance(cc, list):
            msg["Cc"] = ", ".join(cc)
        else:
            msg["Cc"] = cc

    msg["Subject"] = asunto
    msg.set_content(cuerpo)

    # --- Adjuntar archivo ---
    ruta = Path(ruta_archivo)
    if ruta.exists():
        mime_type, _ = mimetypes.guess_type(ruta)
        mime_type = mime_type or "application/octet-stream"
        tipo_principal, sub_tipo = mime_type.split("/")

        with open(ruta, "rb") as f:
            msg.add_attachment(
                f.read(),
                maintype=tipo_principal,
                subtype=sub_tipo,
                filename=ruta.name
            )
    else:
        raise FileNotFoundError(f"No se encontró el archivo: {ruta_archivo}")

    # --- Enviar correo ---
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(USER, PASSWORD)
        server.send_message(msg)



