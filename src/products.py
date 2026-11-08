# Baza produktów Małego Szefa.
# id | nazwa | obrazek | strefa | kolor | en | de | es | słowo (l.poj., do pisowni/liter/głosu) | dopełniacz l.mn. (do liczenia, puste = nie liczymy)
# obrazek: emoji (Fluent 3D) | t:EMOJI:h,s,v (przebarwione emoji) | p:TYP:#KOLOR:EMOJI (opakowanie z ikoną) | d:NAZWA (rysunek)
# strefy: L lodówka, V warzywa, F owoce, S szafka, C słodycze i przekąski, Z zamrażarka
# kolory: r czerwony, y żółty, g zielony, o pomarańczowy, w biały, b brązowy, p fioletowy, k różowy

TABLE = r"""
jajka|Jajka|🥚|L|b|egg|Ei|huevo|jajko|jajek
mleko|Mleko|🥛|L|w|milk|Milch|leche|mleko|
maslo|Masło|🧈|L|y|butter|Butter|mantequilla|masło|
ser_zolty|Ser żółty|🧀|L|y|cheese|Käse|queso|ser|
twarog|Twaróg|t:🧀:0,0.06,1.12|L|w|cottage cheese|Quark|requesón|twaróg|
smietana|Śmietana|p:cup:#DCEBFF:🥛|L|w|sour cream|Sauerrahm|nata agria|śmietana|
smietanka|Śmietanka|p:carton:#FFFFFF:🐄|L|w|cream|Sahne|nata|śmietanka|
jogurt|Jogurt naturalny|p:cup:#FFFFFF:🥄|L|w|yogurt|Joghurt|yogur|jogurt|jogurtów
jogurt_grecki|Jogurt grecki|p:cup:#BFDBFE:🥄|L|w|Greek yogurt|griechischer Joghurt|yogur griego|jogurt|
jogurt_owoc|Jogurt owocowy|p:cup:#FBCFE8:🍓|L|k|fruit yogurt|Fruchtjoghurt|yogur de frutas|jogurt|jogurtów
serek_hom|Serek waniliowy|p:cup:#FDE68A:🍦|L|y|vanilla cheese|Vanillequark|queso de vainilla|serek|serków
kefir|Kefir|p:bottle:#FFFFFF:🐄|L|w|kefir|Kefir|kéfir|kefir|
serek_wiejski|Serek wiejski|p:tub:#D1FAE5:🐄|L|w|cottage cheese|Hüttenkäse|queso fresco|serek|
ser_topiony|Serek topiony|p:tub:#FEF3C7:🧀|L|y|cheese spread|Schmelzkäse|queso fundido|serek|
mozzarella|Mozzarella|d:mozzarella|L|w|mozzarella|Mozzarella|mozzarella|mozzarella|
feta|Feta|p:block:#DBEAFE:🧀|L|w|feta|Feta|queso feta|feta|
parmezan|Parmezan|t:🧀:0,0.6,0.95|L|y|parmesan|Parmesan|parmesano|parmezan|
serek_smietankowy|Serek śmietankowy|p:tub:#FFFFFF:🧀|L|w|cream cheese|Frischkäse|queso crema|serek|
kurczak|Pierś z kurczaka|p:tray:#FCE7E2:🐔|L|k|chicken|Hähnchen|pollo|kurczak|
udka|Udka z kurczaka|🍗|L|b|chicken legs|Hähnchenschenkel|muslos de pollo|udko|udek
indyk|Pierś z indyka|p:tray:#FCE7E2:🦃|L|k|turkey|Pute|pavo|indyk|
mielone|Mięso mielone|p:tray:#FBCFCF:🥩|L|r|minced meat|Hackfleisch|carne picada|mięso|
schab|Schab|🍖|L|k|pork|Schweinefleisch|cerdo|schab|
wolowina|Wołowina|🥩|L|r|beef|Rindfleisch|ternera|wołowina|
boczek|Boczek|🥓|L|r|bacon|Speck|beicon|boczek|
szynka|Szynka|p:tray:#FFE4E6:🐖|L|k|ham|Schinken|jamón|szynka|
kielbasa|Kiełbasa|d:kielbasa|L|r|sausage|Wurst|salchicha|kiełbasa|
parowki|Parówki|🌭|L|k|hot dogs|Würstchen|salchichas|parówka|parówek
kabanosy|Kabanosy|d:kabanosy|L|b|sausage sticks|Mettwurststangen|palitos de salami|kabanos|kabanosów
pasztet|Pasztet|p:block:#E7B98A:🐖|L|b|pâté|Pastete|paté|pasztet|
losos|Łosoś|p:tray:#FDBA8C:🐟|L|o|salmon|Lachs|salmón|łosoś|
ogorek_kiszony|Ogórki kiszone|p:jar:#9CCB8B:🥒|L|g|pickles|Gewürzgurken|pepinillos|ogórek|ogórków
pesto|Pesto|p:jar:#4CAF50:🌿|L|g|pesto|Pesto|pesto|pesto|
ketchup|Ketchup|p:bottle:#E53935:🍅|L|r|ketchup|Ketchup|kétchup|keczup|
musztarda|Musztarda|p:jar:#F2C230:🌭|L|y|mustard|Senf|mostaza|musztarda|
majonez|Majonez|p:jar:#FFFFFF:🥚|L|w|mayonnaise|Mayonnaise|mayonesa|majonez|
tofu|Tofu|p:block:#FFFFFF:🫘|L|w|tofu|Tofu|tofu|tofu|
hummus|Hummus|p:tub:#F3E2B3:🫘|L|y|hummus|Hummus|hummus|hummus|
ziemniaki|Ziemniaki|🥔|V|b|potato|Kartoffel|patata|ziemniak|ziemniaków
bataty|Bataty|🍠|V|o|sweet potato|Süßkartoffel|boniato|batat|batatów
cebula|Cebula|🧅|V|b|onion|Zwiebel|cebolla|cebula|cebul
czosnek|Czosnek|🧄|V|w|garlic|Knoblauch|ajo|czosnek|
por|Por|d:por|V|g|leek|Lauch|puerro|por|
pomidory|Pomidory|🍅|V|r|tomato|Tomate|tomate|pomidor|pomidorów
ogorek|Ogórek|🥒|V|g|cucumber|Gurke|pepino|ogórek|ogórków
papryka|Papryka|🫑|V|g|pepper|Paprika|pimiento|papryka|papryk
marchew|Marchewka|🥕|V|o|carrot|Karotte|zanahoria|marchewka|marchewek
burak|Buraki|d:burak|V|p|beetroot|Rote Bete|remolacha|burak|buraków
cukinia|Cukinia|t:🥒:0,1.1,0.75|V|g|courgette|Zucchini|calabacín|cukinia|cukinii
dynia|Dynia|d:dynia|V|o|pumpkin|Kürbis|calabaza|dynia|
brokul|Brokuł|🥦|V|g|broccoli|Brokkoli|brócoli|brokuł|
kalafior|Kalafior|t:🥦:-75,0.25,1.25|V|w|cauliflower|Blumenkohl|coliflor|kalafior|
fasolka|Fasolka szparagowa|🫛|V|g|green beans|grüne Bohnen|judías verdes|fasolka|
szpinak|Szpinak|🍃|V|g|spinach|Spinat|espinacas|szpinak|
pieczarki|Pieczarki|t:🍄:35,0.35,0.92|V|w|mushroom|Pilz|champiñón|pieczarka|pieczarek
kapusta|Kapusta|🥬|V|g|cabbage|Kohl|col|kapusta|
salata|Sałata|t:🥬:-15,0.7,1.2|V|g|lettuce|Salat|lechuga|sałata|
rukola|Rukola|🌿|V|g|rocket|Rucola|rúcula|rukola|
rzodkiewka|Rzodkiewki|d:rzodkiewka|V|r|radish|Radieschen|rábano|rzodkiewka|rzodkiewek
szczypiorek|Szczypiorek|🌱|V|g|chives|Schnittlauch|cebollino|szczypiorek|
koperek|Koperek|🌿|V|g|dill|Dill|eneldo|koperek|
natka|Natka pietruszki|d:natka|V|g|parsley|Petersilie|perejil|natka|
imbir|Imbir|🫚|V|y|ginger|Ingwer|jengibre|imbir|
banan|Banany|🍌|F|y|banana|Banane|plátano|banan|bananów
jablko|Jabłka|🍎|F|r|apple|Apfel|manzana|jabłko|jabłek
gruszka|Gruszki|🍐|F|g|pear|Birne|pera|gruszka|gruszek
cytryna|Cytryna|🍋|F|y|lemon|Zitrone|limón|cytryna|cytryn
pomarancza|Pomarańcze|🍊|F|o|orange|Orange|naranja|pomarańcza|pomarańczy
mandarynka|Mandarynki|t:🍊:-8,1.1,1.0|F|o|tangerine|Mandarine|mandarina|mandarynka|mandarynek
awokado|Awokado|🥑|F|g|avocado|Avocado|aguacate|awokado|awokado
truskawki|Truskawki|🍓|F|r|strawberry|Erdbeere|fresa|truskawka|truskawek
borowki|Borówki|🫐|F|p|blueberry|Heidelbeere|arándano|borówka|
maliny|Maliny|t:🍓:-25,0.9,1.0|F|k|raspberry|Himbeere|frambuesa|malina|malin
winogrona|Winogrona|🍇|F|p|grapes|Weintrauben|uvas|winogrono|
arbuz|Arbuz|🍉|F|g|watermelon|Wassermelone|sandía|arbuz|
brzoskwinia|Brzoskwinie|🍑|F|o|peach|Pfirsich|melocotón|brzoskwinia|brzoskwiń
sliwki|Śliwki|t:🍑:-120,0.9,0.75|F|p|plum|Pflaume|ciruela|śliwka|śliwek
czeresnie|Czereśnie|🍒|F|r|cherries|Kirschen|cerezas|czereśnia|czereśni
kiwi|Kiwi|🥝|F|g|kiwi|Kiwi|kiwi|kiwi|kiwi
melon|Melon|🍈|F|g|melon|Melone|melón|melon|
mango|Mango|🥭|F|o|mango|Mango|mango|mango|
chleb|Chleb|🍞|S|b|bread|Brot|pan|chleb|
bulki|Bułki|🥖|S|b|bread roll|Brötchen|panecillo|bułka|bułek
rogal|Rogaliki|🥐|S|b|croissant|Croissant|cruasán|rogalik|rogalików
bulka_tarta|Bułka tarta|p:bag:#E8C89A:🍞|S|b|breadcrumbs|Paniermehl|pan rallado|bułka|
tortilla|Tortille|🫓|S|w|tortilla|Tortilla|tortilla|tortilla|tortilli
makaron|Makaron|🍝|S|-|pasta|Nudeln|pasta|makaron|
ryz|Ryż|🍚|S|-|rice|Reis|arroz|ryż|
kasza|Kasza gryczana|p:bag:#C89B6D:🌾|S|b|buckwheat|Buchweizen|trigo sarraceno|kasza|
kasza_jaglana|Kasza jaglana|p:bag:#FFD34D:🌾|S|y|millet|Hirse|mijo|kasza|
kasza_manna|Kasza manna|p:bag:#F5EBD8:🌾|S|w|semolina|Grieß|sémola|kasza|
kuskus|Kuskus|p:bag:#F2D27A:🌾|S|y|couscous|Couscous|cuscús|kuskus|
platki|Płatki owsiane|p:box:#E9C99A:🥣|S|b|oats|Haferflocken|avena|płatki|
platki_kuk|Płatki kukurydziane|p:box:#F59E0B:🌽|S|y|cornflakes|Cornflakes|copos de maíz|płatki|
maka|Mąka|p:bag:#FFFFFF:🌾|S|w|flour|Mehl|harina|mąka|
cukier|Cukier|p:bag:#F8FAFC:🍬|S|w|sugar|Zucker|azúcar|cukier|
sol|Sól|🧂|S|w|salt|Salz|sal|sól|
olej|Olej|p:bottle:#FCD34D:🌻|S|y|oil|Öl|aceite|olej|
passata|Passata|🥫|S|r|tomato sauce|Tomatensoße|salsa de tomate|passata|
fasola|Fasola (puszka)|p:can:#B45309:🫘|S|b|beans|Bohnen|alubias|fasola|
ciecierzyca|Ciecierzyca|p:can:#E0B04F:🫘|S|y|chickpeas|Kichererbsen|garbanzos|ciecierzyca|
soczewica|Soczewica|p:bag:#F08A4B:🫘|S|o|lentils|Linsen|lentejas|soczewica|
kukurydza|Kukurydza (puszka)|p:can:#FACC15:🌽|S|y|corn|Mais|maíz|kukurydza|
ananas|Ananas (puszka)|p:can:#FDE047:🍍|S|y|pineapple|Ananas|piña|ananas|
tunczyk|Tuńczyk|p:can:#3B82F6:🐟|S|-|tuna|Thunfisch|atún|tuńczyk|
kokos|Mleczko kokosowe|p:can:#FFFFFF:🥥|S|w|coconut milk|Kokosmilch|leche de coco|mleczko|
oliwki|Oliwki|p:jar:#65A30D:🫒|S|g|olives|Oliven|aceitunas|oliwka|oliwek
bulion|Kostka rosołowa|p:box:#F59E0B:🍲|S|y|stock cube|Brühwürfel|caldo|kostka|
soja|Sos sojowy|p:bottle:#4A3426:🫘|S|b|soy sauce|Sojasoße|salsa de soja|sos|
curry|Curry|p:spice:#F2B233:🍛|S|y|curry|Curry|curry|curry|
cynamon|Cynamon|d:cynamon|S|b|cinnamon|Zimt|canela|cynamon|
proszek|Proszek do pieczenia|p:sachet:#FFFFFF:🧁|S|w|baking powder|Backpulver|levadura|proszek|
maslo_orz|Masło orzechowe|p:jar:#C68642:🥜|S|b|peanut butter|Erdnussbutter|crema de cacahuete|masło|
miod|Miód|🍯|S|y|honey|Honig|miel|miód|
dzem|Dżem|p:jar:#E53950:🍓|S|r|jam|Marmelade|mermelada|dżem|
kakao|Kakao|p:box:#6B3E26:🍫|S|b|cocoa|Kakao|cacao|kakao|
herbata|Herbata|p:box:#16A34A:🍵|S|g|tea|Tee|té|herbata|
sok|Sok|🧃|S|o|juice|Saft|zumo|sok|soków
woda|Woda|p:bottle:#7DD3FC:💧|S|-|water|Wasser|agua|woda|
budyn|Budyń|p:sachet:#FDE68A:🍮|S|y|pudding|Pudding|natillas|budyń|
kisiel|Kisiel|p:sachet:#F87171:🍒|S|r|fruit jelly drink|Fruchtgrütze|gelatina de frutas|kisiel|
galaretka|Galaretka|p:sachet:#FB7185:🍓|S|r|jelly|Wackelpudding|gelatina|galaretka|
tahini|Tahini|p:jar:#D6B37A:🫘|S|b|tahini|Tahini|tahini|tahini|
sezam|Sezam|p:bag:#F5E6C8:🌱|S|w|sesame|Sesam|sésamo|sezam|
maka_migdalowa|Mąka migdałowa|p:bag:#F3E3C3:🌰|S|w|almond flour|Mandelmehl|harina de almendra|mąka|
erytrytol|Słodzik|p:bag:#FFFFFF:🍬|S|w|sweetener|Süßstoff|edulcorante|słodzik|
czekolada|Czekolada|🍫|C|b|chocolate|Schokolade|chocolate|czekolada|czekolad
ciastka|Ciastka|🍪|C|b|cookies|Kekse|galletas|ciastko|ciastek
wafle|Wafle ryżowe|🍘|C|w|rice cakes|Reiswaffeln|tortitas de arroz|wafel|wafli
precelki|Precelki|🥨|C|b|pretzels|Brezeln|pretzels|precelek|precelków
chrupki|Chrupki kukurydziane|p:bag:#FDE047:🌽|C|y|corn puffs|Maisflips|gusanitos|chrupka|
popcorn|Popcorn|🍿|C|w|popcorn|Popcorn|palomitas|popcorn|
zelki|Żelki|p:bag:#F472B6:🐻|C|k|gummy bears|Gummibärchen|gominolas|żelek|żelków
rodzynki|Rodzynki|p:box:#7C3AED:🍇|C|b|raisins|Rosinen|pasas|rodzynek|
orzechy|Orzechy|🌰|C|b|nuts|Nüsse|nueces|orzech|orzechów
daktyle|Daktyle|p:box:#7B4A2A:🌴|C|b|dates|Datteln|dátiles|daktyl|daktyli
lody|Lody|🍨|Z|w|ice cream|Eis|helado|lody|
frytki_mroz|Frytki mrożone|p:bag:#93C5FD:🍟|Z|y|frozen chips|Pommes frites|patatas fritas|frytki|
paluszki_rybne|Paluszki rybne|p:box:#60A5FA:🐟|Z|o|fish fingers|Fischstäbchen|palitos de pescado|paluszek|paluszków
pierogi_mroz|Pierogi mrożone|p:bag:#BFDBFE:🥟|Z|w|dumplings|Teigtaschen|empanadillas|pieróg|pierogów
pizza_mroz|Pizza mrożona|p:box:#EF4444:🍕|Z|r|frozen pizza|Tiefkühlpizza|pizza congelada|pizza|
warzywa_mroz|Mrożone warzywa|p:bag:#86EFAC:🥦|Z|g|frozen vegetables|Tiefkühlgemüse|verduras congeladas|warzywa|
groszek|Groszek|p:bag:#4ADE80:🫛|Z|g|peas|Erbsen|guisantes|groszek|
dorsz|Ryba (filet)|p:box:#CFE8FF:🐟|Z|w|fish|Fisch|pescado|ryba|
krewetki|Krewetki|🦐|Z|o|prawns|Garnelen|gambas|krewetka|krewetek
"""

