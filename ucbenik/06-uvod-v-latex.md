# Uvod v LaTeX

LaTeX je sistem za stavljenje besedila. 
Je pravzaprav prevajalnik, ki LaTeX datoteko s končnico `.tex`, 
ki vsebuje navadno besedilo, označeno s posebnimi okolji in ukazi, 
pretvori v lepo stavljeno besedila in ga shrani v datoteko PDF s končnico `.pdf`.

LaTeX-ov prevajalnik (mi bomo uporabljali `pdflatex`) je ponavadi treba pognati večkrat, 
da lahko preračuna sklice na izreke in številke strani. 
Uporabnik lahko to stori bodisi sam, bodisi uporabi program `latexmk`, 
ki požene `pdflatex` in nekatere druge programe v sklopu sistema LaTeX. 
Če uporabljate Visual Studio Code, se ob shranjevanju avtomatično požene program `latexmk`.

`````{admonition} Programska oprema
:class: important
- [LaTeX](namestitev:latex),
- [Visual Studio Code](namestitev:vscode) in
- razširitev [LaTeX Workshop](https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop).
`````

## Ukazi in okolja

LaTeX dokumente oblikujemo z _ukazi_ (angl. _command_) in _okolji_ (angl. _environment_), 
kot pri HTML pa lahko uporabljamo tudi _komentarje_.
Ukazom včasih rečemo tudi makroji (angl. _macro_).
```tex
% Okolja so podobna značkam:
\begin{⟨ime-okolja⟩} % začetek okolja
  ⟨vsebina⟩          % vsebina
\end{⟨ime-okolja⟩}   % konec okolja

% Ukazi so bolj enostavni:
\⟨ime-ukaza⟩
```
Nekateri ukazi in okolja sprejmejo tudi dodatne argumente,
ki so lahko obvezni (v zavitih oklepajih `{}`) ali neobvezni (v oglatih oklepajih `[]`).

* Ukaz `\section{Turingovi stroji}` naredi nov razdelek z naslovom "Turingovi stroji".
* Ukaz `frac`, ki v matematičnem okolju naredi ulomek, sprejme dva argumenta, 
  števec in imenovalec: `\frac{22}{7}` izpiše $\frac{22}{7}$.
* Ukaz `rule` za ločnice, ki nariše pravokotnik, sprejme dva obvezna argumenta in enega neobveznega 
  (kako visoko v vrstici stoji ločnica):
  `\rule[⟨višina⟩]{⟨dolžina⟩}{⟨širina⟩}`.

