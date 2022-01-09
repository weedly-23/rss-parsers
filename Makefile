-include .env
export

run:
	@python -m rssparser


lint:
	@mypy rssparser
	@flake8 rssparser
