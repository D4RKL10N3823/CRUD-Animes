from data.models import db, Anime

def existe_anime(titulo):
    return Anime.query.filter(Anime.titulo.ilike(titulo)).first() is not None

def crear_anime(data):
    nuevo_anime = Anime(
        titulo=data['titulo'],
        genero=data['genero'],
        episodios=data['episodios'],
        anio_lanzamaiento=data['anio_lanzamaiento'],
        descripcion=data.get('descripcion', '')
    )
    db.session.add(nuevo_anime)
    db.session.commit()
    return nuevo_anime

def obtener_todos_los_animes():
    return Anime.query.all()

def obtener_anime_por_id(anime_id):
    return Anime.query.get_or_404(anime_id)

def actualizar_animes(anime_id, data):
    anime = obtener_anime_por_id(anime_id)
    anime.titulo = data['titulo']
    anime.genero = data['genero']
    anime.episodios = data['episodios']
    anime.anio_lanzamaiento = data['anio_lanzamaiento']
    anime.descripcion = data.get('descripcion', '')
    db.session.commit()
    return anime

def eliminar_anime(anime_id):
    anime = obtener_anime_por_id(anime_id)
    db.session.delete(anime)
    db.session.commit()
    return anime

def filtrar_animes_por_genero(genero):
    return Anime.query.filter_by(genero=genero).all()