import requests

class SentimentAnalysis:
    def sentiment_analysis(self,txt):

        url = "https://sentiment-analysis9.p.rapidapi.com/sentiment"
        txt = txt

        payload = [
            {
                "id": "1",
                "language": "en",
                "text": txt
            }
        ]
        headers = {
            "x-rapidapi-key": "9e5798f74fmsh7eb5db240729e15p139e5cjsnd7994969f59b",
            "x-rapidapi-host": "sentiment-analysis9.p.rapidapi.com",
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

        response = requests.post(url, json=payload, headers=headers)

        return response.json()[0]['predictions'][0]['prediction']

sent_ana = SentimentAnalysis()
res = sent_ana.sentiment_analysis("I feel like crying")
print(res)


