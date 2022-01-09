from typing import Any


class FeedClient:

    def __init__(self, url: str) -> None:
        self.url = url

    def get_all(self) -> list[dict[str, Any]]:
        return []

    def get_authors(self, uid: str) -> list[dict[str, Any]]:
        return []
