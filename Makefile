.PHONY: build render preview

include config.mk

build:
	docker build --tag quarto-box .

render: 
	docker run --rm --mount type=bind,source=$(PWD),target=/project quarto-box quarto render

preview:
	docker run -it --rm -p 4200:4200 --mount type=bind,source=$(PWD),target=/project quarto-box quarto preview --host 0.0.0.0 --port 4200 --no-browser
