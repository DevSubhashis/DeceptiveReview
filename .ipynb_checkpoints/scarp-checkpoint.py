from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

# Setup browser
options = Options()
options.add_argument("--headless=new")
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(options=options)

url = "https://www.shiksha.com/college/national-institute-of-fashion-technology-delhi-27356/reviews-2"
driver.get(url)

time.sleep(5)  # wait for JS to load

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

driver.quit()

# -------- Extract Reviews --------

reviews = []

cards = soup.find_all("div", class_="review-card")  # class may change!

for card in cards:
    # Title
    title_tag = card.find("a", class_="review-title")
    title = title_tag.text.strip() if title_tag else None

    # Rating
    rating_tag = card.find("span", class_="rating")  # may vary
    rating = rating_tag.text.strip() if rating_tag else None

    # Pros
    pros_tag = card.find("div", class_="pros")
    pros = pros_tag.text.strip() if pros_tag else None

    # Cons
    cons_tag = card.find("div", class_="cons")
    cons = cons_tag.text.strip() if cons_tag else None

    reviews.append({
        "title": title,
        "rating": rating,
        "pros": pros,
        "cons": cons
    })

# Print sample
for r in reviews[:5]:
    print(r)