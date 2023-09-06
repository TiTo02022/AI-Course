from bs4 import BeautifulSoup
import csv
import requests
page=requests.get('https://game3rb.com/')
src=page.content 
print(src)

#with open ('Introduction.html') as html_file:
  #  soup = BeautifulSoup(html_file, 'lxml')
 #   print(soup)