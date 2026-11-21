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
    "__HERO_PHOTO__": "assets/avatars/numero-1.webp",
    "__PORTFOLIO_HERO__": "assets/portfolio-hero.png",
    "__AV_TINY__": "assets/avatars-256/tiny.webp",
    "__AV_EMMANUEL__": "assets/avatars-256/emmanuel.webp",
    "__AV_FANTASMA__": "assets/avatars-256/fantasma.webp",
    "__AV_GASTLY__": "assets/avatars-256/gastly.webp",
    "__AV_MERLIN__": "assets/avatars-256/merlin.webp",
    "__AV_VELOCIRAPTOR__": "assets/avatars-256/velociraptor.webp",
    "__AV_TIRANOSAURIO__": "assets/avatars-256/tiranosaurio-rex.webp",
    "__AV_TIBURON__": "assets/avatars-256/tiburon.webp",
    "__AV_PANDA__": "assets/avatars-256/panda.webp",
    "__AV_ITACHI__": "assets/avatars-256/itachi.webp",
    "__AV_GENGAR_BLANCO__": "assets/avatars-256/gengar-blanco.webp",
    "__AV_GENGAR__": "assets/avatars-256/gengar.webp",
    "__AV_GENGAR_GIGAMAX__": "assets/avatars-256/gengar-gigamax.webp",
    "__AV_BASILISCO__": "assets/avatars-256/basilisco.webp",
    "__AV_MUSHU__": "assets/avatars-256/mushu.webp",
    "__AV_IPHONE__": "assets/avatars-256/iphone.webp",
    "__AV_NUMERO_1__": "assets/avatars-256/numero-1.webp",
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
    "__DEPORTE_NATACION__": "assets/deportes/natacion.jpg",
    "__DEPORTE_MMA__": "assets/deportes/mma.jpg",
    "__PEL_HARRY_POTTER_1__": "assets/peliculas/harry-potter-1.jpg",
    "__PEL_HARRY_POTTER_2__": "assets/peliculas/harry-potter-2.jpg",
    "__PEL_HARRY_POTTER_3__": "assets/peliculas/harry-potter-3.jpg",
    "__PEL_HARRY_POTTER_4__": "assets/peliculas/harry-potter-4.jpg",
    "__PEL_HARRY_POTTER_5__": "assets/peliculas/harry-potter-5.jpg",
    "__PEL_HARRY_POTTER_6__": "assets/peliculas/harry-potter-6.jpg",
    "__PEL_HARRY_POTTER_7__": "assets/peliculas/harry-potter-7.jpg",
    "__PEL_HARRY_POTTER_8__": "assets/peliculas/harry-potter-8.jpg",
    "__PEL_RAPIDO_Y_FURIOSO_1__": "assets/peliculas/rapido-y-furioso-1.jpg",
    "__PEL_RAPIDO_Y_FURIOSO_2__": "assets/peliculas/rapido-y-furioso-2.jpg",
    "__PEL_RAPIDO_Y_FURIOSO_3__": "assets/peliculas/rapido-y-furioso-3.jpg",
    "__PEL_RAPIDO_Y_FURIOSO_4__": "assets/peliculas/rapido-y-furioso-4.jpg",
    "__PEL_RAPIDO_Y_FURIOSO_5__": "assets/peliculas/rapido-y-furioso-5.jpg",
    "__PEL_RAPIDO_Y_FURIOSO_6__": "assets/peliculas/rapido-y-furioso-6.jpg",
    "__PEL_RAPIDO_Y_FURIOSO_7__": "assets/peliculas/rapido-y-furioso-7.jpg",
    "__PEL_RAPIDO_Y_FURIOSO_8__": "assets/peliculas/rapido-y-furioso-8.jpg",
    "__PEL_RAPIDO_Y_FURIOSO_9__": "assets/peliculas/rapido-y-furioso-9.jpg",
    "__PEL_DRAGON_BALL_SUPER_BROLY__": "assets/peliculas/dragon-ball-super-broly.jpg",
    "__PEL_EL_TRANSPORTADOR_2__": "assets/peliculas/el-transportador-2.jpg",
    "__PEL_CONTACTO_SANGRIENTO__": "assets/peliculas/contacto-sangriento.jpg",
    "__PEL_VAN_HELSING__": "assets/peliculas/van-helsing.jpg",
    "__PEL_BATMAN_EL_CABALLERO_DE_LA_NOCHE__": "assets/peliculas/batman-el-caballero-de-la-noche.jpg",
    "__PEL_SOY_LEYENDA__": "assets/peliculas/soy-leyenda.jpg",
    "__PEL_BAD_BOYS_1__": "assets/peliculas/bad-boys-1.jpg",
    "__PEL_BAD_BOYS_2__": "assets/peliculas/bad-boys-2.jpg",
    "__PEL_BAD_BOYS_3__": "assets/peliculas/bad-boys-3.jpg",
    "__PEL_SPACE_JAM__": "assets/peliculas/space-jam.jpg",
    "__PEL_LOGAN__": "assets/peliculas/logan.jpg",
    "__PEL_X_MEN_DIAS_DEL_FUTURO_PASADO__": "assets/peliculas/x-men-dias-del-futuro-pasado.jpg",
    "__PEL_DEADPOOL_1__": "assets/peliculas/deadpool-1.jpg",
    "__PEL_DEADPOOL_2__": "assets/peliculas/deadpool-2.jpg",
    "__PEL_DEADPOOL_3__": "assets/peliculas/deadpool-3.jpg",
    "__PEL_HERCULES__": "assets/peliculas/hercules.jpg",
    "__PEL_ALADDIN__": "assets/peliculas/aladdin.jpg",
    "__TEC_APPLE__": "assets/tecnologia/apple.jpg",
    "__TEC_DELL__": "assets/tecnologia/dell.jpg",
    "__TEC_GAMESIR__": "assets/tecnologia/gamesir.jpg",
    "__TEC_ANKER__": "assets/tecnologia/anker.jpg",
    "__TEC_UGREEN__": "assets/tecnologia/ugreen.jpg",
    "__TEC_VIDITA__": "assets/tecnologia/vidita.jpg",
    "__TEC_MUSE__": "assets/tecnologia/muse.jpg",
    "__HOGWARTS__": "assets/hogwarts/perfil.jpg",
    "__HOGWARTS_VARITA__": "assets/hogwarts/varita.jpg",
    "__HOGWARTS_PATRONUS__": "assets/hogwarts/patronus.jpg",
    "__HOGWARTS_SLYTHERIN__": "assets/hogwarts/slytherin.jpg",
}

