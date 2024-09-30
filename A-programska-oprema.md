(programska-oprema)=
# Nameščanje programske opreme

Pričujoča navodila za nameščanje programske opreme naj vam bodo v pomoč, ni pa mišljeno, da boste v njih našli rešitev za vse možne zagate.
Programje se spreminja dovolj hitro, da bi bilo taka navodila nemogoče vzdrževati.
Če se vam zatakne pri nameščanju programske opreme, najprej poskusite rešitev najti na spletu.
Za nasvet lahko vprašate tudi po Discordu, na forumu v spletni učilnici (obe povezavi sta na [učilnici](https://ucilnica.fmf.uni-lj.si/course/view.php?id=8)) ali na vajah.
Potrudite se, da boste v vprašanju podali dovolj podrobnosti, da vam bomo lahko pomagali. 
Če napišete samo "meni LaTeX ne prime", to ne bo koristno.

Priporočamo se za pripombe in popravke (ki jih predlagajte na Discordu, na forumu ali po e-pošti asistentki).

(namestitev:ukazna)=
## Orodja za ukazno vrstico

Sledite navodilom za vaš operacijski sistem, nato pa še [navodilom za nastavitve za `git`](faq:git-nastavitve).

### Navodila za operacijski sistem Windows

S spletne strani [git](https://git-scm.com/download/win) prenesite in namestite Git for Windows.
Git je orodje za nadzor različic, poleg tega pa Git for Windows ponuja še močno ukazno vrstico.

### Navodila za operacijski sistem MacOS

Če uporabljate MacOS, imate dve možnosti: lahko namestite XCode, ali pa samo XCode Command Line Tools. 
XCode je Appleov paket razvojnih orodij in prevajalnikov - za potrebe Računalniškega praktikuma jih ne potrebujete.
Namestite ga, če se boste počutili bolje z nameščenim prevajalnikom za C.
**Opozorilo:** XCode zasede med 3GB in 4GB, za nemoteno delovanje pa potrebujete kakih 40GB prostega prostora na disku (te številke niso zelo točne).
XCode namestite preko [Apple App Store](https://apps.apple.com/si/app/xcode/id497799835).

Nato izberite eno od spodnjih možnosti. Toplo priporočamo, da se odločite za namestitev z upraviteljem paketov Homebrew.

#### A. Namestitev s Homebrew

1. Namestite [Homebrew](https://brew.sh). Najlažje bo, če prenesete `.pkg` datoteko in jo poženete. 
   Če se boste lotili nameščanja z ukazno vrstico: ko boste vpisovali geslo za vaš računalnik, se ne bo nič videlo, da se kaj dogaja. Vpišite geslo in stisnite <kbd>Enter</kbd>. Homebrew se splača občasno [posodobiti](https://docs.brew.sh/FAQ#how-do-i-update-my-local-packages).
2. Odprite Terminal in v ukazno vrstico napišite `brew install git`. Vedno lahko preverite, kakšna je ustrezna Homebrew formula z [iskalnikom](https://brew.sh), npr. [za git](https://formulae.brew.sh/formula/git#default).

#### B. Samo namestitev XCode Command Line Tools
   
Paket orodij za ukazno vrstico XCode Command Line Tools namestite tako, da odprete Terminal in vtipkate ukaz `xcode-select --install`.
Preverite, da je bila namestitev uspešna tako, da v ukazno vrstico napišete `xcode-select -p`.
Če je vse ok, se bo spodaj izpisalo približno `/Library/Developer/CommandLineTools`.

### Navodila za operacijski sistem Linux

1. Če se še niste, se spoznajte z upraviteljem paketov (angl. _package manager_) na vaši distribuciji (npr. `apt` na Ubuntu/Debian ali `yum`/`dnf` na Red Hat distribucijah).
2. Če še nimate nameščenega git-a, ga namestite zdaj s svojim upraviteljem paketov (če vam je to še neznano, v brskalnik vpišite `<vaš Linux> install git`).
   Za Ubuntu boste verjetno našli [`sudo apt install git-all`](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

(namestitev:vscode)=
## Visual Studio Code

S spletne strani [Visual Studio Code](https://code.visualstudio.com) prenesite in namestite program za vaš operacijski sistem.
Mimogrede, nihče ne govori "visual studio code", ampak krajše "vscode".

Pri namestitvi bodite pozorni na možnosti, še posebej na to, da imate obkljukano "Open with code" - hvaležni si boste (če ste pozabili, lahko ponovite namestitev s to možnostjo).

### Dodatna navodila za operacijski sistem Windows

Če imate že nameščeno ukazno vrstico Git Bash, [jo nastavite za privzeto ukazno vrstico še v urejevalniku](faq:vscode-bash).

* Ne uporabljajte namestitve z ZIP datoteko, ker se stvari ne bodo pravilno nastavile.
* Prenesli ste `.exe` datoteko, ki jo poženete kot adminstrator za vse uporabnike.
* Ena od nastavitev pri namestivi sprašuje, ali naj se VSCode doda v `PATH`. Tu **morate odgovoriti pritrdilno**. ([Kaj je `PATH`?](https://en.wikipedia.org/wiki/PATH_(variable)))
* Priporočamo, da naredite asociacijo med VSCode in tipi datotek, ki jih znan urejati (angl. _file associations_).

### Dodatna navodila za operacijski sistem MacOS

* Prenesli ste ZIP datoteko, ki jo odpakirajte, nato pa prestavite program v _Applications_.

(namestitev:latex)=
## LaTeX

Za začetek v VSCode namestite paket LaTeX Workshop:
1. v meniju View:Extensions (razdelek se bo odprl na levi) 
2. v iskalno polje zgoraj levo vpišete "LaTeX Workshop",
3. izberete podaljšek [LaTeX Workshop](https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop) in ga namestite.

Če ne uporabljate urejevalnika VSCode, poglejte, če za vaš urejevalnik obstaja kak podaljšek za LaTeX.

### Navodila za operacijski sistem Windows

Ta navodila predpostavljajo, da imate že nameščen urejevalnik [Visual Studio Code](namestitev:vscode) in [orodja za ukazno vrstico](namestitev:ukazna).

1. Namestite [Perl](https://www.perl.org/get.html). To je programski jezik, ki ga potrebujete, da vam bo deloval ukaz `latexmk` (ta vam res olajša delo).
   * Prenesite in namestite [Strawberry Perl](https://strawberryperl.com).
   * Pazite, da se bo med namestitvijo Perl dodal v `PATH` (morda boste morali prej še enkrat zagnati računalnik).
2. Namestite [MikTeX](https://miktex.org).
   *Pomembno*: Ko vas vpraša, ali naj samodejno namesti manjkajoče pakete, priporočamo, da izberete samodejno nameščanje. Če boste izbrali, da naj vas sprašuje pred vsako namestitvijo, vas pri prvem zagonu LaTeX-a čaka veliko klikanja.
3. Popravite znake `{`, `}` in `@` v VSCode: sledite navodilom v razdelku [VSCode, LaTeX, Windows in slovenska tipkovnica](faq:vscode-latex-si) pod pogostimi vprašanji.
4. [Preverite namestitev](A:latex-preverjanje) (navodila so v kasnejšem razdelku).

#### Nekatere pogoste težave

- [`The Perl interpreter could not be found.`](https://tex.stackexchange.com/questions/158796/miktex-and-perl-scripts-and-one-python-script): preverite, da imate res nameščen Perl in da operacijski sistem ve, [kje je](https://www.wikihow.com/Change-the-PATH-Environment-Variable-on-Windows). Poti ne spreminjajte sami. Pogosto zadošča, da ponovno zaženete računalnik.

### Navodila za operacijski sistem MacOS

Ta navodila predpostavljajo, da imate že nameščen urejevalnik [Visual Studio Code](namestitev:vscode) in [orodja za ukazno vrstico](namestitev:ukazna).

1. Preverite, da imate nameščen Perl tako, da v ukazno vrstico napišete `perl -v`. 
   Če je vse ok, se bodo izpisale informacije o verziji programa, sicer pa `zsh: command not found: perl` (v tem primeru namestite Perl, npr. s Homebrew).
2. Namestite [MacTeX](https://www.tug.org/mactex/) distribucijo [TeX live](https://tug.org/texlive/) za MacOS. Če imate že nameščen Homebrew, poženite program Terminal in v ukazno vrstico prilepite [ustrezno formulo, ki jo kopirate s Homebrew strani](https://formulae.brew.sh/cask/mactex). Sicer sledite navodilom na strani distribucije.
3. [Preverite namestitev](A:latex-preverjanje)  (navodila so v kasnejšem razdelku).

### Navodila za operacijski sistem Linux

Če uporabljate Linux, verjetno ne potrebujete naših navodil.

(A:latex-preverjanje)=
### Preverjanje namestitve

Preverite, ali vam deluje LaTeX: odprite ukazno vrstico in poženite spodnja ukaza.
V obeh primerih poganjamo program (`pdflatex` in `latexmk`) z dodatkom, da nas zanima samo verzija (`-version`).

1. `pdflatex -version`
2. `latexmk -version`

(namestitev:mathematica)=
## Mathematica

Mathematica je sistem za numerično in simbolno računanje. Namestite jo na domači računalnik, pri čemer sledite [navodilom za namestitev Mathematice](https://www.fmf.uni-lj.si/sl/racunalniski-center/mathematica-za-studente/).

V navodilih zgoraj (morda) manjka korak. Ko se registrirate, pridobite aktivacijsko kodo, ter se prijavite in potrdite svojo e-pošto, lahko program prenesete s strani, na kateri ste pridobili aktivacijsko kodo.

## Oprema in storitve Microsoft

Univerza v Ljubljani vsem študentom omogoča dostop do programske opreme in storitev Microsoft, glejte navodila o [informacijskih storitvah Univerze v Ljubljani](https://www.uni-lj.si/studentsko_zivljenje/informacijske_storitve/). Po lastni izbiri si namestite, kar se vam zdi uporabno. Pri predmetu bomo uporabljali Microsoft Excel.

## Zoom

Na domačem računalniku imejte nameščeno aplikacijo [Zoom](https://zoom.us). Upamo, da je ne boste potrebovali. Aplikacijo lahko namestite tudi na svoj telefon.

Če na Zoom-u še nimate uporabniškega imena, ga ustvarite. Nastavite svoje pravo ime in
priimek, ker se tako spodobi. Tudi profesorji ne predavanjo pod vzdevkom `FunnyBunny42`.
