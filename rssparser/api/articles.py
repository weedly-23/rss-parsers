from typing import Optional

import httpx

from rssparser.api.models import Article


class ArticleClient:

    def __init__(self, url: str) -> None:
        self.url = url

    def check_if_exists(self, author_id, article_url):
        payload = {"article_url": article_url, "author_id": author_id}
        req = httpx.put(f"{self.url}/api/v1/articles/", json=payload).json()
        return bool(req['resp'])

    def add(self, feed_id: int, title: str, description: Optional[str]) -> Article:
        return Article(
            uid=1,
            title='some article',
            description='something interesting',
            feed_id=feed_id,
        )
