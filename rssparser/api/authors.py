import httpx

import structlog

from rssparser.api.models import Author

logger = structlog.getLogger(__name__)


class AuthorClient:

    def __init__(self, url: str) -> None:
        self.url = url

    def get_by_name(self, name, feed_id) -> Author:
        req = httpx.get(f"{self.url}api/v1/feeds/{feed_id}/authors", follow_redirects=True).json()
        for e in req:
            if e['name'] == name:
                return Author(**e)

    def get_by_id(self, author_id) -> Author:
        req = httpx.get(f"{self.url}api/v1/authors/?uid={author_id}").json()
        return Author(**req)

    def add_author(self, name, feed_id) -> Author:
        payload = {"name": name, "feed_id": feed_id}
        req = httpx.post(f'{self.url}api/v1/authors/', json=payload).json()
        logger.debug(f'Добавили в БД: name - {name}, feed_id - {feed_id} .')
        return Author(**req)

    def author_exists(self, name, feed_id) -> bool:
        req = httpx.get(f"{self.url}api/v1/feeds/{feed_id}/authors", follow_redirects=True).json()
        return name in [e['name'] for e in req]
