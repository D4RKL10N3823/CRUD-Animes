from flask import Flask, request, jsonify, render_template
from data.models import db
from business.services import crear_anime, existe_anime, obtener_todos_los_animes

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///animes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/animes', methods=['POST'])
def api_crear_anime():
    data = request.json
    if existe_anime(data['titulo']):
        return jsonify({'msg': 'El anime ya esta registrado'}), 400
    nuevo_anime = crear_anime(data)
    return jsonify({'msg': 'Anime creado', 'id': nuevo_anime.id}), 201

@app.route('/animes', methods=['GET'])
def api_obtener_todos_los_animes():
    animes = obtener_todos_los_animes()

    return jsonify([{
        'id': anime.id,
        'titulo': anime.titulo,
        'genero': anime.genero,
        'episodios': anime.episodios,
        'anio_lanzamaiento': anime.anio_lanzamaiento,
        'descripcion': anime.descripcion
    } for anime in animes])

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)