#!/usr/bin/env python3
"""Genera index.html, avatares.html, videojuegos.html y animes.html
para Mi página web, con las imágenes reales embebidas en base64."""
import base64
import os

BASE = os.path.dirname(os.path.abspath(__file__))


def b64(path):
    ext = os.path.splitext(path)[1].lower()
    mime = "image/png" if ext == ".png" else "image/jpeg" if ext in (".jpg", ".jpeg") else "image/webp"
    with open(os.path.join(BASE, path), "rb") as f:
        return f"data:{mime};base64," + base64.b64encode(f.read()).decode("ascii")


# Todas las imágenes embebidas: marcador -> archivo.
# Un solo diccionario y un solo bucle de sustitución en fill().
IMAGE_FILES = {
    "__HERO_PHOTO__": "assets/avatars/merlin.webp",
    "__PORTFOLIO_HERO__": "assets/portfolio-hero.png",
    "__AV_TINY__": "assets/avatars-256/tiny.webp",
    "__AV_EMMANUEL__": "assets/avatars-256/emmanuel.webp",
    "__AV_FANTASMA__": "assets/avatars-256/fantasma.webp",
    "__AV_GASTLY__": "assets/avatars-256/gastly.webp",
    "__AV_MERLIN__": "assets/avatars-256/merlin.webp",
    "__AV_VELOCIRAPTOR__": "assets/avatars-256/velociraptor.webp",
    "__AV_TIRANOSAURIO__": "assets/avatars-256/tiranosaurio-rex.webp",
    "__AV_TIBURON__": "assets/avatars-256/tiburon.webp",
    "__GAME_RED_DEAD_REDEMPTION__": "assets/games/red-dead-redemption.jpg",
    "__GAME_GTA_V__": "assets/games/gta-v.jpg",
    "__GAME_MANEATER__": "assets/games/maneater.jpg",
    "__GAME_DRAGON_BALL_Z_KAKAROT__": "assets/games/dragon-ball-z-kakarot.jpg",
    "__GAME_MIDNIGHT_CLUB_3__": "assets/games/midnight-club-3.jpg",
    "__GAME_METAL_SLUG_AWAKENING__": "assets/games/metal-slug-awakening.jpg",
    "__GAME_TWISTED_METAL_3__": "assets/games/twisted-metal-3.jpg",
    "__GAME_DRAGON_BALL_LEGENDS__": "assets/games/dragon-ball-legends.jpg",
    "__GAME_POKEMON_GO__": "assets/games/pokemon-go.jpg",
    "__GAME_SUPER_SMASH_BROS__": "assets/games/super-smash-bros.jpg",
    "__GAME_KIRBYS_ADVENTURE__": "assets/games/kirbys-adventure.jpg",
    "__GAME_METAL_SLUG__": "assets/games/metal-slug.jpg",
    "__GAME_METAL_SLUG_2__": "assets/games/metal-slug-2.jpg",
    "__GAME_METAL_SLUG_X__": "assets/games/metal-slug-x.jpg",
    "__GAME_METAL_SLUG_3__": "assets/games/metal-slug-3.jpg",
    "__GAME_METAL_SLUG_4__": "assets/games/metal-slug-4.jpg",
    "__GAME_METAL_SLUG_5__": "assets/games/metal-slug-5.jpg",
    "__ANIME_DRAGON_BALL__": "assets/animes/dragon-ball.jpg",
    "__ANIME_ONE_PIECE__": "assets/animes/one-piece.jpg",
    "__ANIME_NARUTO__": "assets/animes/naruto.jpg",
    "__ANIME_BAKI__": "assets/animes/baki.jpg",
}

IMAGES = {marker: b64(path) for marker, path in IMAGE_FILES.items()}


def fill(template):
    for marker, data in IMAGES.items():
        template = template.replace(marker, data)
    return template


