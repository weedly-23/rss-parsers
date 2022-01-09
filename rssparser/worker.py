import time

import structlog

logger = structlog.getLogger(__name__)


class Worker:

    def __init__(self, period: int = 60) -> None:
        self._is_working = False
        self._period = period

    def start(self) -> None:
        if self._is_working:
            return

        self._is_working = True
        while (self._is_working):
            logger.info('check feeds')

            self._work()

            logger.info('wait', timeout=self._period)
            time.sleep(self._period)

    def stop(self) -> None:
        self._is_working = False

    def _work(self) -> None:
        logger.info('check feeds and grab all of them')
