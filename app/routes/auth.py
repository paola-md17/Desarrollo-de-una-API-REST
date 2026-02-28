from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/login', methods=['POST'])
def login():
    
    """
    Inicio de sesión para obtener Token JWT
    ---
    tags:
      - Autenticación
    parameters:
      - name: body
        in: body
        required: true
        schema:
          id: Login
          required:
            - username
            - password
          properties:
            username:
              type: string
              example: admin
            password:
              type: string
              example: 1234
    responses:
      200:
        description: Token generado con éxito
      401:
        description: Credenciales incorrectas
    """
    
    datos = request.get_json()
    usuario = datos.get('username')
    password = datos.get('password')

    if usuario == 'admin' and password == '1234':
        token = create_access_token(identity=usuario)
        return jsonify({"mensaje": "Bienvenido", "token": token}), 200
    
    return jsonify({"error": "Usuario o contraseña incorrectos"}), 401