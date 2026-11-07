# Mały Szef 🧑‍🍳

Aplikacja dla rodziców niejadków. Dziecko (albo kilkoro dzieci razem) chodzi po kuchni i zaznacza, co znajdzie w lodówce i szafkach. Po drodze rozwiązuje mini-zadania: słówka po angielsku, kolory i liczenie. Rodzic zatwierdza 2–3 dania, a dziecko samo wybiera, co zje, i dostaje naklejkę.

**Otwórz:** https://geezotto-pl.github.io/maly-szef/

## Instalacja na telefonie
- **iPhone:** otwórz link w Safari, stuknij **Udostępnij** i wybierz **Do ekranu początkowego**.
- **Android:** otwórz link w Chrome, stuknij **⋮** i wybierz **Zainstaluj i utwórz skrót**.

## Aktualizacje
Aplikacja aktualizuje się sama przy otwarciu z internetem. Bez internetu działa z zapisanej kopii. Wszystkie dane zostają na telefonie.

## Licencje
Ilustracje produktów i dań: [Fluent Emoji](https://github.com/microsoft/fluentui-emoji) (Microsoft, licencja MIT), pakiet `@lobehub/fluent-emoji-3d`. Opakowania i dźwięki są wygenerowane skryptami w `src/`.

## Kod źródłowy
Katalog `src/`. Przepisy i produkty pochodzą z „Co z lodówki?” i są wyciągane skryptem `extract.js` do `src.json`. Obrazki tworzy `imagegen.py`, dźwięki `soundgen.py`, a całość buduje `python3 src/build.py vN --assets` do katalogu `src/out/`. Bazę produktów (145) i nowe przepisy zawiera `products.py`.
