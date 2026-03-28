import requests
from bs4 import BeautifulSoup
import csv
def song_scraper():
    url= "https://en.wikipedia.org/wiki/List_of_Spotify_streaming_records"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Referer": "https://www.google.com"
    }
    req = requests.get(url, headers=headers)
    if req.status_code!=200:
        print("Request failed")
    else:

        soup=BeautifulSoup(req.text,"lxml")
        table=soup.select("table.wikitable")
        songs=table[0]
        rows= songs.select("tr")
        print(f"{'Rank':<8} {'Title':<50} {'Artist':<20} {'Streams (B)':<14} {'Release date'}")
        print("-"*120)
        with open("most_streamed_songs.csv", "w",newline="",encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Rank","Title","Artist","Streams(Billions)","Release Date"])
            for rank,song in enumerate(rows):
                title_tag=song.select_one("th a")
                artist_tag=song.select_one("td a")
                cells=song.select("td")
                

                if title_tag and artist_tag and len(cells)>=3:
                    title=title_tag.get("title")
                    artist=artist_tag.get("title")
                    streams=cells[-3].text.strip()
                    release_date=cells[-2].get_text()
                    writer.writerow([rank,title,artist,streams,release_date])
                    print(f"{rank:<8} {title:<50} {artist:<20} {streams} {'B':<8} {release_date}")

if __name__=="__main__":
     song_scraper()
