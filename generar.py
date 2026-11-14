#!/usr/bin/env python3
"""Genera index.html y avatares.html para Mi página web con las imágenes reales embebidas en base64."""
import base64
import os

BASE = os.path.dirname(os.path.abspath(__file__))

def b64(path):
    ext = os.path.splitext(path)[1].lower()
    mime = "image/png" if ext == ".png" else "image/jpeg" if ext in (".jpg", ".jpeg") else "image/webp"
    with open(os.path.join(BASE, path), "rb") as f:
        return f"data:{mime};base64," + base64.b64encode(f.read()).decode("ascii")

TINY_HEADER = b64("assets/avatars/merlin.webp")
PORTFOLIO_HERO = b64("assets/portfolio-hero.png")
AV = {
    "tiny": b64("assets/avatars-256/tiny.webp"),
    "emmanuel": b64("assets/avatars-256/emmanuel.webp"),
    "fantasma": b64("assets/avatars-256/fantasma.webp"),
    "gastly": b64("assets/avatars-256/gastly.webp"),
    "merlin": b64("assets/avatars-256/merlin.webp"),
    "velociraptor": b64("assets/avatars-256/velociraptor.webp"),
    "tiranosaurio": b64("assets/avatars-256/tiranosaurio-rex.webp"),
    "tiburon": b64("assets/avatars-256/tiburon.webp"),
}

GAMES = {
    "red-dead-redemption": b64("assets/games/red-dead-redemption.jpg"),
    "gta-v": b64("assets/games/gta-v.jpg"),
    "maneater": b64("assets/games/maneater.jpg"),
    "dragon-ball-z-kakarot": b64("assets/games/dragon-ball-z-kakarot.jpg"),
    "midnight-club-3": b64("assets/games/midnight-club-3.jpg"),
    "metal-slug-awakening": b64("assets/games/metal-slug-awakening.jpg"),
    "twisted-metal-3": b64("assets/games/twisted-metal-3.jpg"),
    "dragon-ball-legends": b64("assets/games/dragon-ball-legends.jpg"),
    "pokemon-go": b64("assets/games/pokemon-go.jpg"),
    "super-smash-bros": b64("assets/games/super-smash-bros.jpg"),
    "kirbys-adventure": b64("assets/games/kirbys-adventure.jpg"),
    "metal-slug": b64("assets/games/metal-slug.jpg"),
    "metal-slug-2": b64("assets/games/metal-slug-2.jpg"),
    "metal-slug-x": b64("assets/games/metal-slug-x.jpg"),
    "metal-slug-3": b64("assets/games/metal-slug-3.jpg"),
    "metal-slug-4": b64("assets/games/metal-slug-4.jpg"),
    "metal-slug-5": b64("assets/games/metal-slug-5.jpg"),
}

ANIMES = {
    "dragon-ball": b64("assets/animes/dragon-ball.jpg"),
    "one-piece": b64("assets/animes/one-piece.jpg"),
    "naruto": b64("assets/animes/naruto.jpg"),
    "baki": b64("assets/animes/baki.jpg"),
}

def fill(template):
    out = template.replace("__TINY_HEADER__", TINY_HEADER)
    out = out.replace("__PORTFOLIO_HERO__", PORTFOLIO_HERO)
    for key, val in AV.items():
        out = out.replace(f"__AV_{key.upper()}__", val)
    for key, val in GAMES.items():
        out = out.replace(f"__GAME_{key.upper().replace('-', '_')}__", val)
    for key, val in ANIMES.items():
        out = out.replace(f"__ANIME_{key.upper().replace('-', '_')}__", val)
    return out

