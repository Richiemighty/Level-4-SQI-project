from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import pandas as pd

# Create a list to hold all scraped data
books_data = []

# Scrape first 3 pages
for i in range(1, 4):
    print(f"Scraping page {i}...")

    # Define URL and open connection
    my_url = f"https://books.toscrape.com/catalogue/category/books_1/page-{i}.html"
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()

    # Parse HTML
    container = soup(page_html, "html.parser")
    con = container.find_all("ol", {"class": "row"})
    view_content = con[0].find_all("li", {"class": "col-xs-6 col-sm-4 col-md-3 col-lg-3"})

    # Loop through all books on the page
    for content in view_content:
        # Title
        product_title = content.find("h3").a["title"]

        # Price
        product_price = content.find("p", class_="price_color").text.strip().replace("£", "")
        product_price = float(product_price)

        # Availability
        availability = content.find("p", class_="instock availability").text.strip()

        # Rating (convert text to number)
        rating_text = content.find("p", class_="star-rating").get("class")[1]
        rating_map = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
        rating = rating_map.get(rating_text, 0)

        # Category (we are scraping only "Books" main category here)
        category = "Books"

        # Append all to the data list
        books_data.append({
            "Title": product_title,
            "Price": product_price,
            "Availability": "In Stock" if "In stock" in availability else "Out of Stock",
            "Rating": rating,
            "Category": category
        })

# Convert to DataFrame
df = pd.DataFrame(books_data)

# Show first 5 rows
print(df.head())

# Save to CSV
df.to_csv("books_data.csv", index=False)
print("✅ Data saved to books_data.csv")
