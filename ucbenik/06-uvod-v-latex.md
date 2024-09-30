# Uvod v LaTeX

LaTeX je sistem za pripravo dokumentov. Deluje drugače kot Microsoft Word in
podobni programi.
V Microsoft Word uporabnik neposredno oblikuje dokument in vidi njegovo 
končno oblik ("What you see is what you get" - WYISYG).
V LaTeXu uporabnik pripravi vhodno datoteko `.tex`, ki vsebuje navadno besedilo
in ukaze za oblikovanje, nato pa datoteko s programom `pdflatex` pretvori v PDF.

Prvi način je bolj prijazen večini uporabnikov, ki niso tehnično podkovani in ki
ne želijo investirati časa v učenje bolj zahtevnega, a tudi bolj kvalitetnega in
zmogljivega sistema.

Včasih je treba ukaz `pdflatex` pognati večkrat zapored, da lahko LaTeX
preračuna sklice na izreke in številke strani. Uporabnik lahko to stori bodisi
sam, bodisi uporabi program `latexmk`, ki sam po potrebi požene `pdflatex` (in
tudi ostale programe, v sklopu sistema LaTeX). Če uporabljate Visual Studio
Code, se ob shranjevanju avtomatično požene program `latexmk`.

## TODO

Definicija novega ukaza z matematičnim načinom ali brez, razloži

## Struktura dokumenta

LaTeX dokument shranimo v datoteko s končnico `.tex`. Dokument je lahko shranjen
tudi v večjih datotekah, ki jih z ukazom `\input{datoteka.tex}` vključimo v
glavno datoteko.

Struktura glavne LaTeX datoteke je naslednja:

```tex
\documentclass[...]{...}

⟨preambula⟩

\begin{document}

  ⟨vsebina⟩

\end{document}
```

Ukaz `\documentclass` določa zvrst dokumenta (članek, knjiga, pismo, ...).
Ime razreda vpišemov zavite oklepaje, nastavitve v oglate, npr. `\documentclass[a4paper]{article}`.
Nastavitve lahko tudi opustimo in pišemo samo `\documentclass{...}`.

V preambuli v dokument vključimo razne pakete, uredimo nastavitve in definiramo makroje:

* paket vključimo z ukazom `\usepackage[...]{imePaketa}`, kjer v `[...]` podamo razne nastavitve.
* nastavitve so odvisne od zvrsti dokumenta.
* makro je okrajšava, ki jo lahko uporabljamo v dokumentu, definiramo ga z
  `\newcommand{\imeMakroja}....`, o tem se bomo več učili kasneje.

