from playwright.sync_api import sync_playwright
import csv

def safe_text(locator):
    return locator.text_content() if locator.count() > 0 else None


def int_extractor(text):
    if text is None:
        return None
    digits = "".join(x for x in text if x.isdigit())
    return int(digits) if digits else None


def  get_comments(subtext):
    links = subtext.locator("a")
    for link in links.all():
        text = link.text_content()
        if "comment" in text or "discuss" in text:
            return int_extractor(text)
    return None

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://news.ycombinator.com/")
    page.wait_for_selector(".athing")
    article= page.locator(".athing")
    more = page.locator(".morelink")
    with open("news.csv","w",encoding="UTF-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Title","User","Score","Comments","Link"])
        while True:
            for news in article.all():
                title_tag = news.locator(".titleline a")
                title = safe_text(title_tag.first)
                link = title_tag.first.get_attribute("href")
                subtext = news.locator("xpath=following-sibling::tr[1]")
                user = safe_text(subtext.locator(".hnuser"))
                score = int_extractor(safe_text(subtext.locator(".score")))
                comments = get_comments(subtext)
                writer.writerow([title or "", user or "", score or "", comments or "", link or ""])
                
            if more.count()==0:
                break
            more.click()

    browser.close()
