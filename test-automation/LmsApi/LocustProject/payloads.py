import random
import string

def random_namee():

    return 'api' + "".join(random.choices(string.ascii_lowercase, k=6))

def random_phonenumber():

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

def random_email():
    random_str = 'api' + "".join(random.choice(string.ascii_letters) for _ in range(7))
    return random_str + "@gmail.com"

def sso_payloads():
    random_name = random_namee()
    random_mail = random_email()
    random_mobile = random_phonenumber()

    sso_payload = {"name": random_name,
                "phone_no": random_mobile,
                "email": random_mail,
                "business_unit": 2,
                "stream": "engineering-btech-mtech",
                "level": "studying-completed-graduation",
                "state": 1,
                "city": 1,
                "pref_state": 9,
                "pref_city": 591}
    
   
                
                # {"name": self.random_namee(),
                # "phone_no": self.random_phonenumber(),
                # "email": self.random_email(),
                # "business_unit": 2,
                # "stream": "engineering-btech-mtech",
                # "level": "studying-completed-12th",
                # "state": ""
                # ,"city": "",
                # "pref_state": 2,
                # "pref_city": "",
                # "object_id": 159,
                # "object_type": "institute",
                # "source_url": "",
                # "first_source_url":"",
                # "budget": "",
                # "ip": ""
                # }
                
    
    return sso_payload
    
def login_payloads():
    login_payload = {
        "phone_no" : "8619007372",
        "password" : "dekho@123"
                    }
    return login_payload