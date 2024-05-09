import numpy as np
import math

from NejvetsiSpad import NejvetsiSpad
from SdruzeneGradienty import SdruzeneGradienty
from Funkce import Funkce
from UdelejGrafy import UdelejGrafy


def funkce(x):
    if len(x) != 2:
        raise ValueError("Funkce je definovana pro dva parametry")

    return (2 * ((x[0] - 2) ** 4)) + (x[1] ** 2)

def nahodny_pocatecni_bod(pocet_parametru):
    return np.random.rand(pocet_parametru)


# -------------------TESTY-------------------
pocet_parametru = 2

trida_funkce = Funkce(funkce, pocet_parametru)
nejvetsi_spad = NejvetsiSpad(trida_funkce)
sdruzene_gradienty = SdruzeneGradienty(trida_funkce)

sdruzene_gradienty_iterace = []
nejvetsi_spad_iterace = []

sg_iterace_celkem = 0
ns_iterace_celkem = 0

sg_rychlejsi = 0
ns_rychlejsi = 0

hodnoty_y_sg = None
hodnoty_y_ns = None

pocet_testu = 100
for i in range(pocet_testu):

    pocatecni_reseni = nahodny_pocatecni_bod(pocet_parametru)
    reseni_sg, pocet_iteraci_sg = sdruzene_gradienty.sdruzene_gradienty(pocatecni_reseni)
    sdruzene_gradienty_iterace.append(pocet_iteraci_sg)

    reseni_ns, pocet_iteraci_ns = nejvetsi_spad.nejvetsi_spad(pocatecni_reseni)
    nejvetsi_spad_iterace.append(pocet_iteraci_ns)

    sg_iterace_celkem += pocet_iteraci_sg
    ns_iterace_celkem += pocet_iteraci_ns

    if pocet_iteraci_sg < pocet_iteraci_ns:
        sg_rychlejsi += 1
    elif pocet_iteraci_sg > pocet_iteraci_ns:
        ns_rychlejsi += 1


UdelejGrafy(pocet_testu, sdruzene_gradienty_iterace, nejvetsi_spad_iterace, sg_iterace_celkem, ns_iterace_celkem, sg_rychlejsi, ns_rychlejsi)