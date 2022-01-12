import httpx

from rssparser.api.models import Author, Feed


class FeedClient:

    def __init__(self, api_url: str) -> None:
        self.api_url = api_url

    def get_all(self) -> list[Feed]:
        raw_feeds = httpx.get(f'{self.api_url}api/v1/feeds/rss').text
        json_feeds = eval(raw_feeds.replace('true', 'True'))
        return [Feed.parse_obj(feed) for feed in json_feeds]

    def get_authors(self, uid: str) -> list[Author]:
        return []
