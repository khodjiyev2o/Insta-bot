from main.scraper import Scraping

with Scraping() as bot:
        try:
            bot.start()
        except RecursionError:
            print("Try again , cannot connect to Internet!")