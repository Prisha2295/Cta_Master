import os
import csv
import json
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv
from utilities.customlogger import Logs
from jsonschema import validate, ValidationError
from selenium.common.exceptions import NoSuchElementException

load_dotenv()

# Initialize logger
logger = Logs.loggen('Schema Validation')

# Database credentials (just for reference; not used in this script)
cld_host_live = os.getenv("cld_host_live")
cld_username_live = os.getenv("cld_username_live")
cld_pass_live = os.getenv("cld_pass_live")
cld_databasename_live = os.getenv("cld_databasename_live")

cld_host_staging = os.getenv("cld_host_staging")
cld_username_staging = os.getenv("cld_username_staging")
cld_pass_staging = os.getenv("cld_pass_staging")
cld_databasename_staging = os.getenv("cld_databasename_staging")

base_urls = {
    'https://www.collegedekho.com/colleges': [
        '/lpu', '/lpu-courses', '/lpu-placement', '/lpu-admission', '/lpu-scholarship', '/lpu-cutoff', '/lpu-campus', '/lpu-reviews', '/lpu-connect', '/lpu-qna',
        '/parul-university', '/parul-university-courses', '/parul-university-placement', '/parul-university-admission', '/parul-university-scholarship', '/parul-university-cutoff', '/parul-university-reviews', '/parul-university-connect', '/parul-university-qna',
        '/iit-delhi', '/iit-delhi-courses', '/iit-delhi-placement', '/iit-delhi-admission', '/iit-delhi-scholarship', '/iit-delhi-cutoff', '/iit-delhi-campus', '/iit-delhi-reviews', '/iit-delhi-connect', '/iit-delhi-qna',
        '/chandigarh-university', '/chandigarh-university-courses', '/chandigarh-university-placement', '/chandigarh-university-admission', '/chandigarh-university-scholarship', '/chandigarh-university-cutoff', '/chandigarh-university-campus', '/chandigarh-university-reviews', '/chandigarh-university-connect', '/chandigarh-university-qna'
    ],
    'https://www.collegedekho.com/university': [
        '/aktu', '/aktu-courses', '/aktu-placement', '/aktu-result', '/aktu-exam-dates', '/aktu-affiliated-colleges', '/aktu-connect',
        '/university-of-rajasthan', '/university-of-rajasthan-courses', '/university-of-rajasthan-placement', '/university-of-rajasthan-result', '/university-of-rajasthan-exam-dates', '/university-of-rajasthan-affiliated-colleges', '/university-of-rajasthan-connect'
    ],
    'https://www.collegedekho.com/courses': [
        '/btech', '/btech-syllabus-subjects', '/btech/jobs', '/btech/salary',
        '/master-of-business-administration-mba', '/master-of-business-administration-mba/syllabus-subjects', '/master-of-business-administration-mba/jobs', '/master-of-business-administration-mba/salary',
        '/bdes', '/bdes-syllabus-subjects', '/bdes-jobs',
        '/bed', '/bed-syllabus-subjects', '/bed/jobs', '/bed/salary',
        '/bachelor-of-architecture-barch', '/bachelor-of-architecture-barch-syllabus-subjects',
        '/b-pharma', '/b-pharma/syllabus-subjects', '/b-pharma/jobs', '/b-pharma/salary'
    ],
    'https://www.collegedekho.com/exam': [
        '/jee-main', '/jee-main/paper-analysis', '/jee-main/response-sheet', '/jee-main/college-predictor', '/jee-main/rank-predictor', '/jee-main/answer-key',
        '/jee-advanced', '/jee-advanced/paper-analysis', '/jee-advanced/response-sheet', '/jee-advanced/college-predictor', '/jee-advanced/rank-predictor', '/jee-advanced/answer-key',
        '/gate', '/gate/paper-analysis', '/gate/response-sheet', '/gate/college-predictor', '/gate/rank-predictor', '/gate/answer-key',
        '/wbjee', '/wbjee/paper-analysis', '/wbjee/response-sheet', '/wbjee/college-predictor', '/wbjee/rank-predictor', '/wbjee/answer-key',
        '/bitsat', '/bitsat/paper-analysis', '/bitsat/response-sheet', '/bitsat/college-predictor', '/bitsat/rank-predictor', '/bitsat/answer-key'
    ]
}

