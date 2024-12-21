![GHA workflow badge](https://github.com/Seba686/eigenface/workflows/CI/badge.svg) [![codecov](https://codecov.io/gh/Seba686/eigenface/graph/badge.svg?token=XAMSGTJHFU)](https://codecov.io/gh/Seba686/eigenface)

# Eigenface
Kasvojentunnistus Eigenface menetelmällä.
## Asennus ja käynnistys

Asenna riippuvuudet komennolla

```bash
poetry install
```

Mene hakemistoon src ja käynnistä ohjelma komennolla

```bash
poetry run python3 index.py
```

Suorita testit komennolla

```bash
poetry run pytest
```

Tiedostossa index.py voi muuttaa harjoituskuvien määrän: kansioiden lukumäärä (1-40) sekä kuinka monta kuvaa valitaan jokaisesta kansiosta (1-9). Suositus on valita enintään noin 60 kuvaa.