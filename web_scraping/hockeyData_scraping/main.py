from bs4 import BeautifulSoup
import requests
import time
import csv
def data_scraper():
    with open("hockey.csv","w") as file:
        writer=csv.writer(file)
        writer.writerow(["Name","Year","Win","Loss","Goal_for","Goal_against"])
        
        for page in range(1,25):
            time.sleep(1)
            print(f"\n>>>>> Scraping page {page}.......\n")
            url=f"https://www.scrapethissite.com/pages/forms/?page_num={page}"
            req=requests.get(url)
            soup=BeautifulSoup(req.text,"lxml")
            content=soup.find_all("tr",class_="team")
            for index in content:
                tname=index.select_one(".name").text.strip()
                year=index.select_one(".year").text.strip()
                win=index.select_one(".wins").text.strip()
                loss=index.select_one(".losses").text.strip()
                goalFor=index.select_one(".gf").text.strip()
                goalAgainst=index.select_one(".ga").text.strip()
                writer.writerow([tname,year,win,loss,goalFor,goalAgainst])

                print(f"Team Name: {tname}")
                print(f"Year: {year}")
                print(f"Win: {win}")
                print(f"Loss: {loss}")
                print(f"Goals for: {goalFor}")
                print(f"Goals against: {goalAgainst}")
                print("-"*120)



if __name__=="__main__":
    data_scraper()
