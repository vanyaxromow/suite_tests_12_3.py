import unittest
from tests_12_3 import RunnerTest, TournamentTest

someST = unittest.TestSuite()
someST.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
someST.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))

runner =unittest.TextTestRunner(verbosity=2)
runner.run(someST)
