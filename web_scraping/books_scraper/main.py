from bs4 import BeautifulSoup
import requests
import time
import csv
from urllib.parse import urljoin

def books_scraper():
    with open("book.csv","w",encoding="utf-8-sig") as file:
        writer=csv.writer(file)
        writer.writerow(["Title","Category","Price","Rating","Availability","Coverpage URL","Book Link"])
        page=1
        base_url="https://books.toscrape.com/catalogue/"
        url="https://books.toscrape.com/catalogue/page-1.html"
        while True:
            time.sleep(0.5)
            print(f"\n {'='*20}Scraping page {page}{'='*20}\n")
            req=requests.get(url)
            if req.status_code!=200:
                print("Request failed")
                break
            req.encoding= "utf-8"
            soup=BeautifulSoup(req.text,"lxml")
            books=soup.select("article.product_pod")
            for book in books:
                title=book.select_one("h3 a").get("title")
                price=book.select_one(".price_color").text
                rating=book.select_one(".star-rating").get("class")[-1]
                avail_tag=book.select_one(".availability")
                availability= avail_tag.text.strip() if avail_tag else "Unknown"
                image_url=book.select_one(".image_container a img").get("src")[2:]
                image_url=urljoin("https://books.toscrape.com",image_url)
                b_link=book.select_one(".image_container a").get("href")
                link=urljoin(base_url,b_link)
                category="unknown"
                subreq=requests.get(link)
                if req.status_code ==200:
                    subsoup=BeautifulSoup(subreq.text,"lxml")
                    cat=subsoup.select(".breadcrumb li")
                    if len(cat)>2:
                        category=cat[2].text.strip()
                writer.writerow([title,category,price,rating,availability,image_url,link,])
                print(f"Book Title: {title}")
                print(f"Book Price: {price}")
                print(f"Availability: {availability}")
                print(f"Rating: {rating}/Five")
                print(f"Category: {category}")
                print(f"Cover Image Link: {image_url}")
                print(f"Book Link: {link}")
                print("-"*120)
            next_url=soup.select_one("ul.pager  .next a")
            if next_url:
                url=urljoin(base_url,next_url.get("href"))
                page+=1
            else:
                print("Done")
                break

if __name__=="__main__":
    books_scraper()


