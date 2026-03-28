import csv
import requests
from bs4 import BeautifulSoup
def scrap_country():
    url="https://www.worldometers.info/world-population/population-by-country/"
    req=requests.get(url)
    if req.status_code!=200:
        print("Request failed")
    else:

        req.encoding="utf-8"
        with open("Country.csv","w",encoding="utf-8-sig") as file:
            writer=csv.writer(file)
            writer.writerow(["Rank","Country","Population(2026)","Yearly Change","Net Change","Land Area(Km^2)","Density(P/Km^2)",
                            "Migrants(net)","Fertility Rate","Median Age","Urban Pop","World Share"])
            
            soup=BeautifulSoup(req.text,"lxml")
            countries=soup.select("tr")
            # Header=(f"{'Rank':<8} {'Country':<30} {'Population(2026)':<20} {'Yearly Change':<15} {'Net Change':<15} {'Land Area(Km^2)':<15} {'Density(P/Km^2)':<15} {'Migrants(net)':<15} {'Fertility Rate':<15} {'Median Age':<15} {'Urban Pop':<15} {'World Share':<15}")
            # print(Header)
            # print("-"*200)
            for country in countries[1:]:

                rank=country.select(".border-e")[0].text
                name=country.select(".border-e")[1].text
                population=country.select(".border-e")[2].text
                yearly_change=country.select(".border-e")[3].text
                net_change=country.select(".border-e")[4].text
                density=country.select(".border-e")[5].text
                land_area=country.select(".border-e")[6].text
                migrants=country.select(".border-e")[7].text
                fertility_rate=country.select(".border-e")[8].text
                median_age=country.select(".border-e")[9].text
                urban_pop=country.select(".border-e")[10].text
                world_share=country.select(".border-e")[11].text
                # print(f"{rank:<8} {name:<30} {population:<20} {yearly_change:<15} {net_change:<15} {land_area:<15} {density:<15} {migrants:<15} {fertility_rate:<15} {median_age:<15} {urban_pop:<15} {world_share:<15}")
                writer.writerow([rank,name,population,yearly_change,net_change,land_area,density,migrants,fertility_rate,median_age,urban_pop,world_share])
            
            
            # print(density,land_area,migrants,fertility_rate,median_age,urban_pop,world_share)
            # print(rank)

if __name__=="__main__":
    scrap_country()