AVATAR_CARDS = """      <article class="card avatar-card current">
        <img src="__AV_TINY__" alt="Tiny">
        <div class="card-body">
          <h3>Tiny</h3>
          <p>Tiny es un pitbull Red Nose, musculoso y sonriente, leal y protector con su familia, con su collar rojo de picos color oro.</p>
        </div>
      </article>
      <article class="card avatar-card">
        <img src="__AV_EMMANUEL__" alt="Emmanuel">
        <div class="card-body">
          <h3>Emmanuel</h3>
          <p>Emmanuel en versión avatar 3D, musculoso, con el pelo corto, shorts blancos y gotas de agua.</p>
        </div>
      </article>
      <article class="card avatar-card">
        <img src="__AV_FANTASMA__" alt="Fantasma">
        <div class="card-body">
          <h3>Fantasma</h3>
          <p>El fantasma negro es una bola oscura con brazos, rodeado de un aura de fuego morado, con ojos blancos, colmillos y boca roja, intimidante y misterioso.</p>
        </div>
      </article>
      <article class="card avatar-card">
        <img src="__AV_GASTLY__" alt="Gastly">
        <div class="card-body">
          <h3>Gastly</h3>
          <p>El fantasma negro es una bola flotante oscura rodeada de un aura de fuego morado, intimidante y misterioso, que parece correr dejando una estela de llamas detrás. Ahora con dos colmillos y la boca roja.</p>
        </div>
      </article>
      <article class="card avatar-card">
        <img src="__AV_MERLIN__" alt="Merlin">
        <div class="card-body">
          <h3>Merlin</h3>
          <p>Merlin es el mago más famoso de la leyenda artúrica, consejero del rey Arturo y maestro de la magia. Con su larga barba blanca, su sombrero puntiagudo y su báculo, es símbolo de sabiduría, poder y misterio.</p>
        </div>
      </article>
      <article class="card avatar-card">
        <img src="__AV_VELOCIRAPTOR__" alt="Velociraptor">
        <div class="card-body">
          <h3>Velociraptor</h3>
          <p>El velociraptor fue un dinosaurio pequeño pero muy inteligente y rápido, famoso por cazar en manada y por su garra en forma de hoz en cada pie. En la cultura popular es símbolo de astucia, velocidad y trabajo en equipo.</p>
        </div>
      </article>
      <article class="card avatar-card">
        <img src="__AV_TIRANOSAURIO__" alt="Tiranosaurio rex">
        <div class="card-body">
          <h3>Tiranosaurio rex</h3>
          <p>El T. rex no es un ser mitológico, pero en la cultura popular es el rey de los dinosaurios: su nombre significa &lsquo;rey lagarto tirano&rsquo; y es símbolo de fuerza y poder.</p>
        </div>
      </article>
      <article class="card avatar-card">
        <img src="__AV_TIBURON__" alt="Tiburón">
        <div class="card-body">
          <h3>Tiburón</h3>
          <p>En la mitología hawaiana, los tiburones son &lsquo;aumākua: espíritus guardianes ancestrales que protegen a las familias, guían a los pescadores en el mar y castigan a quien rompe los kapu, los tabúes sagrados del océano. En muchas culturas del Pacífico el tiburón es un dios y mensajero del mar, símbolo de fuerza, respeto y protección: no se le teme solo como depredador, se le honra como guardián.</p>
        </div>
      </article>
"""

