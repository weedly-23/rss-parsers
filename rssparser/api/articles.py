from typing import Optional

from rssparser.api.models import Article


class ArticleClient:

    def __init__(self, url: str) -> None:
        self.url = url

    def add(
        self, feed_id: int, title: str, description: Optional[str], author_id: Optional[int],
    ) -> Article:
        return Article(
            uid=1,
            title=title,
            description=description,
            feed_id=feed_id,
            author_id=author_id,
        )
