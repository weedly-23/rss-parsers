import arrow
from typing import Optional
from yarl import URL

import httpx
import structlog

from rssparser.api.models import Article

logger = structlog.getLogger(__name__)


class ArticleClient:

    def __init__(self, url: URL) -> None:
        self.url = url

    def add(
        self, feed_id: int, url: str, title: str,
        description: Optional[str],
        author_id: Optional[int], published: arrow.Arrow,
    ) -> Optional[Article]:
        payload = {'title': title, 'url': url,
                   'published': published.for_json(), 'feed_id': feed_id,
                   'author_id': author_id, 'description': description
                   }

        url = self.url / 'api/v1/articles/'

        try:
            req = httpx.post(str(url), json=payload)
            req.raise_for_status()

            req_data = req.json()
            req_data['published'] = arrow.get(req_data['published'])
            return Article(**req_data)

        except httpx._exceptions.HTTPStatusError:
            logger.warning('Статья уже в БД')
            return None
