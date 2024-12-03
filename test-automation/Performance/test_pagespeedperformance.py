import os
import requests
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

performance_api = os.getenv("Performance_api")

def fetch_page_speed_data(url):
    API_KEY =   performance_api
    endpoint = 'https://www.googleapis.com/pagespeedonline/v5/runPagespeed'
    params = {
        'url': url,
        'key': API_KEY,
        'strategy': 'mobile'
    }
    response = requests.get(endpoint, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching data for URL:", url, response.status_code, response.text)
        return None

def extract_performance_metrics(data, url):
    metrics = {
        'URL': url,
        'URL Type': categorize_url(url),
        'Added On': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    if data:
        # Correctly access the performance score
        performance_score = data.get('lighthouseResult', {}).get('categories', {}).get('performance', {}).get('score')
        if isinstance(performance_score, float):
            metrics['Performance Score'] = round(performance_score * 100, 2)  # Convert score to a percentage and round off
        
        audits = data.get('lighthouseResult', {}).get('audits', {})
        key_metrics = {
            'First Contentful Paint': 'first-contentful-paint',
            'Speed Index': 'speed-index',
            'Largest Contentful Paint': 'largest-contentful-paint',
            'Time to Interactive': 'interactive',
            'Total Blocking Time': 'total-blocking-time',
            'Cumulative Layout Shift': 'cumulative-layout-shift',
            'Server Response Time': 'server-response-time'
        }

        for key, audit_key in key_metrics.items():
            metrics[key] = audits.get(audit_key, {}).get('displayValue', 'Data not available')

    return metrics

def categorize_url(url):
    if url.startswith("https://www.collegedekho.com/careers/"):
        return "Careers"
    elif url.startswith("https://www.collegedekho.com/colleges/"):
        return "College Detail"
    elif url.startswith("https://www.collegedekho.com/amp/news/"):
        return "News AMP"
    elif url.startswith("https://www.collegedekho.com/news/"):
        return "News"
    elif url.startswith("https://www.collegedekho.com/exam/"):
        return "Exam"
    elif url.startswith("https://www.collegedekho.com/courses/"):
        return "Course"
    return "Other"

def read_urls_from_file(file_path):
    with open(file_path, 'r') as file:
        urls = file.readlines()
    return [url.strip() for url in urls]

# Main execution
file_path = 'url.txt'
urls = read_urls_from_file(file_path)
all_results = []

for url in urls:
    data = fetch_page_speed_data(url)
    print(url)
    metrics = extract_performance_metrics(data, url)
    all_results.append(metrics)

def save_results_to_csv(results, filename):
    df = pd.DataFrame(results)
    df.to_csv(filename, index=False)
    print(f"Results saved to {filename}")

save_results_to_csv(all_results, 'page_speed_results.csv')





