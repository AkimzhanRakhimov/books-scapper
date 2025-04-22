📚 Book Store Web Scraper

#### 📝 Description
This is a Python script that scrapes book data from [books.toscrape.com](http://books.toscrape.com), a website designed for practicing web scraping.  
It collects information about each book, including the title, price, availability, and rating, and saves the data into a CSV file.

---

#### ⚙️ Technologies Used
- **Python 3**  
- **BeautifulSoup** (for HTML parsing)  
- **Requests** (for sending HTTP requests)  
- **CSV** module (for saving data)

---

#### 📊 Features
- Scrapes data from multiple pages (e.g. the first 5 pages)  
- Extracts book title, price, availability, and rating  
- Saves all collected data to a `CSV` file  
- Handles missing data and unexpected formatting gracefully

---

#### 🚀 How to Run

1. Clone the repository:
```bash
git clone https://github.com/yourusername/bookstore-scraper.git
cd bookstore-scraper
```

2. (Optional) Install dependencies:
```bash
pip install beautifulsoup4 requests
```

3. Run the script:
```bash
python scraper.py
```

4. Check the output file:
```bash
output.csv
```

---

#### 🧪 Sample Output

| Title                          | Price | Availability | Rating   |
|-------------------------------|--------|---------------|----------|
| A Light in the Attic          | £51.77 | In stock      | Three    |
| Tipping the Velvet            | £53.74 | In stock      | One      |

---

#### 📁 Project Structure

```
bookstore-scraper/
├── scraper.py
├── output.csv
└── README.md
```

---

#### 📌 Notes
This project is for educational purposes only. The website used here is specifically made for scraping practice. Always respect a website's `robots.txt` when scraping real data.

---

