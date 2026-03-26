from bs4 import BeautifulSoup
import requests
import time
import csv
def books_scraper():
    with open("book.csv","w",encoding="utf-8-sig") as file:
        writer=csv.writer(file)
        writer.writerow(["Title","Price","Link","Rating","Availability"])
        page=1
        base_url="https://books.toscrape.com/catalogue/"
        url="https://books.toscrape.com/catalogue/page-1.html"
        while True:
            time.sleep(1)
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
                b_link=book.select_one(".image_container a").get("href")
                link=base_url+b_link
                rating=book.select_one(".star-rating").get("class")[-1]
                avail_tag=book.select_one(".availability")
                availability= avail_tag.text.strip() if avail_tag else "Unknown"
                writer.writerow([title,price,link,rating,availability])

                print(f"Book Title: {title}")
                print(f"Book Price: {price}")
                print(f"Book Link: {link}")
                print(f"Rating: {rating}/Five")
                print(f"Availability: {availability}")
                print("-"*120)
            next_url=soup.select_one("ul.pager  .next a")
            if next_url:
                url=base_url+next_url.get("href")
                page+=1
            else:
                break

if __name__=="__main__":
    books_scraper()


