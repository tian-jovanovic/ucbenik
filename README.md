# Zapiski

Za izdelavo HTML datotek si morate namestiti paket [`jupyter-book`](https://jupyterbook.org/). Nato pa pokličete

```bash
jupyter-book build ucbenik
```

Če imate ustrezne pravice, lahko HTML najenostavneje objavite kar prek [GitHub pages](https://pages.github.com) tako, da si namestite še paket [`ghp-import`](https://github.com/c-w/ghp-import) in poženete

```bash
ghp-import --no-jekyll --no-history --force --push ucbenik/_build/html
```
