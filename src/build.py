#!/usr/bin/env python3
"""Mały Szef – buduje wersję webową (index.html, sw.js, manifest, ikony) do katalogu out/.
Użycie: python3 build.py v1"""
import json, sys, os, re
from PIL import Image, ImageDraw, ImageFont

VER = sys.argv[1] if len(sys.argv) > 1 else "v1"
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
os.makedirs(OUT, exist_ok=True)
src = json.load(open(os.path.join(HERE, "src.json")))  # wyciągnięte z Co z lodówki (extract.js)

# id: emoji, strefa (L lodówka, S szafka, W warzywa i owoce, Z zamrażarka), kolor, en, de, es
P = {
"jajka":"🥚 L w|egg|Ei|huevo","mleko":"🥛 L w|milk|Milch|leche","maslo":"🧈 L y|butter|Butter|mantequilla",
"ser_zolty":"🧀 L y|cheese|Käse|queso","twarog":"🧀 L w|cottage cheese|Quark|requesón","smietana":"🫙 L w|sour cream|Sauerrahm|nata agria",
"smietanka":"🫙 L w|cream|Sahne|nata","jogurt":"🥣 L w|yogurt|Joghurt|yogur","jogurt_grecki":"🥣 L w|Greek yogurt|griechischer Joghurt|yogur griego",
"kefir":"🥛 L w|kefir|Kefir|kéfir","serek_wiejski":"🥣 L w|cottage cheese|Hüttenkäse|queso fresco","mozzarella":"🧀 L w|mozzarella|Mozzarella|mozzarella",
"feta":"🧀 L w|feta|Feta|queso feta","parmezan":"🧀 L y|parmesan|Parmesan|parmesano","kurczak":"🍗 L -|chicken|Hähnchen|pollo",
"udka":"🍗 L -|chicken legs|Hähnchenschenkel|muslos de pollo","indyk":"🦃 L -|turkey|Pute|pavo","mielone":"🥩 L r|minced meat|Hackfleisch|carne picada",
"schab":"🥩 L -|pork|Schweinefleisch|cerdo","wolowina":"🥩 L r|beef|Rindfleisch|ternera","boczek":"🥓 L r|bacon|Speck|beicon",
"szynka":"🍖 L -|ham|Schinken|jamón","kielbasa":"🌭 L r|sausage|Wurst|salchicha","parowki":"🌭 L -|sausages|Würstchen|salchichas",
"losos":"🐟 L o|salmon|Lachs|salmón","dorsz":"🐟 Z w|fish|Fisch|pescado","tunczyk":"🥫 S -|tuna|Thunfisch|atún",
"krewetki":"🦐 Z o|prawns|Garnelen|gambas","ziemniaki":"🥔 W b|potato|Kartoffel|patata","bataty":"🍠 W o|sweet potato|Süßkartoffel|boniato",
"cebula":"🧅 W -|onion|Zwiebel|cebolla","czosnek":"🧄 W w|garlic|Knoblauch|ajo","por":"🥬 W g|leek|Lauch|puerro",
"pomidory":"🍅 W r|tomato|Tomate|tomate","ogorek":"🥒 W g|cucumber|Gurke|pepino","ogorek_kiszony":"🥒 L g|pickle|Gewürzgurke|pepinillo",
"papryka":"🫑 W -|pepper|Paprika|pimiento","marchew":"🥕 W o|carrot|Karotte|zanahoria","burak":"🟣 W p|beetroot|Rote Bete|remolacha",
"cukinia":"🥒 W g|courgette|Zucchini|calabacín","dynia":"🎃 W o|pumpkin|Kürbis|calabaza","brokul":"🥦 W g|broccoli|Brokkoli|brócoli",
"kalafior":"🥦 W w|cauliflower|Blumenkohl|coliflor","fasolka":"🫛 W g|green beans|grüne Bohnen|judías verdes","groszek":"🫛 Z g|peas|Erbsen|guisantes",
"szpinak":"🥬 W g|spinach|Spinat|espinacas","pieczarki":"🍄 W w|mushroom|Pilz|champiñón","kapusta":"🥬 W g|cabbage|Kohl|col",
"salata":"🥬 W g|lettuce|Salat|lechuga","rukola":"🌿 W g|rocket|Rucola|rúcula","rzodkiewka":"🔴 W r|radish|Radieschen|rábano",
"szczypiorek":"🌿 W g|chives|Schnittlauch|cebollino","koperek":"🌿 W g|dill|Dill|eneldo","natka":"🌿 W g|parsley|Petersilie|perejil",
"imbir":"🫚 W y|ginger|Ingwer|jengibre","banan":"🍌 W y|banana|Banane|plátano","jablko":"🍎 W r|apple|Apfel|manzana",
"gruszka":"🍐 W g|pear|Birne|pera","cytryna":"🍋 W y|lemon|Zitrone|limón","awokado":"🥑 W g|avocado|Avocado|aguacate",
"truskawki":"🍓 W r|strawberry|Erdbeere|fresa","borowki":"🫐 W p|blueberry|Heidelbeere|arándano","maliny":"🍓 W r|raspberry|Himbeere|frambuesa",
"mango":"🥭 W o|mango|Mango|mango","ananas":"🍍 S y|pineapple|Ananas|piña","chleb":"🍞 S b|bread|Brot|pan",
"bulka_tarta":"🍞 S b|breadcrumbs|Paniermehl|pan rallado","tortilla":"🫓 S w|tortilla|Tortilla|tortilla","makaron":"🍝 S y|pasta|Nudeln|pasta",
"ryz":"🍚 S w|rice|Reis|arroz","kasza":"🌾 S b|buckwheat|Buchweizen|trigo sarraceno","kasza_jaglana":"🌾 S y|millet|Hirse|mijo",
"kasza_manna":"🌾 S w|semolina|Grieß|sémola","kuskus":"🌾 S y|couscous|Couscous|cuscús","platki":"🥣 S b|oats|Haferflocken|avena",
"maka":"🌾 S w|flour|Mehl|harina","passata":"🥫 S r|tomato sauce|Tomatensoße|salsa de tomate","fasola":"🫘 S -|beans|Bohnen|alubias",
"ciecierzyca":"🫘 S y|chickpeas|Kichererbsen|garbanzos","soczewica":"🫘 S o|lentils|Linsen|lentejas","kukurydza":"🌽 S y|corn|Mais|maíz",
"kokos":"🥥 S w|coconut milk|Kokosmilch|leche de coco","oliwki":"🫒 S g|olives|Oliven|aceitunas","bulion":"🍲 S -|stock cube|Brühwürfel|caldo",
"soja":"🍶 S b|soy sauce|Sojasoße|salsa de soja","pesto":"🫙 L g|pesto|Pesto|pesto","musztarda":"🫙 L y|mustard|Senf|mostaza",
"majonez":"🫙 L w|mayonnaise|Mayonnaise|mayonesa","ketchup":"🍅 L r|ketchup|Ketchup|kétchup","curry":"🧂 S y|curry|Curry|curry",
"maslo_orz":"🥜 S b|peanut butter|Erdnussbutter|crema de cacahuete","miod":"🍯 S y|honey|Honig|miel","dzem":"🫙 S r|jam|Marmelade|mermelada",
"kakao":"🍫 S b|cocoa|Kakao|cacao","czekolada":"🍫 S b|chocolate|Schokolade|chocolate","proszek":"🧂 S w|baking powder|Backpulver|levadura",
"cynamon":"🟤 S b|cinnamon|Zimt|canela","orzechy":"🌰 S b|nuts|Nüsse|nueces","rodzynki":"🍇 S b|raisins|Rosinen|pasas",
"tofu":"⬜ L w|tofu|Tofu|tofu","hummus":"🫙 L y|hummus|Hummus|hummus","tahini":"🫙 S b|tahini|Tahini|tahini","sezam":"⚪ S w|sesame|Sesam|sésamo",
"daktyle":"🌴 S b|dates|Datteln|dátiles","bulki":"🥖 S b|bread rolls|Brötchen|panecillos","maka_migdalowa":"🌾 S w|almond flour|Mandelmehl|harina de almendra",
"serek_smietankowy":"🧀 L w|cream cheese|Frischkäse|queso crema","erytrytol":"🧂 S w|sweetener|Süßstoff|edulcorante",
}
prods = {}
for k, (name, cat) in src["ING"].items():
    head, en, de, es = P[k].split("|")
    emo, zone, col = head.split(" ")
    prods[k] = [name.split(" (")[0].split(" / ")[0], emo, zone, "" if col == "-" else col, en, de, es]

