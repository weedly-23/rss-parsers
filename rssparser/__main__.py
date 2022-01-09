import logging

import structlog

from rssparser.worker import Worker

logging.basicConfig(level=logging.DEBUG)

logger = structlog.getLogger(__name__)


def main():
    logger.info('start parser')
    worker = Worker(url='http://localhost:5000')

    try:
        worker.start()
    except KeyboardInterrupt:
        logger.info('received stop signal')
        worker.stop()

    logger.info('stop parser')


if __name__ == '__main__':
    main()
