import logging
from datetime import datetime
from typing import Optional

import arrow
from pydantic import BaseModel, validator, Field

logger = logging.getLogger(__name__)


class Article(BaseModel):
    title: str
    link: str
    author: Optional[str]
    author_id: Optional[int]
    published: arrow.Arrow = Field(default_factory=datetime.utcnow, alias='published_parsed')
    description: Optional[str]

    @validator('published', pre=True)
    def convert_data(cls, value):
        if isinstance(value, arrow.Arrow):
            return value

        return arrow.get(value)

    class Config:
        arbitrary_types_allowed = True
