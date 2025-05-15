from src.services.news_api import News_API

news = News_API()
def get_news():
    return news.get_top_headlines()

print(get_news())