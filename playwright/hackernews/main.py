import csv
import random
import asyncio

from playwright.async_api import async_playwright



async def safe_text(locator):
    return await locator.text_content() if await locator.count() > 0 else None


def int_extractor(text):
    if text is None:
        return None
    digits = "".join(x for x in text if x.isdigit())
    return int(digits) if digits else None


async def goto_with_retry(page,url,attempts=3):
    for attempt in range(1,attempts+1):
        try:
            await page.goto(url,timeout=10_000)
            await page.wait_for_selector(".athing",timeout= 10_000)
            return True
        except Exception as e:
            print(f"Attempt {attempt} failed : {e}") 
            if attempt == attempts:
                return False
            await asyncio.sleep(2*attempt)
    return False


async def get_comments(subtext):
    links = subtext.locator("a")
    for link in await links.all():
        text = await link.text_content()
        if "comment" in text or "discuss" in text:
            return int_extractor(text)
    return None


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        viewport={"width": 1920, "height": 1080})
        await context.add_init_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

        page = await context.new_page()
        url = "https://news.ycombinator.com/"
        
        if not await goto_with_retry(page,url):
            print("Could not load the page")
            await browser.close()
            return
        
        data = page.locator(".athing")
        more = page.locator(".morelink")

        with open("news.csv","w",encoding="UTF-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Title","User","Score","Comments","Link"])
            while True:
                for news in await data.all():
                    title_tag = news.locator(".titleline a")
                    title = await safe_text(title_tag.first)
                    link = await title_tag.first.get_attribute("href")
                    subtext = news.locator("xpath=following-sibling::tr[1]")
                    user = await safe_text(subtext.locator(".hnuser"))
                    score = int_extractor(await safe_text(subtext.locator(".score")))
                    comments = await get_comments(subtext)
                    writer.writerow([title or "", user or "", score or "", comments or "", link or ""])
                    # print(title)

                if await more.count()==0:
                    break
                await page.wait_for_timeout(random.randint(800,2000))
                await more.click()

        await browser.close()


asyncio.run(main())