GAMES_CARDS = """        <a class="game-card" href="https://www.rockstargames.com/reddeadredemption" target="_blank" rel="noopener">
          <img src="__GAME_RED_DEAD_REDEMPTION__" alt="Red Dead Redemption">
          <span>Red Dead Redemption</span>
        </a>
        <a class="game-card" href="https://www.rockstargames.com/gta-v" target="_blank" rel="noopener">
          <img src="__GAME_GTA_V__" alt="GTA V">
          <span>GTA V</span>
        </a>
        <a class="game-card" href="https://store.steampowered.com/app/629820/Maneater/" target="_blank" rel="noopener">
          <img src="__GAME_MANEATER__" alt="Maneater">
          <span>Maneater</span>
        </a>
        <a class="game-card" href="https://store.steampowered.com/app/851850/DRAGON_BALL_Z_KAKAROT/" target="_blank" rel="noopener">
          <img src="__GAME_DRAGON_BALL_Z_KAKAROT__" alt="Dragon Ball Z Kakarot">
          <span>Dragon Ball Z Kakarot</span>
        </a>
        <a class="game-card" href="https://en.wikipedia.org/wiki/Midnight_Club_3:_DUB_Edition" target="_blank" rel="noopener">
          <img src="__GAME_MIDNIGHT_CLUB_3__" alt="Midnight Club 3: DUB Edition">
          <span>Midnight Club 3: DUB Edition</span>
        </a>
        <a class="game-card" href="https://metalslugawk.vnggames.com/" target="_blank" rel="noopener">
          <img src="__GAME_METAL_SLUG_AWAKENING__" alt="Metal Slug Awakening">
          <span>Metal Slug Awakening</span>
        </a>
        <a class="game-card" href="https://en.wikipedia.org/wiki/Twisted_Metal_3" target="_blank" rel="noopener">
          <img src="__GAME_TWISTED_METAL_3__" alt="Twisted Metal 3">
          <span>Twisted Metal 3</span>
        </a>
        <a class="game-card" href="https://dragonball-legends.com/" target="_blank" rel="noopener">
          <img src="__GAME_DRAGON_BALL_LEGENDS__" alt="Dragon Ball Legends">
          <span>Dragon Ball Legends</span>
        </a>
        <a class="game-card" href="https://pokemongolive.com/" target="_blank" rel="noopener">
          <img src="__GAME_POKEMON_GO__" alt="Pokemon Go">
          <span>Pokemon Go</span>
        </a>
        <a class="game-card" href="https://en.wikipedia.org/wiki/Super_Smash_Bros._(video_game)" target="_blank" rel="noopener">
          <img src="__GAME_SUPER_SMASH_BROS__" alt="Super Smash Bros">
          <span>Super Smash Bros</span>
        </a>
        <a class="game-card" href="https://en.wikipedia.org/wiki/Kirby%27s_Adventure" target="_blank" rel="noopener">
          <img src="__GAME_KIRBYS_ADVENTURE__" alt="Kirby's Adventure">
          <span>Kirby's Adventure</span>
        </a>
        <a class="game-card" href="https://en.wikipedia.org/wiki/Metal_Slug_(video_game)" target="_blank" rel="noopener">
          <img src="__GAME_METAL_SLUG__" alt="Metal Slug">
          <span>Metal Slug</span>
        </a>
        <a class="game-card" href="https://en.wikipedia.org/wiki/Metal_Slug_2" target="_blank" rel="noopener">
          <img src="__GAME_METAL_SLUG_2__" alt="Metal Slug 2">
          <span>Metal Slug 2</span>
        </a>
        <a class="game-card" href="https://en.wikipedia.org/wiki/Metal_Slug_X" target="_blank" rel="noopener">
          <img src="__GAME_METAL_SLUG_X__" alt="Metal Slug X">
          <span>Metal Slug X</span>
        </a>
        <a class="game-card" href="https://en.wikipedia.org/wiki/Metal_Slug_3" target="_blank" rel="noopener">
          <img src="__GAME_METAL_SLUG_3__" alt="Metal Slug 3">
          <span>Metal Slug 3</span>
        </a>
        <a class="game-card" href="https://en.wikipedia.org/wiki/Metal_Slug_4" target="_blank" rel="noopener">
          <img src="__GAME_METAL_SLUG_4__" alt="Metal Slug 4">
          <span>Metal Slug 4</span>
        </a>
        <a class="game-card" href="https://en.wikipedia.org/wiki/Metal_Slug_5" target="_blank" rel="noopener">
          <img src="__GAME_METAL_SLUG_5__" alt="Metal Slug 5">
          <span>Metal Slug 5</span>
        </a>
"""

