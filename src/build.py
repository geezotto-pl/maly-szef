#!/usr/bin/env python3
"""Mały Szef – buduje wersję webową do katalogu out/.
Użycie: python3 build.py v2 [--assets]   (--assets: generuje też obrazki i dźwięki)"""
import json, sys, os, re, subprocess
import products

VER = sys.argv[1] if len(sys.argv) > 1 else "v2"
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
os.makedirs(OUT, exist_ok=True)
if "--assets" in sys.argv:
    subprocess.run([sys.executable, os.path.join(HERE, "imagegen.py"), "/home/claude/emoji/f3d/package/assets", os.path.join(OUT, "img")], check=True)
    subprocess.run([sys.executable, os.path.join(HERE, "soundgen.py"), os.path.join(OUT, "snd")], check=True)

src = json.load(open(os.path.join(HERE, "src.json")))  # przepisy z Co z lodówki (extract.js)
PT = products.parse()

# ---- pisownia: błędne warianty do zadania „Jak się pisze?” (dla 7–10 lat)
RULES = [("ó", "u"), ("ó", "o"), ("rz", "ż"), ("rz", "sz"), ("ż", "rz"), ("ż", "sz"), ("ch", "h"), ("h", "ch"), ("u", "ó"),
         ("ą", "on"), ("ą", "om"), ("ę", "en"), ("ę", "em"), ("dk", "tk"), ("wk", "fk"), ("bk", "pk"),
         ("b", "p"), ("d", "t"), ("g", "k"), ("w", "f")]
HINT = [("ó", "ó z kreską"), ("rz", "rz"), ("ż", "ż z kropką"), ("ch", "ch"), ("h", "samo h"), ("ą", "ą"), ("ę", "ę"),
        ("dk", "d, choć słychać t"), ("wk", "w, choć słychać f"), ("bk", "b, choć słychać p"), ("u", "zwykłe u")]
NO_SPELL = {"hummus", "kuskus", "tahini", "pesto", "curry", "mango", "kiwi", "tofu"}  # obce słowa
FINAL = {"b": "p", "d": "t", "g": "k", "w": "f"}  # ubezdźwięcznienie na końcu wyrazu
def misspell(w):
    if w in NO_SPELL: return []
    out = []
    for a, b in RULES:
        if a == "h" and "ch" in w: continue
        if a == "u" and "ó" in w: continue
        i = w.find(a)
        while i >= 0:
            ok = True
            if a == "rz" and b == "sz": ok = i > 0 and w[i - 1] in "ptk"            # przy, trzy, krzesło
            if a == "ż" and b == "sz": ok = i == len(w) - 1                          # ryż → rysz
            if a in FINAL: ok = i == len(w) - 1 and w.endswith(a)                    # chleb → chlep
            if ok:
                v = w[:i] + b + w[i + len(a):]
                if v != w and v not in out: out.append(v)
            i = w.find(a, i + 1)
    return out
def hint(w):
    for a, t in HINT:
        if a in w and not (a == "h" and "ch" in w): return t
    return ""

P = {}
for k, p in PT.items():
    sp = p["sp"]
    bad = misspell(sp) if " " not in sp else []
    P[k] = [p["name"], p["zone"], p["col"], p["en"], p["de"], p["es"], sp, p["cnt"], bad[:4], hint(sp) if len(bad) >= 1 else "", 0 if p["img"].startswith("p:") else 1]

