import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("books_data.csv")



print(df["Availability"].value_counts())

# --- 10. Percentage in stock ---
in_stock_percent = (df["Availability"].value_counts() / sum(df["Availability"].value_counts()) ) * 100

print(in_stock_percent)

