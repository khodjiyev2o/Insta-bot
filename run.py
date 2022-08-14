from main.scraper import Scraping

with Scraping() as bot:
    bot.land_first_page()
    bot.authentication()
    bot.later()
    bot.search(input("Enter username..."))