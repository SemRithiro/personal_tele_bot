from newsapi import NewsApiClient

from src.configurations.app import NEWS_API_TOKEN

class News_API():
    newsapi = NewsApiClient(api_key=NEWS_API_TOKEN)
    def __init__(self):
        pass

    def get_top_headlines(self):
        options = {}
        top_headlines = self.newsapi.get_top_headlines(country='us', language='en')
        for articale in top_headlines['articles']:
            options[articale['title']] = {
                'url': articale['url'],
                'photo': articale['urlToImage'],
                'specified_size': None,
                'message': articale['description'],
                'options': {}
            }
        return options