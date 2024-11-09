import unittest
import numpy as np
from matriisilaskin import Matriisilaskin

class TestMatriisilaskin(unittest.TestCase):
    def setUp(self):
        self.laskin = Matriisilaskin()

        self.A = [
            [-4.432, 17.255, -1.411],
            [-19.101, -15.801, 15.313]
        ]

        self.B = [
            [7.462, 5.936],
            [8.718, 6.926],
            [-9.943, -8.442]
        ]

        self.C = [
            [-7.469, 10.219, -9.71],
            [-17.166, -1.364, -12.821]
        ]

        self.D = [
            [-13.928],
            [0.932],
            [5.231],
            [1.002],
            [-7.811]
        ]


    def test_matriisitulo_toimii(self):
        tulo = self.laskin.matriisitulo(self.A, self.B)
        oikea = [
            [131.387, 105.111],
            [-432.542, -352.094]
        ]
        np.testing.assert_allclose(tulo, oikea, atol=0.001)

    def test_matriisitulo_vaara_koko(self):
        with self.assertRaises(ValueError):
            self.laskin.matriisitulo(self.A, self.C)

    def test_matriisisumma(self):
        oikea = [
            [-11.901, 27.474, -11.121],
            [-36.267, -17.165, 2.492]
        ]
        np.testing.assert_allclose(self.laskin.matriisisumma(self.A, self.C), oikea, atol=0.001)
    
    def test_matriisisumma_vaara_koko(self):
        with self.assertRaises(ValueError):
            self.laskin.matriisisumma(self.A, self.B)

    def test_skalaaritulo(self):
        oikea = [
            [18.925, -73.679, 6.025],
            [81.561, 67.470, -65.387]
        ]
        np.testing.assert_allclose(self.laskin.skalaaritulo(self.A, -4.27), oikea, atol=0.001)

    def test_matriisierotus(self):
        oikea = [
            [3.037, 7.036, 8.299],
            [-1.935, -14.437, 28.134]
        ]
        np.testing.assert_allclose(self.laskin.matriisierotus(self.A, self.C), oikea, atol=0.001)

    def test_matriisin_transpoosi(self):
        oikea = [
            [-4.432, -19.101],
            [17.255, -15.801],
            [-1.411, 15.313]
        ]
        self.assertEqual(self.laskin.transpoosi(self.A), oikea)

    def test_normi(self):
        self.assertAlmostEqual(self.laskin.normi(self.D), 16.859, places=3)