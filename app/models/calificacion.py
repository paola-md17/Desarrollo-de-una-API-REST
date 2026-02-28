from app import db
from datetime import datetime

class Calificacion(db.Model):
    __tablename__ = 'calificaciones'

    id = db.Column(db.Integer, primary_key=True)
    materia = db.Column(db.String(100), nullable=False)
    puntaje = db.Column(db.Float, nullable=False)
    fecha_evaluacion = db.Column(db.DateTime, default=datetime.utcnow)
    
    # La Llave Foránea: Conecta esta calificación con un estudiante específico
    estudiante_id = db.Column(db.Integer, db.ForeignKey('estudiantes.id'), nullable=False)
    materia_id = db.Column(db.Integer, db.ForeignKey('materias.id'), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "materia": self.materia,
            "puntaje": self.puntaje,
            "estudiante_id": self.estudiante_id
        }