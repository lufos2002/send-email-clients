# Importa las bibliotecas necesarias.
import smtplib
from email.message import EmailMessage
from flask import request, jsonify
import re
# Key.

# Codigo compartido con el fronted.
key = "01am22"
# Define los datos del remitente y el servidor SMTP.
smtp_server = "smtp.hostinger.com"  # Reemplaza con tu servidor SMTP
smtp_port = 587  # El puerto puede variar según el servidor de correo
sender_email = "info@amarresdeparejas.com"
sender_password = "a@4lk752cM/6BC"


# Funciones.
# Validamos email.
def validate_email(email):
    email_pattern = re.compile(r"([a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})$")
    return bool(re.match(email_pattern, email))


# Validamos numero telefonico.
def validate_phone(phone):
    phone_regex = r"^\d{12}$"
    if re.match(phone_regex, phone):
        return True
    else:
        return False


# Función para enviar el correo electrónico.
def enviar_correo():
    # VAlidacion.
    if not request.data:
        return jsonify({"error": "Acceso denegado."}), 400

    # Recibimos los datos request POSTH y los pasamos a json
    data = request.json["data"]
    # Files (datos).

    if data["id"] != key:
        return jsonify({"error": "Acceso denegado."}), 400

    ruquied_fields = ["id", "receiveEmail", "name", "email", "phone", "contry", "case"]
    # Validamos que todos los campos esten presentes (No esten vacios o nullos).

    for field in ruquied_fields:
        if field not in data or not data[field]:
            return jsonify({"error": f"El campo '{field}' es obligatorio."}), 400

    # Validamos correo quien recibe el email.
    if not validate_email(data["receiveEmail"]) or not validate_email(data["email"]):
        return jsonify({"error": "Formato de correo electrónico no válido."}), 400

    # Validamos numero telefonico.
    if not validate_phone(data["phone"]):
        return jsonify({"error": "Número telefónico incorrecto."})

    mesagge_whatsApp = "Hola,%20somos%20la%20congregación%20amarres%20de%20parejas%20muchas%20gracias%20por%20enviarnos%20su%20consulta."  # Mensaje de whatsApp
    what_url = f"https://api.whatsapp.com/send?phone={data['phone']}&text={mesagge_whatsApp}"  # Url WhatsApp (cliente).

    # Formato formulario.
    html_content = f"""<!DOCTYPE html>
    <html lang="es">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title></title>
    </head>

<body>
    <div
        style="overflow: hidden; margin: auto; width: 100%; max-width: 900px !important; font-family: 'Trebuchet MS', Verdana, sans-serif;">
        <h2
            style="background-color: #363062; color: #d6d4da; padding-left: 10px; padding-right: 10px; padding-top: 20px; padding-bottom: 20px;">
            Nuevo Cliente</h2>
        <table style="width: 100% !important;">
            <tr>
                <td style="background-color: #435585; color: #ffffff; padding: 5px; width: 10% !important;">Nombre:</td>
                <td style="background-color: #F5E8C7; color: #363062; padding: 5px;">{data['name']}</td>
            </tr>
            <tr>
                <td style="background-color: #435585; color: #ffffff; padding: 5px; width: 10% !important;">Email:</td>
                <td style="background-color: #F5E8C7; color: #363062; padding: 5px;">{data['email']}</td>
            </tr>
            <tr>
                <td style="background-color: #435585; color: #ffffff; padding: 5px; width: 10% !important;">Teléfono:</td>
                <td style="background-color: #F5E8C7; color: #363062; padding: 5px;">{data['phone']}</td>
            </tr>
            <tr>
                <td style="background-color: #435585; color: #ffffff; padding: 5px; width: 10% !important;">País:</td>
                <td style="background-color: #F5E8C7; color: #363062; padding: 5px;">{data['contry']}</td>
            </tr>

        </table>
        <h3
            style="background-color: #363062; color: #d6d4da; padding-left: 10px; padding-right: 10px; padding-top: 20px; padding-bottom: 20px;">
            Consulta:</h3>
        <p
            style="background-color: #F5E8C7; padding-left: 5px; padding-right: 5px; padding-top: 10px; padding-bottom: 10px; color: #363062;">
            {data['case']}</p>
        <hr />
        <div style="background-color: #128c7e; padding-top: 10px; padding-left: 5px; padding-bottom: 30px;">
            <h5 style="color: #ece5dd; font-size: 18px;">Escríbale al cliente por WhatsApp</h5>
            <a href="{what_url}"
                style="background-color: #25d366 !important; padding: 10px; text-decoration: none; color: #ffffff; font-weight: bold;">Contactar</a>
        </div>
    </div>
</body>

</html> """

    try:
        # Creamos un objeto EmailMassage.
        mail = EmailMessage()
        mail[
            "from"
        ] = sender_email  # Correo que valida el envio. (info@amarresdeparejas.com)
        mail["To"] = data["receiveEmail"]  # Correo quien recibe el mensaje.
        mail["Subject"] = "Consulta – Nuevo cliente."  # Titulo del correo.
        # Adjuntamos html.
        mail.add_alternative(html_content, subtype="html")  # html formato.
        # Configuaracion SMTP
        smtp = smtplib.SMTP(smtp_server, smtp_port)  # SMTP
        smtp.starttls()
        smtp.login(
            sender_email, sender_password
        )  # Autenticamos correo de verificacion.(info@amarresdeparejas.com)
        smtp.sendmail(sender_email, data["receiveEmail"], mail.as_string())
        smtp.quit()

        # Respuesta.
        return jsonify({"felicitaciones": "Mensaje enviado exitosamente."}), 200

    except Exception as ex:
        return str(ex)


# Llama a la función enviar_correo para enviar el correo electrónico.
if __name__ == "__main__":
    resultado = enviar_correo()
