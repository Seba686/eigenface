from matriisilaskin import Matriisilaskin, QR_algoritmi
import numpy as np
from PIL import Image, ImageOps
import os

class Eigenface:
    def __init__(self):
        self.laskin = Matriisilaskin()
        self.alg = QR_algoritmi(self.laskin)
        kuvat = []
        for hakemisto in os.listdir("data"):
            for henkilo in os.listdir(f"data/{hakemisto}"):
                kuva = Image.open(f"data/{hakemisto}/{henkilo}")
                kuva = ImageOps.grayscale(kuva)
                kuvavektori = np.array(kuva, dtype=float).flatten()
                kuvat.append(kuvavektori)

        ka_kuva = [[]]
        kuvat = self.laskin.transpoosi(kuvat)
        for i in kuvat:
            ka_kuva[0].append(sum(i)/len(i))
        ka_kuva = self.laskin.transpoosi(ka_kuva)
        ka_kuva = np.tile(np.array(ka_kuva), 400)
        kuvat = self.laskin.matriisierotus(kuvat, ka_kuva)
        #kovarianssimatriisi = self.laskin.matriisitulo(self.laskin.transpoosi(kuvat), kuvat)
        kovarianssimatriisi = np.matmul(np.array(kuvat).transpose(), np.array(kuvat))
        self.laskin.skalaaritulo(kovarianssimatriisi, 1/len(kovarianssimatriisi))
        a, b = self.alg.qr_algoritmi(kovarianssimatriisi)
        print(len(a))

Eigenface()