# Generate URLs
urls = [f"{base_url}{endpoint}" for base_url, endpoints in base_urls.items() for endpoint in endpoints]

csv_filename = '_schemaoutputnew.csv'

# Define the JSON-LD schema
json_ld_schema = {
    "type": "object",
    "properties": {
        "@context": {"type": "string"},
        "@type": {"type": "string"},
        "inLanguage": {"type": "string"},
        "headline": {"type": "string"},
        "description": {"type": "string"},
        "dateModified": {"type": "string"},
        "datePublished": {"type": "string"},
        "mainEntityOfPage": {
            "type": "object",
            "properties": {
                "id": {"type": "string"},
                "@type": {"type": "string"},
                "Name": {"type": "string"}
            },
            "required": ["id", "@type", "Name"]
        },
        "Author": {
            "type": "object",
            "properties": {
                "@type": {"type": "string"},
                "name": {"type": "string"}
            },
            "required": ["@type", "name"]
        },
        "Publisher": {
            "type": "object",
            "properties": {
                "@type": {"type": "string"},
                "name": {"type": "string"},
                "logo": {
                    "type": "object",
                    "properties": {
                        "@type": {"type": "string"},
                        "name": {"type": "string"},
                        "url": {"type": "string"},
                        "height": {"type": "string"},
                        "width": {"type": "string"}
                    },
                    "required": ["@type", "name", "url", "height", "width"]
                }
            },
            "required": ["@type", "name", "logo"]
        },
        "image": {
            "type": "object",
            "properties": {
                "@type": {"type": "string"},
                "url": {"type": "string"}
            },
            "required": ["@type", "url"]
        }
    },
    "required": ["@context", "@type"]
}

class TestSchemaValidate:
    def __init__(self):
        # Set up Chrome options for headless mode
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        # Install ChromeDriver and set up options
        self.service = ChromeService(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service, options=chrome_options)
        self.driver.maximize_window()

    def __del__(self):
        self.driver.quit()
        logger.info('Browser closed successfully')

    def validate_schema(self, url):
        logger.info(f"******* Starting Schema Validation for URL: {url} **********")
        self.driver.get(url)
        logger.info(f'Opened URL: {url}')
        
        try:
            # Extract JSON-LD script from the page
            json_ld_element = self.driver.find_element("xpath", '//script[@type="application/ld+json"]')
            json_ld_text = json_ld_element.get_attribute('innerHTML')
            json_ld_data = json.loads(json_ld_text)

            # Validate JSON-LD data against the schema
            validate(instance=json_ld_data, schema=json_ld_schema)
            logger.info(f"JSON-LD script is valid on the page: {url}")
            return "Pass", ""

        except NoSuchElementException:
            logger.error(f"No JSON-LD element found on the page: {url}")
            return "Fail", "No JSON-LD script found"
        except ValidationError as e:
            logger.error(f"JSON-LD script is invalid on the page: {url}. Error: {e.message}")
            return "Fail", str(e)
import os
import csv
import json
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv
from utilities.customlogger import Logs
from jsonschema import validate, ValidationError
from selenium.common.exceptions import NoSuchElementException

load_dotenv()

# Initialize logger
logger = Logs.loggen('Schema Validation')

# Database credentials (just for reference; not used in this script)
cld_host_live = os.getenv("cld_host_live")
cld_username_live = os.getenv("cld_username_live")
cld_pass_live = os.getenv("cld_pass_live")
cld_databasename_live = os.getenv("cld_databasename_live")

