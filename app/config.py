import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY_SI_ES_MIA_PROFE_PAU", "clave-por-defecto-insegura")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL") # Solo el nombre de la variable
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True

class DevelopmentConfig(Config):
    DEBUG = True