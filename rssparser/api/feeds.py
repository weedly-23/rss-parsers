from rssparser.api.models import Author, Feed


class FeedClient:

    def __init__(self, url: str) -> None:
        self.url = url

    def get_all(self) -> list[Feed]:
        return [Feed(uid=1, url='https://www.ya.ru')]

    def get_authors(self, uid: str) -> list[Author]:
        return []
