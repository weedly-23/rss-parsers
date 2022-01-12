from typing import Optional

from rssparser.api.models import Article


class ArticleClient:

    def __init__(self, api_url: str) -> None:
        self.api_url = api_url

    def add(self, feed_id: int, title: str, description: Optional[str]) -> Article:
        return Article(
            uid=1,
            title='some article',
            description='something interesting',
            feed_id=feed_id,
        )
