import time

import structlog

from rssparser import rss
from rssparser.api.client import ApiClient
from rssparser.config import AppConfig

logger = structlog.getLogger(__name__)


class Worker:

    def __init__(self, config: AppConfig) -> None:
        self._is_working = False
        self._period = config.period
        self._client = ApiClient(config.api_url)
        self._feeds: dict[int, rss.Client] = {}

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

    def _update_feeds(self) -> None:
        feeds = self._client.feeds.get_all()

        # TODO: check deleted and modified feeds later
        for feed in feeds:

            # only add new feeds
            if feed.uid not in self._feeds:
                self._feeds[feed.uid] = rss.Client(feed.url)

    def _work(self) -> None:
        logger.info('check feeds and grab all of them')
        self._update_feeds()

        for feed_id, feed in self._feeds.items():
            logger.info('get rss from feed', feed=feed_id)
            articles = feed.parse()

            for article in articles:
                self._client.articles.add(
                    feed_id=feed_id,
                    title=article.title,
                    description=article.description,
                )

            logger.info('feed processed', feed=feed_id, articles=len(articles))
