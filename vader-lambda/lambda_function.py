from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import json

def lambda_handler(event, context):
    sentence = event['sentence']
    sid_obj = SentimentIntensityAnalyzer()
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
        "statusCode": 200,
        "body": json.dumps({"sentiment": sentiment}),
        "headers": {
          "Content-Type": "application/json"
        }
    }