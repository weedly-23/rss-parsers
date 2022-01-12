from datetime import datetime

import feedparser
import structlog

from rssparser.rss.models import Article

logger = structlog.getLogger(__name__)


class Client:

    def __init__(self, url: str, last_published: datetime = None) -> None:
        self.url = url
        self.last_published = last_published

    def parse(self) -> list[Article]:
        feed = feedparser.parse(self.url)
        if feed['bozo']:
            logger.error(f'неправильная rss ссылыка --- {feed["bozo_exception"]}')
            raise ValueError(f'неправильная rss ссылыка --- {feed["bozo_exception"]}')

        articles = feed['entries']
        return [Article(**article) for article in articles]
