import structlog

logger = structlog.getLogger(__name__)


class AuthorClient:

    def __init__(self, api_url: str, feed_id: int = None) -> None:
        self.feed_id = feed_id
        self.api_url = api_url

    def get_author_id(self, author_name) -> int:
        """если автор есть - отдает его id. нет - добавляет и затем отдает id."""
        pass

    def _add_author(self, name) -> int:
        """добавляет автора в БД, отдает его ID."""
        pass
