from html_parser import MyHTMLParser
import urllib.request
from bs4 import BeautifulSoup
import requests

from language_detecter import LanguageDetector


parser = MyHTMLParser()
#url = "https://www.vpnverbinding.nl/beste-vpn/netflix/"
url = "https://www.vpnconexion.es/blog/mejor-vpn-para-netflix/?_ga=2.224715098.1306859094.1600959792-1235625754.1600959792"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
response = urllib.request.urlopen(req)
html = response.read()
page = requests.get(url).text 
soup = BeautifulSoup(page, "html.parser")
print("Analyzing....")
print(soup.title.string)

#get the webpage language
language = soup.html["lang"].replace("-","_")

print("The language webpage is: "+language)

lang_validate = LanguageDetector(language)

print("-----------")

#find the titles h3,h2,h1 too text in p, div and span inside the divs 
contentTable  = soup.find('div')
rows  = contentTable.find_all(['h3', 'h2', 'h1', 'p', 'div', 'span', 'img', 'li', 'ul'])
for row in rows:
	if not (row.string is None):
	   #print(row.string)
	   #print("············")
	   #append to set the blocks read in the webpage. (use Set for no repeated)
	   lang_validate.html_blocks.add(row)


for block in lang_validate.html_blocks:
	lang_validate.is_in_setlanguage(block.string.strip())

    
print("-----# blocks ------> "+str(len(lang_validate.html_blocks)))

print("=========================")
print("Words Not translated....")
print("=========================")
#lang_validate.clear_not_translated_words()
for i in lang_validate.not_translated:
	print(i)