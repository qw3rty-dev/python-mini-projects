# Hacker News Scraper (Playwright)

An async Playwright scraper for [Hacker News](https://news.ycombinator.com/) that extracts story title, author, score, comment count, and link across all paginated pages, exporting to CSV.

Built as a Playwright drill, deliberately targeting a messy real-world site (inconsistent markup across post types) rather than a clean scraping sandbox.

## What it does

- Scrapes every story on the front page and follows "More" pagination until exhausted
- Extracts: title, link, author, score, comment count
- Handles missing fields gracefully (job posts and Ask HN posts often lack a score, author, or comment count)
- Outputs results to `news.csv`

## Techniques demonstrated

- **Async Playwright** — concurrency-ready structure using `async`/`await` throughout
- **Defensive extraction** — every field is checked for existence (`locator.count()`) before being read, so a missing element never crashes the run
- **Retry logic with backoff** — page loads are retried up to 3 times with increasing delay before giving up
- **Stealth basics** — custom user-agent, standard viewport, and overriding the `navigator.webdriver` flag to avoid trivial bot detection
- **Human-like pacing** — randomized delays before pagination clicks instead of fixed intervals

## Setup

```bash
pip install playwright
playwright install
python hackernews.py
```

## Note

Hacker News offers a free public API ([Firebase HN API](https://github.com/HackerNews/API)), which would be the more efficient way to pull this data in production. This project intentionally uses browser automation instead, as a Playwright learning exercise — same site, but through the lens of what you'd need for a JS-rendered site *without* an API.

## Possible extensions

- Keyword filtering (e.g. only save posts mentioning a given topic)
- Scheduled re-runs for a standing "alert me" monitor
- Concurrent scraping of multiple sources using `asyncio.gather`

