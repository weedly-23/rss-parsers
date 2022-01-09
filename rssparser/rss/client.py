from datetime import datetime

from rssparser.rss.models import Article


class Client:

    def __init__(self, url: str, last_published: datetime = None) -> None:
        self.url = url
        self.last_published = last_published

    def parse(self) -> list[Article]:
        # call httpx.get to get last rss articles from feed
        return [
            Article(title='some article', description='some description'),
        ]
