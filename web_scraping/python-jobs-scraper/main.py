from bs4 import BeautifulSoup
import csv
import requests
from urllib.parse import urljoin
import time
def search_job(keyword,writer):
    total=0
    keyword= keyword.replace(" ","+") if " " in keyword else keyword
    url=f"https://www.python.org/search/?q={keyword}&submit="
    print(url)
    homepage=False
    while True:
        time.sleep(1)
        req=requests.get(url)
        if req.status_code!=200:
            print("Request failed")
            break

        soup=BeautifulSoup(req.text,"lxml")
        jobs=soup.select(".list-recent-events li")
        if "No results found." in jobs[-1].text:
                print("No results found.")
                break
        else:
            total+=page_scraper(jobs,url,homepage,writer)              

        temp=soup.select_one(".list-recent-events")       
        next_div = temp.find_next_sibling("div")
        if not next_div:
            print("Reached last page")
            break
        next_url=None
        next_tag=next_div.select("a")
        for link in next_tag:
            if "Next" in link.text:
                next_url=link.get("href")
                break
        if not next_url:
             print("Reached last page")
             break
        url=urljoin(url,next_url)
    print(f"\n Total jobs scraped: {total}")


def homepage(writer):
    total=0
    url= "https://www.python.org/jobs/"
    homepage=True
    req=requests.get(url)
    print(url)
    if req.status_code!=200:
        print("Request failed")

    soup=BeautifulSoup(req.text,"lxml")
    jobs=soup.select(".list-recent-jobs li")
    if jobs:
        total+=page_scraper(jobs,url,homepage,writer)
    else:
        print("No results found.")
    print(f"\nTotal jobs scraped: {total}")

    
    
def page_scraper(jobs,url,homepage,writer):
    count=0
    for job in jobs:
        job_url=job.select_one(".listing-company a").get("href") if homepage else job.select_one("h3 a").get("href")
        if "/jobs/" in job_url:
            job_url=urljoin(url,job_url)
        else:
            continue
        print(job_url)
       
        sub_req=requests.get(job_url) 
        if sub_req.status_code!=200:
             print("Request failed")
             continue
      
        sub_soup=BeautifulSoup(sub_req.text,"lxml")
        desc=sub_soup.select_one(".job-description")

        if desc:
            text=desc.get_text(separator=" ").strip()
            bad_words=["Key information","Position Details","Responsibilities","About the role","About the company"]


            if "Job Description" in text:
                text= text.split("Job Description",1)[1].strip()
            text=" ".join(text.split())
            for word in bad_words:  
                text=text.replace(word,"") 

            text=text.lstrip(":, ")
                   
            brief=text[:150]+"....." if len(text)>150 else text
            company_tag=sub_soup.select_one(".company-name")
            if company_tag:
                data=list(company_tag.stripped_strings)
                job_title=data[0]
                company_name=data[-1]
            else:
                job_title= "Not available"
                company_name= "Not available"
            location_tag =sub_soup.select_one(".listing-location")
            location=location_tag.text.strip() if location_tag else "Not specified"
            date_tag=sub_soup.select_one(".listing-posted time")
            date=date_tag.text.strip() if location_tag else "Not available"

            writer.writerow([job_title,company_name,location,brief,date,job_url])
            count+=1
         
        else:
            continue
    return count
        
def jobs_scraper():
    with open("Jobs.csv","w",encoding="utf-8-sig") as file:
        writer=csv.writer(file)
        writer.writerow(["Job title","Company","Location","Description","Posted on","Job link"])
        print(f'{"="*40} \n \t   PYTHON JOB SCRAPER \n{"="*40}\n ' )

        print("Enter keywords to search jobs\n"
              "Or press Enter to scrape the latest jobs")

        keyword=input("Search: ")
        if keyword:
            search_job(keyword,writer)
            
        else:
            homepage(writer)

if __name__=="__main__":
    jobs_scraper()
