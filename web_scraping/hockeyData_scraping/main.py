from bs4 import BeautifulSoup
import requests
import time
import csv
def data_scraper():
    with open("book.csv","w",encoding="utf-8-sig") as file:
        writer=csv.writer(file)
        writer.writerow(["Name","Year","Win","Loss","Goal_for","Goal_against"])
        page=1
        base_url="https://www.scrapethissite.com/"
        while True:
            time.sleep(1)
            url=f"https://www.scrapethissite.com/pages/forms/?page_num={page}"
            req=requests.get(url)
            if req.status_code!=200:
                print("Request failed")
                break
            soup=BeautifulSoup(req.text,"lxml")
            teams=soup.select(".team")
            if not teams:
                print("Done")
                break
            print(f"\n {'='*20}Page {page}{'='*20}\n")
            for team in teams:
                tname=team.select_one(".name").text.strip()
                year=team.select_one(".year").text.strip()
                win=team.select_one(".wins").text.strip()
                loss=team.select_one(".losses").text.strip()
                goalFor=team.select_one(".gf").text.strip()
                goalAgainst=team.select_one(".ga").text.strip()
                writer.writerow([tname,year,win,loss,goalFor,goalAgainst])

                print(f"Team Name: {tname}")
                print(f"Year: {year}")
                print(f"Win: {win}")
                print(f"Loss: {loss}")
                print(f"Goals for: {goalFor}")
                print(f"Goals against: {goalAgainst}")
                print("-"*120)
            page+=1



if __name__=="__main__":
    data_scraper()
