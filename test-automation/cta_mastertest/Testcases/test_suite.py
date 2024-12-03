import unittest
from conftest import *
from test_Articledetail import Test_Articledetail
from test_Articlelisting import Test_Articlelisting
from test_Boarddetail import Test_Boarddetail
from test_Caf import Test_Caf
from test_Careerdetail import Test_Careerdetail
from test_Collegedetail import Test_Collegedetail
from test_Collegelisting import Test_Collegelisting
from test_Coursedetail import Test_Coursedetail
from test_DUcollegepredictor import Test_DUCollegePredictor
from test_Examdetail import Test_Examdetail
from test_Examlisting import Test_Examlisting
from test_Fullform import Test_Fullform
from test_Homepage import Test_HomePage
from test_Insurancedetail import Test_Insurancedetail
from test_Jobassureddetail import Test_Jobassureddetail
from test_Jobassuredlisting import Test_Jobassuredlisting
from test_Newsdetail import Test_Newsdetail
from test_Newslisting import Test_Newslisting
from test_Psychometricdetail import Test_Psychometric
from test_Universitydetail import Test_Universitydetail
from common_functions import *

class TestSuit(commonfunctions):
    def test_testsuit(self):
        # Get all tests from the test cases
        test_classes = [
            Test_Articledetail(),
            Test_Articlelisting(),
            Test_Boarddetail,
            Test_Caf,
            Test_Careerdetail,
            Test_Collegedetail,
            Test_Collegelisting,
            Test_Coursedetail,
            Test_DUCollegePredictor,
            Test_Examdetail,
            Test_Examlisting,
            Test_Fullform,
            Test_HomePage,
            Test_Insurancedetail,
            Test_Jobassureddetail,
            Test_Jobassuredlisting,
            Test_Newsdetail,
            Test_Newslisting,
            Test_Psychometric,
            Test_Universitydetail
        ]

        # Create a test suite to run all test cases sequentially
        AllTestCases = unittest.TestSuite()

        for test_class in test_classes:
            test_loader = unittest.TestLoader()
            test_suite = test_loader.loadTestsFromTestCase(test_class)
            AllTestCases.addTest(test_suite)

        # Run the test suite
        unittest.TextTestRunner().run(AllTestCases)

if __name__ == '__main__':
    unittest.main()