Pri teh vajah boste srečali okolja `abstract`, `verbatim` (oznaka ` ``` ` v Markdown-u), 
`itemize` in `enumerate` (znački `ul` in `ol` v HTML).
Tudi za matematični način uporabljamo okolje, in sicer
`math` za vrstičnega in `displaymath` za prikaznega (tako da izraz stoji v svoji vrstici).
Ker bi bilo zelo zamudno pisati `\begin{math}1 + 1\end{math}`, ima LaTeX za ti dve okolji posebni okrajšavi:

```
\[
  ⟨matematični izraz na sredini vrstice⟩
\]
```

ali `\(⟨matematični izraz v vrstici⟩\)`.
Včasih boste morda videli tudi starejši okrajšavi `$$` za prikazni in `$` za vrstični način.
Uporabo teh dveh okrajšav močno odsvetujemo - ko boste naleteli na napako, jo boste veliko težje razbrali.

`````{admonition} Ukazi za matematične izraze
:class: tip
V matematičnih okoljih lahko uporabljamo ukaze za matematične izraze, 
kot so `frac` za ulomke, `int` za integrale, ukaze za matrike itd. 
Ti ukazi delajo **samo v matematičnih okoljih**, izven njih pa sprožijo napako.
`````

## Struktura dokumenta

LaTeX dokument shranimo v datoteko s končnico `.tex`. Dokument je lahko shranjen
tudi v večjih datotekah, ki jih z ukazom `\input{datoteka.tex}` vključimo v
glavno datoteko.
Struktura glavne LaTeX datoteke je videti takole:

```tex
\documentclass[...]{...}

⟨preambula⟩

\begin{document}

  ⟨vsebina⟩

\end{document}
```

Ukaz `\documentclass` določa zvrst dokumenta (članek, knjiga, pismo, ...),
ki jo določimo v obveznem argumentu, takole: `\documentclass{article}`.
Možne zvrsti dokumentov so vnaprej definirane in se razlikujejo tudi po oblikovanju.
Dodatne nastavitve, kot na primer za velikost strani, lahko zapišemo v oglate oklepaje:
`\documentclass[a4paper]{article}`.

V preambuli v dokument vključimo razne pakete, uredimo nastavitve in definiramo nove makroje in okolja:

* paket vključimo z ukazom `\usepackage[⟨nastavitve⟩]{⟨ime-paketa⟩}`.
* nove ukaze in okolja definiramo ga z ukazoma `newcommand` in `newenvironment`.

LaTeX ima okoli [6000 paketov](https://www.ctan.org). Najbolj uporabni so že vključeni v
distribucijo LaTeXa, ki ste jo namestili na svojo računalnik.

### Ločevanje vsebine in predstavitve

Tudi v LaTeX-u bomo v dokumentu **določili vsebinski pomen** elementov besedila:
z ukazi za nov razdelek, podrazdelek, z okoljem za zapis izreka, itd.
Taka vrsta oblikovanja je dosti bolj prijazna uporabniku, sistematična
in prilagodljiva.

Za primer, v LaTeX-u vsebinsko oblikujemo besedilo izreka z okoljem `theorem`.
Videz izreka bi lahko oblikovali neposredno, kot spodaj, vendar 
bi bilo potem težje skrbeti za to, da vsi izreki izgledajo enako, 
da so vsi pravilno oštevilčeni, ipd.

```tex
% vsebinsko oblikovanje
\begin{theorem}
  ⟨besedilo izreka⟩
\end{theorem}

% neposredno oblikovanje
\textbf{Izrek 1.1} \textit{⟨besedilo izreka⟩}
```

Še nekaj primerov vsebinskega oblikovanja so posebni ukazi za vsebino, kot so
`section`, `subsection` in `footnote`.

### Splošna priporočila za urejanje LaTeX dokumentov

* Za vsak LaTeX dokument imejte datoteke spravljene v imeniku, ki vsebuje
  samo datoteke za ta dokument. Ta imenik potem odprite v urejevalniku
  Visual Studio Code. 
  Razlog za to je, da LaTeX med prevajanjem naredi množico datotek, 
  ki so za uporabnika večino časa neuporabne.
  Asistenti vam bodo hvaležni (sčasoma pa boste verjetno
  hvaležni tudi sami sebi).
* Napake, ki jih javlja LaTeX, niso vedno razumljive. Med drugim to pomeni, da
  jih je v besedilu težko najti. En način, da si pri tem pomagamo, je ta, da
  dokument pogosto prevedemo. 
  Ni narobe, če datoteko shranite (in s tem prevedete) po vsakem do konca napisanem ukazu.
  Tako boste vedeli, da se je napaka pojavila od takrat, ko
  je LaTeX nazadnje uspešno prevedel dokument.
  Pri tem bodite pozorni na to, kaj se dogaja v statusni vrstici.
  Hitrejši boste z <kbd>Ctrl</kbd>+<kbd>S</kbd> (🍎 <kbd>Cmd</kbd>+<kbd>S</kbd>).
* Najmanjši dokument, ki vam ga bo LaTeX še smiselno prevedel, mora vsebovati
  ukaz `\documentclass` in okolje `document`. Poglejte si, kakšne napake javi
  LaTeX, če prevajate brez tega: tako jih boste naslednjič prepoznali.

## 1. naloga: VSCode in LaTeX

Najprej preverimo, ali je vaš urejevalnik pripravljen za delo z 
[LaTeX](https://www.latex-project.org)-om. 

1. V VSCode odprite imenik s svojim repozitorijem.
   V njem naredite nov imenik `06-uvod-v-latex`, v tem imeniku še imenik `test`,
   v njem pa novo datoteko `latex-test.tex`, ki jo odprite.
2. Preverite, da spodaj desno v statusni vrstici piše LaTeX;
   če ne, morate verjetno namestiti razširitev LaTeX Workshop.
3. Preverite, da v imenih imenikov nad to datoteko **ni nobenih šumnikov ali presledkov**.
   LaTeX je tako star, da to lahko povzroča težave, še posebej na operacijskem sistemu Windows.
4. V datoteko `latex-test.tex` prekopirajte spodnje navadno besedilo in jo shranite
   s <kbd>Ctrl</kbd>+<kbd>S</kbd> (🍎 <kbd>Cmd</kbd>+<kbd>S</kbd>).
   ```
   \documentclass{article}
   \begin{document}
   \section*{Pitagorov izrek}
   V pravokotnem trikotniku s katetama \(a\) in \(b\) ter hipotenuzo \(c\) velja
   \[ a^2 + b^2 = c^2 \]
   \end{document}
   ```
5. S paleto ukazov poženite ukaz _LaTeX Workshop: Build LaTeX project_.
   Poglejte spodaj levo v statusno vrstico.
   Na desni strani bi moralo pisati _↻ Build_, ko se prevajanje konča, pa bi morali videti kljukico ✓.
   V nadaljevanju bi za prevajanje moralo zadoščati, da datoteko shranite z bližnjico
   <kbd>Ctrl</kbd>+<kbd>S</kbd> (🍎 <kbd>Cmd</kbd>+<kbd>S</kbd>).
6. Oglejte si dobljeni rezultat (datoteka `latex.pdf`).
7. V urejevalniku spremenite datoteko `latex.tex` tako, da bo na koncu enačbe znak za piko `.`. 
   Lahko dopišete tudi enačbo z izraženo hipotenuzo `c = ...` (poiščite LaTeX ukaz za koren).
8. Ponovite 5. in 6. korak.
9. Če ste na operacijskem sistemu Windows in uporabljate slovensko tipkovnico, 
   si preberite [navodila za pisanje posebnih znakov](faq:vscode-latex-si) (če tega še niste naredili).

## 2. naloga: urnik 

1. V glavnem imeniku repozitorija naredite nov imenik, `latex-pregled` in 
   v njem odpakirajte arhiv [`latex-pregled.zip`](06-uvod-v-latex/latex-pregled.zip).
2. V imenik `06-uvod-v-latex` shranite [datoteke za nalogo Urnik](TODO)
3. Besedilo v datoteki `urnik.tex` oblikujte v LaTeX-u tako, 
   da bo prevedena PDF datoteka čim bolj podobna rešitvi.
   Pri reševanju si pomagajte z uvodno pregledno datoteko.

V datoteki `urnik.tex` je vsebina že označena z okoljem `document`, vrsta
dokumenta pa je že nastavljena na `article`. 
V paleti ukazov boste pod `latex surround` našli dva uporabna ukaza:

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
    *Replace* in regularnimi izrazi. V polju za iskanje 
    (odpremo ga z <kbd>Ctrl</kbd> + <kbd>F</kbd> oz. 🍎 <kbd>Cmd</kbd> + <kbd>F</kbd>) 
    izberemo možnost za iskanje z regularnimi izrazi (gumb z napisom `.*`). 
    Vpišite vzorec `/(.*)/`, ki pomeni, da iščemo nize znakov (`(.*)`) obdane z dvema poševnicama. 
    Za zamenjavo vpišemo `\emph{$1}`: niz `$1` se bo zamenjal s tistim, kar je prej stalo med
    poševnicami.
    
8.  Kjer v besedilu najdeš dva vprašaja, ju nadomesti z ustreznim matematičnim
    izrazom. Nadomesti prvi izraz, ostale pa na koncu, če ostane čas. *Pozor:*
    dva izraza sta zapisana sredinsko poravnano v svoji vrstici (na predavanjih
    ste videli, kako se to naredi). Piko za množenje dobiš z ukazom `\cdot`.
    Kadar je potrebno del besedila zapisati v matematičnem okolju, uporabi ukaz
    `\text` iz paketa `amsmath`.
    
9.  Odstavki, ki sledijo seznamom in postopkom, nimajo zamaknjene prve vrstice.
    To dosežeš z ukazom `\noindent` na začetku odstavka.
    
10. V besedilu je *16* vezajev in pomišljajev. Pomišljaje napravi daljše
    (širše), vezaje pa pusti takšne kot so. Pomišljaje prepoznate po tem, da so
    obdani s presledkoma: ` - `. Popravite lahko vse naenkrat s pomočjo iskanja
    in zamenjave. Pomišljaj napišemo z dvema črticama med dvema
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
    
14. Poskrbite, da presledki za pikami, ki ne pomenijo konca stavka, ne bodo
    preveliki. Taki so na primer presledki v datumu ter za kraticami npr. in
    t.i.
    Pomagate si lahko z iskanjem in zamenjavo z regularnimi izrazi.
    Pazite, da boste vključili tudi razlikovanje velikih in malih črk (gumb `Aa`).
    Kaj naredi vzorec `\. ([a-z])`?

15. Če tega niste naredili prej, je sedaj čas, da zamenjate vse `??` s
    pripadajočimi matematičnimi izrazi.


## Domača naloga

1. Dokončajte vaje, če jih še niste.