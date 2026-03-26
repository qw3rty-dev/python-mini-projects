from bs4 import BeautifulSoup
import requests
import csv
from urllib.parse import urljoin
import time
def quote_scrap():
    url=f"https://quotes.toscrape.com"
    base_url=f"https://quotes.toscrape.com"
    print("Working........")
    with open("quotes.csv","w",encoding="utf-8-sig") as file:
        writer=csv.writer(file)
        writer.writerow(["Quote","Author","Tags"])
        page=1
        while True: 
            time.sleep(1)
            print(f"\n {'='*20}Scraping page {page}{'='*20}\n")
            req=requests.get(url)
            if req.status_code!=200:
                print("Request failed")
                break
            soup=BeautifulSoup(req.text,"lxml")
            cards=soup.select(".quote")
            for card in cards:
                quote=card.select_one(".text").text.strip()
                author=card.select_one(".author").text.strip()
                tags=card.select_one(".tags meta").get("content")
                tags=tags.split(",")
                writer.writerow([quote,author,tags])
                print(f"Quote  : {quote}")
                print(f"Author : {author}")
                print(f"Tags   : {tags}")
                print("-"*120)
            next_url=soup.select_one("li.next a")
            if next_url:
                url= urljoin(base_url,next_url.get("href"))
                page+=1
            else:
                print("Done")
                break


if __name__=="__main__":
    quote_scrap()



