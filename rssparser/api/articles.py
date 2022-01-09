from typing import Any


class ArticleClient:

    def __init__(self, url: str) -> None:
        self.url = url

    def add(self, feed_id: int, title: str, description: str) -> dict[str, Any]:
        return {}
