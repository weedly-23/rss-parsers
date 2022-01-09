import time
from typing import Any

import structlog

from rssparser.api.client import ApiClient
from rssparser.api.models import Feed
from rssparser.config import AppConfig

logger = structlog.getLogger(__name__)


class Worker:

    def __init__(self, config: AppConfig) -> None:
        self._is_working = False
        self._period = config.period
        self._client = ApiClient(config.api_url)
        self._feeds: list[Feed] = []

    def start(self) -> None:
        if self._is_working:
            return

        self._is_working = True
        while (self._is_working):
            logger.info('check feeds')

            self._work()

            logger.info('wait', timeout=self._period)
            time.sleep(self._period)

    def stop(self) -> None:
        self._is_working = False

    def _work(self) -> None:
        logger.info('check feeds and grab all of them')
        self._feeds = self._client.feeds.get_all()

        for feed in self._feeds:
            logger.info('get rss from feed', feed=feed.uid)

            # emulate articles received from feed
            articles: list[dict[str, Any]] = [{
                'uid': 1,
                'title': 'some article',
                'description': 'something interesting',
            }]

            for article in articles:
                self._client.articles.add(
                    feed_id=feed.uid,
                    title=article['title'],
                    description=article['description'],
                )

            logger.info('feed processed', feed=feed.uid, articles=len(articles))
