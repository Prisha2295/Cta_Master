import unittest
import time
from datetime import datetime
import requests
import urllib
import json
import pandas as pd

urls = ["https://www.collegedekho.com/colleges/iit-delhi",
"https://www.careers360.com/university/indian-institute-of-technology-delhi",
"https://www.shiksha.com/university/iit-delhi-indian-institute-of-technology-53938",
"https://collegedunia.com/university/25455-iit-delhi-indian-institute-of-technology-iitd-new-delhi",
"https://www.getmyuni.com/college/indian-institute-of-technology-iit-delhi",
"https://www.collegedekho.com/courses/master-of-law-llm/",
"https://www.shiksha.com/ll-m-chp",
"https://collegedunia.com/courses/master-of-laws-llm",
"https://www.getmyuni.com/llm-course",
"https://www.collegedekho.com/exam/cat",
"https://bschool.careers360.com/exams/cat",
"https://www.shiksha.com/mba/cat-exam",
"https://collegedunia.com/exams/cat",
"https://www.getmyuni.com/exams/cat",
"https://www.collegedekho.com/btech-colleges-in-india/",
"https://engineering.careers360.com/colleges/list-of-be-btech-colleges-in-india",
"https://www.shiksha.com/engineering/colleges/b-tech-colleges-india",
"https://collegedunia.com/btech-colleges",
"https://www.getmyuni.com/btech-colleges",
"https://www.collegedekho.com/articles/list-of-iim-colleges-in-india-ranking-courses-offered/",
"https://bschool.careers360.com/articles/iim-personal-interview-how-tackle-questions-related-your-hobbies",
"https://www.shiksha.com/mba/articles/iims-in-india-blogId-20013",
"https://collegedunia.com/news/e-242-cat-varc-types-of-articles",
"https://www.getmyuni.com/articles/how-to-crack-cat-exam",
"https://www.collegedekho.com/cbse-class-10-sample-papers-brd",
"https://news.careers360.com/cbse-releases-class-10-12-sample-paper-2023-at-cbseacademicnicin-direct-link-steps-download",
"https://www.shiksha.com/boards/cbse-10th-board",
"https://collegedunia.com/news/cbse-class-10-12-term-ii-exam-2022-sample-papers-released-alertid-47112",
"https://www.getmyuni.com/news/cbse-class-10-and-12-sample-papers-2023-are-released-check-the-direct-link-here"]


