# World Population Data Scraper

Scrapes current world population statistics for all countries from Worldometers.

## Link

https://www.worldometers.info/world-population/population-by-country/

## Data Collected
- Rank
- Country
- Population (2026)
- Yearly Change
- Net Change
- Land Area (Km²)
- Density (P/Km²)
- Migrants (net)
- Fertility Rate
- Median Age
- Urban Population
- World Share

## Output
Saves data to `Country.csv`

## Tools and Libraries used

- requests
- BeautifulSoup
- lxml
- csv

## How to run
- Install required libraries(pip install....)
- Run the script: python main.py

## Note
Population numbers are in Indian number format as sourced directly from Worldometers.

