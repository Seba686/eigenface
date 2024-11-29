import numpy as np
from PIL import Image
from matriisilaskin import Matriisilaskin, QR_algoritmi

class Eigenface:
    def __init__(self):
        p = 4
        l = 6
        self.laskin = Matriisilaskin()
        self.alg = QR_algoritmi(self.laskin)
        self.id = []

        kuvat = self.muodosta_kuvamatriisi(p, l)

        self.ka_kuva, kuvat = self.kuvien_keskiarvo(kuvat, p, l)

        kovarianssimatriisi = self.laskin.matriisitulo(self.laskin.transpoosi(kuvat), kuvat)
        kovarianssimatriisi = self.laskin.skalaaritulo(kovarianssimatriisi,
                                                       1/len(kovarianssimatriisi))

        ominaisvektorit = self.laske_paakomponentit(kovarianssimatriisi)
        ominaisvektorit = self.laskin.matriisitulo(kuvat, ominaisvektorit)
        self.ominaisvektorit = self.laskin.transpoosi(ominaisvektorit)

        uudet = []
        for i in self.ominaisvektorit:
            tmp = self.laskin.skalaaritulo([i], 1/self.laskin.normi_r(i))
            uudet.append(tmp[0])

        self.painot = self.laskin.matriisitulo(uudet, kuvat)

    # Palauttaa matriisin missä jokainen sarake vastaa yhtä kuvaa.
    def muodosta_kuvamatriisi(self, p, l):
        kuvat = []
        for i in range(1, p+1):
            for j in range(1, l+1):
                self.id.append(f"s{i}, {j}.pgm")
                kuva = Image.open(f"data/s{i}/{j}.pgm")
                kuvavektori = np.array(kuva, dtype=float).flatten()
                kuvat.append(list(kuvavektori))
        return self.laskin.transpoosi(kuvat)

    # Palauttaa kaikkien kuvien keskiarvon sekä standardisoidun kuvamatriiisin
    # (jonka sarakkeiden keskiarvo on 0).
    def kuvien_keskiarvo(self, kuvat, p, l):
        ka_kuva = [[]]
        for i in kuvat:
            ka_kuva[0].append(sum(i)/len(i))
        ka_kuva = self.laskin.transpoosi(ka_kuva)
        ka_kuvamatriisi = np.tile(np.array(ka_kuva), p*l)
        kuvat = self.laskin.matriisierotus(kuvat, ka_kuvamatriisi)
        return ka_kuva, kuvat

    # Palauttaa ne ominaisvektorit jotka vastaavat 99 % kuvien varianssista.
    def laske_paakomponentit(self, kovarianssimatriisi):
        ominaisarvot, ominaisvektorit = self.alg.qr_algoritmi(kovarianssimatriisi)
        summa = sum(ominaisarvot)
        tot = 0
        for i, j in enumerate(ominaisarvot):
            tot += j
            if tot / summa > 0.99:
                count = i
                break
        ominaisarvot = ominaisarvot[:count]
        ominaisvektorit = self.laskin.transpoosi(ominaisvektorit)[:count]
        ominaisvektorit = self.laskin.transpoosi(ominaisvektorit)
        return ominaisvektorit

    # Tunnistaa henkilön kuvasta.
    def tunnista(self, kuva):
        painot = self.laskin.matriisitulo(self.ominaisvektorit,
                                          self.laskin.matriisierotus(kuva, self.ka_kuva))
        painot = self.laskin.transpoosi(painot)
        tmp = self.laskin.transpoosi(self.painot)
        pituudet = []
        for i, j in enumerate(tmp):
            pituudet.append((self.laskin.normi_r(self.laskin.matriisierotus([j], painot)), i))

        pituudet.sort(key=lambda x: x[0])
        return self.id[pituudet[0][1]]

    def testi(self):
        total = 0
        oikein = 0
        for i in range(1, 5):
            for j in range(7, 11):
                total += 1
                kuva = Image.open(f"./data/s{i}/{j}.pgm")
                kuvavektori = np.array(kuva, dtype=float).flatten()
                veikkaus = self.tunnista(self.laskin.transpoosi([kuvavektori]))
                if f"s{i}" in veikkaus:
                    oikein += 1
        print(f"Tunnistettu {100*oikein/total} % kuvista.")

test = Eigenface()
test.testi()