# ---- przepisy
EXTRA = """Placuszki bananowe|Parówki z musztardą|Zapiekanka makaronowa z brokułem|Kurczak miodowo-musztardowy z ryżem|Nuggetsy z kurczaka|
Quesadilla z fasolą|Pizza na tortilli|Leniwa lasagne makaronowa|Jajecznica z parówkami|Naleśniki z szynką i serem|Frytki z batatów|Kopytka|
Placuszki jogurtowe z borówkami|Pierogi ruskie|Kurczak z brokułem w sosie serowym|Kluski kładzione|Naleśniki z jabłkami i cynamonem|
Parówki zapiekane w tortilli z serem|Quesadilla z kurczakiem|Placuszki dyniowe|Zapiekanka makaronowa z kurczakiem|Kurczak z ryżem z jednego garnka"""
EXTRA = {x.strip() for x in EXTRA.split("|")}
SKIP = {"Sałatka grecka", "Mizeria", "Surówka z kapusty"}
# v7: proste dania z jajek, mleka, chleba itp. z „Co z lodówki?” – w grupie „Dla dzieci”
KIDS_EXTRA = """Tosty francuskie|Jajko w okienku|Tost z masłem orzechowym i bananem|Smoothie bananowo-truskawkowe|Pieczone jabłka z cynamonem|
Ryż na mleku z jabłkami|Lody bananowe|Kiełbasa z cebulką i ziemniakami|Makaron z szynką i groszkiem|Krem z zielonego groszku|Ryż z warzywami|
Pudding z kaszy manny z malinami|Serek wiejski z truskawkami|Śniadaniowe burrito|Omlet na słodko z dżemem|Kanapki z twarożkiem i dżemem|
Owsianka czekoladowa z malinami|Pieczone gruszki z miodem|Gorąca czekolada|Frittata z ziemniakami|Sałatka z makaronem i szynką|
Placki twarogowe (serniczki)|Ciasteczka owsiane|Placki bananowo-kakaowe|Owsianka z gruszką i cynamonem|Koktajl malinowy|Ciasto w kubku|
Twarożek z pomidorami i szczypiorkiem|Pancakes twarogowe|Twarożek z borówkami i orzechami|Pudding twarogowo-kakaowy"""
KIDS_EXTRA = {x.strip() for x in KIDS_EXTRA.split("|")}
EMO = [(r"tosty francuskie|jajko w okienku|frittata", ""), (r"ciasto w kubku", "🧁"), (r"pudding", "🍮"), (r"burrito", "🌯"),
       (r"gorąca czekolada|smoothie", "🥤"), (r"placki (twarog|banan)", "🥞"), (r"pizz", "🍕"), (r"^lody", "🍦"), (r"szaszłyki owoc", "🍓"), (r"mus jabł", "🍎"), (r"koktajl|kakao", "🥤"), (r"szarlotk", "🥧"),
       (r"ciasteczk", "🍪"), (r"babecz|muffin", "🧁"), (r"gofr", "🧇"), (r"budyń", "🍮"), (r"kisiel|galaretk", "🍒"), (r"sałatka owoc", "🍊"),
       (r"zup|rosół|ogórkowa", "🍲"), (r"spaghetti|makaron|lasagne", "🍝"), (r"naleś|pancake|placuszk|racuch", "🥞"), (r"pierog", "🥟"),
       (r"parów", "🌭"), (r"burger", "🍔"), (r"frytk", "🍟"), (r"tortill|quesadill|roladki", "🌯"), (r"^(kanap|tost)|buźki|żołnierzyk|grzank", "🥪"),
       (r"^(jajecznica|omlet|jajka sadzone)", "🍳"), (r"^owsiank|^płatki|kasza manna|kasza jaglana z musem", "🥣")]
def emo(n):
    for rx, e in EMO:
        if re.search(rx, n, re.I): return e
    return ""
def cp(e): return "-".join(f"{ord(c):x}" for c in e if ord(c) != 0xFE0F)

SWEET_ING = {"czekolada", "kakao", "dzem", "miod", "erytrytol", "daktyle", "budyn", "kisiel", "galaretka"}
recipes = []
STRONG = set("🍕🍦🍓🍎🥤🥧🍪🧁🧇🥞🍮🍒🍊🍲🍝🥟🌭🍔🍟🌯🥪🍳🥣")   # dania z jednoznacznym emoji
DRAWN = [(r"kopytk", "kopytka"), (r"kluski", "kluski"), (r"placki ziemniaczane", "placki")]
MEAT = ["kurczak","udka","indyk","mielone","schab","wolowina","boczek","szynka","kielbasa","parowki","kabanosy","losos","dorsz","tunczyk","krewetki","paluszki_rybne","tofu"]
CARB = ["ziemniaki","frytki_mroz","ryz","makaron","kasza","kasza_jaglana","kasza_manna","kuskus","bataty","chleb","bulki","tortilla","pierogi_mroz","platki"]
MINOR = {"maka","maslo","smietana","smietanka","cebula","czosnek","bulion","sol","olej","cukier","proszek","cynamon","curry","soja","musztarda",
         "majonez","bulka_tarta","mleko","natka","koperek","szczypiorek","woda","jajka","imbir","passata","kokos","ketchup"}
def dish_image(r):
    n = r["n"]
    for rx, key in DRAWN:
        if re.search(rx, n, re.I): return ("draw", key)
    e = emo(n)
    if e in STRONG: return ("emoji", e)
    ing = list(r["i"])
    meat = [k for k in ing if k in MEAT]; carb = [k for k in ing if k in CARB]
    other = [k for k in ing if k not in MEAT and k not in CARB and k not in MINOR]
    pick = (meat[:1] + carb[:1] + other)[:3]
    if len(pick) < 2: pick += [k for k in ing if k not in pick and k in ("jajka", "ketchup", "passata")][:2 - len(pick)]
    if not pick: pick = ing[:1]
    return ("plate", pick)

def add(r, gr):
    e = emo(r["n"])
    sweet = 1 if ("d" in r["m"] or SWEET_ING & set(r["i"])) else 0
    for k in list(r["i"]) + list(r.get("o", {})): assert k in P, (r["n"], k)
    kind, val = dish_image(r)
    im = "e-" + cp(val) if kind == "emoji" else "d-" + re.sub(r"[^a-z0-9]+", "-", r["n"].lower().translate(str.maketrans("ąćęłńóśźż", "acelnoszz"))).strip("-")
    recipes.append({"n": r["n"], "im": im, "m": r["m"], "t": r["t"], "s": r["s"], "k": r["k"], "i": r["i"], "o": r.get("o", {}),
                    "st": r["st"], "gr": gr, "sw": sweet, "_img": (kind, val)})

