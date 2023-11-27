#Configuración de desarrollo.
class DevelopmentConfig():
    DEBUG=True
    #Conexion a la db.
    # MYSQL_HOST = 'localhost'
    # MYSQL_USER = 'root'
    # MYSQL_PASS = ''
    # MYSQL_DB   = 'db_zona_medios'  
    SECRET_KEY = "7c9ba6c4d12cf1151949babfcbef26cd85c6b8901cfdda982d15970e31f64ac9"
config ={
    'development': DevelopmentConfig    
}