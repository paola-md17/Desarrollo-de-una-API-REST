from app import db
from datetime import datetime

class Estudiante(db.Model):
    __tablename__ = 'estudiantes'

    id = db.Column(db.Integer, primary_key=True)
    matricula = db.Column(db.String(10), unique=True, nullable=False)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    carrera = db.Column(db.String(100), nullable=False)
    semestre = db.Column(db.Integer, default=1)
    fecha_registro = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        """Convierte el objeto en un diccionario para enviarlo como JSON."""
        return {
            "id": self.id,
            "matricula": self.matricula,
            "nombre_completo": f"{self.nombre} {self.apellido}",
            "email": self.email,
            "carrera": self.carrera,
            "semestre": self.semestre
        }
        
    # Añade esto debajo de tus columnas
calificaciones = db.relationship('Calificacion', backref='estudiante', lazy=True)