LaTeX ima okoli [6000 paketov](https://www.ctan.org). Najbolj uporabni so že vključeni v
distribucijo LaTeXa, ki ste jo namestili na svojo računalnik.

### Ukazi

V LaTeXu ukaze pišemo z `\imeUkaza`. Ukazu lahko dodamo tudi argumente, ki jih pišemo v `{...}`, na primer:

* `\section{Turingovi stroji}` naredi nov razdelek z naslovom "Turingovi stroji"
* `\textbf{....}` oblikuje besedilo v **krepkem** tisku.

Ukaz lahko sprejme tudi več argumentov, na primer `\ukaz{arg₁}{arg₂}...{argᵢ}`,
poznamo pa tudi neobvezne argumente, ki jih lahko bodisi izpustimo bodisi podamo
v oglatih oklepajih, na primer `\ukaz[arg₁]{arg₂}`.

### Okolja

Kadar oblikujemo več, kot samo nekaj besed, uporabimo okolje. 
Srečali ste že okolje `document`, ki vsebuje celotno vsebino dokumenta.
Okolja ponavadi pišemo takole:

```tex
\begin{ime-okolja}
  ⟨vsebina⟩
\end{ime-okolja}
```

Pri teh vajah boste srečali okolja `abstract`, `verbatim`, `itemize` in `enumerate`.
Tudi matematični način (v resnici poznamo dva, vrstičnega in prikaznega) si lahko predstavljate
kot okolje, za katerega pa uporabljamo okrajšavo:

```
\[
  ⟨matematični izraz na sredini vrstice⟩
\]
```

ali `\( ⟨matematični izraz v vrstici⟩ \)`.

### Razlika med oblikovnimi in vsebinskimi ukazi

Besedilo lahko oblikujemo na dva načina:

1. **Oblikujemo videz** z ukazi, ki nastavijo velikost in stil pisave, z ukazi
   za prelom vrstice, vstavljamo zamike ipd.
2. **Določimo vsebinski pomen** z ukazi, ki nakazujejo *pomen* kosov besedila,
   na primer ukazi za nov razdelek, podrazdelek, okolje za zapis izreka, okolje
   za zapis dokaza, itd.

Vsebinsko oblikovanje dokumenta je dosti bolj prijazno uporabniku, sistematično
in fleksibilno. LaTeX tako oblikovanje zelo dobro podpira.

Za primer, v LaTeX-u vsebinsko oblikujemo besedilo izreka z okoljem `theorem`.

```tex
\begin{theorem}
  ⟨besedilo izreka⟩
\end{theorem}
```

Če bi neposredno oblikovali videz izreka kot spodaj,
bi bilo težje skrbeti za to, da vsi izreki izgledajo enako, da so vsi pravilno
oštevilčeni, ipd.

```tex
\textbf{Izrek 1.1} \textit{⟨besedilo izreka⟩}
```

Še nekaj primerov vsebinskega oblikovanja so posebni ukazi za vsebino, kot so
`\section`, `\subsection`, `\footnote`, ...

### Splošna priporočila za urejanje LaTeX dokumentov

* Za vsak LaTeX dokument imejte datoteke spravljene v imeniku, ki vsebuje
  samo datoteke za ta dokument. Ta imenik potem odprite v urejevalniku
  Visual Studio Code. Asistenti vam bodo hvaležni (sčasoma pa boste verjetno
  hvaležni tudi sami sebi).
* Napake, ki jih javlja LaTeX, niso vedno razumljive. Med drugim to pomeni, da
  jih je v besedilu težko najti. En način, da si pri tem pomagamo, je ta, da
  dokument pogosto prevedemo. Tako vemo, da se je napaka pojavila od takrat, ko
  je LaTeX nazadnje uspešno prevedel dokument.
* Najmanjši dokument, ki vam ga bo LaTeX še smiselno prevedel, mora vsebovati
  ukaz `\documentclass` in okolje `document`. Poglejte si, kakšne napake javi
  LaTeX, če prevajate brez tega: tako jih boste naslednjič prepoznali.

## 1. VSCode in LaTeX

Naslednjih nekaj tednov bomo spoznavali [LaTeX](https://www.latex-project.org). Da bo delo
teklo nemoteno, bomo preverili, ali je vaš urejevalnik pripravljen za delo z njim.

LaTeX je sistem za stavljenje besedila. Je pravzaprav prevajalnik, ki LaTeX datoteko s končnico `.tex`, ki vsebuje navadno besedilo, označeno s posebnimi LaTeX značkami in ukazi, pretvori v lepo stavljeno besedila in ga shrani v datoteko PDF s končnico `.pdf`. A več o tem bomo povedali naslednjič.

VSCode podpira delo z LaTeX. Ko odprete datoteko s končnico `.tex`, se v VSCode vklopi posebni način urejanja LaTeX (spodaj desno). LaTeX lahko poženete kar iz VSCode, prav tako si lahko znotraj VSCode ogledate datoteko PDF, ki jo naredi LaTeX.

Preizkusite, ali VSCode podpira delo z LaTeX:

1. Na svojem disku naredite imenik z imenom `latex-test` (ali kaj podobnega). Ta imenik naj *na operacijskem sistemu Windows ne bo v imeniku Desktop, Downloads, Namizje ali Prenosi.* Prav tako v imenu imenika (ali tistih nad njim) ne sme biti nobenih presledkov in šumnikov.
2. Odprite imenik `latex-test` v VSCode. Če še niste namestili razširitve [LaTeX Workshop](https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop), to naredite zdaj.
2. V VSCode naredite novo datoteko, ki jo poimenujte npr. `latex.tex`.
3. Vanjo prekopirajte vsebino:
```
\documentclass{article}
\begin{document}
\section*{Pitagorov izrek}
V pravokotnem trikotniku s katetama $a$ in $b$ ter hipotenuzo $c$ velja
$$ a^2 + b^2 = c^2 $$
\end{document}
```
4. Preverite, ali ste v načinu LaTeX (spodaj desno). Če niste, glejte navodila za namestitev VSCode in LaTeX.
5. Poženite ukaz "LaTeX Workshop: Build LaTeX project". Bolj natančno:
  * Odprete paleto ukazov z bližnjico <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>P</kbd> (Windows) ali <kbd>Cmd</kbd>+<kbd>Shift</kbd>+<kbd>P</kbd> (MacOS) in nikamor ne klikate z miško.
  * Začnete tipkati ime ukaza `latex wo...` (velike tiskane črke niso pomembne). Pod vnosnim poljem se vam bo odprl seznam ukazov, ki ustrezajo iskanju. S puščico navzdol na tipkovnici se pomaknite navzdol do ustreznega ukaza in stisnite [vnašalko](https://sl.wikipedia.org/wiki/Vnašalka) oz. po angleško tipko [Enter](https://en.wikipedia.org/wiki/Enter_key).
6. Oglejte si dobljeni rezultat (datoteka `latex.pdf`).
7. V urejevalniku spremenite datoteko `latex.tex` tako, da bo na koncu enačbe znak za piko `.`. Lahko dopišete tudi enačbo z izraženo hipotenuzo `c = ...` (poiščite LaTeX ukaz za koren).
8. Ponovite 4. in 5. korak.

[VSCode, LaTeX, Windows in slovenska tipkovnica](faq:vscode-latex-si).

## 2. Urnik 

1. Naredite nov imenik, npr. `rp-latex-urnik`.
2. V ta imenik shranite
  [uvodno pregledno datoteko](https://ucilnica.fmf.uni-lj.si/pluginfile.php/86539/mod_folder/content/0/1-osnove.tex?forcedownload=1).
3. V isti imenik shranite tudi
  [datoteke za nalogo Urnik](https://ucilnica.fmf.uni-lj.si/mod/folder/view.php?id=59982)
  (najdete jih tudi spodaj, pod razdelkom Uvod v LaTeX).
4. Besedilo v datoteki
   [urnik.tex](https://ucilnica.fmf.uni-lj.si/pluginfile.php/127250/mod_folder/content/0/urnik.tex?forcedownload=1)
   oblikujte v LaTeX-u tako, da bo prevedena PDF datoteka čim bolj podobna
   [rešitvi](https://ucilnica.fmf.uni-lj.si/pluginfile.php/127250/mod_folder/content/0/urnik-resitev.pdf?forcedownload=1).
   Pri reševanju si pomagajte z uvodno pregledno datoteko.
5. Česar ne boste rešili na vajah, rešujte doma.  

V datoteki `urnik.tex` je vsebina že označena z okoljem `document`, vrsta
dokumenta pa je že nastavljena na `article`. 
Pri naslednjih nalogah vam bo prišla prav paleta ukazov, ki jo ponuja VSCode.
Do nje dostopate z bližnjico `Ctrl+Shift+P` oz. `Cmd+Shift+P`.
V vnosno polje vpišite `latex surround`. Med rezultati boste našli dva ukaza.
S tipkami gor/dol in tipko `Enter` izberite pravega.

* _LaTeX Workshop: Surround selection with LaTeX command_, 
  ki izbrano besedilo obda z ukazom, `\ukaz{izbrano besedilo}`. 
  Ko izberete ta ukaz, se vam pokaže še vnosno polje, 
  v katerem izberete LaTeX-ov ukaz (`title`, `section`, itd.).
* _LaTeX Workshop: Surround selection with \begin{}...\end{}_. 
  Ta ukaz izbrano besedilo obda z `\begin{}` in `\end{}` in pripravi dva kurzorja 
  (enega v `begin` in drugega v `end`), s katerima lahko napišete ime okolja. 
  Dveh kurzorjev se iznebite tako, da stisnete tipko `Esc`.

Pri nekaterih nalogah se splača uporabiti več kurzorjev hkrati;
bližnjice poiščite v [plonkcu](bliznjice:vscode).

1.  Velikost strani naj bo `A4`, osnovna velikost pisave pa `10pt` (to so
    nastavitve za ukaz `documentclass`, ki jih ločite z vejicami).
    
2.  Vključite pakete za podporo slovenščini, prepoznavo vhodnega kodiranja
    `utf8` in izhodnega kodiranja `T1`.
    
3.  Pri tej nalogi (in tudi vseh naslednjih) si pomagajte s paleto ukazov!
    Naslov, avtor, datum in povzetek naj bodo izdelani z uporabo ukazov in
    okolja, ki so v ta namen definirani v razredu `article`. Da se bo glava
    dokumenta s temi podatki prikazala, morate uporabiti ukaz `\maketitle`.
    
4.  V besedilu določi, kaj so naslovi razdelkov, podrazdelkov in
    podpodrazdelkov. Dovolj je, na določite enega ali dva na začetku, ostale pa sproti.
    
5.  Primer vsebine XML datoteke in načrti postopkov naj bodo prikazani v
    posebnem okolju, ki ohranja presledke na začetku vrstic, prelome vrstic, ter
    prikaže odstavek, kot da je napisan na pisalni stroj. To okolje se imenuje
    `verbatim`.
    
6.  Poskrbi za oštevilčene in neoštevilčene sezname. S pomočjo ukaza iz palete
    naredite ustrezno okolje. Z večimi kurzorji hkrati napišite še ukaze `\item`, 
    kjer jih potrebujete.
    Pri prvem seznamu se vsi elementi začnejo z besedo `Razred`, zato lahko več 
    kurzorjev na pravih mestih dobite enostavno s pomočjo iskanja.
    Navodila za ležeče besede so v naslednji nalogi.

7.  V besedilu je definiranih nekaj novih pojmov. Zapisani so med poševnima
    črtama. Da bodo prikazani ležeče, uporabi ukaz `\emph`. Pomagaj si z orodjem
    *Replace* in regularnimi izrazi. V polju za iskanje (odpremo ga z `Ctrl/Cmd + F`) 
    izberemo možnost za iskanje z regularnimi izrazi (gumb z napisom `.*`). 
    Vpišite vzorec `/(.*)/`, ki pomeni, da iščemo nize znakov (`(.*)`) obdane z dvema poševnicama. 
    Za zamenjavo vpišemo `\emph{$1}`: niz `$1` se bo zamenjal s tistim, kar je prej stalo med
    narekovaji.
    
8.  Kjer v besedilu najdeš dva vprašaja, ju nadomesti z ustreznim matematičnim
    izrazom. Nadomesti prvi izraz, ostale pa na koncu, če ostane čas. *Pozor:*
    dva izraza sta zapisana sredinsko poravnano v svoji vrstici (na predavanjih
    ste videli, kako se to naredi). Piko za množenje dobiš z ukazom `\cdot`.
    Kadar je potrebno del besedila zapisati v matematičnem okolju, uporabi ukaz
    `\text` iz paketa `amsmath`.
    Na predavanjih ste izvedeli, da sta oba matematična 
    
9.  Odstavki, ki sledijo seznamom in postopkom, nimajo zamaknjene prve vrstice.
    To dosežeš z ukazom `\noindent` na začetku odstavka.
    
10. V besedilu je *16* vezajev in pomišljajev. Pomišljaje napravi daljše
    (širše), vezaje pa pusti takšne kot so. Pomišljaje prepoznate po tem, da so
    obdani s presledkoma: ` - `. Popravite lahko vse naenkrat s pomočjo iskanja
    in zamenjave (`Ctrl/Cmd + F`). Pomišljaj napišemo z dvema črticama med dvema
    presledkoma: ` -- `.
    
11. Na dveh mestih je del besedila zapisan v dvojnih narekovajih. Poskrbi, da
    bodo narekovaji pravilni slovenski. Slovenske narekovaje v LaTeX-u dobimo
    ``">takole"<`` ali pa ``"`takole"'``. Napačni načini pisanja narekovajev:
    znaka za levi in desni narekovaj nista enaka, zato se *ne* piše
    ``'takole'`` ali ``''takole''``. Še posebej pa se ne piše ``"takole"``.
    Uporabite iskanje in zamenjavo z regularnimi izrazi. 
    Vzorec iz 7. naloge morate samo malo popraviti: 
    namesto poševnic napišite dvojne narekovaje, pri zamenjavi pa obdržite `$1`,
    začetek in konec pa popravite: `\emph{` zamenjajte z `">`, `}` pa z `"<`.
    
12. V predzadnjem odstavku so tri črke podčrtane.
    
13. Pred podrazdelkom Omejitve morajo biti tri besede (`bool`, `true`, `false`)
    zapisane v drugačni pisavi (kot bile natipkane s pisalnim strojem).
    
14. Poskrbi, da presledki za pikami, ki ne pomenijo konec stavka, ne bodo
    preveliki. Taki so na primer presledki v datumu ter za kraticami npr. in
    t.i.
    Pomagate si lahko z iskanjem in zamenjavo z regularnimi izrazi.
    Pazite, da boste vključili tudi razlikovanje velikih in malih črk (gumb `Aa`).
    Kaj naredi vzorec `\. ([a-z])`?

15. Če tega nisi naredil prej, je sedaj čas, da zamenjaš vse `??` s
    pripadajočimi matematičnimi izrazi.
