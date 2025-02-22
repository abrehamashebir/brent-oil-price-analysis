
import matplotlib.pyplot as plt
import pandas as pd

def visualizer(df):
    plt.figure(figsize=(12, 6))
    plt.plot(df["Date"], df["Price"], label="Brent Oil Price")
    plt.xlabel("Year")
    plt.ylabel("Price (USD)")
    plt.title("Brent Oil Prices Over Time")
    plt.legend()
    plt.show()