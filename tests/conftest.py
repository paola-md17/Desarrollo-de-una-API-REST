import pytest
from app import create_app, db as _db
from app.config import TestingConfig

from flask_jwt_extended import create_access_token

@pytest.fixture
def auth_headers(app):
    """Fixture para cuando necesites enviar un token válido"""
    with app.app_context():
        token = create_access_token(identity='admin')
        return {"Authorization": f"Bearer {token}"}

@pytest.fixture(scope="session")
def app():
    """Crea la app de Flask una sola vez para toda la sesión."""
    app = create_app(TestingConfig)
    yield app

@pytest.fixture(scope="session")
def db(app):
    """Crea las tablas en la BD de prueba y las limpia al terminar."""
    with app.app_context():
        _db.create_all()
        yield _db
        _db.drop_all()

@pytest.fixture(scope="function")
def session(db):
    """Garantiza que cada prueba sea independiente mediante un Rollback."""
    connection = db.engine.connect()
    transaction = connection.begin()
    db.session.bind = connection
    yield db.session
    db.session.remove()
    transaction.rollback()
    connection.close()

@pytest.fixture(scope="function")
def client(app):
    """Cliente HTTP para simular peticiones sin prender el servidor."""
    return app.test_client()