# (nombre, marcador de imagen, descripción, es el avatar puesto)
AVATARS = [
    ("Tiny", "__AV_TINY__",
     "Tiny es un pitbull Red Nose, musculoso y sonriente, leal y protector con su familia, con su collar rojo de picos color oro.",
     True),
    ("Emmanuel", "__AV_EMMANUEL__",
     "Emmanuel en versión avatar 3D, musculoso, con el pelo corto, shorts blancos y gotas de agua.",
     False),
    ("Fantasma", "__AV_FANTASMA__",
     "El fantasma negro es una bola oscura con brazos, rodeado de un aura de fuego morado, con ojos blancos, colmillos y boca roja, intimidante y misterioso.",
     False),
    ("Gastly", "__AV_GASTLY__",
     "El fantasma negro es una bola flotante oscura rodeada de un aura de fuego morado, intimidante y misterioso, que parece correr dejando una estela de llamas detrás. Ahora con dos colmillos y la boca roja.",
     False),
    ("Merlin", "__AV_MERLIN__",
     "Merlin es el mago más famoso de la leyenda artúrica, consejero del rey Arturo y maestro de la magia. Con su larga barba blanca, su sombrero puntiagudo y su báculo, es símbolo de sabiduría, poder y misterio.",
     False),
    ("Velociraptor", "__AV_VELOCIRAPTOR__",
     "El velociraptor fue un dinosaurio pequeño pero muy inteligente y rápido, famoso por cazar en manada y por su garra en forma de hoz en cada pie. En la cultura popular es símbolo de astucia, velocidad y trabajo en equipo.",
     False),
    ("Tiranosaurio rex", "__AV_TIRANOSAURIO__",
     "El T. rex no es un ser mitológico, pero en la cultura popular es el rey de los dinosaurios: su nombre significa &lsquo;rey lagarto tirano&rsquo; y es símbolo de fuerza y poder.",
     False),
    ("Tiburón", "__AV_TIBURON__",
     "En la mitología hawaiana, los tiburones son &lsquo;aumākua: espíritus guardianes ancestrales que protegen a las familias, guían a los pescadores en el mar y castigan a quien rompe los kapu, los tabúes sagrados del océano. En muchas culturas del Pacífico el tiburón es un dios y mensajero del mar, símbolo de fuerza, respeto y protección: no se le teme solo como depredador, se le honra como guardián.",
     False),
]

# (nombre, enlace, marcador de imagen)
GAMES = [
    ("Red Dead Redemption", "https://www.rockstargames.com/reddeadredemption", "__GAME_RED_DEAD_REDEMPTION__"),
    ("GTA V", "https://www.rockstargames.com/gta-v", "__GAME_GTA_V__"),
    ("Maneater", "https://store.steampowered.com/app/629820/Maneater/", "__GAME_MANEATER__"),
    ("Dragon Ball Z Kakarot", "https://store.steampowered.com/app/851850/DRAGON_BALL_Z_KAKAROT/", "__GAME_DRAGON_BALL_Z_KAKAROT__"),
    ("Midnight Club 3: DUB Edition", "https://en.wikipedia.org/wiki/Midnight_Club_3:_DUB_Edition", "__GAME_MIDNIGHT_CLUB_3__"),
    ("Metal Slug Awakening", "https://metalslugawk.vnggames.com/", "__GAME_METAL_SLUG_AWAKENING__"),
    ("Twisted Metal 3", "https://en.wikipedia.org/wiki/Twisted_Metal_3", "__GAME_TWISTED_METAL_3__"),
    ("Dragon Ball Legends", "https://dragonball-legends.com/", "__GAME_DRAGON_BALL_LEGENDS__"),
    ("Pokemon Go", "https://pokemongolive.com/", "__GAME_POKEMON_GO__"),
    ("Super Smash Bros", "https://en.wikipedia.org/wiki/Super_Smash_Bros._(video_game)", "__GAME_SUPER_SMASH_BROS__"),
    ("Kirby's Adventure", "https://en.wikipedia.org/wiki/Kirby%27s_Adventure", "__GAME_KIRBYS_ADVENTURE__"),
    ("Metal Slug", "https://en.wikipedia.org/wiki/Metal_Slug_(video_game)", "__GAME_METAL_SLUG__"),
    ("Metal Slug 2", "https://en.wikipedia.org/wiki/Metal_Slug_2", "__GAME_METAL_SLUG_2__"),
    ("Metal Slug X", "https://en.wikipedia.org/wiki/Metal_Slug_X", "__GAME_METAL_SLUG_X__"),
    ("Metal Slug 3", "https://en.wikipedia.org/wiki/Metal_Slug_3", "__GAME_METAL_SLUG_3__"),
    ("Metal Slug 4", "https://en.wikipedia.org/wiki/Metal_Slug_4", "__GAME_METAL_SLUG_4__"),
    ("Metal Slug 5", "https://en.wikipedia.org/wiki/Metal_Slug_5", "__GAME_METAL_SLUG_5__"),
]

