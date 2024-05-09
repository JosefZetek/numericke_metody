import numpy as np

from Funkce import Funkce
from NejvetsiSpad import NejvetsiSpad


class SdruzeneGradienty:
    def __init__(self, trida_funkce: Funkce):
        self.trida_funkce = trida_funkce

    def spocitej_beta(self, predchozi_smer, hessovo_matice, reziduum):
        # citatel i jmenovatel maji rozmer 1x1
        citatel = np.dot(predchozi_smer, np.dot(hessovo_matice, np.transpose(reziduum)))[0][0]
        jmenovatel = np.dot(predchozi_smer, np.dot(hessovo_matice, np.transpose(predchozi_smer)))[0][0]

        return citatel / jmenovatel

    def spocitej_smer(self, predchozi_smer, hessovo_matice, reziduum):
        beta = self.spocitej_beta(predchozi_smer, hessovo_matice, reziduum)
        return reziduum + beta * predchozi_smer

    def spocitej_delku_kroku(self, predchozi_smer, predchozi_reziduum, hessovo_matice):
        if len(hessovo_matice.shape) != 2:
            raise ValueError("Hessovo matice neni 2D")

        if len(predchozi_reziduum.shape) != 2:
            raise ValueError("Reziduum neni 2D")

        if hessovo_matice.shape[0] != hessovo_matice.shape[1]:
            raise ValueError("Hessovo matice neni ctvercova")

        if hessovo_matice.shape[0] != predchozi_reziduum.shape[1]:
            raise ValueError("Hessovo matice nema spravne rozmery")

        #citatel i jmenovatel maji rozmer 1x1
        citatel = np.dot(predchozi_smer, np.transpose(predchozi_reziduum))[0][0]
        jmenovatel = np.dot(predchozi_smer, np.dot(hessovo_matice, np.transpose(predchozi_smer)))[0][0]
        return citatel / jmenovatel

    def sdruzene_gradienty(self, x0, h=0.00001, tol=1e-5, max_iter=1000):

        if x0 is None:
            raise ValueError("Pocatecni bod nesmi byt None")

        x = x0

        pocet_iteraci = 1

        # V prvni iteraci se postupuje jako u nejvetsiho spadu
        nejvetsi_spad = NejvetsiSpad(self.trida_funkce)

        smer = self.trida_funkce.spocitej_reziduum(x, h)
        delka_kroku = nejvetsi_spad.spocitej_delku_kroku(smer, self.trida_funkce.spocti_hessovo_matici(x, h))
        nove_x = x + delka_kroku * smer.flatten()
        predchozi_smer = smer
        predchozi_reziduum = smer


        while pocet_iteraci < max_iter:

            if np.linalg.norm(x - nove_x) < tol:
                return nove_x, pocet_iteraci

            hessovo_matice = self.trida_funkce.spocti_hessovo_matici(nove_x, h)
            reziduum = self.trida_funkce.spocitej_reziduum(nove_x, h)
            smer = self.spocitej_smer(predchozi_smer, hessovo_matice, reziduum)
            delka_kroku = self.spocitej_delku_kroku(predchozi_smer, predchozi_reziduum, hessovo_matice)

            x = nove_x
            nove_x = x + delka_kroku * smer.flatten()

            predchozi_reziduum = reziduum
            predchozi_smer = smer

            pocet_iteraci += 1

        return nove_x, pocet_iteraci
