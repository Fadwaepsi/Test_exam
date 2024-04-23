# unit test case 
import unittest
from Add_Test import add

  
class TestAddMethods(unittest.TestCase): 
    # test function to test equality of two value 
    def test_add_positive_numbers():
          
        self.assertEqual(add(5,3),8, "its equal") 
  
if __name__ == '__main__': 
    unittest.main() 