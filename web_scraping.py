
#Author kricksaw
#NOTE: BS4 must be installed: sudo apt-get install pyhton3-bs4
import requests
from bs4 import BeautifulSoup

page = requests.get('https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/')

soup = BeautifulSoup(page.content,'html.parser')

page_title = soup.title
page_body = soup.body
page_head = soup.head

all_links = []

image_data = []

images = soup.select('img')

for image in images:
	src = image.get('src')
	alt = image.get('alt')
	image_data.append({"src": src, "alt":alt})

print(image_data)

#print(page.text)
#print(page.status_code)
#print(page_title)
#print(page_body)
#print(page_head)

#links = soup.select('a')

#for ahref in links:
	#text = ahref.text
	#text = text.strip() if text is not None else ''

	#href = ahref.get('href')
	#href = href.strip() if href is not None else ''
	#all_links.append({"href": href, "text": text})

#print(all_links)