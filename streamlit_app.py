import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("books_data.csv")

# Page title
st.title("Level 4 Project: Book Scraping Dashboard")

st.subheader("Dataset Preview")

with st.expander("Dataset Preview (Click to Expand/Collapse)"):
    st.dataframe(df.head())

# 1. Total books 
st.header("Key Insights")

col1, col2, col3 = st.columns(3)

with col1:
    total_books = len(df)
    st.metric("Total Books Scraped", total_books)

# 2. Average price 
with col2:
    avg_price = df["Price"].mean()
    st.metric("Average Book Price", f"£{avg_price:.2f}")

#  3. Highest and lowest price 
with col3:
    min_price = df["Price"].min()
    max_price = df["Price"].max()
    st.metric("Price Range (Highest and Lowest)", f"£{min_price:.2f} - £{max_price:.2f}")

#  4. Category with most books 
most_books_cat = df["Category"].value_counts().idxmax()
st.write(f"**Category with the Most Books:** {most_books_cat}")


# 5. Average price per category 
avg_price_per_category = df.groupby("Category")["Price"].mean()
st.write("**Average Price per Category:**")
st.dataframe(avg_price_per_category)


# 6. Most expensive category on average 
expensive_cat = avg_price_per_category.idxmax()
expensive_cat_price = avg_price_per_category.max()
st.write(f"**Category with Most Expensive Books (on average):** {expensive_cat} (£{expensive_cat_price:.2f})")


# 7. Number of books per rating 
st.subheader("Number of Books by Star Rating")
rating_counts = df["Rating"].value_counts().sort_index()
st.bar_chart(rating_counts)

# 8. Correlation between price and rating 
st.subheader("Price vs Rating")
correlation = df["Price"].corr(df["Rating"])
st.write(f"**Correlation between Price and Rating:** `{correlation:.2f}`")

fig_corr, ax_corr = plt.subplots()
sns.regplot(x="Rating", y="Price", data=df, ax=ax_corr)
st.pyplot(fig_corr)


# --- 9. In Stock vs Out of Stock ---
st.subheader("Availability Count")
availability_counts = df["Availability"].value_counts()
st.dataframe(availability_counts)


# --- 10. Percentage in stock ---
in_stock_percent = (df["Availability"].value_counts() / sum(df["Availability"].value_counts()) ) * 100

st.write(f"**Percentage of Books In Stock:** {in_stock_percent[0]}%")




# --------------------------------------- Visualizations ---------------------------------------

st.header("Visualizations")

# 1. Bar chart: Number of books per category
st.subheader("Number of Books per Category")
fig1, ax1 = plt.subplots()
df["Category"].value_counts().plot(kind="bar", color="skyblue", ax=ax1)
plt.xticks(rotation=45)
st.pyplot(fig1)

# 2. Pie chart: Availability ratio
st.subheader("Availability Ratio")
fig2, ax2 = plt.subplots()
ax2.pie(availability_counts, labels=availability_counts.index, autopct="%1.1f%%", colors=["green", "red"])
st.pyplot(fig2)

# 3. Histogram: Price distribution
st.subheader("Price Distribution")
fig3, ax3 = plt.subplots()
sns.histplot(df["Price"], bins=20, kde=True, ax=ax3, color="purple")
st.pyplot(fig3)

# 4. Line/Bar chart: Rating vs average price
st.subheader("Average Price per Rating")
rating_avg_price = df.groupby("Rating")["Price"].mean()
fig4, ax4 = plt.subplots()
rating_avg_price.plot(kind="bar", ax=ax4, color="orange")
plt.xlabel("Star Rating")
plt.ylabel("Average Price (£)")
st.pyplot(fig4)

# Footer
st.markdown("---")
st.markdown("Created by Kehinde Richard | Data from Books to Scrape @ https://books.toscrape.com/")