for r in src["ALLR"]:
    kid = "dzieci" in r["g"]
    if kid or r["n"] in KIDS_EXTRA or (r.get("b") and r["n"] not in SKIP) or r["n"] in EXTRA:
        add(r, "kids" if (kid or r["n"] in KIDS_EXTRA) else ("base" if r.get("b") else "more"))
for r in products.NEW_RECIPES: add(r, "kids")
import imagegen
imagegen.OUT = os.path.join(OUT, "img")
os.makedirs(os.path.join(OUT, "img"), exist_ok=True)
for r in recipes:
    kind, val = r.pop("_img")
    path = os.path.join(OUT, "img", r["im"] + ".webp")
    if kind == "emoji":
        if not os.path.exists(path): imagegen.save(imagegen.emoji(val, imagegen.N).resize((imagegen.SIZE, imagegen.SIZE)), r["im"])
    elif kind == "draw": imagegen.dish_drawn(val).resize((imagegen.SIZE, imagegen.SIZE), imagegen.Image.LANCZOS).save(path, "WEBP", quality=88, method=6)
    else: imagegen.plate_of([PT[k]["img"] for k in val]).resize((imagegen.SIZE, imagegen.SIZE), imagegen.Image.LANCZOS).save(path, "WEBP", quality=88, method=6)
data = {"P": P, "R": recipes, "ALG": src["ALG"]}
print(len(recipes), "przepisów,", len(P), "produktów,", sum(1 for v in P.values() if v[9]), "słów do pisowni")

html = open(os.path.join(HERE, "app.html"), encoding="utf-8").read()
html = html.replace("/*__DATA__*/", "const D=" + json.dumps(data, ensure_ascii=False, separators=(",", ":")) + ";")
html = html.replace("__VER__", VER)
open(os.path.join(OUT, "index.html"), "w", encoding="utf-8").write(html)

# service worker: najpierw sieć (aktualizacje), bez sieci zapisana kopia; obrazki i dźwięki z cache
imgs = sorted("./img/" + f for f in os.listdir(os.path.join(OUT, "img")))
snds = sorted("./snd/" + f for f in os.listdir(os.path.join(OUT, "snd")))
sw = """const C="maly-szef-%s";
const CORE=["./","./index.html","./manifest.webmanifest","./icon-192.png","./icon-512.png","./apple-touch-icon.png"];
const MEDIA=%s;
self.addEventListener("install",e=>{e.waitUntil(caches.open(C).then(async c=>{await c.addAll(CORE);try{await c.addAll(MEDIA)}catch(x){}}));self.skipWaiting()});
self.addEventListener("activate",e=>{e.waitUntil(caches.keys().then(k=>Promise.all(k.filter(x=>x!==C).map(x=>caches.delete(x)))));self.clients.claim()});
self.addEventListener("fetch",e=>{
  if(e.request.method!=="GET")return;
  const u=new URL(e.request.url);
  if(u.origin===location.origin){
    if(/\\/(img|snd)\\//.test(u.pathname)){ // obrazki i dźwięki: najpierw cache
      e.respondWith(caches.match(e.request).then(r=>r||fetch(e.request).then(res=>{const cp=res.clone();caches.open(C).then(c=>c.put(e.request,cp));return res})));return}
    e.respondWith(fetch(e.request,{cache:"no-cache"}).then(r=>{const cp=r.clone();caches.open(C).then(c=>c.put(e.request,cp));return r}).catch(()=>caches.match(e.request,{ignoreSearch:true}).then(r=>r||caches.match("./index.html"))));
  }else if(u.hostname.includes("fonts.g")){
    e.respondWith(caches.match(e.request).then(r=>r||fetch(e.request).then(res=>{const cp=res.clone();caches.open(C).then(c=>c.put(e.request,cp));return res})));
  }
});
""" % (VER, json.dumps(imgs + snds))
open(os.path.join(OUT, "sw.js"), "w").write(sw)

man = {"name": "Mały Szef", "short_name": "Mały Szef", "lang": "pl", "start_url": "./", "scope": "./", "display": "standalone",
       "orientation": "portrait", "background_color": "#FFF4E3", "theme_color": "#FFF4E3",
       "icons": [{"src": "icon-192.png", "sizes": "192x192", "type": "image/png"},
                 {"src": "icon-512.png", "sizes": "512x512", "type": "image/png"},
                 {"src": "icon-maskable-512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable"}]}
json.dump(man, open(os.path.join(OUT, "manifest.webmanifest"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
open(os.path.join(OUT, ".nojekyll"), "w").close()
print("OK", VER)