class Pagespeed(unittest.TestCase):
    def test_pagespeed(self):

        r=1
        templist = []
        time = datetime.now()
        added_on = time.strftime('%Y-%m-%d %H:%M:%S')

        for url in urls:
            response = requests.get(url)
            response_time = response.elapsed.microseconds / 1000
            
            if url.startswith("https://www.collegedekho.com/colleges/"):
                url_type = "Collegedekho College Detail"

            if url.startswith("https://www.careers360.com/university/indian-institute-of-technology-delhi"):
                url_type = "Career360 College detail"

            if url.startswith("https://www.shiksha.com/university/iit-delhi-indian-institute-of-technology-53938"):
                url_type = "Siksha College detail"

            if url.startswith("https://collegedunia.com/university/25455-iit-delhi-indian-institute-of-technology-iitd-new-delhi"):
                url_type = "Collegedunia College detail"

            if url.startswith("https://collegedunia.com/university/25455-iit-delhi-indian-institute-of-technology-iitd-new-delhi"):
                url_type = "GetMyUni College detail"

            if url.startswith("https://www.collegedekho.com/courses/btech/"):
                url_type = "Collegedekho Course detail"

            if url.startswith("https://www.shiksha.com/ll-m-chp"):
                url_type = "Siksha Course detail"

            if url.startswith("https://collegedunia.com/courses/master-of-laws-llm"):
                url_type = "COllegedunia Course detail"

            if url.startswith("https://www.getmyuni.com/llm-course"):
                url_type = "GetMyUni Course detail"

            if url.startswith("https://www.collegedekho.com/exam/jee-main"):
                url_type = "Collegedekho Exam Detail"

            if url.startswith("https://bschool.careers360.com/exams/cat"):
                url_type = "Career360 Exam Detail"

            if url.startswith("https://www.shiksha.com/mba/cat-exam"):
                url_type = "Shiksha Exam Detail"

            if url.startswith("https://collegedunia.com/exams/cat"):
                url_type = "Collegedunia Exam Detail"

            if url.startswith("https://www.getmyuni.com/exams/cat"):
                url_type = "GetMyUni Exam Detail"
                
            if url.startswith("https://www.collegedekho.com/btech-colleges-in-india/"):
                url_type = "Collegedekho College Listing"

            if url.startswith("https://engineering.careers360.com/colleges/list-of-be-btech-colleges-in-india"):
                url_type = "Careers360 College Listing"

            if url.startswith("https://www.shiksha.com/engineering/colleges/b-tech-colleges-india"):
                url_type = "Siksha College Listing"

            if url.startswith("https://collegedunia.com/btech-colleges"):
                url_type = "Collegedunia College Listing"

            if url.startswith("https://www.getmyuni.com/btech-colleges"):
                url_type = "GetMyUni College Listing"

            
            if url.startswith("https://www.collegedekho.com/news/kcet-verification-slip-2022-link-today-official-website-link-to-download-reference-links-31604/"):
                url_type = "Collegedekho News detail"

            if url.startswith("https://bschool.careers360.com/articles/iim-personal-interview-how-tackle-questions-related-your-hobbies"):
                url_type = "Career360 News detail"

            if url.startswith("https://www.shiksha.com/mba/articles/iims-in-india-blogId-20013"):
                url_type = "Siksha News detail"

            if url.startswith("https://collegedunia.com/news/e-242-cat-varc-types-of-articles"):
                url_type = "Collegedunia News detail"

            if url.startswith("https://www.getmyuni.com/articles/how-to-crack-cat-exam"):
                url_type = "GetMyUni News detail"

            if url.startswith("https://www.collegedekho.com/cbse-class-10-sample-papers-brd"):
                url_type = "Collegedekho Board"

            if url.startswith("https://news.careers360.com/cbse-releases-class-10-12-sample-paper-2023-at-cbseacademicnicin-direct-link-steps-download"):
                url_type = "Career360 Board"

            if url.startswith("https://www.shiksha.com/boards/cbse-10th-board"):
                url_type = "Shiskha Board"

            if url.startswith("https://collegedunia.com/news/cbse-class-10-12-term-ii-exam-2022-sample-papers-released-alertid-47112"):
                url_type = "Collegedunia Board"

            if url.startswith("https://www.getmyuni.com/news/cbse-class-10-and-12-sample-papers-2023-are-released-check-the-direct-link-here"):
                url_type = "GetMyUni Board"
            
            

            link = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={}&strategy=mobile&locale=en&key=AIzaSyDEsDFs_UuwRLZhEiMIKp6CfBzY8qR1j6U".format(url)
            #Note that you can insert your URL with the parameter URL and you can also modify the device parameter if you would like to get the data for desktop.
            try:
                response = urllib.request.urlopen(link)
            except urllib.error.HTTPError:
                print(link, "returned 500")
                continue
            # response = urllib.request.urlopen(link)
            data = json.loads(response.read())

            fcp = "" 
            fcp_temp = data["loadingExperience"]["metrics"].get("FIRST_CONTENTFUL_PAINT_MS",{})
            if fcp_temp:
                fcp = fcp_temp.get("percentile","")/1000 if type(fcp_temp.get("percentile","")) == type(1) else "Data not found"
                
            
            fid = ""
            fidtemp = data["loadingExperience"]["metrics"].get('FIRST_INPUT_DELAY_MS',{})
            if fidtemp:
                fid = fidtemp.get("percentile","Data not found")
            

            Lcp = ""
            Lcp_temp = data["loadingExperience"]["metrics"].get("LARGEST_CONTENTFUL_PAINT_MS",{})
            if Lcp_temp:
                Lcp =Lcp_temp.get("percentile","")/1000 if type(Lcp_temp.get("percentile","")) == type(1) else "Data not found"
               
            
            cls = ""
            cls_temp = data["loadingExperience"]["metrics"].get("CUMULATIVE_LAYOUT_SHIFT_SCORE",{})
            if cls_temp:
                cls =cls_temp.get("percentile","")/1000 if type(cls_temp.get("percentile","")) == type(1) else "Data not found"
                

            Lnp = ""
            Lnptemp = data["loadingExperience"]["metrics"].get("EXPERIMENTAL_INTERACTION_TO_NEXT_PAINT",{})
            if Lnptemp:
                Lnp = Lnptemp.get("percentile","Data not found")
                

            fcp_catagory = ""
            fcp_catagory_temp = data["loadingExperience"]["metrics"].get("FIRST_CONTENTFUL_PAINT_MS",{})
            if fcp_catagory_temp:
                fcp_catagory = fcp_catagory_temp.get("category","Data not found")
                
                
            
            fid_catagory = ""
            fid_catagory_temp = data["loadingExperience"]["metrics"].get("FIRST_INPUT_DELAY_MS",{})
            if fid_catagory_temp:
                fid_catagory = fid_catagory_temp.get("category","Data not found")
                
            
            Lcp_catagory = ""
            Lcp_catagory_temp = data["loadingExperience"]["metrics"].get("LARGEST_CONTENTFUL_PAINT_MS",{})
            if Lcp_catagory_temp:
                Lcp_catagory = Lcp_catagory_temp.get("category","Data not found")
                
            cls_catagory = ""
            cls_catagory_temp = data["loadingExperience"]["metrics"].get("CUMULATIVE_LAYOUT_SHIFT_SCORE",{})
            if cls_catagory_temp:
                cls_catagory = cls_catagory_temp.get("category","Data not found")
                           
                
            Lnp_catagory = ""
            Lnp_catagory_temp = data["loadingExperience"]["metrics"].get("EXPERIMENTAL_INTERACTION_TO_NEXT_PAINT",{})
            Lnp_catagory = Lnp_catagory_temp.get("category","Data not found") 
            
            
            overall_score = data["lighthouseResult"]["categories"]["performance"]["score"] * 100
            
            
            


            
            Table_dict={'URL' : url,'url_type' : url_type,'added_on' : added_on,'fcp' : fcp, 'fcp_catagory' : fcp_catagory, 'fid' : fid, 'fid_catagory' : fid_catagory, 
            'Lcp' : Lcp, 'Lcp_catagory' : Lcp_catagory, 'cls' : cls, 'cls_catagory' : cls_catagory ,'Lnp': Lnp,'Lnp_catagory' : Lnp_catagory,'overall_score' : overall_score,'response_time' : response_time}
            
                                
            templist.append(Table_dict) 
            df = pd.DataFrame(templist)
                
            r += 1
            
            df.to_csv('verticalperformance_load.csv')