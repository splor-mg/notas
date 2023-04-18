SRC_DIR := $(CURDIR)
WINPTY := ''

ifeq ($(shell uname), Darwin)
# default works
else ifeq ($(shell uname), Linux)
# default works
else ifeq ($(shell uname | head -c 5) , MINGW)
# git bash needs prefixing with winpty
	WINPTY := 'winpty '
else
# for cmd and powershell
	SRC_DIR := "c:$(SRC_DIR)"
endif

DOCKER_RENDER = $(shell echo $(WINPTY) docker run -it --rm --mount type=bind,source=$(PWD),target=/project quarto-box quarto render)
DOCKER_PREVIEW = $(shell echo $(WINPTY) docker run -it --rm -p 4200:4200 --mount type=bind,source=$(SRC_DIR),target=/project quarto-box quarto preview --host 0.0.0.0 --port 4200 --no-browser)
