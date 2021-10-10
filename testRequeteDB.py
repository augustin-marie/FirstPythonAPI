import unittest
from manipulationDB.requetesDB import RequetesDB

class RequeteDBTestCase(unittest.TestCase):
    def test_Creer_requete(self):
        requete1 = RequetesDB("interventions.db")
        self.assertIsNotNone(requete1)





if __name__ == '__main__':
    unittest.main()
