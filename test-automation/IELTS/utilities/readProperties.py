import configparser
import os

# Initialize the config parser
config = configparser.RawConfigParser()

# Define the path to the config file
config_path = os.path.join(os.path.dirname(__file__), '../configuration/config.ini')

# Read the config file
config.read(config_path)

# Print path for debugging purposes
print("Config file read from:", config_path)

class ReadConfig:
    @staticmethod
    def getIELTSURL():
        try:
            Ielts_url = config.get('common info', 'Base_url1')
            return Ielts_url
        except configparser.NoOptionError:
            print("Error: Base_url1 not found in the config file.")
            return None
        except configparser.NoSectionError:
            print("Error: 'common info' section not found in the config file.")
            return None
        
    def getArticleURL():
        try:
            article_url = config.get('common info', 'Article_url')
            return article_url
        except configparser.NoOptionError:
            print("Error: Url not found in the config file.")
            return None
        except configparser.NoSectionError:
            print("Error: 'common info' section not found in the config file.")
            return None
        
    def getServiceURL():
        try:
            service_url = config.get('common info', 'Services_url')
            return service_url
        except configparser.NoOptionError:
            print("Error: Url not found in the config file.")
            return None
        except configparser.NoSectionError:
            print("Error: 'common info' section not found in the config file.")
            return None




    @staticmethod
    def getGISURL():
        try:
            GIS_url = config.get('common info', 'Base_url2')
            return GIS_url
        except configparser.NoOptionError:
            print("Error: Base_url2 not found in the config file.")
            return None
        except configparser.NoSectionError:
            print("Error: 'common info' section not found in the config file.")
            return None
        
    @staticmethod
    def getTOEFLURL():
        try:
            TOEFL_url = config.get('common info', 'Base_url3')
            return TOEFL_url
        except configparser.NoOptionError:
            print("Error: Base_url3 not found in the config file.")
            return None
        except configparser.NoSectionError:
            print("Error: 'common info' section not found in the config file.")
            return None