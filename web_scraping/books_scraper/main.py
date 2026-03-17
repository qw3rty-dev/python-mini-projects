from bs4 import BeautifulSoup
import requests
import time
import csv
def books_scraper():
    with open("book.csv","w",encoding="utf-8-sig") as file:
        writer=csv.writer(file)
        writer.writerow(["Bname","Price","Rating","Availability"])
        page=1
        while True:
            time.sleep(1)
            print(f"\n>>>>> Scraping page {page}.......\n")
            url=f"https://books.toscrape.com/catalogue/page-{page}.html"
            req=requests.get(url)
            req.encoding= "utf-8"
            soup=BeautifulSoup(req.text,"lxml")
            books=soup.find_all("article",class_= "product_pod")
            for i in books:
                title=i.h3.a["title"]
                price=i.find("p",class_="price_color").text
                rating=i.find("p",class_="star-rating")["class"][-1]
                availability=i.find("p",class_="instock availability").text.strip()
                writer.writerow([title,price,rating,availability])

                print(f"Book Title: {title}")
                print(f"Book Price: {price}")
                print(f"Rating: {rating}/Five")
                print(f"Availability: {availability}")
                print("-"*120)
            next_page=soup.find("li",class_="next")
            if next_page:
                page+=1
            else:
                break

if __name__=="__main__":
    books_scraper()


