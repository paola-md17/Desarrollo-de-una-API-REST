from flask import Blueprint, request, jsonify
from app import db
from app.models.estudiante import Estudiante
from flask_jwt_extended import jwt_required

# Definimos el blueprint con el prefijo /estudiantes
estudiantes_bp = Blueprint('estudiantes', __name__, url_prefix='/estudiantes')

@estudiantes_bp.route('/', methods=['POST'])
def registrar_estudiante():
    """
    Registrar un nuevo estudiante
    ---
    tags:
      - Estudiantes
    parameters:
      - name: body
        in: body
        required: true
        schema:
          properties:
            nombre:
              type: string
              example: "Juan Pérez"
            matricula:
              type: string
              example: "12345678"
    responses:
      201:
        description: Estudiante creado con éxito
    """
    
    try:
        datos = request.get_json()
        nuevo_estudiante = Estudiante(
            matricula=datos['matricula'],
            nombre=datos['nombre'],
            apellido=datos['apellido'],
            email=datos['email'],
            carrera=datos['carrera']
        )
        db.session.add(nuevo_estudiante)
        db.session.commit()
        return jsonify({
            "status": "success",
            "mensaje": "¡Estudiante registrado con éxito!",
            "estudiante": nuevo_estudiante.to_dict()
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"status": "error", "mensaje": str(e)}), 400

@estudiantes_bp.route('/', methods=['GET'])
def obtener_estudiantes():
    """
    Obtener la lista completa de estudiantes
    ---
    tags:
      - Estudiantes
    responses:
      200:
        description: Lista de estudiantes obtenida correctamente
        schema:
          type: array
          items:
            properties:
              id:
                type: integer
              nombre:
                type: string
              matricula:
                type: string
    """
    estudiantes = Estudiante.query.all()
    return jsonify([e.to_dict() for e in estudiantes]), 200

# --- ACTUALIZAR UN ESTUDIANTE (PUT) ---
@estudiantes_bp.route('/<int:id>', methods=['PUT'])
def actualizar_estudiante(id):
    """
    Actualizar nombre o matrícula de un estudiante
    ---
    tags:
      - Estudiantes
    parameters:
      - name: id
        in: path
        type: integer
        required: true
      - name: body
        in: body
        required: true
        schema:
          properties:
            nombre:
              type: string
              example: "Juan Pérez Modificado"
            matricula:
              type: string
              example: "87654321"
    responses:
      200:
        description: Estudiante actualizado correctamente
      404:
        description: Estudiante no encontrado
    """
    estudiante = Estudiante.query.get_or_404(id)
    datos = request.get_json()
    
    # Si en el JSON viene el campo, lo cambia; si no, deja el que ya estaba
    estudiante.nombre = datos.get('nombre', estudiante.nombre)
    estudiante.apellido = datos.get('apellido', estudiante.apellido)
    estudiante.email = datos.get('email', estudiante.email)
    estudiante.carrera = datos.get('carrera', estudiante.carrera)
    
    db.session.commit()
    return jsonify({"mensaje": "Estudiante actualizado", "estudiante": estudiante.to_dict()})

# --- ELIMINAR UN ESTUDIANTE (DELETE) ---
@estudiantes_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def eliminar_estudiante(id):
    """
    Eliminar un estudiante (Requiere Token JWT)
    ---
    tags:
      - Estudiantes
    security:
      - Bearer: []
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID del estudiante a eliminar
    responses:
      200:
        description: Estudiante eliminado con éxito
      401:
        description: No autorizado - Falta Token
      404:
        description: Estudiante no encontrado
    """
    estudiante = Estudiante.query.get_or_404(id)
    db.session.delete(estudiante)
    db.session.commit()
    return jsonify({"mensaje": f"Estudiante con ID {id} eliminado correctamente"})