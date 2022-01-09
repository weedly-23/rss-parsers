import os
from dataclasses import dataclass


@dataclass
class AppConfig:
    api_url: str
    period: int


def load_from_env() -> AppConfig:
    return AppConfig(
        api_url=os.environ['API_URL'],
        period=int(os.getenv('TASK_PERIOD', 60)),
    )
