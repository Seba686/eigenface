import unittest
import random
import numpy as np
from matriisilaskin import QR_algoritmi, Matriisilaskin
random.seed(10)

class StubLaskin:
    def matriisitulo(self, A, B):
        return np.matmul(A, B)
    
    def matriisisumma(self, A, B):
        return np.add(A, B)
    
    def skalaaritulo(self, A, s):
        return np.multiply(A, s)
    
    def transpoosi(self, A):
        return np.transpose(A)
    
    def normi(self, A):
        return np.linalg.norm(A)
    
class TestQR_algoritmi(unittest.TestCase):
    def setUp(self):
        self.alg = QR_algoritmi(StubLaskin())
        self.laskin = Matriisilaskin()
        self.alg2 = QR_algoritmi(self.laskin)

        self.A = np.random.rand(20, 20)

        self.B = [
            [4, 4, 0],
            [9, -1, 9],
            [-15, 2, 10]
        ]

        a = [[random.random() for _ in range(100)] for _ in range(10)]
        b = self.laskin.transpoosi(a)
        self.C = self.laskin.matriisitulo(a, b)

    def test_identiteettimatriisi(self):
        np.testing.assert_allclose(self.alg.identiteettimatriisi(20), np.identity(20))

    def test_matriisin_laajentaminen(self):
        oikea = [
            [1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 4, 4, 0],
            [0, 0, 9, -1, 9],
            [0, 0, -15, 2, 10]
        ]

        self.assertEqual(self.alg.Q_i(self.B, 5), oikea)

    def test_qr_hajotelma(self):
        Q, R = self.alg.qr_hajotelma(self.A)
        np.testing.assert_allclose(np.matmul(Q, R), self.A)

    def test_laskee_oikeat_ominaisarvot(self):
        oikea, _ = np.linalg.eigh(self.C)
        oikea[::-1].sort()
        ominaisarvot, _ = self.alg2.qr_algoritmi(self.C)
        np.testing.assert_allclose(ominaisarvot, oikea, rtol=0.05)
