import time
import json
import os
import pandas as pd
from datetime import datetime

# Function to run Lighthouse and fetch performance data
def run_lighthouse(url, name):
    getdate = datetime.now().strftime("%m-%d-%y")

    try:
        # Run Lighthouse and wait
        stream = os.popen(f'lighthouse --quiet --no-update-notifier --no-enable-error-reporting --output=json --output-path={name}_{getdate}.report.json --chrome-flags="--headless" {url}')
        time.sleep(120)

        # Load the JSON report
        json_filename = f'{name}_{getdate}.report.json'
        with open(json_filename) as json_data:
            loaded_json = json.load(json_data)

        return loaded_json
    except Exception as e:
        print(f"Error fetching data for URL: {url}. Error: {str(e)}")
        return None


# Function to process Lighthouse data for a list of URLs
def process_lighthouse_data(name, urls):
    dfs = []  # List to store DataFrames for each URL
    performance_data = []

    for url in urls:
        loaded_json = run_lighthouse(url, name)

        performance = str(round(loaded_json["categories"]["performance"]["score"] * 100))
        fcp = loaded_json["audits"]["first-contentful-paint"]["displayValue"]
        toi = loaded_json["audits"]["interactive"]["displayValue"]
        speed_index = loaded_json["audits"]["speed-index"]["displayValue"]
        total_blocking_time = loaded_json["audits"]["total-blocking-time"]["displayValue"]
        largest_contentful_paint = loaded_json["audits"]["largest-contentful-paint"]["displayValue"]
        cumulative_layout_shift = loaded_json["audits"]["cumulative-layout-shift"]["displayValue"]
        max_potential_fid = loaded_json["audits"]["max-potential-fid"]["displayValue"]

        df = pd.DataFrame({
            "URL": [url],
            "Performance": [performance],
            "toi": [toi],
            "first-contentful-paint": [fcp],
            "speed_index": [speed_index],
            "total_blocking_time": [total_blocking_time],
            "largest_contentful_paint": [largest_contentful_paint],
            "cumulative_layout_shift": [cumulative_layout_shift],
            "max_potential_fid": [max_potential_fid]
        })

        dfs.append(df)

        performance_data.append({
            "url": url,
            "Performance": performance,
            "toi": toi,
            "first-contentful-paint": fcp,
            "speed_index": speed_index,
            "total_blocking_time": total_blocking_time,
            "largest_contentful_paint": largest_contentful_paint,
            "cumulative_layout_shift": cumulative_layout_shift,
            "max_potential_fid": max_potential_fid
        })

    # Concatenate DataFrames
    df_result = pd.concat(dfs, ignore_index=True)

    # Save to CSV
    getdate = datetime.now().strftime("%m-%d-%y")
    df_result.to_csv(f'lighthouse_{name}_{getdate}.csv')

    return df_result, performance_data

# Main function to compare performance metrics
def extract_numeric_value(value_str):
    try:
        # Remove non-breaking space (\xa0) and any non-numeric characters
        numeric_str = ''.join(filter(str.isdigit, value_str.replace('\xa0', '')))
        return float(numeric_str)  # Convert to float
    except ValueError:
        return None  # Handle invalid values gracefully

def compare_performance_metrics(staging_df, branch_df):
    comparison_df = pd.DataFrame(columns=["URL", "Metric", "Staging Value", "Branch Value", "Difference"])

    for metric in ["Performance", "toi", "first-contentful-paint", "speed_index", "total_blocking_time", "largest_contentful_paint", "cumulative_layout_shift", "max_potential_fid"]:
        staging_values = staging_df[metric].apply(extract_numeric_value)  # Extract and convert to float
        branch_values = branch_df[metric].apply(extract_numeric_value)    # Extract and convert to float
        differences = staging_values - branch_values

        metric_df = pd.DataFrame({
            "URL": staging_df["URL"],
            "Metric": metric,
            "Staging Value": staging_values,
            "Branch Value": branch_values,
            "Difference": differences
        })

        comparison_df = pd.concat([comparison_df, metric_df], ignore_index=True)

    return comparison_df
# Main function
def main():
    staging_urls = ["https://user:pass@staging-hz.collegedekho.com/"]
    branch_urls = ["https://user:pass@staging-hz.collegedekho.com/exam/cat"]

    df_staging, _ = process_lighthouse_data("test_staging", staging_urls)
    df_branch, _ = process_lighthouse_data("test_branch", branch_urls)

    # Compare performance metrics
    comparison_result = compare_performance_metrics(df_staging, df_branch)

    # Save comparison result to CSV
    comparison_result.to_csv('performance_comparison.csv', index=False)

if __name__ == "__main__":
    main()
