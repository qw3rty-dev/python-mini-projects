# Python Job Scraper

A command-line tool that scrapes live job listings from Python.org — search by keyword or browse the latest openings, all saved to a clean CSV in seconds.

## Why This Exists
Manually browsing job boards is slow. This tool lets you search Python.org jobs programmatically, filter by keyword, and export everything to a spreadsheet you can sort, filter, and share.

## Features
- Scapes the latest Python job listings
- Support keyword search
- Extracts job title,company,location,description, and posting date
- Opens each job page individually to collect accurate data
- Saves results in a clean CSV format

## Data Collected
- Job Title
- Company Name
- Location
- Description Preview
- Date Posted
- Direct Job URL

## How to Run
1. Install dependencies:
```
   pip install requests beautifulsoup4 lxml
```
2. Run:
```
   python main.py
```
3. Enter a keyword like `django`, `remote`, `fastapi`, `automation` — or press Enter to browse latest listings

## Output
Clean `Jobs.csv` ready to open in Excel or Google Sheets

## Tech Used
- Python
- requests
- BeautifulSoup4
- csv
- urllib
