import unittest
import numpy as np
from matriisilaskin import Matriisilaskin

class TestMatriisilaskin(unittest.TestCase):
    def setUp(self):
        self.laskin = Matriisilaskin()

        self.A = np.random.rand(50, 500)

        self.B = np.random.rand(500, 25)

        self.C = np.random.rand(500, 1)

        self.D = np.random.rand(1, 500)

    def test_matriisitulo_toimii(self):
        oikea = np.matmul(self.A, self.B)
        tulo = self.laskin.matriisitulo(self.A, self.B)
        np.testing.assert_allclose(tulo, oikea)

    def test_matriisitulo_vaara_koko(self):
        with self.assertRaises(ValueError):
            self.laskin.matriisitulo(self.B, self.A)

    def test_matriisisumma(self):
        oikea = np.add(self.A, self.A)
        summa = self.laskin.matriisisumma(self.A, self.A)
        np.testing.assert_allclose(summa, oikea)
    
    def test_matriisisumma_vaara_koko(self):
        with self.assertRaises(ValueError):
            self.laskin.matriisisumma(self.A, self.B)

    def test_skalaaritulo(self):
        s = 3.17
        oikea = self.A * s
        skalaaritulo = self.laskin.skalaaritulo(self.A, s)
        np.testing.assert_allclose(skalaaritulo, oikea)

    def test_matriisierotus(self):
        oikea = np.subtract(self.A, self.A)
        erotus = self.laskin.matriisierotus(self.A, self.A)
        np.testing.assert_allclose(erotus, oikea)

    def test_matriisin_transpoosi(self):
        oikea = np.transpose(self.A)
        transpoosi = self.laskin.transpoosi(self.A)
        np.testing.assert_array_equal(transpoosi, oikea)

    def test_normi(self):
        oikea = np.linalg.norm(self.C)
        normi = self.laskin.normi(self.C)
        self.assertAlmostEqual(normi, oikea)

    def test_normi_r_matriisi_syotteena(self):
        oikea = np.linalg.norm(self.D)
        normi = self.laskin.normi_r(self.D)
        self.assertAlmostEqual(normi, oikea)

    def test_normi_r_lista_syotteena(self):
        A = np.random.rand(100)
        oikea = np.linalg.norm(A)
        normi = self.laskin.normi_r(A)
        self.assertAlmostEqual(normi, oikea)