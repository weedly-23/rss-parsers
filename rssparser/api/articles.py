from rssparser.api.models import Article


class ArticleClient:

    def __init__(self, url: str) -> None:
        self.url = url

    def add(self, feed_id: int, title: str, description: str) -> Article:
        return Article(
            uid=1,
            title='some article',
            description='something interesting',
            feed_id=feed_id,
        )
