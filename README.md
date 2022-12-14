# digiato.com-scraper

This python script scrapes today's news from https://digiato.com (a Persian tech news website).

You can clone this repository into your system by:

```bash
git clone https://github.com/ansari1375/digiato.com-scraper.git
cd digiato.com-scraper
```

Then, make sure that you have the required libraries installed in your environment:

```bash
pip3 install -r requirements.txt
```

Now you can either use it as a standalone script:

```bash
python3 scraper.py
```

which saves the results as a json file (results_YYYY_MM_DD_HH_MM.json).

Or, you can import it in your own code and use it as a function which returns a python dictionary.

```python
from scraper import scrape
results = scrape()
```
