from math import sqrt, copysign

# Numpya tarvitaan vain tyypin tarkistamista varten normi_r funktiossa.
import numpy as np

class QR_algoritmi:
    def __init__(self, laskin):
        self.laskin = laskin

    # Laskee matriisin QR-hajotelman käyttämällä Householderin kuvauksia.
    def qr_hajotelma(self, A):
        n = len(A)
        R = A
        Q = [[0 for _ in range(n)] for _ in range(n)]
        I = self.identiteettimatriisi(n)

        for k in range(n-1):
            x = [[rivi[k]] for rivi in R[k:]]
            e = [[rivi[k]] for rivi in I[k:]]
            alpha = -1 * copysign(1, x[0][0]) * self.laskin.normi(x)
            e = self.laskin.skalaaritulo(e, alpha)

            u = self.laskin.matriisisumma(x, e)
            u_normi = self.laskin.normi(u)
            v = self.laskin.skalaaritulo(u, 1/u_normi)

            Q_min = self.laskin.matriisitulo(v, self.laskin.transpoosi(v))
            Q_min = self.laskin.skalaaritulo(Q_min, -2)
            I_Q = self.identiteettimatriisi(n - k)
            Q_min = self.laskin.matriisisumma(Q_min, I_Q)

            Q_t = self.Q_i(Q_min, n)

            if k == 0:
                Q = Q_t
                R = self.laskin.matriisitulo(Q_t, A)
            else:
                Q = self.laskin.matriisitulo(Q_t, Q)
                R = self.laskin.matriisitulo(Q_t, R)
        return self.laskin.transpoosi(Q), R

    # Laskee matriisin ominaisarvot ja ominaisvektorit. Palauttaa listan ominaisarvoista
    # ja matriisin missä jokainen sarake vastaa yhtä ominaisvektoria. Ominaisarvot
    # ja niitä vastaavat ominaisvektorit on järjestetty suurimmasta pienimpään.
    def qr_algoritmi(self, A):
        k = 20
        ominaisvektorit = self.identiteettimatriisi(len(A))
        A_k = A

        for i in range(k):
            Q, R = self.qr_hajotelma(A_k)
            A_k = self.laskin.matriisitulo(R, Q)
            ominaisvektorit = self.laskin.matriisitulo(ominaisvektorit, Q)

        ominaisarvot = []
        for i in range(len(A)):
            for j in range(len(A)):
                if i == j:
                    ominaisarvot.append(A_k[i][j])

        ominaisvektorit = self.laskin.transpoosi(ominaisvektorit)
        ominaisvektorit.reverse()

        ominaisarvot, ominaisvektorit = \
        (list(t) for t in zip(*sorted(zip(ominaisarvot, ominaisvektorit), reverse=True)))

        ominaisvektorit = self.laskin.transpoosi(ominaisvektorit)
        ominaisvektorit.reverse()
        return ominaisarvot, ominaisvektorit

    # Palauttaa [I, 0
    #            0, Q_min]
    # matriisin, missä I on n*n identiteettimatriisi.
    def Q_i(self, Q_min, n):
        q = len(Q_min)
        Q = []
        for i in range(n):
            Q.append([])
            for j in range(n):
                if i >= n - q and j >= n - q:
                    Q[i].append(Q_min[i-(n-q)][j-(n-q)])
                elif i == j:
                    Q[i].append(1)
                else:
                    Q[i].append(0)
        return Q

    # Palauttaa n*n identiteettimatriisin.
    def identiteettimatriisi(self, n):
        return [[float(i == j) for i in range(n)] for j in range(n)]

class Matriisilaskin:
    # Laskee tulon A * B.
    def matriisitulo(self, A, B):
        m = len(A)
        n = len(B[0])

        if len(B) != len(A[0]):
            raise ValueError(f"Vääränkokoiset matriisit: \
                             ({len(A)}, {len(A[0])}) ja ({len(B)}, {len(B[0])}).")
        tulo = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                tmp = 0
                for k in range(len(B)):
                    tmp += A[i][k] * B[k][j]
                tulo[i][j] = tmp
        return tulo

    # Laskee summan A + B.
    def matriisisumma(self, A, B):
        m = len(A)
        n = len(A[0])
        if m != len(B) or n != len(B[0]):
            raise ValueError(f"Vääränkokoiset matriisit: \
                             ({len(A)}, {len(A[0])}) ja ({len(B)}, {len(B[0])}).")
        summa = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                summa[i][j] = A[i][j] + B[i][j]
        return summa

    # Laskee erotuksen A - B.
    def matriisierotus(self, A, B):
        return self.matriisisumma(A, self.skalaaritulo(B, -1))

    # Kertoo matriisin A skalarilla s.
    def skalaaritulo(self, A, s):
        tulo = [[0 for _ in range(len(A[0]))] for _ in range(len(A))]
        for i in range(len(A)):
            for j in range(len(A[0])):
                tulo[i][j] = A[i][j] * s
        return tulo

    # Laskee matriisin transpoosin.
    def transpoosi(self, A):
        return [[i[j] for i in A] for j in range(len(A[0]))]

    # Laskee sarakevektorin pituuden.
    def normi(self, A):
        pistetulo = 0
        for i in A:
            pistetulo += i[0]**2
        return sqrt(pistetulo)

    # Laskee rivivektorin pituuden. Syöte voi olla matriisi tai yksiuloitteinen lista.
    def normi_r(self, A):
        summa = 0
        if isinstance(A[0], (list, np.ndarray)):
            for i in A[0]:
                summa += i**2
            return sqrt(summa)
        for i in A:
            summa += i**2
        return sqrt(summa)
