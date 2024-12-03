import configparser

config=configparser.RawConfigParser()

path = config.read("../Config.ini")
# print(path)

class ReadConfig():
    @staticmethod
    
    def CafURL():
        caf_url=config.get('common info','Base_url')
        caf_url += 'college-admission-form'
        return caf_url
    
    def HomepageURL():
        homepage_url=config.get('common info','Base_url')
        return homepage_url
    
    def NewslistingURL():
        newslisting_url=config.get('common info','Base_url')
        newslisting_url += 'news/'
        return newslisting_url

    def CourseURL():
        course_url=config.get('common info','Base_url')
        course_url += 'courses/mba-media-management'
        return course_url

    def ExamDashboardURL():
        examdashboard_url=config.get('common info','Base_url')
        examdashboard_url += 'dashboard/exam/'
        return examdashboard_url

    def NewsDashboardURL():
        newsdashboard_url=config.get('common info','Base_url')
        newsdashboard_url += 'admin/news-dashboard/'
        return newsdashboard_url

    def CMSDashboardURL():
        CMSSdashboard_url = 'https://cms.collegedekho.com/institute'
        return CMSSdashboard_url

    def ExamdetailURL():
        examdetail_url=config.get('common info','Base_url')
        examdetail_url += 'exams/jee-main?magicflag'
        return examdetail_url
    
    def CollegedetailURL():
        collegedetail_url=config.get('common info','Base_url')
        collegedetail_url += 'colleges/lpu'

        return collegedetail_url
    
    def ExamdetailURL():
        examdetail_url=config.get('common info','Base_url')
        examdetail_url += 'exam/cat'

        return examdetail_url


    



