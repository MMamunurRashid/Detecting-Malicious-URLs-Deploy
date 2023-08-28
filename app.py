from flask import Flask, render_template, request
import joblib
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from tokenizer import tokenizer

app = Flask(__name__)

# Load the trained model and vectorizer
with open("model.joblib", "rb") as model_file:
    model = joblib.load(model_file)

with open("vectorizer.joblib", "rb") as vectorizer_file:
    tVac = joblib.load(vectorizer_file)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    url = request.form["url"]

    # Tokenize and vectorize the URL using the tokenizer from the separate module
    tokenized_url = tokenizer(url)
    vectorized_url = tVac.transform(tokenized_url)

    # Make a prediction
    prediction = model.predict(vectorized_url)
    result = "Malicious" if prediction[0] == "bad" else "Safe"

    return render_template("index.html", url=url, result=result)


if __name__ == "__main__":
    app.run(debug=True)
