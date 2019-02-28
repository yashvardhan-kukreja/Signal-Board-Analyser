import requests
import json

"""
   Sample article object:


       {
           "source": {
               "id": "the-jerusalem-post",
               "name": "The Jerusalem Post"
           },
           "author": "By ANNA AHRONHEIM",
           "title": "The Day after Daesh",
           "description": "Some description.",
           "url": "https://www.jpost.com/Middle-East/The-Day-after-Daesh-581005",
           "urlToImage": "https://images.jpost.com/image/upload/f_auto,fl_lossy/t_Article2016_ControlFaceDetect/426563",
           "publishedAt": "2019-02-18T12:37:02Z",
           "content": "Some content"
       }

   """


def fetch_news(place, api_key="86a49e231a1f44509577fd4784b438bd"):
    url = "https://newsapi.org/v2/everything?q={}&from=2019-01-18&sortBy=publishedAt&apiKey={}".format(place, api_key)
    client = requests.get(url)
    output = json.loads(client.text)
    return output["articles"]

