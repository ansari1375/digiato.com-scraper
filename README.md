# digiator.com-scraper

This python script scrapes today's news from https://digiato.com (a tech news website).
You can either use it as a standalone script:

python3 scraper.py

The results will be saved as a json file (results.json).

Or, you can import it in your own code and use it as a function which returns a python dictionary.

from scraper import scrape
results = scrape()
