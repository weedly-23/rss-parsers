from rssparser.api.articles import ArticleClient
from rssparser.api.authors import AuthorClient
from rssparser.api.feeds import FeedClient


class ApiClient:

    def __init__(self, api_url: str) -> None:
        self.articles = ArticleClient(api_url)
        self.feeds = FeedClient(api_url)
        self.authors = AuthorClient(api_url)
        self.api_url = api_url
