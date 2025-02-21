from flask import Flask, request, jsonify, render_template
from data.models import db
from business.services import crear_anime, existe_anime, obtener_todos_los_animes, obtener_anime_por_id, actualizar_animes, eliminar_anime, filtrar_animes_por_genero, buscar_animes

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
    genero = request.args.get('genero')
    keyword = request.args.get('buscar')

    if genero:  
        animes = filtrar_animes_por_genero(genero)
    if keyword: 
        animes = buscar_animes(keyword) 

    animes = obtener_todos_los_animes()

    return jsonify([{
        'id': anime.id,
        'titulo': anime.titulo,
        'genero': anime.genero,
        'episodios': anime.episodios,
        'anio_lanzamaiento': anime.anio_lanzamaiento,
        'descripcion': anime.descripcion
    } for anime in animes])

@app.route('/animes/<int:anime_id>', methods=['GET'])
def api_obtener_anime(anime_id):
    anime = obtener_anime_por_id(anime_id)
    return jsonify({
        'id': anime.id,
        'titulo': anime.titulo,
        'genero': anime.genero,
        'episodios': anime.episodios,
        'anio_lanzamaiento': anime.anio_lanzamaiento,
        'descripcion': anime.descripcion
    })

@app.route('/animes/<int:anime_id>', methods=['PUT'])
def api_actualizar_anime(anime_id):
    data = request.json
    actualizar_anime = actualizar_animes(anime_id, data)
    return jsonify({'msg': 'Anime Actualizado', 'id': actualizar_anime.id})

@app.route('/animes/<int:anime_id>', methods=['DELETE'])
def api_eliminar_anime(anime_id):
    eliminar_anime(anime_id)
    return jsonify({'msg': 'Anime Eliminado'})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)