from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer

from flask import Flask, request, jsonify

app = Flask(__name__)

sentimentCache = {}

custom_analyzer = NaiveBayesAnalyzer()
#analyzers = [NaiveBayesAnalyzer() for _ in range(10)]

@app.route("/batch-sentiment", methods = ["POST"])
def batch_sentiment():
    messages = request.json

    sentiments = []

    for message in messages:
        if sentimentCache.get(message, None):
            sentiments.append(sentimentCache[message])
            next

        blob = TextBlob(message, analyzer=custom_analyzer)

        negative_sentiment = blob.sentiment.p_neg

        sentimentCache[message] = negative_sentiment

        sentiments.append(negative_sentiment)

    return jsonify(sentiments)

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=3470)
