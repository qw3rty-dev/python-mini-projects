# Hacker News Scraper

This project is a Python web scraping script that extracts posts from Hacker News and saves the top 10 highest-scoring posts into a CSV file.


## Link
https://news.ycombinator.com/

## Features

- Scrapes multiple pages automatically
- Extracts post title, score, and link
- Handles posts that do not have a score
- Sorts posts based on highest score
- Saves the top 10 posts into a CSV file

## Technologies Used

- requests
- BeautifulSoup
- lxml
- CSV 

## How it works

The script:
1. Open the Hacker news homepage
2. Follows the "More" button to move to the next pages
3. Collects posts from multiple pages
4. Sorts them based on score
5. saves the top 10 highest-scoring posts into a CSV file

## How to run 

- Install required libraries(pip instal...)
- Run the script: python main.py

