# Testausraportti

## Yksikkötestit

Yksikkötestejä varten käytetään unittest ja Numpy kirjastoja. Yksikkötestit testaavat luokkia Matriisilaskin ja QR_algoritmi. Matriisilaskin -luokan testausta varten luodaan ensin matriiseja (kooltaan esimerkiksi 500 kertaa 50) satunnaisilla luvuilla ja tarkistetaan, että matriisioperaatiot antavat saman vastauksen kuin Numpy kirjasto.

QR_algoritmin -luokassa testataan joitakin apumetodeja sekä QR-hajotelmaa. QR-hajotelman testauksessa tarkistetaan että matriisien Q ja R tulo on yhtä kuin alkuperäinen matriisi.

## Pääohjelman testaus

Kansiossa src/data on kymmenen kuvaa neljästäkymmenestä eri henkilön kasvoista. Kun pääohjelma käynnistyy valitaan satunnaisesti esimerkiksi viisi kuvaa viidestä eri henkilöstä, ja nämä kuvat käytetään harjoitusdatana. Loput kuvat käytetään testausdatana, eli testikuvia on tässä tapauksessa 25.
