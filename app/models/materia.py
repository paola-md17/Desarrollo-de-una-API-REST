from .. import db

class Materia(db.Model):
    __tablename__ = 'materias'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False, unique=True)
    creditos = db.Column(db.Integer, default=5)
    
    # Relación: Una materia tiene muchas calificaciones
    calificaciones = db.relationship('Calificacion', backref='materia_rel', lazy=True)

    def to_dict(self):
        return {"id": self.id, "nombre": self.nombre, "creditos": self.creditos}