import numpy as np

from Funkce import Funkce

class NejvetsiSpad:

    def __init__(self, trida_funkce: Funkce):
        self.trida_funkce = trida_funkce

    def spocitej_delku_kroku(self, reziduum, hessovo_matice):
        if len(hessovo_matice.shape) != 2:
            raise ValueError("Hessovo matice neni 2D")

        if len(reziduum.shape) != 2:
            raise ValueError("Reziduum neni 2D")

        if hessovo_matice.shape[0] != hessovo_matice.shape[1]:
            raise ValueError("Hessovo matice neni ctvercova")

        if hessovo_matice.shape[0] != reziduum.shape[1]:
            raise ValueError("Hessovo matice nema spravne rozmery")

        transponovane_reziduum = np.transpose(reziduum)

        # citatel i jmenovatel jsou rozmeru 1x1
        citatel = np.dot(reziduum, transponovane_reziduum)[0][0]
        jmenovatel = np.dot(reziduum, np.dot(hessovo_matice, transponovane_reziduum))[0][0]

        return citatel / jmenovatel

    def nejvetsi_spad(self, x0, h=0.00001, tol=1e-5, max_iter=1000):

        if x0 is None:
            raise ValueError("Pocatecni bod nesmi byt None")

        x = x0
        pocet_iteraci = 0

        while pocet_iteraci < max_iter:

            pocet_iteraci += 1

            hessovo_matice = self.trida_funkce.spocti_hessovo_matici(x, h)
            smer = self.trida_funkce.spocitej_reziduum(x, h)
            velikost_kroku = self.spocitej_delku_kroku(smer, hessovo_matice)

            nove_x = x + velikost_kroku * smer.flatten()

            if np.linalg.norm(x - nove_x) < tol:
                return nove_x, pocet_iteraci

            x = nove_x

        return x, pocet_iteraci
