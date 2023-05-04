import api

api = api.API()


text="ABhishek is a good boy from mumbai"
response = api.sentiment_analysis(text)
print(response)

for i in response['sentiment']:
    print(i['negative'])