cld_host_staging = os.getenv("cld_host_staging")
cld_username_staging = os.getenv("cld_username_staging")
cld_pass_staging = os.getenv("cld_pass_staging")
cld_databasename_staging = os.getenv("cld_databasename_staging")

base_urls = {
    'https://www.collegedekho.com/colleges': [
        '/lpu', '/lpu-courses', '/lpu-placement', '/lpu-admission', '/lpu-scholarship', '/lpu-cutoff', '/lpu-campus', '/lpu-reviews', '/lpu-connect', '/lpu-qna',
        '/parul-university', '/parul-university-courses', '/parul-university-placement', '/parul-university-admission', '/parul-university-scholarship', '/parul-university-cutoff', '/parul-university-reviews', '/parul-university-connect', '/parul-university-qna',
        '/iit-delhi', '/iit-delhi-courses', '/iit-delhi-placement', '/iit-delhi-admission', '/iit-delhi-scholarship', '/iit-delhi-cutoff', '/iit-delhi-campus', '/iit-delhi-reviews', '/iit-delhi-connect', '/iit-delhi-qna',
        '/chandigarh-university', '/chandigarh-university-courses', '/chandigarh-university-placement', '/chandigarh-university-admission', '/chandigarh-university-scholarship', '/chandigarh-university-cutoff', '/chandigarh-university-campus', '/chandigarh-university-reviews', '/chandigarh-university-connect', '/chandigarh-university-qna'
    ],
    'https://www.collegedekho.com/university': [
        '/aktu', '/aktu-courses', '/aktu-placement', '/aktu-result', '/aktu-exam-dates', '/aktu-affiliated-colleges', '/aktu-connect',
        '/university-of-rajasthan', '/university-of-rajasthan-courses', '/university-of-rajasthan-placement', '/university-of-rajasthan-result', '/university-of-rajasthan-exam-dates', '/university-of-rajasthan-affiliated-colleges', '/university-of-rajasthan-connect'
    ],
    'https://www.collegedekho.com/courses': [
        '/btech', '/btech-syllabus-subjects', '/btech/jobs', '/btech/salary',
        '/master-of-business-administration-mba', '/master-of-business-administration-mba/syllabus-subjects', '/master-of-business-administration-mba/jobs', '/master-of-business-administration-mba/salary',
        '/bdes', '/bdes-syllabus-subjects', '/bdes-jobs',
        '/bed', '/bed-syllabus-subjects', '/bed/jobs', '/bed/salary',
        '/bachelor-of-architecture-barch', '/bachelor-of-architecture-barch-syllabus-subjects',
        '/b-pharma', '/b-pharma/syllabus-subjects', '/b-pharma/jobs', '/b-pharma/salary'
    ],
    'https://www.collegedekho.com/exam': [
        '/jee-main', '/jee-main/paper-analysis', '/jee-main/response-sheet', '/jee-main/college-predictor', '/jee-main/rank-predictor', '/jee-main/answer-key',
        '/jee-advanced', '/jee-advanced/paper-analysis', '/jee-advanced/response-sheet', '/jee-advanced/college-predictor', '/jee-advanced/rank-predictor', '/jee-advanced/answer-key',
        '/gate', '/gate/paper-analysis', '/gate/response-sheet', '/gate/college-predictor', '/gate/rank-predictor', '/gate/answer-key',
        '/wbjee', '/wbjee/paper-analysis', '/wbjee/response-sheet', '/wbjee/college-predictor', '/wbjee/rank-predictor', '/wbjee/answer-key',
        '/bitsat', '/bitsat/paper-analysis', '/bitsat/response-sheet', '/bitsat/college-predictor', '/bitsat/rank-predictor', '/bitsat/answer-key'
    ]
}

# Generate URLs
urls = [f"{base_url}{endpoint}" for base_url, endpoints in base_urls.items() for endpoint in endpoints]

csv_filename = '_schemaoutputnew.csv'

