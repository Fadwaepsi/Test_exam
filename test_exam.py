import unittest
from unittest.mock import patch

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

#resultat = nombreGrand()
#print(f"Le plus grand nombre parmi les nombres saisis est :{resultat}")
# affiche le nombre le plus grand

class TestNombreGrand(unittest.TestCase):
    @patch('builtins.input', sideeffect=['3', '1', '2'])
    def testincreasingorder(self, mockinput):
        result = nombreGrand()
        self.assertEqual(result, 3, "Should return the largest number in increasing order")

    if __name__ == '__main__':
        unittest.main()
