import unittest
from IELTS.TestCases.conftest import *
from IELTS.TestCases.test_Ieltssignup import Test_IELTSignup
from IELTS.TestCases.test_GISsignup import Test_GISignup
from IELTS.TestCases.test_toeflsignup import Test_TOEFLSignup

class TestSuit(unittest.TestSuite):
    def __init__(self):
        super(TestSuit, self).__init__()

        # List of test case classes to include in the suite
        test_classes = [Test_IELTSignup, Test_GISignup, Test_TOEFLSignup]

        # Create a test loader
        test_loader = unittest.TestLoader()

        # Add tests from each test case to the suite
        for test_class in test_classes:
            test_suite = test_loader.loadTestsFromTestCase(test_class)
            self.addTests(test_suite)

if __name__ == '__main__':
    # Create a test suite instance and run it
    test_suite = TestSuit()
    unittest.TextTestRunner().run(test_suite)