EXTRA = """Placuszki bananowe|Parówki z musztardą|Zapiekanka makaronowa z brokułem|Kurczak miodowo-musztardowy z ryżem|Nuggetsy z kurczaka|
Quesadilla z fasolą|Pizza na tortilli|Leniwa lasagne makaronowa|Jajecznica z parówkami|Naleśniki z szynką i serem|Frytki z batatów|Kopytka|
Placuszki jogurtowe z borówkami|Pierogi ruskie|Kurczak z brokułem w sosie serowym|Kluski kładzione|Naleśniki z jabłkami i cynamonem|
Parówki zapiekane w tortilli z serem|Quesadilla z kurczakiem|Placuszki dyniowe|Zapiekanka makaronowa z kurczakiem|Kurczak z ryżem z jednego garnka"""
EXTRA = {x.strip() for x in EXTRA.split("|")}
SKIP = {"Sałatka grecka", "Mizeria", "Surówka z kapusty"}

EMO = [(r"pizz", "🍕"), (r"lody", "🍦"), (r"szaszłyki owoc", "🍓"), (r"mus jabł", "🍎"), (r"koktajl", "🥤"), (r"szarlotk", "🥧"),
       (r"ciasteczk", "🍪"), (r"babecz|muffin", "🧁"), (r"gofr", "🧇"), (r"naleś|pancake|placuszk|placki|racuch", "🥞"),
       (r"zup|rosół|ogórkowa|pomidorowa|jarzynowa", "🍲"), (r"spaghetti|makaron|lasagne", "🍝"), (r"pierog|kopytk|kluski", "🥟"),
       (r"parów", "🌭"), (r"burger", "🍔"), (r"frytk", "🍟"), (r"tortill|quesadill|roladki", "🌯"), (r"kanap|tost|buźki|żołnierzyk|grzank", "🥪"),
       (r"paluszki rybne|łoso|ryb", "🐟"), (r"nuggets|kurczak|udka|kotleciki z kurczaka", "🍗"), (r"jaj|omlet", "🍳"),
       (r"owsiank|kasza jaglana z", "🥣"), (r"ryż", "🍚"), (r"kotlet|schabow|pulpe|gołąbki", "🍖"), (r"kapust", "🥬"),
       (r"ziemnia|zapiekank", "🥔"), (r"kasz", "🥣"), (r"twaroż|pasta", "🥣")]
