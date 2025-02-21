from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Anime(db.Model):
    __tablename__ = 'animes'
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    genero = db.Column(db.String(50), nullable=False)
    episodios = db.Column(db.Integer, nullable=False)
    anio_lanzamaiento = db.Column(db.Integer, nullable=False)
    descripcion = db.Column(db.Text, nullable=True)