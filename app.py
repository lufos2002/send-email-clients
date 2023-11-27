#Principal.

#Import.
from flask import Flask,jsonify
from flask_cors import CORS

#Import.
# from src.routes.route import r
from src.routes.route import r
from config import config

app = Flask(__name__)
CORS(app)

app.register_blueprint(r)



#mensaje 404 error de ruta.
def error_404(error):    
    return jsonify({'error404': 'Error 404, la página no existe.'}),404


if __name__ == "__main__":
    app.config.from_object(config["development"])
    app.register_error_handler(404,error_404)
    app.run(host='0.0.0.0', port=5000)
    



