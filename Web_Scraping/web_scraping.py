from bs4 import BeautifulSoup
import requests

page_to_scrape = requests.get("https://quotes.toscrape.com/")
soup_malone = BeautifulSoup(page_to_scrape.text, "html.parser")

author_quotes = soup_malone.find_all("span", attrs={"class": "text"})
# <span class="text" itemprop="text">
# “It is our choices, Harry, that show what we truly are, far more than our abilities.
# ”</span>
author_name = soup_malone.find_all("small", attrs={"class": "author"})
# <small class="author" itemprop="author">J.K. Rowling</small>

# for author, quote in zip(author_quotes, author_name):
    # print(author.text + " - " + quote.text)
    
# for author in author_quotes:
    # print(author.text)