ANIMES = [
    ("Dragon Ball", "https://es.dragon-ball-official.com", "__ANIME_DRAGON_BALL__"),
    ("One Piece", "https://one-piece.com", "__ANIME_ONE_PIECE__"),
    ("Naruto", "https://naruto-official.com/es", "__ANIME_NARUTO__"),
    ("Baki", "https://baki-anime.jp", "__ANIME_BAKI__"),
]


def avatar_cards():
    cards = []
    for name, img, text, current in AVATARS:
        cls = "card avatar-card current" if current else "card avatar-card"
        cards.append(
            f'      <article class="{cls}">\n'
            f'        <img src="{img}" alt="{name}">\n'
            f'        <div class="card-body">\n'
            f'          <h3>{name}</h3>\n'
            f'          <p>{text}</p>\n'
            f'        </div>\n'
            f'      </article>'
        )
    return "\n".join(cards) + "\n"


def link_cards(items):
    cards = []
    for name, url, img in items:
        cards.append(
            f'        <a class="game-card" href="{url}" target="_blank" rel="noopener">\n'
            f'          <img src="{img}" alt="{name}">\n'
            f'          <span>{name}</span>\n'
            f'        </a>'
        )
    return "\n".join(cards) + "\n"


index_html = """<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Mi página web | Emmanuel Salomón Santiago Bustamante</title>
<meta name="description" content="Mi página web personal: mi portafolio, mis avatares y mis proyectos en un solo lugar.">
<link rel="stylesheet" href="style.css">
</head>
<body>
<header class="hero">
  <nav class="nav">
    <a href="#proyectos">Mis proyectos</a>
    <a href="#pasatiempos">Mis pasatiempos</a>
    <a href="#contacto">Contacto</a>
  </nav>
  <div class="hero-inner">
    <div class="profile-wrap">
      <video class="hero-avatar hero-video" id="hero-video" src="assets/videos/merlin.mp4" autoplay loop muted playsinline></video>
      <img class="hero-avatar hero-photo" id="hero-photo" src="__HERO_PHOTO__" alt="Merlin, el mago: con su larga barba blanca, su sombrero puntiagudo y su báculo" hidden>
      <button class="profile-arrow" id="profile-arrow" type="button" aria-label="Cambiar foto de perfil" aria-expanded="false">▼</button>
      <div class="profile-menu" id="profile-menu" hidden>
        <button type="button" data-avatar="tiny">Tiny</button>
        <button type="button" data-avatar="emmanuel">Emmanuel</button>
        <button type="button" data-avatar="fantasma">Fantasma</button>
        <button type="button" data-avatar="gastly">Gastly</button>
        <button type="button" data-avatar="merlin">Merlin</button>
        <button type="button" data-avatar="velociraptor">Velociraptor</button>
        <button type="button" data-avatar="tiranosaurio">Tiranosaurio rex</button>
        <button type="button" data-avatar="tiburon">Tiburón</button>
      </div>
    </div>
    <h1>Emmanuel Salomón Santiago Bustamante</h1>
    <p class="hero-sub">Bienvenido a mi página. Aquí podrás encontrar desde mis trabajos realizados en mi portafolio, hasta mis gustos, pasatiempos, como la creación de mis avatares y más. Espero disfrutes de tu visita.</p>
  </div>
</header>

<main>
  <section id="proyectos" class="section">
    <div class="perimeter-box">
      <h2 class="section-title-small">Mis proyectos</h2>
      <p class="section-subtitle">Portafolio</p>
      <div class="grid">
        <a class="card portfolio-link" href="https://portafolio-essb.vercel.app/" target="_blank" rel="noopener">
          <img src="__PORTFOLIO_HERO__" alt="Mi portafolio">
        </a>
      </div>
    </div>
  </section>

  <section id="pasatiempos" class="section section-alt">
    <div class="perimeter-box">
      <h2>Mis pasatiempos</h2>
      <p class="section-subtitle">Mis avatares</p>
      <div class="grid">
        <a class="card avatar-toggle" href="avatares.html">
          <img src="__AV_TINY__" alt="Mis avatares">
        </a>
      </div>
      <p class="section-subtitle">Videojuegos</p>
      <div class="grid">
        <a class="card avatar-toggle" href="videojuegos.html">
          <img src="__GAME_GTA_V__" alt="Videojuegos">
        </a>
      </div>
      <p class="section-subtitle">Animes</p>
      <div class="grid">
        <a class="card avatar-toggle" href="animes.html">
          <img src="__ANIME_DRAGON_BALL__" alt="Animes">
        </a>
      </div>
    </div>
  </section>

  <section id="contacto" class="section section-alt">
    <div class="perimeter-box">
      <h2>Contacto</h2>
      <p class="section-intro">¿Quieres contactarme? Aquí estoy.</p>
      <div class="contact-list">
        <p><strong>E-mail:</strong> <a href="mailto:sanbus.emma@gmail.com">sanbus.emma@gmail.com</a></p>
        <p><strong>Teléfono:</strong> <a href="tel:+522411100307">+52 241 110 03 07</a></p>
        <p><strong>GitHub:</strong> <a href="https://github.com/Emmanuelevy" target="_blank" rel="noopener">github.com/Emmanuelevy</a></p>
        <p><strong>Ubicación:</strong> Tzompantepec, Tlaxcala, México</p>
      </div>
    </div>
  </section>
</main>

<footer>
  <p>&copy; 2026 Ing. Emmanuel Salomón Santiago Bustamante. Hecho en México.</p>
  <button class="back-to-top" id="back-to-top" type="button" aria-label="Volver arriba">↑</button>
</footer>
<script>
  if (window.self !== window.top) {
    document.body.classList.add('embedded');
  }
  var AVATARS = {
    tiny: "__AV_TINY__",
    emmanuel: "__AV_EMMANUEL__",
    fantasma: "__AV_FANTASMA__",
    gastly: "__AV_GASTLY__",
    merlin: "__AV_MERLIN__",
    velociraptor: "__AV_VELOCIRAPTOR__",
    tiranosaurio: "__AV_TIRANOSAURIO__",
    tiburon: "__AV_TIBURON__"
  };
  var AVATAR_VIDEOS = {
    tiny: "assets/videos/tiny.mp4",
    emmanuel: "assets/videos/emmanuel.mp4",
    fantasma: "assets/videos/fantasma.mp4",
    gastly: "assets/videos/gastly.mp4",
    merlin: "assets/videos/merlin.mp4",
    velociraptor: "assets/videos/velociraptor.mp4",
    tiranosaurio: "assets/videos/tiranosaurio.mp4",
    tiburon: "assets/videos/tiburon.mp4"
  };
  (function () {
    document.querySelectorAll('.nav a[href^="#"]').forEach(function (a) {
      a.addEventListener('click', function (e) {
        e.preventDefault();
        var el = document.querySelector(a.getAttribute('href'));
        if (el) el.scrollIntoView({ behavior: 'smooth' });
      });
    });
  })();
  (function () {
    var video = document.getElementById('hero-video');
    var photo = document.getElementById('hero-photo');
    var arrow = document.getElementById('profile-arrow');
    var menu = document.getElementById('profile-menu');
    arrow.addEventListener('click', function (e) {
      e.stopPropagation();
      var open = menu.hidden;
      menu.hidden = !open;
      arrow.setAttribute('aria-expanded', String(open));
    });
    menu.addEventListener('click', function (e) {
      var btn = e.target.closest('button[data-avatar]');
      if (!btn) return;
      var key = btn.getAttribute('data-avatar');
      var videoSrc = AVATAR_VIDEOS[key];
      if (videoSrc) {
        video.src = videoSrc;
        video.hidden = false;
        photo.hidden = true;
        video.play();
      } else {
        photo.src = AVATARS[key];
        photo.alt = btn.textContent;
        video.hidden = true;
        photo.hidden = false;
        video.pause();
      }
      menu.hidden = true;
      arrow.setAttribute('aria-expanded', 'false');
    });
    document.addEventListener('click', function (e) {
      if (!menu.hidden && !e.target.closest('.profile-wrap')) {
        menu.hidden = true;
        arrow.setAttribute('aria-expanded', 'false');
      }
    });
  })();
  (function () {
    var btn = document.getElementById('back-to-top');
    btn.addEventListener('click', function () {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  })();
</script>
</body>
</html>
"""

