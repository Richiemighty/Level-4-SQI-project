import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("books_data.csv")


st.title("Books to Scrape: Data Dashboard")


st.header("Key Insights")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Books", len(df))

with col2:
    st.metric("Average Price", f"£{df['Price'].mean():.2f}")

with col3:
    st.metric("Price Range", f"£{df['Price'].min():.2f} - £{df['Price'].max():.2f}")







most_books_cat = df["Category"].value_counts().idxmax()
st.write(f"**Category with the Most Books:** {most_books_cat}")

# Average price per category
avg_price_per_cat = df.groupby("Category")["Price"].mean().sort_values(ascending=False)


# Most expensive category
expensive_cat = avg_price_per_cat.idxmax()
st.write(f"**Category with the Most Expensive Books on Average:** {expensive_cat} (£{avg_price_per_cat.max():.2f})")




#####  Rating Distribution
st.subheader("Ratings Breakdown")
rating_counts = df["Rating"].value_counts().sort_index()
st.bar_chart(rating_counts)


###   Price vs Rating Relationship
st.subheader("Price vs. Rating")
corr = df["Price"].corr(df["Rating"])
st.write(f"Correlation between Price and Rating: `{corr:.2f}`")

fig_corr, ax_corr = plt.subplots()
sns.regplot(data=df, x="Rating", y="Price", ax=ax_corr)
st.pyplot(fig_corr)



###    Availability
st.subheader("Stock Availability")
availability_counts = df["Availability"].value_counts()
st.write(availability_counts)

# Availability percent
percentage_available = (df["Availability"] == "In Stock").mean() * 100
st.write(f"**Books In Stock:** {percentage_available:.2f}%")




# --- VISUALIZATIONS SECTION ---

st.header("Visualizations")

# Books per Category
st.subheader("Number of Books per Category")
fig1, ax1 = plt.subplots()
df["Category"].value_counts().plot(kind="bar", color="skyblue", ax=ax1)
plt.xticks(rotation=45)
st.pyplot(fig1)



# Availability
st.subheader("Availability Ratio")
fig2, ax2 = plt.subplots()
ax2.pie(availability_counts, labels=availability_counts.index, autopct="%1.1f%%", colors=["green", "red"])
st.pyplot(fig2)



# Price Distribution
st.subheader("Price Distribution")
fig3, ax3 = plt.subplots()
sns.histplot(df["Price"], bins=20, kde=True, ax=ax3, color="purple")
st.pyplot(fig3)



# Rating vs Average Price
st.subheader("Average Price per Rating")
rating_avg_price = df.groupby("Rating")["Price"].mean()
fig4, ax4 = plt.subplots()
rating_avg_price.plot(kind="bar", ax=ax4, color="orange")
plt.xlabel("Star Rating")
plt.ylabel("Average Price (£)")
st.pyplot(fig4)

# Footer
st.markdown("---")
st.markdown("Created by Kehinde Richard | Data from [Books to Scrape](https://books.toscrape.com/)")
