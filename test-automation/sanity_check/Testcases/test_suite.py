import pytest
from conftest import *
from common_functions import *
from test_Dashboardcheck import Test_DashboardCheck
from test_CTAcheck import Test_CTAcheck
from test_Cafcheck import Test_Caf
from test_login import Test_Logincheck
from test_otplogin import Test_checkloginotp
from test_signup import Test_Signupcheck
# from test_schemavalidatorsanity import TestSchemaValidate
# from test_ampvalidsanity import Test_AmpValidate

# List of test classes for pytest to discover
test_classes = [
    Test_DashboardCheck,
    Test_CTAcheck,
    Test_Caf,
    Test_Logincheck,
    Test_checkloginotp,
    Test_Signupcheck
    # TestSchemaValidate,
    # Test_AmpValidate

]

def test_suite():
    for test_class in test_classes:
        pytest.main(["-v", "-s", "--maxfail=1", "--disable-warnings", "--tb=short", f"{test_class.__module__}::{test_class.__name__}"])

if __name__ == "__main__":
    test_suite()
