-include .env
export

run:
	@python -m parser


lint:
	@mypy parser
	@flake8 parser