def emo(n):
    for rx, e in EMO:
        if re.search(rx, n, re.I): return e
    return "🍽️"

SWEET_ING = {"czekolada", "kakao", "dzem", "miod", "erytrytol", "daktyle"}
recipes = []
for r in src["ALLR"]:
    kid = "dzieci" in r["g"]
    if not (kid or (r.get("b") and r["n"] not in SKIP) or r["n"] in EXTRA): continue
    sweet = 1 if ("d" in r["m"] or SWEET_ING & set(r["i"])) else 0
    recipes.append({"n": r["n"], "e": emo(r["n"]), "m": r["m"], "t": r["t"], "s": r["s"], "k": r["k"], "i": r["i"], "o": r.get("o", {}),
                    "st": r["st"], "gr": "kids" if kid else ("base" if r.get("b") else "more"), "sw": sweet})
used = set()
for r in recipes: used |= set(r["i"])
prods = {k: v for k, v in prods.items() if k in used}
data = {"P": prods, "R": recipes, "ALG": src["ALG"]}
print(len(recipes), "przepisów,", len(prods), "produktów")

html = open(os.path.join(HERE, "app.html"), encoding="utf-8").read()
html = html.replace("/*__DATA__*/", "const D=" + json.dumps(data, ensure_ascii=False, separators=(",", ":")) + ";")
html = html.replace("__VER__", VER)
open(os.path.join(OUT, "index.html"), "w", encoding="utf-8").write(html)