IMAGES = {marker: b64(path) for marker, path in IMAGE_FILES.items()}


def fill(template):
    for marker, data in IMAGES.items():
        template = template.replace(marker, data)
    return template


# (nombre, marcador de imagen, descripción, es el avatar puesto)
AVATARS = [
    ("Número 1", "__AV_NUMERO_1__",
     "Esta criatura es Número 1, el líder de los Chicos del Barrio, con sus lentes negros, su playera roja y sus botas enormes, siempre listo para la misión.",
     True),
    ("iPhone", "__AV_IPHONE__",
     "Esta criatura es un iPhone 17 Pro rojo con patitas y manitas, siempre listo con su carita bonita.",
     False),
    ("Mushu", "__AV_MUSHU__",
     "Esta criatura es Mushu, el dragoncito rojo de Mulán, siempre listo para ayudar con su ingenio, su valentía y su gran corazón.",
     False),
    ("Basilisco", "__AV_BASILISCO__",
     "Esta criatura es el basilisco macho de Herpo el Loco, el primer basilisco del que hay constancia en los libros de Harry Potter. Nace de un huevo de gallina incubado por un sapo, y el macho luce una pluma escarlata sobre la cabeza. Su mirada mata a quien la ve directo a sus ojos amarillos.",
     False),
    ("Gengar Gigamax", "__AV_GENGAR_GIGAMAX__",
     "Es de tipo fantasma y veneno. Shiny. Al gigamaxizarse, gran parte de su cuerpo queda sumergido en otra dimensión a través de una enorme boca abierta en el suelo, esperando atrapar a quien se acerque.",
     False),
    ("Gengar", "__AV_GENGAR__",
     "Es de tipo fantasma y veneno. Siempre lleva una sonrisa ya que nunca se rinde, es muy alegre, su lealtad y su vínculo son inquebrantables, además es muy afectuoso.",
     False),
    ("Mega Gengar", "__AV_GENGAR_BLANCO__",
     "Es de tipo fantasma y veneno, es shiny, tiene un tercer ojo que jamás parpadea y le permite checar otras dimensiones.",
     False),
    ("Itachi", "__AV_ITACHI__",
     "Esta criatura es Itachi Uchiha, ninja de Akatsuki con su capa negra de nubes rojas y su banda de Konoha, serio y misterioso.",
     False),
    ("Panda", "__AV_PANDA__",
     "Esta criatura es un panda adorable con su traje rojo y dorado, siempre listo para iluminar el camino con su linterna.",
     False),
    ("Tiny", "__AV_TINY__",
     "Tiny es un pitbull Red Nose, musculoso y sonriente, leal y protector con su familia, con su collar rojo de picos color oro.",
     False),
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

DEPORTES = [
    ("Natación", "https://www.facebook.com/share/1bzUXzov5L/?mibextid=wwXIfr", "__DEPORTE_NATACION__"),
    ("MMA (Artes Marciales Mixtas)", "https://www.facebook.com/share/1ECEGSu2F7/?mibextid=wwXIfr", "__DEPORTE_MMA__"),
]

PELICULAS = [
    ("Harry Potter y la piedra filosofal", "https://es.wikipedia.org/wiki/Harry_Potter_y_la_piedra_filosofal_(pel%C3%ADcula)", "__PEL_HARRY_POTTER_1__"),
    ("Harry Potter y la cámara secreta", "https://es.wikipedia.org/wiki/Harry_Potter_y_la_c%C3%A1mara_secreta_(pel%C3%ADcula)", "__PEL_HARRY_POTTER_2__"),
    ("Harry Potter y el prisionero de Azkaban", "https://es.wikipedia.org/wiki/Harry_Potter_y_el_prisionero_de_Azkaban_(pel%C3%ADcula)", "__PEL_HARRY_POTTER_3__"),
    ("Harry Potter y el cáliz de fuego", "https://es.wikipedia.org/wiki/Harry_Potter_y_el_c%C3%A1liz_de_fuego_(pel%C3%ADcula)", "__PEL_HARRY_POTTER_4__"),
    ("Harry Potter y la Orden del Fénix", "https://es.wikipedia.org/wiki/Harry_Potter_y_la_Orden_del_F%C3%A9nix_(pel%C3%ADcula)", "__PEL_HARRY_POTTER_5__"),
    ("Harry Potter y el misterio del príncipe", "https://es.wikipedia.org/wiki/Harry_Potter_y_el_misterio_del_pr%C3%ADncipe_(pel%C3%ADcula)", "__PEL_HARRY_POTTER_6__"),
    ("Harry Potter y las Reliquias de la Muerte: parte 1", "https://es.wikipedia.org/wiki/Harry_Potter_y_las_Reliquias_de_la_Muerte:_parte_1", "__PEL_HARRY_POTTER_7__"),
    ("Harry Potter y las Reliquias de la Muerte: parte 2", "https://es.wikipedia.org/wiki/Harry_Potter_y_las_Reliquias_de_la_Muerte:_parte_2", "__PEL_HARRY_POTTER_8__"),
    ("Rápido y furioso", "https://es.wikipedia.org/wiki/The_Fast_and_the_Furious", "__PEL_RAPIDO_Y_FURIOSO_1__"),
    ("Rápido y furioso 2", "https://es.wikipedia.org/wiki/2_Fast_2_Furious", "__PEL_RAPIDO_Y_FURIOSO_2__"),
    ("Rápido y furioso: reto Tokio", "https://es.wikipedia.org/wiki/The_Fast_and_the_Furious:_Tokyo_Drift", "__PEL_RAPIDO_Y_FURIOSO_3__"),
    ("Rápido y furioso 4", "https://es.wikipedia.org/wiki/Fast_%26_Furious", "__PEL_RAPIDO_Y_FURIOSO_4__"),
    ("Rápido y furioso 5", "https://es.wikipedia.org/wiki/Fast_Five", "__PEL_RAPIDO_Y_FURIOSO_5__"),
    ("Rápido y furioso 6", "https://es.wikipedia.org/wiki/Fast_%26_Furious_6", "__PEL_RAPIDO_Y_FURIOSO_6__"),
    ("Rápido y furioso 7", "https://es.wikipedia.org/wiki/Furious_7", "__PEL_RAPIDO_Y_FURIOSO_7__"),
    ("Rápido y furioso 8", "https://es.wikipedia.org/wiki/The_Fate_of_the_Furious", "__PEL_RAPIDO_Y_FURIOSO_8__"),
    ("Rápido y furioso 9", "https://es.wikipedia.org/wiki/F9_(pel%C3%ADcula)", "__PEL_RAPIDO_Y_FURIOSO_9__"),
    ("Dragon Ball Super: Broly", "https://es.wikipedia.org/wiki/Dragon_Ball_Super:_Broly", "__PEL_DRAGON_BALL_SUPER_BROLY__"),
    ("El transportador 2", "https://es.wikipedia.org/wiki/Transporter_2", "__PEL_EL_TRANSPORTADOR_2__"),
    ("Contacto sangriento", "https://es.wikipedia.org/wiki/Bloodsport", "__PEL_CONTACTO_SANGRIENTO__"),
    ("Van Helsing: el cazador de monstruos", "https://es.wikipedia.org/wiki/Van_Helsing_(pel%C3%ADcula)", "__PEL_VAN_HELSING__"),
    ("Batman: el caballero de la noche", "https://es.wikipedia.org/wiki/The_Dark_Knight", "__PEL_BATMAN_EL_CABALLERO_DE_LA_NOCHE__"),
    ("Soy leyenda", "https://es.wikipedia.org/wiki/Soy_leyenda_(pel%C3%ADcula)", "__PEL_SOY_LEYENDA__"),
    ("Bad Boys", "https://es.wikipedia.org/wiki/Bad_Boys", "__PEL_BAD_BOYS_1__"),
    ("Bad Boys 2", "https://es.wikipedia.org/wiki/Bad_Boys_II", "__PEL_BAD_BOYS_2__"),
    ("Bad Boys 3", "https://es.wikipedia.org/wiki/Bad_Boys_for_Life", "__PEL_BAD_BOYS_3__"),
    ("Space Jam", "https://es.wikipedia.org/wiki/Space_Jam", "__PEL_SPACE_JAM__"),
    ("Logan", "https://es.wikipedia.org/wiki/Logan_(pel%C3%ADcula)", "__PEL_LOGAN__"),
    ("X-Men: días del futuro pasado", "https://es.wikipedia.org/wiki/X-Men:_d%C3%ADas_del_futuro_pasado", "__PEL_X_MEN_DIAS_DEL_FUTURO_PASADO__"),
    ("Deadpool", "https://es.wikipedia.org/wiki/Deadpool_(pel%C3%ADcula)", "__PEL_DEADPOOL_1__"),
    ("Deadpool 2", "https://es.wikipedia.org/wiki/Deadpool_2", "__PEL_DEADPOOL_2__"),
    ("Deadpool 3", "https://es.wikipedia.org/wiki/Deadpool_%26_Wolverine", "__PEL_DEADPOOL_3__"),
    ("Hércules", "https://es.wikipedia.org/wiki/H%C3%A9rcules_(pel%C3%ADcula_de_1997)", "__PEL_HERCULES__"),
    ("Aladdín", "https://es.wikipedia.org/wiki/Aladd%C3%ADn_(pel%C3%ADcula_de_1992)", "__PEL_ALADDIN__"),
]

TECNOLOGIA = [
    ("Apple", "https://www.apple.com", "__TEC_APPLE__"),
    ("Dell", "https://www.dell.com", "__TEC_DELL__"),
    ("GameSir", "https://gamesir.com", "__TEC_GAMESIR__"),
    ("Anker", "https://www.anker.com", "__TEC_ANKER__"),
    ("UGREEN", "https://www.ugreen.com", "__TEC_UGREEN__"),
    ("VIDITA", "https://www.mercadolibre.cl/tienda/vidita", "__TEC_VIDITA__"),
    ("Muse", "https://muse.ai", "__TEC_MUSE__"),
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
<link rel="icon" type="image/png" href="favicon.png">
<link rel="apple-touch-icon" href="favicon.png">
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
      <video class="hero-avatar hero-video" id="hero-video" src="assets/videos/numero-1.mp4" autoplay loop muted playsinline></video>
      <img class="hero-avatar hero-photo" id="hero-photo" src="__HERO_PHOTO__" alt="Número 1, el líder de los Chicos del Barrio" hidden>
      <button class="profile-arrow" id="profile-arrow" type="button" aria-label="Cambiar foto de perfil" aria-expanded="false">▼</button>
      <div class="profile-menu" id="profile-menu" hidden>
        <button type="button" data-avatar="numero_1">Número 1</button>
        <button type="button" data-avatar="iphone">iPhone</button>
        <button type="button" data-avatar="mushu">Mushu</button>
        <button type="button" data-avatar="basilisco">Basilisco</button>
        <button type="button" data-avatar="gengar_gigamax">Gengar Gigamax</button>
        <button type="button" data-avatar="gengar">Gengar</button>
        <button type="button" data-avatar="gengar_blanco">Mega Gengar</button>
        <button type="button" data-avatar="itachi">Itachi</button>
        <button type="button" data-avatar="panda">Panda</button>
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
    <p class="hero-sub">Bienvenido a mi página. Aquí podrás encontrar desde mis trabajos realizados en mi portafolio, hasta mis gustos, pasatiempos; como la creación de mis avatares y más. Espero disfrutes de tu visita.</p>
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
      <p class="portfolio-text">Todos mis proyectos se encuentran alojados en mi portafolio digital, desde el juego de pingpong; creado en el curso de ALURA LATAM, hasta la app de Mi Wuawua; dedicada a todos los perritos del mundo. Puedes entrar y consultar mis proyectos dando clic en mi foto.</p>
    </div>
  </section>

  <section id="pasatiempos" class="section section-alt">
    <div class="perimeter-box">
      <h2>Mis pasatiempos</h2>
      <p class="section-subtitle">Avatares</p>
      <div class="grid">
        <a class="card avatar-toggle" href="avatares.html">
          <img src="__AV_TINY__" alt="Avatares">
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
      <p class="section-subtitle">Deportes</p>
      <div class="grid">
        <a class="card avatar-toggle" href="deportes.html">
          <img src="__DEPORTE_NATACION__" alt="Deportes">
        </a>
      </div>
      <p class="section-subtitle">Películas</p>
      <div class="grid">
        <a class="card avatar-toggle" href="peliculas.html">
          <img src="__PEL_HARRY_POTTER_1__" alt="Películas">
        </a>
      </div>
      <p class="section-subtitle">Tecnología</p>
      <div class="grid">
        <a class="card avatar-toggle" href="tecnologia.html">
          <img src="__TEC_APPLE__" alt="Tecnología">
        </a>
      </div>
      <p class="section-subtitle">Hogwarts</p>
      <div class="grid">
        <a class="card avatar-toggle" href="hogwarts.html">
          <img src="__HOGWARTS__" alt="Hogwarts">
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
    numero_1: "__AV_NUMERO_1__",
    iphone: "__AV_IPHONE__",
    mushu: "__AV_MUSHU__",
    basilisco: "__AV_BASILISCO__",
    gengar_gigamax: "__AV_GENGAR_GIGAMAX__",
    gengar: "__AV_GENGAR__",
    gengar_blanco: "__AV_GENGAR_BLANCO__",
    itachi: "__AV_ITACHI__",
    panda: "__AV_PANDA__",
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
    numero_1: "assets/videos/numero-1.mp4",
    iphone: "assets/videos/iphone.mp4",
    mushu: "assets/videos/mushu.mp4",
    basilisco: "assets/videos/basilisco.mp4",
    gengar_gigamax: "assets/videos/gengar-gigamax.mp4",
    gengar: "assets/videos/gengar.mp4",
    gengar_blanco: "assets/videos/gengar-blanco.mp4",
    itachi: "assets/videos/itachi.mp4",
    panda: "assets/videos/panda.mp4",
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
<link rel="icon" type="image/png" href="favicon.png">
<link rel="apple-touch-icon" href="favicon.png">
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
    "Avatares",
    "Avatares: Tiny, Emmanuel, Fantasma, Gastly, Merlin, Velociraptor, Tiranosaurio rex y Tiburón.",
    "Avatares",
    "Te presento a mis avatares, fueron creados en modelo 3D, elegí estos personajes porque me gustan mucho y son algunos de mis favoritos.",
    "grid avatars-grid",
    avatar_cards(),
)))
write_page("videojuegos.html", fill(subpage(
    "Mis videojuegos",
    "Mis videojuegos favoritos: Red Dead Redemption, GTA V, Maneater, Dragon Ball Z Kakarot, Metal Slug y más.",
    "Mis videojuegos",
    "Te presento mis videojuegos favoritos. Me gustan porque unos tienen modo historia, puedes seguir mejorando al personaje, tienen modo libre y algunos incluyen todo junto. Sin duda son geniales.",
    "games-grid",
    link_cards(GAMES),
)))
write_page("animes.html", fill(subpage(
    "Mis animes",
    "Mis animes favoritos: Dragon Ball, One Piece, Naruto y Baki.",
    "Mis animes",
    "Te presento algunos de mis animes favoritos. Sin duda geniales, aunque para mí el mejor de todos, es el padre de los animes y sin duda alguna mi favorito, Dragon Ball.",
    "games-grid",
    link_cards(ANIMES),
)))
write_page("deportes.html", fill(subpage(
    "Mis deportes",
    "Mis deportes favoritos: Natación y MMA (Artes Marciales Mixtas).",
    "Mis deportes",
    "Te presento mis deportes favoritos. Son deportes muy completos en el cual te ayudan a relajarte muy bien.",
    "games-grid",
    link_cards(DEPORTES),
)))
write_page("peliculas.html", fill(subpage(
    "Mis películas",
    "Mis películas favoritas: Harry Potter, Rápido y furioso, Dragon Ball Super: Broly, Deadpool y más.",
    "Mis películas",
    "Te presentó mis películas favoritas. Me encantan porque tienen una buena trama y te mantienen con un interés bueno, además hay acción, romance, suspenso, fantasía y comedia. Sin duda son de las mejores que existen.",
    "games-grid",
    link_cards(PELICULAS),
)))
write_page("tecnologia.html", fill(subpage(
    "Mi tecnología",
    "Mi tecnología favorita: Apple, Dell y GameSir.",
    "Mi tecnología",
    "Te presento mi tecnología favorita. Esta tecnología me encanta porque además de presentar un diseño único y muy elegante en el hardware, su software es fluido y limpio, lo que permite realizar tus cosas siempre a gusto.",
    "games-grid",
    link_cards(TECNOLOGIA),
)))
write_page("hogwarts.html", fill(subpage(
    "Hogwarts",
    "Mi perfil de Hogwarts: Slytherin, patrón Dragón y varita de Madera de Anciano.",
    "Hogwarts",
    "Estudié en Hogwarts, perteneciente a la casa de Slytherin, soy el heredero de Salazar Slytherin, hablo pársel, mi varita es la varita de saúco, mi patronus es un dragón, mi basilisco es macho; por eso tiene una pluma escarlata en la cabeza, solo yo lo controlo y es el que puedes seleccionar en el perfil de esta página. Soy el mago más poderoso de todos los tiempos.",
    "games-grid",
    '        <a href="https://www.harrypotter.com/profile/788ac0ad-a932-4110-ae7a-259d1bfebe04" target="_blank" rel="noopener" style="display: block; width: 100%; max-width: 700px; margin: 0 auto; grid-column: 1 / -1;"><img src="__HOGWARTS__" alt="Mi perfil de Hogwarts" style="width: 100%; border-radius: 20px; display: block;"></a>\n'
    '        <div style="width: 100%; max-width: 700px; margin: 30px auto 0; grid-column: 1 / -1; text-align: justify;"><img src="__HOGWARTS_SLYTHERIN__" alt="Escudo de Slytherin" style="width: 120px; border-radius: 20px; float: left; margin: 0 20px 10px 0;">En <strong>Slytherin</strong> las cualidades siempre son:<br><br><em>Ambición</em>: Tienen metas muy altas y un fuerte deseo de alcanzar el éxito y destacar.<br><em>Astucia</em>: Son estratégicos, calculadores y saben analizar las situaciones antes de actuar.<br><em>Auto preservación</em>: Piensan con calma y sopesan los riesgos o resultados posibles antes de tomar una decisión.<br><em>Liderazgo e ingenio</em>: Poseen un fuerte carácter para hacerse cargo de las situaciones y encontrar soluciones creativas.<br><em>Determinación</em>: Cuando se ponen un objetivo, son sumamente perseverantes y no se detienen hasta conseguirlo.</div>\n'
    '        <div style="width: 100%; max-width: 700px; margin: 30px auto 0; grid-column: 1 / -1; text-align: justify;"><img src="__HOGWARTS_VARITA__" alt="Mi varita de saúco" style="width: 120px; border-radius: 20px; float: left; margin: 0 20px 10px 0;">La <strong>varita de saúco</strong> es el artefacto más poderoso de todo el mundo mágico. Fue creada por el hermano mayor de los Peverell; Antioch Peverell, ya que el cuento solo fue eso! Un cuento.</div>\n'
    '        <div style="width: 100%; max-width: 700px; margin: 30px auto 0; grid-column: 1 / -1; text-align: justify;"><img src="__HOGWARTS_PATRONUS__" alt="Mi patronus, un dragón" style="width: 120px; border-radius: 20px; float: left; margin: 0 20px 10px 0;">El <strong>patronus de Dragón</strong>, en su rareza: Forma parte de las criaturas legendarias y mágicas (junto al fénix y el unicornio), lo que indica que quien lo conjura posee un nivel de habilidad mágica muy poco común.<br><br>Su presencia: Refleja una fuerza interior inmensa, una intensidad abrumadora y una valentía imposible de intimidar. Son personas con una energía inconfundible, firmeza en sus convicciones y un papel innato de protectores y líderes feroces.</div>\n',
)))
