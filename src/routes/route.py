#Rutas app.
from flask import Blueprint
from flask_cors import cross_origin

#Components.
from src.components.send_email_client import enviar_correo


r = Blueprint("r",__name__)

#home.
@r.route("/")
@cross_origin()
def home():
    return "Inicio."

#Send Email.
@r.route("/send-email", methods=["POST"])
@cross_origin()
def send_email():
     return enviar_correo()