ANIMES_CARDS = """        <a class="game-card" href="https://es.wikipedia.org/wiki/Dragon_Ball" target="_blank" rel="noopener">
          <img src="__ANIME_DRAGON_BALL__" alt="Dragon Ball">
          <span>Dragon Ball</span>
        </a>
        <a class="game-card" href="https://es.wikipedia.org/wiki/One_Piece" target="_blank" rel="noopener">
          <img src="__ANIME_ONE_PIECE__" alt="One Piece">
          <span>One Piece</span>
        </a>
        <a class="game-card" href="https://es.wikipedia.org/wiki/Naruto" target="_blank" rel="noopener">
          <img src="__ANIME_NARUTO__" alt="Naruto">
          <span>Naruto</span>
        </a>
        <a class="game-card" href="https://es.wikipedia.org/wiki/Baki_the_Grappler" target="_blank" rel="noopener">
          <img src="__ANIME_BAKI__" alt="Baki">
          <span>Baki</span>
        </a>
"""

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
      <img class="hero-avatar hero-photo" id="hero-photo" src="__TINY_HEADER__" alt="Merlin, el mago: con su larga barba blanca, su sombrero puntiagudo y su báculo" hidden>
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

avatares_html = """<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Mis avatares | Emmanuel Salomón Santiago Bustamante</title>
<meta name="description" content="Mis avatares: Tiny, Emmanuel, Fantasma, Gastly, Merlin, Velociraptor, Tiranosaurio rex y Tiburón.">
<link rel="stylesheet" href="style.css">
</head>
<body>
<header class="hero">
  <nav class="nav">
    <a href="index.html">← Volver a mi página</a>
  </nav>
  <div class="hero-inner">
    <h1>Mis avatares</h1>
    <p class="hero-sub">Te presento mis avatares, realizados en modelo 3D.</p>
  </div>
</header>

<main>
  <section class="section">
    <div class="grid avatars-grid">
__AVATAR_CARDS__
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

videojuegos_html = """<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Mis videojuegos | Emmanuel Salomón Santiago Bustamante</title>
<meta name="description" content="Mis videojuegos favoritos: Red Dead Redemption, GTA V, Maneater, Dragon Ball Z Kakarot, Metal Slug y más.">
<link rel="stylesheet" href="style.css">
</head>
<body>
<header class="hero">
  <nav class="nav">
    <a href="index.html">← Volver a mi página</a>
  </nav>
  <div class="hero-inner">
    <h1>Mis videojuegos</h1>
    <p class="hero-sub">Te presento mis videojuegos favoritos.</p>
  </div>
</header>

<main>
  <section class="section">
    <div class="games-grid">
__GAMES_CARDS__
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

animes_html = """<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Mis animes | Emmanuel Salomón Santiago Bustamante</title>
<meta name="description" content="Mis animes favoritos: Dragon Ball, One Piece, Naruto y Baki.">
<link rel="stylesheet" href="style.css">
</head>
<body>
<header class="hero">
  <nav class="nav">
    <a href="index.html">← Volver a mi página</a>
  </nav>
  <div class="hero-inner">
    <h1>Mis animes</h1>
    <p class="hero-sub">Te presento mis animes favoritos.</p>
  </div>
</header>

<main>
  <section class="section">
    <div class="games-grid">
__ANIMES_CARDS__
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

index_out = fill(index_html)
with open(os.path.join(BASE, "index.html"), "w", encoding="utf-8") as f:
    f.write(index_out)
print("index.html:", len(index_out), "bytes")

avatares_out = fill(avatares_html.replace("__AVATAR_CARDS__", AVATAR_CARDS))
with open(os.path.join(BASE, "avatares.html"), "w", encoding="utf-8") as f:
    f.write(avatares_out)
print("avatares.html:", len(avatares_out), "bytes")

videojuegos_out = fill(videojuegos_html.replace("__GAMES_CARDS__", GAMES_CARDS))
with open(os.path.join(BASE, "videojuegos.html"), "w", encoding="utf-8") as f:
    f.write(videojuegos_out)
print("videojuegos.html:", len(videojuegos_out), "bytes")

animes_out = fill(animes_html.replace("__ANIMES_CARDS__", ANIMES_CARDS))
with open(os.path.join(BASE, "animes.html"), "w", encoding="utf-8") as f:
    f.write(animes_out)
print("animes.html:", len(animes_out), "bytes")
