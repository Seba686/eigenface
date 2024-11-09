import unittest
import numpy as np
from matriisilaskin import QR_algoritmi

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
        self.A = [
            [4, 4, 0],
            [9, -1, 9],
            [-15, 2, 10]
        ]

    def test_identiteettimatriisi(self):
        np.testing.assert_allclose(self.alg.identiteettimatriisi(7), np.identity(7))

    def test_matriisin_laajentaminen(self):
        oikea = [
            [1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 4, 4, 0],
            [0, 0, 9, -1, 9],
            [0, 0, -15, 2, 10]
        ]

        self.assertEqual(self.alg.Q_i(self.A, 5), oikea)

    def test_qr_hajotelma(self):
        Q, R = self.alg.qr_hajotelma(self.A)
        np.testing.assert_allclose(np.matmul(Q, R), self.A, atol=0.001)