import random
import string


class Attributes():
    def random_namee(self):

        return 'api' + "".join(random.choices(string.ascii_lowercase, k=6))

    def random_phonenumber(self):

        ph_no = []

        ph_no.append(random.randint(6, 9))

        for i in range(1, 10):
            ph_no.append(random.randint(0, 9))

        number = ""

        for i in ph_no:
            print(i, end="")
            number += str(i)
        print(number)

        return number

    def random_email(self):
        random_str = 'api' + "".join(random.choice(string.ascii_letters) for _ in range(7))
        return random_str + "@gmail.com"

    def gmusso_payloads(self):

        sso_payload = [{"name": self.random_namee(),
                    "phone_no": self.random_phonenumber(),
                    "email": self.random_email(),
                    "business_unit": 2,
                    "stream": "engineering-btech-mtech",
                    "level": "studying-completed-graduation",
                    "state": 1,
                    "city": 1,
                    "pref_state": 9,
                    "pref_city": 591,
                    "source":43,
                    "source_url" : "https://www.getmyuni.com/"}]
        
        return sso_payload
    

    def sso_cldpayload():
        pass

    def cld_ctasubmission(self):
        
        data = [{
                "name": self.random_namee(),
                "email": self.random_email(),
                "phone": self.random_phonenumber(),
                "stream": 4,
                "pref_level": 2,
                "state": 14,
                "budget": "",
                "board": "",
                "exam": 1388,
                "institute":"",
                "country": 1,
                "utm_source": "",
                "utm_medium": "",
                "utm_campaign": "",
                "content_type": 22,
                "object_id": "",
                "cta": 120,
                "button": 7,
                "whatsapp_preference": "on"
                }]
        
        
        
        return data

        
    def login_payloads(self):
        
        login_payload = {
            "phone_no" : "8619007372",
            "password" : "dekho@123"
                        }
        
        
        return login_payload
    


