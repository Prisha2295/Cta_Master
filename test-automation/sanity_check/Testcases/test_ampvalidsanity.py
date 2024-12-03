import concurrent.futures
import subprocess
import unittest
import mysql.connector
import pandas as pd
import logging
import os
from datetime import datetime
import glob
from dotenv import load_dotenv

load_dotenv()

# Database credentials
cld_host_live = os.getenv("cld_host_live")
cld_username_live = os.getenv("cld_username_live")
cld_pass_live = os.getenv("cld_pass_live")
cld_databasename_live = os.getenv("cld_databasename_live")

cld_host_staging = os.getenv("cld_host_staging")
cld_username_staging = os.getenv("cld_username_staging")
cld_pass_staging = os.getenv("cld_pass_staging")
cld_databasename_staging = os.getenv("cld_databasename_staging")

# Define the log filename based on the current date and time
log_filename = f'amp_validation_log_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log'

# Remove previous log files
log_files = glob.glob('amp_validation_log_*.log')
for log_file in log_files:
    try:
        os.remove(log_file)
    except OSError as e:
        print(f"Error: {log_file} : {e.strerror}")

# Configure logging
logging.basicConfig(filename=log_filename, filemode='w', level=logging.INFO, 
                    format='%(asctime)s :%(levelname)s :%(message)s')

# Initialize the logger
logger = logging.getLogger()


class Test_AmpValidate(unittest.TestCase):

    def create_connection(self):
        return mysql.connector.connect(
            host=cld_host_live,
            user=cld_username_live,
            password=cld_pass_live,
            database=cld_databasename_live
        )

    def run_amp_validator(self, url, language, output_filename):
        current_date = datetime.now().strftime("%Y-%m-%d")
        c = 'amphtml-validator'
        r = subprocess.run([c, url], capture_output=True)
        response = r.returncode

        if response == 0:
            res = "Pass"
        else:
            res = "Fail"

        table_dict = {
            'date': current_date,
            'url': url,
            'response_code': response,
            'output': r.stdout.decode().strip(),
            'res': res
        }

        df = pd.DataFrame([table_dict])    

        # Write headers only if the file does not exist
        if not os.path.isfile(output_filename):
            df.to_csv(output_filename, mode='w', header=True, index=False)
        else:
            df.to_csv(output_filename, mode='a', header=False, index=False)

        # Log the result
        logger.info(f"{current_date} - URL: {url}, Response Code: {response}, Result: {res}")

    def process_language(self, language, query_template):
        conn = self.create_connection()

        try:
            cursor = conn.cursor()
            cursor.execute(query_template)
            rows = cursor.fetchall()
            urls = [f"{i[0]}" for i in rows]

            # Define output filename
            output_filename = f'{language}_amp_response.csv'

            # Remove previous CSV files
            if os.path.isfile(output_filename):
                os.remove(output_filename)

            with concurrent.futures.ThreadPoolExecutor() as executor:
                # Set the maximum number of threads based on your needs
                # Adjust the chunk size as needed
                chunk_size = 10
                futures = []

                for chunk_start in range(0, len(urls), chunk_size):
                    chunk_urls = urls[chunk_start:chunk_start + chunk_size]

                    for url in chunk_urls:
                        futures.append(executor.submit(self.run_amp_validator, url, language, output_filename))

                # Wait for all threads to complete before moving to the next language
                concurrent.futures.wait(futures)

        finally:
            conn.close()

    def test_process_language(self):
        query_templates = {
            'english': """SELECT CONCAT("https://www.collegedekho.com/amp/news/", slug, "-", uri_id, "/") AS "slug"
                        FROM news_news
                        WHERE date(published_on) IS NOT NULL AND news_type = 1 AND language_id = 1 AND qa_status = 2
                        ORDER BY id DESC LIMIT 100""",
            'hindi': """SELECT CONCAT("https://www.collegedekho.com/hi/amp/news/", slug, "-", uri_id, "/") AS "slug"
                    FROM news_news
                    WHERE date(published_on) IS NOT NULL AND news_type = 1 AND language_id = 2 AND qa_status = 2
                    ORDER BY id DESC LIMIT 100""",
            'telugu': """SELECT CONCAT("https://www.collegedekho.com/te/amp/news/", slug, "-", uri_id, "/") AS "slug"
                        FROM news_news
                        WHERE date(published_on) IS NOT NULL AND news_type = 1 AND language_id = 3 AND qa_status = 2
                        ORDER BY id DESC LIMIT 100"""
        }

        for lang, template in query_templates.items():
            self.process_language(lang, template)

if __name__ == '__main__':
    unittest.main()