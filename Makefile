.PHONY: default
default: help

.PHONY: help
help:
	@echo "All Commands:"
	@echo "	run - Run application."

.PHONY: run
run:
	python -m pythonframework.server

