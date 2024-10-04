# Plonkec za Git

Pogled _Source Control_ v stranskem meniju urejevalnika VSCode ima tri dele (ponavadi se ne izpišejo se vsi).
Razdelek _Changes_ vsebuje datoteke, ki so se spremenile od zadnje zabeležene spremembe (oz. angl. _commit_-a),
razdelek _Staged Changes_ pa datoteke, ki bodo vključene v naslednjo zabeleženo spremembo.

Več o shranjevanju sprememb v Git si lahko preberete v prijaznem povzetku na 
[Atlassian spletni strani](https://www.atlassian.com/git/tutorials/saving-changes),
povezave na dokumentacijo za posamezne ukaze pa so spodaj.

(git:osnovni-ukazi)=
## Osnovni ukazi

- Ukaz [`add`](https://github.com/git-guides/git-add) 
  zbira datoteke s spremembami, ki jih želite vključiti v naslednjo zabeleženo spremembo. 
  V ukazno vrstico napišete `git add`, in naštejete datoteke, s spremembami, ki jih želite vključiti, npr.
  `git add README.md`.
  V pogledu _Source Control_ v VSCode to naredite tako, da prestavite datoteke iz _Changes_ v _Staged Changes_.
- Ukaz [`commit`](https://github.com/git-guides/git-commit)
  v repozitorij zabeleži spremembe, ki ste jih vključili z `add`.
  Vsak tak zabeležek je posnetek stanja v tistem trenutku.
  V ukazno vrstico napišete `git commit -m "⟨sporočilo z opisom spremembe⟩"`.
  Z oznako `-m` ukazu `commit` poveste, da sledi kratko sporočilo.
  Obstajajo tudi drugi načini pisanja teh sporočil, ki presegajo obseg tega plonkca.
  V pogledu _Source Control_ v VSCode pod `Message` napišete kratko sporočilo z opisom spremembe, 
  ter s pritiskom na gumb _Commit_ spremembo ustvarite.
- Spremembe pošljete na strežnik z ukazom [`push`](https://github.com/git-guides/git-push).
  V ukazno vrstico napišete `git push`. 
  V VSCode uporabite ukaz _Git: Push_ iz palete ukazov.
  Če se `push` ne izvede, je najbolje, da prosite za pomoč, narobe gre lahko več stvari.
- Spremembe povlečete s strežnika z ukazom [`pull`](https://github.com/git-guides/git-pull).
  V ukazno vrstico napišete `git pull`. 
  V VSCode uporabite ukaz _Git: Pull_ iz palete ukazov.
  Če se `push` ne izvede, je najbolje, da prosite za pomoč, narobe gre lahko več stvari.

Ukaz `add` med drugim omogoči, da veliko spremembo razdelite na več manjših
(če ne vključite vseh datotek, ki so se spremenile), kar poenostavi branje zgodovine sprememb. 

Urejevalnik VSCode ima v statusni vrstici tudi gumb za sinhronizacijo, ki kaže število čakajočih sprememb na obeh straneh,
ob kliku pa uskladi v obe smeri.

(git:init)=
## Priprava novega repozitorija

V ukazni vrstici poženete ukaz `git init` v imeniku, v katerem želite vzpostaviti repozitorij. 
Če imate imenik odprt v VSCode, lahko repozitorij vzpostavite tudi z ukazom _Git: Initialize repository_ iz palete ukazov.
Tudi če repozitorija nimate namena deliti z nikomer, je lahko koristen - kot varnostna kopija, ali pa za pregled zgodovine.

Če želite imeti repozitorij tudi na strežniku (npr. GitHub), lahko nanj naložite lokalnega. 
Še bolj enostavno pa je, če ga ustvarite na strežniku in od tam klonirate. 
V ukazni vrstici to naredite z ukazom `git clone`, ki mu poveste naslov repozitorija
(npr. `git clone git@github.com:katjabercic/rp-git-zgodba.git`).
V VSCode to lahko naredite z ukazom _Git: Clone_, ki vas bo prav tako vprašal za naslov repozitorija
(npr. `git@github.com:katjabercic/rp-git-zgodba.git`).
Če ste povezali GitHub z VSCode, boste repozitorij verjetno lahko izbrali s seznama.
S tem ukazu se na našem računalniku ustvari popoln klon repozitorija na strežniku.

(git:gitignore)=
## Datoteka `.gitignore`

V datoteko `.gitignore` naštejemo vse datoteke, ki jim v Gitu ne želimo slediti.
Dober primer tega so datoteke, specifične za naš računalnik, varnostno občutljive datoteke in datoteke, 
ki jih računalnik ustvari sam (in jih zato lahko ustvarimo na novo):

- MacOS rad ustvarja datoteke `.DS_Store` in direktorije `__MACOSX`,
- Windowsi ustvarjajo datoteke `thumbs.db`,
- Python (ki ga boste srečali pri Uvodu v programiranje) ustvari množico datotek v imeniku `__pycache__`, 
- LaTeX ustvari PDF datoteke ter pomožne datoteke s končnicami `.aux`, `.log` in podobno). 

S tem, ko take datoteke izključimo, poskribmo, da repozitorij ostane čist, pregleden in lažji za delo.
Primer ustrezne datoteke `.gitignore` bi bil:

```sh
# VSCode uporabniške nastavitve
.vscode/

# LaTeX
*.aux
*.bbl
*.blg
*.fdb_latexmk
*.toc
*.fls
*.log
*.out
*.pdf
*.pyc
*.synctex.gz

# MacOS
__MACOSX
.DS_Store

# Windows
thumbs.db

# Python
__pycache__
```

(git:nastavitve)=
## Nastavitve za `git`

Git morate nastaviti na vsakem računalniku, kjer ga uporabljate, tudi na računalniku na fakulteti.

(git:nastavitve-uporabnika)=
### 0. Uporabniške nastavitve

Najprej [poženite ukazno vrstico](bliznjice:zaganjanje-ukazna), nato pa poženite spodnje ukaze.
(To naredite tako, da ukaz kopirate, prilepite v ukazno vrstico, ustrezno pokažete, ter izvedete tako, da stisnete vnašalko <kbd>↵</kbd>.)

1. Nastavite svoje ime z ukazom `git config --global user.name "⟨vaše ime⟩"` (npr. `git config --global user.name "Emmy Noether"`).
2. Nastavite svojo e-pošto (tisto, ki jo uporabljate za GitHub) z ukazom `git config --global user.email ⟨vaša pošta⟩` (npr. `git config --global user.email en3141@student.uni-lj.si`).
3. Nastavite privzeti urejevalnik na nekaj prijaznega (če znate uporabljati `vim`, vam tega seveda ni treba) `git config --global core.editor nano`.
4. Preverite, če ste nastavitve uspešno shranili: `git config --list`.

### 1. Zgenerirajte SSH ključ

```shell
ssh-keygen
```

Klic programa [`ssh-keygen`](https://en.wikipedia.org/wiki/Ssh-keygen) je dovolj, da se vaš ključ zgenerira in spravi na pravo mesto.
Privzeto ime datoteke bo verjetno `id_rsa.pub` ali `id_ed25519.pub` v imeniku `.ssh` v vašem domačem imeniku 
(npr. `/c/Users/⟨fmf-uporabnisko-ime⟩/` oz. 🍎 `/Users/⟨domace-uporabnisko-ime⟩`).
Še posebej, če ste na računalniku na fakulteti, si izberite dobro geslo (zapomnite si ga).

Če boste git uporabljali na več računalnikih, potrebujete na vsakem računalniku svoj ključ.

### 2. Kopirajte javni ključ na odložišče

Najprej sestavimo pot do ključa. Takole se bomo sklicevali na vaš domači imenik`⟨domaci-imenik⟩`,
ki je videti takole:
- na fakulteti (Windows): `/c/Users/⟨fmf-uporabnisko-ime⟩`,
- vaš računalnik (Windows): `/c/Users/⟨domace-uporabnisko-ime⟩`,
- MacOS: `/Users/⟨domace-uporabnisko-ime⟩`.

Z ukazom `ls ⟨domaci-imenik⟩/.ssh` preverite, da se v vašem domačem imeniku nahaja imenik `.ssh` v katerem je spravljen ključ:
v izpisu poiščite datoteko s končnico `.pub`.
Če je ne najdete, prosite za pomoč, če pa jo najdete, si zapomnite ime, tu bomo napisali `⟨datoteka-s-kljucem⟩`.
Na operacijskem sistemu Windows na fakulteti bo ime najverjetneje `id_rsa.pub`, na operacijskem sistemu MacOS pa `id_ed25519.pub`. 

Uporabite ukaz za vaš operacijski sistem, ki ga ustrezno popravite.

Windows (Git Bash):
```shell
cat ⟨domaci-imenik⟩/.ssh/⟨datoteka-s-kljucem⟩ | clip
```

MacOS (Terminal)
```shell
cat ⟨domaci-imenik⟩/.ssh/⟨datoteka-s-kljucem⟩ | pbcopy
```

Program [`cat`](https://en.wikipedia.org/wiki/Cat_(Unix)) ste spoznali na prvih vajah.
Navpična črta `|` ([pipa, angl. _pipe_](https://en.wikipedia.org/wiki/Pipeline_(Unix))) 
preusmeri rezultat programa na levi strani (v tem primeru `cat`) na vhod programa na desni strani črte. 
V našem primeru sta to `clip` oz. `pbcopy`, ki skopirata vhod na odložišče.

### 3. Nastavite javni ključ na svojem GitHub računu

Sledite navodilom v [GitHub dokumentaciji](https://docs.github.com/en/enterprise-cloud@latest/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account#adding-a-new-ssh-key-to-your-account), točkam 2-8 (v točki 6 izberite "authentication").

Ime ključa nastavite tako, da boste vedeli, na katerem računalniku ste ga naredili.

(git:vscode)=
## Git, GitHub in VSCode

Pripravite VSCode za delo z Git-om. 
Spodaj levo kliknite na ikono _Accounts_ (nad zobnikom za nastavitve) in izberite _Sign in with GitHub..._. 
Če te možnosti ne vidite, lahko prijavo v vaš GitHub račun poskusite sprožiti s kloniranjem: 
<kbd>Ctrl</kbd>/<kbd>Cmd</kbd>+<kbd>Shift</kbd>+<kbd>P</kbd> > **Git: Clone**.
Prilepite naslov repozitorija v pogovorno okno.
Če še niste prijavljeni, se bo pojavilo pogovorno okno s sporočilom
"The extension 'GitHub' wants to sign in using GitHub."
Izberite gumb _Allow_. Prestaviti bi vas moralo v brskalnik, kjer se prijavite 
(zna se pojaviti še kako pogovorno okno, ki vas bo spraševalo za dovoljenje).

Ukaz <kbd>Ctrl</kbd>/<kbd>Cmd</kbd>+<kbd>Shift</kbd>+<kbd>P</kbd> > **Git: Clone** > **Clone from GitHub** 
vam ponudi seznam repozitorijev, do katerih imate dostop.
Zaenkrat je videti, kot da ta ukaz uporablja manj varno kloniranje s protokolom HTTPS,
pri tem predmetu pa bomo uporabljali protokol SSH.

(git:konflikti)=
## Zlivanje sprememb in konflikti

Ta razdelek je vključen za primer, če kaj ne bo šlo po načrtu.
Če na repozitoriju dela več ljudi ali delate na večih računalnikih, se lahko zgodi, 
da se sprememb ne da enostavno uskladiti. 

Če je na strežniku sprememba, ki je v našem repozitoriju še ni, se lokalnih sprememb ne bo dalo poslati na strežnik. 
Najprej je treba povleči spremembe s strežnika na računalnik, ter jih zliti (angl. _merge_) z lokalnimi.
Šele nato lahko vse skupaj pošljete na strežnik. 
To najenostavneje naredimo z gumbom za sinhronizacijo, pri čemer Git pazi, da se nobena izmed sprememb ne izgubi. 
Na primer, če je v spremembi na eni strani popravljena vrstica na enem koncu datoteke, 
v spremembi na drugi strani pa vrstica na drugem koncu datoteke, bosta v združeni različici spremenjeni obe vrstici.

Prelepo bi bilo, če bi bilo vedno tako :smile:. 
Če je na obeh straneh spremenjena ista vrstica, nastane konfklit pri zlivanju (angl. _merge conflict_), 
ki ga je treba natančno pogledati in razrešiti ročno. 
Git take konflikte označi v datoteki sami in sicer tako, da na mesto konflikta vstavi posebna ločila ter vsebini obeh različic. 

Začnemo s spodnjim besedilom.

```
In der stadt gab es auch ein paar barbaren
Die hatten von Barbaras rabarberbar erfahren
Und da sie fortan jeden tag bei Barbara waren
Nannte man sie bald die "rabarberbar-barbaren"
```

Na eni strani je nekdo opazil, da samostalniki niso napisani z veliko začetnico.

```
In der Stadt gab es auch ein paar Barbaren
Die hatten von Barbaras Rabarberbar erfahren
Und da sie fortan jeden Tag bei Barbara waren
Nannte man sie bald die "Rabarberbar-Barbaren"
```

Na drugi strani pa je nekdo drug opazil, da manjka črka h v _Rhabarberbar_.

```
In der stadt gab es auch ein paar barbaren
Die hatten von Barbaras rhabarberbar erfahren
Und da sie fortan jeden tag bei Barbara waren
Nannte man sie bald die "rhabarberbar-barbaren"
```

Ob združevanju bi prišlo do konflikta, ki bi ga Git v datoteki označil kot:

```
<<<<<<< HEAD
In der Stadt gab es auch ein paar Barbaren
Die hatten von Barbaras Rabarberbar erfahren
Und da sie fortan jeden Tag bei Barbara waren
Nannte man sie bald die "Rabarberbar-Barbaren"
=======
In der stadt gab es auch ein paar barbaren
Die hatten von Barbaras rhabarberbar erfahren
Und da sie fortan jeden tag bei Barbara waren
Nannte man sie bald die "rhabarberbar-barbaren"
>>>>>>> 4b24623835d5ebbfb9288cae00d84f5261889111
```

Urejevalnik VSCode konflikte jasno označi, ponudi možnosti (izberi prvega, izberi drugega, izberi oba, primerjaj, ...). 
Po temeljitem premisleku vidimo, da bo najlažje začeti s prvo spremembo (pobrišemo oznake in drugo spremembo), 
nato pa dodati manjkajoči črki h v obeh ponovitvah besede _Rhabarberbar_.

```
In der Stadt gab es auch ein paar Barbaren
Die hatten von Barbaras Rhabarberbar erfahren
Und da sie fortan jeden Tag bei Barbara waren
Nannte man sie bald die "Rhabarberbar-Barbaren"
```

Nato shranimo datoteko, zabeležimo spremembo, ter zlite spremembe pošljemo na strežnik.
