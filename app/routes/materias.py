from flask import Blueprint, request, jsonify
from app import db
from app.models.materia import Materia
from flask_jwt_extended import jwt_required

materias_bp = Blueprint('materias', __name__, url_prefix='/materias')

@materias_bp.route('/', methods=['POST'])
@jwt_required()
def crear_materia():
    """
    Obtener lista de todas las materias
    ---
    tags:
      - Materias
    responses:
      200:
        description: Lista de materias obtenida con éxito
    """
    datos = request.get_json()
    nueva = Materia(nombre=datos['nombre'], creditos=datos.get('creditos', 5))
    db.session.add(nueva)
    db.session.commit()
    return jsonify({"mensaje": "Materia creada", "materia": nueva.to_dict()}), 201

@materias_bp.route('/', methods=['GET'])
def listar_materias():
    """
    Ver el catálogo completo de materias disponibles
    ---
    tags:
      - Materias
    responses:
      200:
        description: Catálogo de materias obtenido
    """
    materias = Materia.query.all()
    return jsonify([m.to_dict() for m in materias]), 200

@materias_bp.route('/<int:id>', methods=['PUT'])
def editar_materia(id):
    """
    Modificar nombre o créditos de una materia
    ---
    tags:
      - Materias
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
              example: "Programación Avanzada"
            creditos:
              type: integer
              example: 10
    responses:
      200:
        description: Materia actualizada
    """
    materia = Materia.query.get_or_404(id)
    datos = request.get_json()
    
    materia.nombre = datos.get('nombre', materia.nombre)
    materia.creditos = datos.get('creditos', materia.creditos)
    
    db.session.commit()
    return jsonify({"mensaje": "Materia actualizada", "materia": {"id": materia.id, "nombre": materia.nombre}})


@materias_bp.route('/<int:id>', methods=['DELETE'])
def eliminar_materia(id):
    """
    Eliminar una materia del catálogo por su ID
    ---
    tags:
      - Materias
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Materia eliminada correctamente
      404:
        description: Materia no encontrada
    """
    materia = Materia.query.get_or_404(id)
    db.session.delete(materia)
    db.session.commit()
    return jsonify({"mensaje": f"Materia {id} eliminada correctamente"})