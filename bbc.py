# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 18:48:53 2019

@author: desh
"""

import requests
import csv
from bs4 import BeautifulSoup
from datetime import datetime

response = requests.get('http://www.bbc.co.uk/news')
page = BeautifulSoup(response.text, 'html.parser')

# Let's grab all the headlines

headlines = page.find_all('h3')

# And the links with date and time

now = datetime.now()
time_string = now.strftime("%H:%M:%S")
date_string = now.strftime("%%yy-%mm-%dd")
    
urls = page.find_all('a', { 'class': 'gs-c-promo-heading' })


summaries = page.find_all('p', { 'class': 'gs-c-promo-summary' })

# for summary in summaries:
#   print(summary.text)
   
# Output results to a CSV file (for now until we figure out what database we want to use)
    
with open('BBCNewsCrawl Results.csv', 'w') as csvFile:
    resultswriter = csv.writer(csvFile, lineterminator="\n")
    
# Create our header for the CSV file
    resultswriter.writerow(["Headline", "Link", "Date", "Time"])

# Cycle through all the links
    for link in urls:
        resultswriter.writerow([link.text, link['href'], date_string, time_string])
        



    