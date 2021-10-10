import unittest
from manipulationDB.intervention import Intervention

class InterventionTestCase(unittest.TestCase):
    def test_Creer_Intervention(self):
        inter1 = Intervention(1 , 1 , "a" , "a", True, "a")
        self.assertIsNotNone(inter1)



if __name__ == '__main__':
    unittest.main()