# Plantilla común de las páginas de lista (avatares, videojuegos, animes):
# solo cambian el título, la descripción, el encabezado, la intro,
# la clase de la rejilla y las tarjetas.
SUBPAGE = """<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>__TITLE__ | Emmanuel Salomón Santiago Bustamante</title>
<meta name="description" content="__DESCRIPTION__">
<link rel="stylesheet" href="style.css">
</head>
<body>
<header class="hero">
  <nav class="nav">
    <a href="index.html">← Volver a mi página</a>
  </nav>
  <div class="hero-inner">
    <h1>__HEADING__</h1>
    <p class="hero-sub">__INTRO__</p>
  </div>
</header>

<main>
  <section class="section">
    <div class="__GRID_CLASS__">
__CARDS__
    </div>
  </section>
</main>

<footer>
  <p>&copy; 2026 Ing. Emmanuel Salomón Santiago Bustamante. Hecho en México.</p>
</footer>
<script>
  if (window.self !== window.top) {
    document.body.classList.add('embedded');
  }
</script>
</body>
</html>
"""


def subpage(title, description, heading, intro, grid_class, cards):
    page = SUBPAGE
    page = page.replace("__TITLE__", title)
    page = page.replace("__DESCRIPTION__", description)
    page = page.replace("__HEADING__", heading)
    page = page.replace("__INTRO__", intro)
    page = page.replace("__GRID_CLASS__", grid_class)
    page = page.replace("__CARDS__", cards)
    return page


def write_page(filename, html):
    path = os.path.join(BASE, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"{filename}: {len(html)} bytes")


write_page("index.html", fill(index_html))
write_page("avatares.html", fill(subpage(
    "Mis avatares",
    "Mis avatares: Tiny, Emmanuel, Fantasma, Gastly, Merlin, Velociraptor, Tiranosaurio rex y Tiburón.",
    "Mis avatares",
    "Te presento mis avatares, realizados en modelo 3D.",
    "grid avatars-grid",
    avatar_cards(),
)))
write_page("videojuegos.html", fill(subpage(
    "Mis videojuegos",
    "Mis videojuegos favoritos: Red Dead Redemption, GTA V, Maneater, Dragon Ball Z Kakarot, Metal Slug y más.",
    "Mis videojuegos",
    "Te presento mis videojuegos favoritos.",
    "games-grid",
    link_cards(GAMES),
)))
write_page("animes.html", fill(subpage(
    "Mis animes",
    "Mis animes favoritos: Dragon Ball, One Piece, Naruto y Baki.",
    "Mis animes",
    "Te presento mis animes favoritos.",
    "games-grid",
    link_cards(ANIMES),
)))
