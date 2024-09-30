# Plonkec za ukazno vrstico

- Ukaz [`pwd`](https://en.wikipedia.org/wiki/Pwd) (_**p**rint **w**orking **d**irectory_) izpiše 
  celotno pot do trenutnega delovnega imenika.
- Ukaz [`cd`](https://en.wikipedia.org/wiki/Cd_(command)) (_**c**hange **d**irectory_) 
  spremeni trenutni delovni imenik v skladu s potjo (relativno ali absolutno), ki jo podamo.
  Primeri:
    - `cd ..` spremeni trenutni delovni imenik na en imenik višje v hierarhiji (oz. na starša, oz. na en imenik bližje korenskemu, npr. iz `Users/racunalniski-praktikum/vaje1` v `Users/racunalniski-praktikum`),
    - `cd ~` spremeni trenutni delovni imenik na domači imenik uporabnika (`/c/Users/⟨uporabnisko-ime⟩` na Windows in `/Users/⟨uporabnisko-ime⟩` na MacOS),
    - `cd ../⟨sosednji-imenik⟩` spremeni delovni imenik na imenik `⟨sosednji-imenik⟩`, ki se nahaja v istem staršu kot trenutni delovni imenik (seveda, če ta obstaja, npr. iz `Users/racunalniski-praktikum/vaje1` v `Users/racunalniski-praktikum/vaje2`),
    - podobno se lahko premaknemo tudi za več imenikov navzgor, npr. iz `Users/racunalniski-praktikum/vaje1` v `Users` z ukazom `cd ../..`,
    - `cd -` spremeni delovni imenik na prejšnji delovni imenik 
      (če smo se nazadnje premaknili iz `Users/racunalniski-praktikum/vaje1` v `Users/racunalniski-praktikum/vaje2`, 
      premaknemo nazaj v `Users/racunalniski-praktikum/vaje1`).
- Ukaz [`ls`](https://en.wikipedia.org/wiki/Ls) (_**l**i**s**t_) izpiše seznam datotek in imenikov. 
  Če ne podamo dodatnih parametrov ali oznak, to naredi za trenutni delovni imenik.
  Če podamo pot, izpiše seznam vsebine za imenik na koncu poti.
- Ukaz [`cat`](https://en.wikipedia.org/wiki/Cat_(Unix))(_[**cat**enate](https://en.wiktionary.org/wiki/catenate)_) izpiše vsebino datoteke (ali datotek) na standardni izhod.
  Primeri:
    - `cat datoteka.txt` izpiše vsebino datoteke `datoteka.txt` v trenutnem delovnem imeniku,
    - več datotek lahko izpišemo tako, da naštejemo imena datotek ločena s presledki: `cat datoteka1.txt datoteka2.txt`,
    - `cat *` izpiše vsebino vseh datotek v trenutnem delovnem imeniku,
    - znak `*` pomeni približno "karkoli" in ga lahko uporabimo tudi v drugačnih vzorcih;
      `cat *.txt` izpiše vsebino vseh datotek s končnico `txt`. 
- Ukaz [`touch`](https://en.wikipedia.org/wiki/Touch_(command)) je v privzeti uporabi enakovreden 
  ustvarjanju ali odpiranju datoteke ter njenemu shranjevanju brez kakršnekoli spremembe vsebine. 
  S tem ukazom se lahko izognemo odpiranju, shranjevanju in zapiranju datoteke, 
  kadar želimo datoteko ustvariti ali samo posodobiti podatke o njej 
  (s `touch` lahko posodobimo tudi podatke o imeniku, ustvarimo pa ga lahko z `mkdir`).
- Program [`nano`](https://en.wikipedia.org/wiki/GNU_nano) je preprost urejevalnik navadnega besedila za ukazno vrstico.
  uporabimo ga tako: `nano ⟨datoteka⟩`.