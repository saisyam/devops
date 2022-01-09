from fastapi import FastAPI

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

app = FastAPI()
sid_obj = SentimentIntensityAnalyzer()


def get_sentiment(sentence):
    # polarity_scores method of SentimentIntensityAnalyzer
    # object gives a sentiment dictionary.
    # which contains pos, neg, neu, and compound scores.
    sentiment_dict = sid_obj.polarity_scores(sentence)
    sentiment = ""
 
    # decide sentiment as positive, negative and neutral
    if sentiment_dict['compound'] >= 0.05 :
        sentiment = "positive"
    elif sentiment_dict['compound'] <= - 0.05 :
        sentiment = "negative"
    else :
        sentiment = "neutral"
    return {
        "sentiment": sentiment
    }

@app.post("/sentiment")
async def sentiment(sentence: str):
    return get_sentiment(sentence)