# proste dziecięce przepisy z nowymi produktami (m: s śniadanie, o obiad, k kolacja, d deser)
NEW_RECIPES = [
 {"n":"Płatki kukurydziane z mlekiem","m":"s","t":3,"s":1,"k":250,"i":{"platki_kuk":"40 g","mleko":"200 ml"},"o":{"banan":"½ szt."},
  "st":["Wsyp płatki do miski.","Zalej zimnym albo ciepłym mlekiem.","Możesz dodać pokrojonego banana."]},
 {"n":"Kanapki z serkiem topionym","m":"sk","t":5,"s":1,"k":300,"i":{"chleb":"2 kromki","ser_topiony":"2 łyżki"},"o":{"ogorek":"kilka plasterków","szczypiorek":"do posypania"},
  "st":["Posmaruj chleb serkiem.","Połóż plasterki ogórka i posyp szczypiorkiem."]},
 {"n":"Kanapki z pasztetem i ogórkiem","m":"sk","t":5,"s":1,"k":330,"i":{"chleb":"2 kromki","pasztet":"40 g","ogorek":"½ szt."},"o":{"maslo":"cienko"},
  "st":["Posmaruj chleb pasztetem.","Ułóż plasterki ogórka."]},
 {"n":"Paluszki rybne z frytkami","m":"o","t":25,"s":2,"k":520,"i":{"paluszki_rybne":"10 szt.","frytki_mroz":"300 g"},"o":{"ketchup":"do podania","ogorek":"do podania"},
  "st":["Rozgrzej piekarnik do 200°C.","Rozłóż frytki i paluszki na blasze z papierem.","Piecz 18–20 minut, w połowie przewróć."]},
 {"n":"Pierogi z masłem","m":"o","t":15,"s":2,"k":480,"i":{"pierogi_mroz":"400 g","maslo":"20 g"},"o":{"cebula":"1 szt."},
  "st":["Wrzuć zamrożone pierogi do osolonej wrzącej wody.","Gotuj 3–4 minuty od wypłynięcia.","Polej roztopionym masłem."]},
 {"n":"Pizza z piekarnika","m":"ko","t":20,"s":2,"k":600,"i":{"pizza_mroz":"1 szt."},"o":{"papryka":"½ szt.","kukurydza":"2 łyżki"},
  "st":["Rozgrzej piekarnik zgodnie z opakowaniem.","Możesz dołożyć warzywa na wierzch.","Piecz około 12–15 minut."]},
 {"n":"Warzywa na parze z masłem","m":"ok","t":15,"s":2,"k":160,"i":{"warzywa_mroz":"450 g","maslo":"15 g"},"o":{"bulka_tarta":"1 łyżka"},
  "st":["Ugotuj warzywa na parze albo w małej ilości wody, około 8 minut.","Odcedź i dodaj masło."]},
 {"n":"Kabanosy z chrupiącymi warzywami","m":"k","t":5,"s":1,"k":350,"i":{"kabanosy":"3 szt.","ogorek":"½ szt.","papryka":"½ szt."},"o":{"chleb":"1 kromka"},
  "st":["Pokrój warzywa w słupki.","Ułóż na talerzu z kabanosami."]},
 {"n":"Serek waniliowy z owocami","m":"sd","t":3,"s":1,"k":220,"i":{"serek_hom":"1 kubeczek","truskawki":"garść"},"o":{"borowki":"garść"},
  "st":["Przełóż serek do miseczki.","Dodaj umyte owoce."]},
 {"n":"Wafle ryżowe z masłem orzechowym i bananem","m":"sd","t":3,"s":1,"k":280,"i":{"wafle":"2 szt.","maslo_orz":"1 łyżka","banan":"½ szt."},
  "st":["Posmaruj wafle masłem orzechowym.","Połóż plasterki banana."]},
 {"n":"Ryż z jabłkami","m":"od","t":35,"s":3,"k":420,"i":{"ryz":"200 g","jablko":"3 szt.","jogurt":"200 g"},"o":{"cynamon":"szczypta","cukier":"1 łyżka"},
  "st":["Ugotuj ryż.","Zetrzyj jabłka i podduś je chwilę z cynamonem.","Wymieszaj ryż z jabłkami, podawaj z jogurtem."]},
 {"n":"Makaron z truskawkami","m":"od","t":20,"s":2,"k":480,"i":{"makaron":"200 g","truskawki":"300 g","smietana":"150 g"},"o":{"cukier":"1 łyżka"},
  "st":["Ugotuj makaron.","Zmiksuj truskawki ze śmietaną (i cukrem, jeśli trzeba).","Polej makaron sosem truskawkowym."]},
 {"n":"Kasza manna na mleku","m":"s","t":10,"s":1,"k":280,"i":{"kasza_manna":"3 łyżki","mleko":"300 ml"},"o":{"dzem":"1 łyżeczka","maliny":"garść"},
  "st":["Zagotuj mleko.","Wsypuj kaszę, cały czas mieszając.","Gotuj 3 minuty, podawaj z owocami albo dżemem."]},
 {"n":"Zupa mleczna z makaronem","m":"s","t":15,"s":2,"k":300,"i":{"makaron":"80 g","mleko":"500 ml"},"o":{},
  "st":["Ugotuj drobny makaron.","Zagotuj mleko i dodaj do niego makaron."]},
 {"n":"Budyń waniliowy","m":"d","t":10,"s":2,"k":230,"i":{"budyn":"1 opak.","mleko":"500 ml"},"o":{"maliny":"garść"},
  "st":["Zagotuj większość mleka.","Proszek budyniowy rozmieszaj w reszcie mleka i wlej do gotującego się, mieszając.","Gotuj chwilę, aż zgęstnieje."]},
 {"n":"Kisiel z owocami","m":"d","t":10,"s":2,"k":150,"i":{"kisiel":"1 opak."},"o":{"truskawki":"garść"},
  "st":["Zagotuj wodę według przepisu na opakowaniu.","Wlej rozmieszany kisiel, mieszając.","Podawaj z owocami."]},
 {"n":"Galaretka z owocami","m":"d","t":15,"s":4,"k":110,"i":{"galaretka":"1 opak.","truskawki":"150 g"},"o":{"banan":"1 szt."},
  "st":["Rozpuść galaretkę w gorącej wodzie (robi to dorosły).","Ułóż owoce w miseczkach i zalej przestudzoną galaretką.","Wstaw do lodówki na 2 godziny."]},
 {"n":"Sałatka owocowa","m":"sd","t":10,"s":2,"k":170,"i":{"banan":"1 szt.","jablko":"1 szt.","mandarynka":"2 szt."},"o":{"winogrona":"garść","jogurt":"2 łyżki"},
  "st":["Obierz i pokrój owoce (krojenie – dorosły).","Wymieszaj w misce, możesz polać jogurtem."]},
 {"n":"Kakao na mleku","m":"s","t":5,"s":1,"k":200,"i":{"kakao":"1 łyżeczka","mleko":"250 ml"},"o":{"miod":"1 łyżeczka"},
  "st":["Podgrzej mleko.","Wymieszaj z kakao i odrobiną miodu."]},
 {"n":"Naleśniki z dżemem","m":"sd","t":30,"s":3,"k":380,"i":{"maka":"200 g","mleko":"300 ml","jajka":"2 szt.","dzem":"4 łyżki"},"o":{},
  "st":["Zmiksuj mąkę, mleko, jajka i szczyptę soli.","Smaż cienkie naleśniki na rozgrzanej patelni.","Posmaruj dżemem i zwiń."]},
]

