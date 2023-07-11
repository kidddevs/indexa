# Indexa - Website Indexing Script Documentation

This documentation provides an overview of the Python script used to submit URLs to search engines and indexing sites for website indexing.

## Overview

The `indexa.py` script reads URLs from a text file and submits them to popular search engines and indexing sites. It sends HTTP requests to notify these platforms about the existence of your URLs and helps improve their discoverability in search results.

## Prerequisites

- Python 3.x installed on your machine
- `requests` library installed. You can install it using the following command: pip3 install requests


## Usage

1. Create a text file named `urls.txt` in the same directory as the script.
2. Add the URLs you want to submit for indexing in the `urls.txt` file, with each URL on a new line.
3. Modify the `search_engines` list in the script to include the desired search engines and indexing sites. You can add or remove URLs as needed.
4. Run the script using the following command: python indexa.py
5. The script will submit each URL to the specified search engines and indexing sites and generate a submission report.
6. The submission report will be saved in a CSV file named `submission_report.csv` in the same directory as the script.

## Submission Report

The submission report provides information about the success or failure of each URL submission to the search engines and indexing sites. The report is saved in CSV format for easy readability and further analysis.

The report contains the following columns:

- Search Engine: The URL of the search engine or indexing site.
- URL: The submitted URL.
- Status: The status of the submission (Success or Error).

## Disclaimer

Submitting URLs to search engines and indexing sites does not guarantee immediate indexing or improved search rankings. The effectiveness of this script may vary, and it's recommended to employ other SEO techniques in addition to URL submission for better results.

---

