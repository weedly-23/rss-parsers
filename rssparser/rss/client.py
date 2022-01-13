from datetime import datetime

import httpx
import feedparser
import structlog

from rssparser.rss.models import Article

logger = structlog.getLogger(__name__)


class Client:

    def __init__(self, url: str, last_published: datetime = None) -> None:
        self.url = url
        self.last_published = last_published

    def parse(self) -> list[Article]:
        resp = httpx.get(self.url)
        feed = feedparser.parse(resp.text)
        articles = feed['entries']

        if not articles:
            raise ValueError(f'No articles in {self.url}')

        return [Article(**article) for article in articles]
