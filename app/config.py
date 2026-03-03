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
    
# app/config.py

class TestingConfig(Config): # O (object) si no tienes una clase Config base
    """
    Configuración exclusiva para pruebas.
    Usa SQLite en memoria: ultra rápido y no requiere PostgreSQL.
    """
    TESTING = True
    DEBUG = False
    
    # SQLite en memoria: la BD vive solo durante los tests 
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    
    # Desactivar seguridad extra para facilitar el testeo 
    WTF_CSRF_ENABLED = False
    
    # El token JWT no expira durante las pruebas 
    JWT_ACCESS_TOKEN_EXPIRES = False