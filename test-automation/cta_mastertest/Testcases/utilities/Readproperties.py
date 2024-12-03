import configparser

config=configparser.RawConfigParser()

path = config.read("../Config.ini")
# print(path)

class ReadConfig():
    @staticmethod
    def HomepageURL():
        homepage_url=config.get('common info','Base_url')

        return homepage_url
    
    @staticmethod
    def CollegedetailURL():
        collegedetail_url=config.get('common info','Base_url')
        collegedetail_url += 'colleges/lpu'

        return collegedetail_url

    @staticmethod
    def CoursedetailURL():
        coursedetail_url=config.get('common info','Base_url')
        coursedetail_url += 'courses/master-of-business-administration-mba'

        return coursedetail_url

    @staticmethod
    def UniversitydetailURL():
        universitydetail_url=config.get('common info','Base_url')
        universitydetail_url += 'university/delhi-university'

        return universitydetail_url

    @staticmethod
    def ExamdetailURL():
        examdetail_url=config.get('common info','Base_url')
        examdetail_url += 'exam/cat'

        return examdetail_url

    @staticmethod
    def CareerdetailURL():
        careerdetail_url=config.get('common info','Base_url')
        careerdetail_url += 'careers/pilot'

        return careerdetail_url

    @staticmethod
    def ExamlistingURL():
        examlisting_url=config.get('common info','Base_url')
        examlisting_url += 'engineering-entrance-exams/'

        return examlisting_url

    @staticmethod
    def CollegelistingURL():
        collegelisting_url=config.get('common info','Base_url')
        collegelisting_url += 'btech-colleges-in-india/?magicflag=1'

        return collegelisting_url

    @staticmethod
    def NewslistingURL():
        newslisting_url=config.get('common info','Base_url')
        newslisting_url += 'news/'
        return newslisting_url

    @staticmethod
    def ArticlelistingURL():
        articlelisting_url=config.get('common info','Base_url')
        articlelisting_url += 'articles/'

        return articlelisting_url    

    @staticmethod
    def FullformURL():
        fullform_url=config.get('common info','Base_url')
        fullform_url += 'aids-full-form'

        return fullform_url

    @staticmethod
    def InsurancedetailURL():
        insurancedetail_url=config.get('common info','Base_url')
        insurancedetail_url += 'insurance'

        return insurancedetail_url

    @staticmethod
    def DUCollegePredictorURL():
        ducollegepredictor_url=config.get('common info','Base_url')
        ducollegepredictor_url += 'du-college-predictor'

        return ducollegepredictor_url

    @staticmethod
    def PsychometricURL():
        psychometric_url=config.get('common info','Base_url')
        psychometric_url += 'psychometric-test'

        return psychometric_url

    @staticmethod
    def JobassuredlistingURL():
        jobassuredlisting_url=config.get('common info','Base_url')
        jobassuredlisting_url += 'learn/'

        return jobassuredlisting_url

    @staticmethod
    def JobassureddetailURL():
        jobassureddetail_url=config.get('common info','Base_url')
        jobassureddetail_url += 'learn-all-courses-lpcl'

        return jobassureddetail_url                  

    @staticmethod
    def CafURL():
        caf_url=config.get('common info','Base_url')
        caf_url += 'college-admission-form'

        return caf_url
    