import numpy as np
from random import sample
from PIL import Image
from matriisilaskin import Matriisilaskin, QR_algoritmi

class Eigenface:
    def __init__(self, p, l):
        self.laskin = Matriisilaskin()
        self.alg = QR_algoritmi(self.laskin)
        self.id = {k: sample(range(1, 11), l) for k in sample(range(1, 41), p)}

        kuvat = self.muodosta_kuvamatriisi()

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
    def muodosta_kuvamatriisi(self):
        kuvat = []
        self.ttt = []
        for i in self.id.keys():
            for j in self.id[i]:
                self.ttt.append(i)
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
        #print(pituudet)
        pituudet.sort(key=lambda x: x[0])
        lahimmat = pituudet[:3]
        #print(f"on {lahimmat[1]}")
        #abc = lahimmat[0][1] #//len(self.id.keys())
        #print(len(self.ttt))
        for i in lahimmat:
            #print(f"On {self.ttt[i[1]]}")
            pass
        return self.ttt[pituudet[0][1]]

    def testi(self):
        total = 0
        oikein = 0
        for i in self.id.keys():
            for j in range(1, 11):
                if j not in self.id[i]:
                    total += 1
                    kuva = Image.open(f"./data/s{i}/{j}.pgm")
                    kuvavektori = np.array(kuva, dtype=float).flatten()
                    #print(f"Pitäisi olla {i}")
                    veikkaus = self.tunnista(self.laskin.transpoosi([kuvavektori]))
                    if i == veikkaus:
                        oikein += 1
        print(f"Tunnistettu {100*oikein/total} % kuvista.")

for i in range(5):
    test = Eigenface(5, 6)
    test.testi()
