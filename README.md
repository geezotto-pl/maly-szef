# Mały Szef 🧑‍🍳

Aplikacja dla rodziców niejadków. Dziecko chodzi po kuchni i zaznacza, co znajdzie w lodówce i szafkach. Po drodze rozwiązuje mini-zadania: słówka po angielsku, kolory i liczenie. Rodzic zatwierdza 2–3 dania, a dziecko samo wybiera, co zje, i dostaje naklejkę.

**Otwórz:** https://geezotto-pl.github.io/maly-szef/

## Instalacja na telefonie
- **iPhone:** otwórz link w Safari, stuknij **Udostępnij** i wybierz **Do ekranu początkowego**.
- **Android:** otwórz link w Chrome, stuknij **⋮** i wybierz **Zainstaluj i utwórz skrót**.

## Aktualizacje
Aplikacja aktualizuje się sama przy otwarciu z internetem. Bez internetu działa z zapisanej kopii. Wszystkie dane zostają na telefonie.

## Kod źródłowy
Katalog `src/`. Przepisy i produkty pochodzą z „Co z lodówki?” i są wyciągane skryptem `extract.js` do `src.json`. Wersję buduje `python3 src/build.py vN`, który zapisuje wynik w `src/out/`.
