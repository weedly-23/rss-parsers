# standard logging
import logging

# advanced logging library
import structlog

# make this only once per project
logging.basicConfig(level=logging.DEBUG)

# make it in every class that use logger
logger = structlog.getLogger(__name__)


def main():
    logger.info('start parser')

    logger.info('stop parser')


if __name__ == '__main__':
    main()
