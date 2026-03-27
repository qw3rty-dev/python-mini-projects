import requests
from bs4 import BeautifulSoup
import csv
from urllib.parse import urljoin
import time
def news_scraper():

    page=1
    posts=[]
    url="https://news.ycombinator.com/"
    while True:
        time.sleep(1)
        print(f"Page {page}")
        req=requests.get(url)
        if req.status_code != 200:
            print("Request failed")
            break
        soup=BeautifulSoup(req.text,"lxml")
        data=soup.select(".athing")
        for news in data:

            title_tag=news.select_one(".titleline a")
            title=title_tag.text
            link = title_tag.get("href")
            subtext=news.find_next_sibling("tr")
            score_tag=subtext.select_one(".score")
            if score_tag:
                score=int(score_tag.text.replace("points",""))
            else:
                score=0

            post={"title":title,"link":link,"score":score}
            posts.append(post)

        more_link=soup.select_one(".morelink")
        if more_link:
            url= urljoin(url,more_link.get("href"))
            page+=1
        else:
            print("Reached last page")
            break

    posts=sorted(posts,key= lambda x: x['score'],reverse=True)
    top10=posts[:10]
    with open("news.csv","w",encoding="utf-8") as f:
        writer=csv.writer(f) 
        writer.writerow(["Title","Score","Link"])
        for i in top10:    
            writer.writerow([i["title"],i["score"],i["link"]])

if __name__== "__main__":
    news_scraper()
