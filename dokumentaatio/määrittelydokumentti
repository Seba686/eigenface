# Määrittelydokumentti

Opinto-ohjelma: tietojenkäsittelytiede, kandidaatin tutkinto.

Projekti on Pythonilla toteutettava kasvojentunnistusohjelma, joka käyttää eigenface menetelmää. Projekti dokumentoidaan suomeksi.

Menetelmässä käytetään pääkomponenttianalyysiä jotta paljon tietoa sisältävistä kasvojen kuvista saadaan tunnistettua pääpiirteet ja näin ollen ongelman laskennallinen vaativuus pysyy kohtuullisena. Kasvojen pääpirteet ovat kovarianssimatriisin ominaisvektorit. Jokainen kasvo on jokin lineaarikombinaatio näistä ominaisvektorista, eli tunnistus tapahtuu selvittämällä tämä lineaarikombinaatio ja vertaamalla se harjoitteludataan.

Keskeinen tietorakenne on matriisi, joka voidaan esittää kaksiuloitteisena listana. Eigenface menetelmää varten tarvitaan tapa laskea matriisin ominaisarvot ja niitä vastaavat ominaisvektorit. Tätä varten voidaan käyttää QR algoritmia, joka perustuu matriisin QR hajotelmaan. QR hajotelma puolestaan voidaan laskea käyttämällä Householderin kuvausta. Tämä edellyttää seuraavien matriisien laskutoimituksien toteuttamista: matriisin kertominen skalarilla, matriisin tulo ja matriisin summa.

Ohjelman suoritusta varten tarvitaan dataa, esimerkiksi kymmenen eri kuvaa sadasta eri henkilöstä. Ohjelmaa toimii kahdessa osassa: ensiksi alustetaan ohjelmaa jolloin puolet kunkin henkilön kuvista käytetään harjoitteludatana. Tämän jälkeen loput kuvista käytetään testausta varten. Datana voi käyttää esimerkiksi AT&T Database of Faces.

Kahden n kertaa n matriisin tulon aikavaativuus on O(n^3), mutta tätä voi parantaa käyttämällä Strassenin algoritmia. Matriisien koot eivät kuitenkaan riipu harjoitusdatasta.

## Viitteet
https://en.wikipedia.org/wiki/Eigenface
https://en.wikipedia.org/wiki/QR_algorithm
https://www.kaggle.com/datasets/kasikrit/att-database-of-faces
