import matplotlib.pyplot as plt
import numpy as np

class UdelejGrafy:
    def __init__(self, pocet_testu, sdruzene_gradienty_iterace, nejvetsi_spad_iterace, sg_iterace_celkem, ns_iterace_celkem, sg_rychlejsi, ns_rychlejsi):
        plt.figure(figsize=(10, 5))
        plt.plot(np.arange(pocet_testu), sdruzene_gradienty_iterace, label="Metoda sdružených gradientů")
        plt.plot(np.arange(pocet_testu), nejvetsi_spad_iterace, label="Metoda největšího spád")
        plt.legend()
        plt.xlabel("Iterace")
        plt.ylabel("Počet iterací")
        #plt.savefig("porovnani_iteraci.pdf")
        plt.show()

        plt.figure(figsize=(10, 5))
        labels = ["Metoda sdružených gradientů", "Metoda největšího spádu"]
        plt.pie([sg_iterace_celkem, ns_iterace_celkem], labels=['', ''], autopct='%1.1f%%')
        plt.legend(labels=labels)
        plt.title("Poměr celkových počtů iterací pro všechny testy", fontweight='bold')
        #plt.savefig("porovnani_celkoveho_poctu_iteraci.pdf")
        plt.show()

        plt.figure(figsize=(10, 5))
        labels = ["Rychlejší metoda sdružených gradientů", "Rychlejší metoda největšího spádu"]
        plt.pie([sg_rychlejsi, ns_rychlejsi], labels=['', ''], autopct='%d%%')
        plt.title("Porovnání počtu rychlejší konvergence", fontweight='bold')
        plt.legend(labels=labels)
        #plt.savefig("porovnani_rychlosti_konvergence.pdf")
        plt.show()