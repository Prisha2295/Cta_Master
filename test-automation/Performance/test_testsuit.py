import unittest
from test_pagespeedperformance import Pagespeed
from test_studyabroadperfromance import StudyabroadPagespeed



#Get All Tests from Signup,Login,LOgin OTP 
TC1_pagespeed = unittest.TestLoader().loadTestsFromTestCase(Pagespeed)
TC2_studyabroadpagespeed = unittest.TestLoader().loadTestsFromTestCase(StudyabroadPagespeed)
# TC3_LoginOtp = unittest.TestLoader().loadTestsFromTestCase(Pagespeedvertical)

#Creating Test Suites acc to Sanity,Masters,Functionality

AllTestCases = unittest.TestSuite([TC1_pagespeed,TC2_studyabroadpagespeed])
unittest.TextTestRunner().run(AllTestCases)