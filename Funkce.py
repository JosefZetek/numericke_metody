import numpy as np


class Funkce:

    def __init__(self, f, pocet_parametru):
        self.f = f
        self.pocet_parametru = pocet_parametru

    def gradient(self, x, h):
        if len(x) != self.pocet_parametru or len(h) != self.pocet_parametru:
            raise ValueError("Gradient je definovan pro " + str(self.pocet_parametru) + " parametry")

        return (self.f(x + h) - self.f(x)) / max(h)

    def spocitej_reziduum(self, x, h):
        reziduum = np.zeros(len(x))

        for i in range(len(reziduum)):
            h_array = np.zeros(len(reziduum))
            h_array[i] = h

            try:
                reziduum[i] = -self.gradient(x, h_array)
            except ValueError as e:
                raise e

        return reziduum.reshape((1, -1))

    def spocti_hessovo_matici(self, x, h=0.01):
        n = len(x)

        # Pocatecni nastaveni hessovo matice
        hessovo_matice = np.zeros((len(x), len(x)))

        for i in range(len(x)):
            for j in range(len(x)):
                # Spocitani castecnych derivaci druheho radu pomoci centralni diference
                dx1 = np.zeros(n)
                dx1[i] = h

                dx2 = np.zeros(n)
                dx2[j] = h

                hessovo_matice[i, j] = (self.f(x + dx1 + dx2) - self.f(x + dx1) - self.f(x + dx2) + self.f(x)) / (h ** 2)

        return hessovo_matice
