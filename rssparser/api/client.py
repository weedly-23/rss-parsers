from rssparser.api.articles import ArticleClient
from rssparser.api.authors import AuthorClient
from rssparser.api.feeds import FeedClient


class ApiClient:

    def __init__(self, url: str) -> None:
        self.articles = ArticleClient(url)
        self.feeds = FeedClient(url)
        self.authors = AuthorClient(url)
        self.api_url = url