# bardzo proste dania „na szybko” (v6)
SIMPLE = [
 ("Frytki z ketchupem","ok",20,2,420,{"frytki_mroz":"400 g","ketchup":"4 łyżki"},{},["Rozgrzej piekarnik do 220°C (dorosły).","Rozłóż frytki na blasze i piecz około 18 minut, w połowie przewróć.","Podawaj z ketchupem."]),
 ("Frytki z parówkami","ok",20,2,560,{"frytki_mroz":"400 g","parowki":"4 szt.","ketchup":"4 łyżki"},{"ogorek":"do podania"},["Upiecz frytki w piekarniku (ok. 18 minut).","Parówki podgrzej w gorącej wodzie przez 4 minuty.","Podawaj z ketchupem."]),
 ("Nuggetsy z frytkami","o",30,2,620,{"kurczak":"300 g","jajka":"1 szt.","bulka_tarta":"5 łyżek","frytki_mroz":"400 g"},{"ketchup":"do podania"},["Pokrój kurczaka w kawałki, obtocz w jajku i bułce tartej.","Upiecz nuggetsy i frytki w piekarniku w 200°C przez ok. 20 minut."]),
 ("Parówki z bułką i ketchupem","sk",7,1,380,{"parowki":"2 szt.","bulki":"1 szt.","ketchup":"1 łyżka"},{"musztarda":"odrobina"},["Podgrzej parówki w gorącej wodzie przez 4 minuty.","Podawaj z bułką i ketchupem."]),
 ("Kanapki z serem","sk",5,1,330,{"chleb":"2 kromki","ser_zolty":"2 plastry"},{"maslo":"cienko","pomidory":"kilka plasterków"},["Posmaruj chleb masłem.","Połóż plasterki sera."]),
 ("Kanapki z szynką","sk",5,1,300,{"chleb":"2 kromki","szynka":"2 plastry"},{"maslo":"cienko","ogorek":"kilka plasterków"},["Posmaruj chleb masłem.","Połóż szynkę."]),
 ("Chleb z masłem i dżemem","sd",3,1,280,{"chleb":"2 kromki","dzem":"2 łyżeczki"},{"maslo":"cienko"},["Posmaruj chleb masłem i dżemem."]),
 ("Chleb z masłem i miodem","s",3,1,270,{"chleb":"2 kromki","miod":"2 łyżeczki"},{"maslo":"cienko"},["Posmaruj chleb masłem i miodem."]),
 ("Tosty z serem","sk",8,1,360,{"chleb":"2 kromki","ser_zolty":"2 plastry"},{"ketchup":"do podania"},["Włóż ser między kromki.","Opiecz w tosterze albo na patelni (dorosły) 3–4 minuty."]),
 ("Ziemniaki z jajkiem sadzonym","o",25,2,430,{"ziemniaki":"600 g","jajka":"4 szt."},{"ogorek":"1 szt.","koperek":"do posypania"},["Ugotuj ziemniaki w osolonej wodzie (ok. 20 minut).","Usmaż jajka sadzone.","Podawaj z ogórkiem albo mizerią."]),
 ("Makaron z masłem i serem","o",15,2,480,{"makaron":"200 g","ser_zolty":"60 g"},{"maslo":"20 g"},["Ugotuj makaron.","Wymieszaj z masłem i startym serem."]),
 ("Makaron z ketchupem i serem","o",15,2,470,{"makaron":"200 g","ketchup":"4 łyżki","ser_zolty":"50 g"},{},["Ugotuj makaron.","Wymieszaj z ketchupem i posyp startym serem."]),
 ("Kiełbaska z chlebem","k",10,1,420,{"kielbasa":"100 g","chleb":"1 kromka"},{"ketchup":"do podania","ogorek_kiszony":"1 szt."},["Podsmaż albo podgrzej kiełbaskę (dorosły).","Podawaj z chlebem i ketchupem."]),
 ("Jogurt z bananem","sd",3,1,200,{"jogurt":"1 kubek","banan":"1 szt."},{"miod":"1 łyżeczka"},["Pokrój banana w plasterki (nożyk – dorosły).","Wymieszaj z jogurtem."]),
 ("Banan z masłem orzechowym","d",3,1,230,{"banan":"1 szt.","maslo_orz":"1 łyżka"},{},["Obierz banana.","Maczaj w maśle orzechowym."]),
 ("Lody z owocami","d",5,2,260,{"lody":"4 gałki","truskawki":"garść"},{"borowki":"garść"},["Nałóż lody do miseczek.","Dodaj umyte owoce."]),
 ("Jajko na twardo z chlebem","sk",12,1,280,{"jajka":"2 szt.","chleb":"1 kromka"},{"szczypiorek":"do posypania","maslo":"cienko"},["Gotuj jajka 9 minut (dorosły).","Ostudź w zimnej wodzie, obierz i podawaj z chlebem."]),
 ("Kanapki z jajkiem","sk",12,1,300,{"chleb":"2 kromki","jajka":"2 szt."},{"maslo":"cienko","szczypiorek":"do posypania"},["Ugotuj jajka na twardo (9 minut, dorosły).","Obierz, pokrój w plasterki i połóż na chlebie z masłem."]),
 ("Naleśniki z cukrem","sd",30,3,350,{"maka":"200 g","mleko":"300 ml","jajka":"2 szt."},{"cukier":"do posypania"},["Zmiksuj mąkę, mleko, jajka i szczyptę soli.","Smaż cienkie naleśniki (dorosły).","Posyp cukrem i zwiń."]),
 ("Mleko z płatkami owsianymi","s",5,1,280,{"platki":"40 g","mleko":"250 ml"},{"miod":"1 łyżeczka","banan":"½ szt."},["Podgrzej mleko.","Zalej płatki i odstaw na 2 minuty."]),
 ("Pomidory z serem","k",5,1,250,{"pomidory":"2 szt.","ser_zolty":"40 g"},{"chleb":"1 kromka"},["Pokrój pomidory i ser (nożyk – dorosły).","Ułóż na talerzu."]),
]
for n, m, t, s_, k, i, o, st in SIMPLE:
    NEW_RECIPES.append({"n": n, "m": m, "t": t, "s": s_, "k": k, "i": i, "o": o, "st": st})

def parse():
    out = {}
    for line in TABLE.strip().splitlines():
        f = line.split("|")
        assert len(f) == 10, line
        k, name, img, zone, col, en, de, es, sp, cnt = f
        out[k] = dict(name=name, img=img, zone=zone, col="" if col == "-" else col, en=en, de=de, es=es, sp=sp, cnt=cnt)
    return out
