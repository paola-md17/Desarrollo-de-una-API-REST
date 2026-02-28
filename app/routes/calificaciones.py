from flask import Blueprint, request, jsonify
from app import db
from app.models.calificacion import Calificacion
from app.models.estudiante import Estudiante

calificaciones_bp = Blueprint('calificaciones', __name__, url_prefix='/calificaciones')

# --- ASIGNAR UNA CALIFICACIÓN (POST) ---
@calificaciones_bp.route('/', methods=['POST'])
def agregar_calificacion():
    
    """
    Asignar calificación a un estudiante en una materia
    ---
    tags:
      - Calificaciones
    parameters:
      - name: body
        in: body
        required: true
        schema:
          properties:
            puntaje:
              type: number
              example: 9.5
            estudiante_id:
              type: integer
              example: 1
            materia_id:
              type: integer
              example: 1
    responses:
      201:
        description: Calificación registrada correctamente
    """
    
    datos = request.get_json()
    
    # Verificamos que el estudiante exista antes de calificarlo
    estudiante = Estudiante.query.get(datos['estudiante_id'])
    if not estudiante:
        return jsonify({"error": "El estudiante no existe"}), 404

    nueva_calificacion = Calificacion(
        materia=datos['materia'],
        puntaje=datos['puntaje'],
        estudiante_id=datos['estudiante_id']
    )
    
    db.session.add(nueva_calificacion)
    db.session.commit()
    
    return jsonify({
        "mensaje": "Calificación registrada",
        "detalle": nueva_calificacion.to_dict()
    }), 201

# --- VER CALIFICACIONES POR ESTUDIANTE (GET) ---
@calificaciones_bp.route('/estudiante/<int:e_id>', methods=['GET'])
def ver_calificaciones(e_id):
    """
    Obtener boleta de calificaciones de un estudiante específico
    ---
    tags:
      - Calificaciones
    parameters:
      - name: e_id
        in: path
        type: integer
        required: true
        description: ID del estudiante
    responses:
      200:
        description: Lista de calificaciones del alumno
      404:
        description: El estudiante no tiene calificaciones registradas
    """
    estudiante = Estudiante.query.get_or_404(e_id)
    # Gracias a la relación, podemos acceder a 'calificaciones' directamente
    notas = [c.to_dict() for c in estudiante.calificaciones]
    
    return jsonify({
        "estudiante": f"{estudiante.nombre} {estudiante.apellido}",
        "calificaciones": notas
    }), 200
    

# --- ACTUALIZAR CALIFICACIÓN (PUT) ---
@calificaciones_bp.route('/<int:id>', methods=['PUT'])
def actualizar_calificacion(id):
    """
    Actualizar el puntaje de una calificación existente
    ---
    tags:
      - Calificaciones
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
            puntaje:
              type: number
              example: 10.0
    responses:
      200:
        description: Calificación actualizada correctamente
      404:
        description: ID de calificación no encontrado
    """
    # Buscamos la calificación por su ID propio
    calificacion = Calificacion.query.get_or_404(id)
    datos = request.get_json()
    
    # Solo permitimos actualizar la materia o el puntaje
    calificacion.materia = datos.get('materia', calificacion.materia)
    calificacion.puntaje = datos.get('puntaje', calificacion.puntaje)
    
    db.session.commit()
    return jsonify({
        "mensaje": "Calificación actualizada con éxito",
        "detalle": calificacion.to_dict()
    })

# --- ELIMINAR CALIFICACIÓN (DELETE) ---
@calificaciones_bp.route('/<int:id>', methods=['DELETE'])
def eliminar_calificacion(id):
    """
    Eliminar el registro de una calificación por su ID
    ---
    tags:
      - Calificaciones
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Calificación eliminada con éxito
      404:
        description: Registro no encontrado
    """
    calificacion = Calificacion.query.get_or_404(id)
    db.session.delete(calificacion)
    db.session.commit()
    return jsonify({"mensaje": f"Calificación con ID {id} eliminada correctamente"})
