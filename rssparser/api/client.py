from rssparser.api.articles import ArticleClient
from rssparser.api.feeds import FeedClient


class ApiClient:

    def __init__(self, url: str) -> None:
        self.articles = ArticleClient(url)
        self.feeds = FeedClient(url)
