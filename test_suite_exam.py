import unittest
from activite3Boucle import nombreGrand
from unittest.mock import patch

class TestnombreGrand(unittest.TestCase):
    @patch('builtins.input', sideeffect=['9', '1', '5'])
    def test_nombreGrand_nombreplusgrand (self, mockinput):
        resultat=nombreGrand()
        self.assertEqual(resultat, 9, "retourner le nombre le plus grand")

    @patch('builtins.input', sideeffect=['3', '1', '2'])
    def test_nombreGrand_nombrelepluspetit (self, mockinput):
        resultat=nombreGrand()
        self.assertEqual(resultat, 1, "rtourner le nombre le plus petit")

    @patch('builtins.input', sideeffect=['2', '2', '2'])
    def test_nombreGrand_nombreegeux (self, mockinput):
        resultat=nombreGrand()
        self.assestEqual(resultat, 2, "retourner le meme chiffre")

    if __name__ == '__main__' :
        unittest.main()



