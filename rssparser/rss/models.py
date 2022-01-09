from pydantic import BaseModel


# rss article as is
class Article(BaseModel):
    title: str
    description: str
