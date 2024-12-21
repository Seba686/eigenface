# Toteutusdokumentti
Työssä ei ole käytetty tekoälyä.
## Ohjelman rakenne
Ohjelma käyttää Eigenface menetelmää kasvojentunnistusta varten. Ohjelma on jaettu kahteen tiedostoon: pääohjelma index.py ja matriisilaskin.py.

Pääohjelma muodostaa aluksi kuvamatriisin hakemalla kansiosta data yhteensä 25 satunnaisesti valittua kuvaa. Matriisin jokainen sarake vastaa yhtä kuvaa. Samalla otetaan talteen tieto mitä kuvia käytetään harjoitusdatana, niin että loput kuvista voidaan käyttää testidatana. Seuraavaksi muodostetaan kuvamatriisista kovarianssimatriisi ja lasketaan kovarianssimatriisin ominaisarvot ja ominaisvektorit. Kyseessä on siis pääkomponenttianalyysi ja ajatuksena on että mikä tahansa kuva voidaan approksimoida näiden ominaisvektorien lineaarikombinaationa. Lineaarikombinaation kertoimet lasketaan ja tallennetaan muuttujaan self.painot. Lopuksi suoritetaan testit: valitaan kaikki ne kuvat, jotka ei ole käytetty harjoitusdatana, ja lasketaan jokaiselle kuvalle painot. Näitä painoja verrataan harjoituskuvien painoihin ja valitaan lähin oleva kuva.

Tiedosto matriisilaskin tarjoaa pääohjelmalle tarvittavat matriisioperaatiot. Esimerkiksi matriisitulo, matriisisumma ja transpoosi on toteutettu suoraan vastaavista määritelmistä. Ominaisarvojen ja ominaisvektorien laskeminen on huomattavasti haastavampaa, ja sitä varten on käytetty QR algoritmia. QR algoritmi laskee ensin matriisin QR-hajotelman ja sitten matriisitulon RQ. Noin 20 iteraation jälkeen saadaan tarpeeksi hyvä arvio ominaisarvoille ja ominaisvektoreille.

## Aika- ja tilavaativuudet
Kuvamatriisia varten tarvitaan tilaa O(plm), missä p ja l ovat kuvien pituus ja leveys pikseleinä, ja m on kuvien määrä. Matriisitulon aikavaativuus on O(n^3) ja matriisisumman aikavaativuus on O(n^2). QR-hajotelman ja QR algoritmin aikavaativuus on O(n^4) koska QR-hajotelmassa lasketaan matriisituloja n-1 kertaa.

## Puutteet ja parannusehdotukset
Tällä hetkellä ohjelmaa valitsee satunnaisesti kuvia kansiosta data. Kuvat ovat kaikki mustavalkoisia sekä saman kokoisia. Yksi hyvä ominaisuus olisi siis omien kuvien lisääminen, jolloin pitää kuitenkin varmistaa että kuvien koot ovat samat. Toinen tärkeä asia mitä voisi parantaa on ohjelman tehokkuus. Jos valitaan enemmän kuin noin 60 kuvaa alkaa ohjelman suoritus hidastua. Suurin syy tähän on QR algoritmin toteutus, joka ei ole tehokkain mahdollinen.

Ohjelmalle voisi lisätä myös graafisen käyttöliittymän joka näyttäisi kuvat jotka tunnistettiin.

## Lähteet
[Wikipedia: Eigenface](https://en.wikipedia.org/wiki/Eigenface)

[Wikipedia: QR algorithm](https://en.wikipedia.org/wiki/QR_algorithm)