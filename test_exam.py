import unittest

def nombreGrand():
    nombres = []
# j'initialise une liste vide pour enregistrer les nombres
    for i in range(3):
        nombre = int(input("Entrez le nombre : "))
        nombres.append(nombre)
    plus_grand_nombre = nombres[0]
    for elt in nombres:
        if elt > plus_grand_nombre:
            plus_grand_nombre = elt
    return plus_grand_nombre

resultat = nombreGrand()
print(f"Le plus grand nombre parmi les nombres saisis est :{resultat}")
# affiche le nombre le plus grand

class TestnombreGrandSimple(unittest.TestCase):
    def test_nombreGrand_simple(self):
        self.assertEqual(nombreGrand(2, 5, 3), 5, "my values is ok")

    if __name__ == '__main__':
        unittest.main()
