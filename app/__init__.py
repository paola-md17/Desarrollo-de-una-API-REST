from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from .config import DevelopmentConfig
from flask_jwt_extended import JWTManager
from flasgger import Swagger

# 1. Inicializar db fuera para que sea accesible por los modelos
db = SQLAlchemy()

def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.config['JWT_SECRET_KEY'] = 'tu_clave_secreta_utng_2026' 
    
    app.config['SWAGGER'] = {
        'title': 'Sistema Escolar UTNG API',
        'uiversion': 3,
        'description': 'Documentación oficial de la API para control escolar y tienda'
    }
    
    # 2. Inicializar extensiones
    db.init_app(app)
    swagger = Swagger(app)
    CORS(app)
    jwt = JWTManager(app)
    
    # 3. Importaciones dentro del contexto para evitar errores circulares
    with app.app_context():
        # Importar modelos
        from .models.estudiante import Estudiante
        from .models.calificacion import Calificacion
        from .models.materia import Materia 
        from .models.tienda import Producto, Venta # <-- Nuevo modelo
        
        # Importar Blueprints
        from .routes import main_bp
        from .routes.estudiantes import estudiantes_bp
        from .routes.calificaciones import calificaciones_bp
        from .routes.materias import materias_bp 
        from .routes.auth import auth_bp
        from .routes.tienda import tienda_bp # <-- Nueva ruta

        # 4. Registrar Blueprints
        app.register_blueprint(main_bp)
        app.register_blueprint(estudiantes_bp)
        app.register_blueprint(calificaciones_bp)
        app.register_blueprint(materias_bp)
        app.register_blueprint(auth_bp)
        app.register_blueprint(tienda_bp) # <-- Registro correcto

        # Crear tablas en PostgreSQL
        db.create_all()

    return app