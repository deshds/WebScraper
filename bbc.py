# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 18:48:53 2019

@author: desh
"""

import requests
import csv
from bs4 import BeautifulSoup
from datetime import datetime

URL = 'http://www.bbc.co.uk/news'

response = requests.get(URL)
page = BeautifulSoup(response.text, 'html.parser')

# Let's grab all the headlines - not sure why I wanted to do this but seemed like the right thing to do at the time

headlines = page.find_all('h3')

# for headline in headlines :
#    print(headline.text)
    

# And the links with date and time

now = datetime.now()
time_string = now.strftime("%H:%M:%S")
date_string = now.strftime("%Y-%m-%d")
    
urls = page.find_all('a', { 'class': 'gs-c-promo-heading' })

# Create a summary to go with each link but again not sure if this is really necessary. Might be useful for categorization so let's keep it around
# summaries = page.find_all('p', { 'class': 'gs-c-promo-summary' })

# for summary in summaries :
#    print(summary.text)
   
# Output results to a CSV file (for now until we figure out what database we want to use)
    
with open('BBCNewsCrawl Results.csv', 'w') as csvFile:
    resultswriter = csv.writer(csvFile, lineterminator="\n")
    
# Create our header for the CSV file
    resultswriter.writerow(["Headline", "Link", "Date", "Time"])

# Cycle through all the links
    for link in urls:
        resultswriter.writerow([link.text, link['href'], date_string, time_string])
        



    
