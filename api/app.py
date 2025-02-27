from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

# Load data
df = pd.read_csv("brent_oil_prices.csv", parse_dates=["Date"], dayfirst=True)

@app.route("/api/data")
def get_data():
    return jsonify(df.to_dict(orient="records"))

if __name__ == "__main__":
    app.run(debug=True)
