import requests
from bs4 import BeautifulSoup
import csv

base_url = "http://books.toscrape.com/catalogue/page-{}.html"
headers = ["Title", "Price", "Availability", "Rating"]
all_books = []

for page in range(1, 6):  # собираем первые 5 страниц
    url = base_url.format(page)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.select(".product_pod")
    for book in books:
        title = book.h3.a["title"]
        price = book.select_one(".price_color").text
        availability = book.select_one(".availability").text.strip()
        rating = book.p["class"][1]  # example: "Three", "Five"
        all_books.append([title, price, availability, rating])

with open("output.csv", "w", newline='', encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(all_books)

print("Done! Data saved to output.csv")
