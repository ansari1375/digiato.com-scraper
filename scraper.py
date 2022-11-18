#!/usr/bin/env python
# coding: utf-8

import json
import requests
import datetime
from bs4 import BeautifulSoup


def get_soup(url):
    resp = requests.get(url)
    soup = BeautifulSoup(resp.content, features="lxml")
    return soup

def get_by_class(soup, name, class_name):
    return soup.find_all(name, {'class':class_name})


def scrape():
    results = {}
    url = 'https://digiato.com/'
    soup = get_soup(url)
    items = soup.find_all('div', {'class':'rowCard homeTodayItem'})
    for i in range(len(items)):
        results[i] = {}
        results[i]['category'] = get_by_class(items[i], 'a', 'rowCard__category')[0].text.strip()
        results[i]['title'] = get_by_class(items[i], 'a', 'rowCard__title')[0].text.strip()
        results[i]['description'] = get_by_class(items[i], 'p', 'rowCard__description')[0].text.strip()
        results[i]['author'] = get_by_class(items[i], 'div', 'rowCard__author')[0].text.strip()
        results[i]['picture'] = get_by_class(items[i], 'a', 'rowCard__picture')[0].img['data-src']
    return results



if __name__=='__main__':
    results = scrape()
    today = datetime.datetime.now()
    year, month, day, hour, minute = today.year, today.month, today.day, today.hour, today.minute
    json.dump(results, open(f'results_{year}_{month}_{day}_{hour}_{minute}.json','w'))


