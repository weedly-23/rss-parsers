from pydantic import BaseModel


class Feed(BaseModel):
    uid: int
    url: str


class Article(BaseModel):
    uid: int
    title: str
    description: str
    feed_id: int


class Author(BaseModel):
    uid: int
    name: str
    feed_id: int
