from bs4 import BeautifulSoup
import requests
import csv
import time
def quote_scrap():
    print("Working........")
    with open("quotes.csv","w",encoding="utf-8-sig") as file:
        writer=csv.writer(file)
        writer.writerow(["Quote","Author","Tags"])
        page=1
        while True: 
            time.sleep(1)
            print(f"\n>>>>> Scraping page {page}.......\n")
            url=f"https://quotes.toscrape.com/page/{page}/"
            req=requests.get(url)
            soup=BeautifulSoup(req.text,"lxml")
            cards=soup.find_all('div',class_="quote")
            for content in cards:
                quote=content.find(class_="text").text.strip()
                author=content.find(class_="author").text.strip()
                tags=[tag.text for tag in content.find_all(class_="tag")]
                tags=", ".join(tags)
                writer.writerow([quote,author,tags])
                print(f"Quote : {quote}")
                print(f"Author : {author}")
                print(f"Tags : {tags}")
                print("-"*120)
            next_button=soup.find("li",class_="next")
            if next_button:
                page+=1
            else:
                break


if __name__=="__main__":
    quote_scrap()