# Define the JSON-LD schema
json_ld_schema = {
    "type": "object",
    "properties": {
        "@context": {"type": "string"},
        "@type": {"type": "string"},
        "inLanguage": {"type": "string"},
        "headline": {"type": "string"},
        "description": {"type": "string"},
        "dateModified": {"type": "string"},
        "datePublished": {"type": "string"},
        "mainEntityOfPage": {
            "type": "object",
            "properties": {
                "id": {"type": "string"},
                "@type": {"type": "string"},
                "Name": {"type": "string"}
            },
            "required": ["id", "@type", "Name"]
        },
        "Author": {
            "type": "object",
            "properties": {
                "@type": {"type": "string"},
                "name": {"type": "string"}
            },
            "required": ["@type", "name"]
        },
        "Publisher": {
            "type": "object",
            "properties": {
                "@type": {"type": "string"},
                "name": {"type": "string"},
                "logo": {
                    "type": "object",
                    "properties": {
                        "@type": {"type": "string"},
                        "name": {"type": "string"},
                        "url": {"type": "string"},
                        "height": {"type": "string"},
                        "width": {"type": "string"}
                    },
                    "required": ["@type", "name", "url", "height", "width"]
                }
            },
            "required": ["@type", "name", "logo"]
        },
        "image": {
            "type": "object",
            "properties": {
                "@type": {"type": "string"},
                "url": {"type": "string"}
            },
            "required": ["@type", "url"]
        }
    },
    "required": ["@context", "@type"]
}

class TestSchemaValidate:
    def __init__(self):
        # Set up Chrome options for headless mode
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        # Install ChromeDriver and set up options
        self.service = ChromeService(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service, options=chrome_options)
        self.driver.maximize_window()

    def __del__(self):
        self.driver.quit()
        logger.info('Browser closed successfully')

    def validate_schema(self, url):
        logger.info(f"******* Starting Schema Validation for URL: {url} **********")
        self.driver.get(url)
        logger.info(f'Opened URL: {url}')
        
        try:
            # Extract JSON-LD script from the page
            json_ld_element = self.driver.find_element("xpath", '//script[@type="application/ld+json"]')
            json_ld_text = json_ld_element.get_attribute('innerHTML')
            json_ld_data = json.loads(json_ld_text)

            # Validate JSON-LD data against the schema
            validate(instance=json_ld_data, schema=json_ld_schema)
            logger.info(f"JSON-LD script is valid on the page: {url}")
            return "Pass", ""

        except NoSuchElementException:
            logger.error(f"No JSON-LD element found on the page: {url}")
            return "Fail", "No JSON-LD script found"
        except ValidationError as e:
            logger.error(f"JSON-LD script is invalid on the page: {url}. Error: {e.message}")
            return "Fail", str(e)

    def run_validation(self):
        # Write results to CSV file
        with open(csv_filename, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            # Write the header row
            csv_writer.writerow(['URL', 'Schema Validation', 'Error'])
            logger.info('CSV file generated')

            # Loop through each URL and check for the presence of JSON-LD script
            for url in urls:
                status, error = self.validate_schema(url)
                csv_writer.writerow([url, status, error])

@pytest.fixture(scope="module")
def schema_validator():
    validator = TestSchemaValidate()
    yield validator
    validator.__del__()

def test_schema_validation(schema_validator):
    schema_validator.run_validation()

    def run_validation(self):
        # Write results to CSV file
        with open(csv_filename, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            # Write the header row
            csv_writer.writerow(['URL', 'Schema Validation', 'Error'])
            logger.info('CSV file generated')

            # Loop through each URL and check for the presence of JSON-LD script
            for url in urls:
                status, error = self.validate_schema(url)
                csv_writer.writerow([url, status, error])

@pytest.fixture(scope="module")
def schema_validator():
    validator = TestSchemaValidate()
    yield validator
    validator.__del__()

def test_schema_validation(schema_validator):
    schema_validator.run_validation()