sw = """const C="maly-szef-%s";
const FILES=["./","./index.html","./manifest.webmanifest","./icon-192.png","./icon-512.png","./apple-touch-icon.png"];
self.addEventListener("install",e=>{e.waitUntil(caches.open(C).then(c=>c.addAll(FILES)));self.skipWaiting()});
self.addEventListener("activate",e=>{e.waitUntil(caches.keys().then(k=>Promise.all(k.filter(x=>x!==C).map(x=>caches.delete(x)))));self.clients.claim()});
self.addEventListener("fetch",e=>{
  if(e.request.method!=="GET")return;
  const u=new URL(e.request.url);
  if(u.origin===location.origin){
    // najpierw sieć (aktualizacje), bez sieci — zapisana kopia
    e.respondWith(fetch(e.request,{cache:"no-cache"}).then(r=>{const cp=r.clone();caches.open(C).then(c=>c.put(e.request,cp));return r}).catch(()=>caches.match(e.request,{ignoreSearch:true}).then(r=>r||caches.match("./index.html"))));
  }else if(u.hostname.includes("fonts.g")){
    e.respondWith(caches.match(e.request).then(r=>r||fetch(e.request).then(res=>{const cp=res.clone();caches.open(C).then(c=>c.put(e.request,cp));return res})));
  }
});
""" % VER
open(os.path.join(OUT, "sw.js"), "w").write(sw)

man = {"name": "Mały Szef", "short_name": "Mały Szef", "lang": "pl", "start_url": "./", "scope": "./", "display": "standalone",
       "orientation": "portrait", "background_color": "#FFF4E3", "theme_color": "#FFF4E3",
       "icons": [{"src": "icon-192.png", "sizes": "192x192", "type": "image/png"},
                 {"src": "icon-512.png", "sizes": "512x512", "type": "image/png"},
                 {"src": "icon-maskable-512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable"}]}
json.dump(man, open(os.path.join(OUT, "manifest.webmanifest"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)

# ikona: emoji kucharza na pomarańczowym tle
font = ImageFont.truetype("/usr/share/fonts/truetype/noto/NotoColorEmoji.ttf", 109)
g = Image.new("RGBA", (136, 128), (0, 0, 0, 0))
ImageDraw.Draw(g).text((0, 0), "🧑‍🍳", font=font, embedded_color=True)
g = g.crop(g.getbbox())
def icon(size, scale, path, round_=False):
    im = Image.new("RGBA", (size, size), (255, 122, 69, 255))
    if round_:
        im = Image.new("RGBA", (size, size), (0, 0, 0, 0))
        ImageDraw.Draw(im).rounded_rectangle((0, 0, size - 1, size - 1), radius=size // 5, fill=(255, 122, 69, 255))
    w = int(size * scale); e = g.resize((w, int(w * g.height / g.width)), Image.LANCZOS)
    im.alpha_composite(e, ((size - e.width) // 2, (size - e.height) // 2))
    im.save(os.path.join(OUT, path))
icon(192, .7, "icon-192.png"); icon(512, .7, "icon-512.png"); icon(512, .55, "icon-maskable-512.png"); icon(180, .7, "apple-touch-icon.png")
open(os.path.join(OUT, ".nojekyll"), "w").close()
print("OK", VER)
