# digiato.com-scraper

This python script scrapes today's news from https://digiato.com (a tech news website).

First of all, make sure that you have the required libraries installed in your environment:

```bash
pip3 install -r requirements.txt
```

Then, you can either use it as a standalone script:

```bash
python3 scraper.py
```

The results will be saved as a json file (results.json).

Or, you can import it in your own code and use it as a function which returns a python dictionary.

```python
from scraper import scrape
results = scrape()
```
