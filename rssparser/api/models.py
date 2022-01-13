from typing import Optional

from pydantic import BaseModel


class Feed(BaseModel):
    uid: int
    url: str
    category: str
    is_rss: bool
    name: str


class Article(BaseModel):
    uid: int
    title: str
    description: str
    feed_id: int
    author_id: Optional[int]


class Author(BaseModel):
    uid: int
    name: str
    feed_id: int
