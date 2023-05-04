import paralleldots as pd


class API:
    def __init__(self):
        pd.set_api_key('8oMtxkKLmwc703UmLQ0KDDTgvg1qIX6i45JmZnAQdr0')

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