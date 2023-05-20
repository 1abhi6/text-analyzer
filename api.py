import paralleldots as pd
from config import API_KEY

class API:
    def __init__(self):
        pd.set_api_key(API_KEY)

    def sentiment_analysis(self, text):
        response = pd.sentiment(text)
        return response

    def ner_analysis(self, text, lang_code="en"):
        response = pd.ner(text, lang_code)
        return response

    def emotion_prediction(self, text):
        response = pd.emotion(text)
        return response
    
    def abuse_detection(self, text):
        response = pd.abuse(text)
        return response
    
    def keyword_detection(self, text):
        response = pd.keywords(text)
        return response