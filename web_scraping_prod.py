#Author kricksaw
#NOTE 1: BS4 must be installed: sudo apt-get install pyhton3-bs4
#NOTE 2: Lets gonna use this web: https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/
import requests
import csv
from bs4 import BeautifulSoup

page = requests.get('https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/')

soup = BeautifulSoup(page.content,'html.parser')


all_products = []

# Extract and store in top_items according to instructions on the left
products = soup.select('div.thumbnail')
for product in products:
    name = product.select('h4 > a')[0].text.strip()
    description = product.select('p.description')[0].text.strip()
    price = product.select('h4.price')[0].text.strip()
    reviews = product.select('div.ratings')[0].text.strip()
    image = product.select('img')[0].get('src')

    all_products.append({
        "name": name,
        "description": description,
        "price": price,
        "reviews": reviews,
        "image": image
    })


keys = all_products[0].keys()

with open('products.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(all_products)