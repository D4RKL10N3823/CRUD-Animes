document.getElementById('formulario-anime').addEventListener('submit', async (e) => {
    e.preventDefault();
    const data = {
        titulo: document.getElementById('titulo').value,
        genero: document.getElementById('genero').value,
        episodios: document.getElementById('episodios').value,
        anio_lanzamaiento: document.getElementById('anio-lanzamiento').value,
        descripcion: document.getElementById('descripcion').value,
    };

    const response = await fetch('/animes', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data),
    });

    if (response.ok) {
        toastr.success('Anime agregado con éxito');
        cargarAnimes();
        document.getElementById('formulario-anime').reset();
    } else {
        const result = await response.json();
        toastr.error(result.msg);
    }
});

async function cargarAnimes(filters = {}) {
    const params = new URLSearchParams(filters);
    const response = await fetch(`/animes?${params.toString()}`);
    const animes = await response.json();
    const lista = document.getElementById('lista-animes');
    lista.innerHTML = '';

    if (animes.length === 0) {
        lista.innerHTML = '<p>No hay animes registrados.</p>';
        return;
    }

    animes.forEach(anime => {
        const div = document.createElement('div');
        div.classList.add('tarjeta-anime');
        div.innerHTML = `
            <h3>${anime.titulo}</h3>
            <p><strong>Género:</strong> ${anime.genero}</p>
            <p><strong>Episodios:</strong> ${anime.episodios}</p>
            <p><strong>Año:</strong> ${anime.anio_lanzamaiento}</p>
            <p>${anime.descripcion}</p>
            <div class="acciones">
                <button class="editar" onclick="editarAnime(${anime.id})">Editar</button>
                <button class="eliminar" onclick="eliminarAnime(${anime.id})">Eliminar</button>
            </div>
        `;
        lista.appendChild(div);
    });
}

cargarAnimes();