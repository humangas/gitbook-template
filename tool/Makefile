all:
	@echo "You can use gitbook-template more easily with the following command."
	@echo ""
	@echo "Usage:"
	@echo "- install:  Install convenient software and initialize git"
	@echo "- list:     Show asstes contents list in markdown link format"
	@echo "- build:    Build contents to docs diretory with gitbook build"
	@echo "- deploy:   Deploy to git server"
	@echo "- serve:    Show contents on Local Server"

help:
	@make all

install:
	@brew install direnv
	@brew install go
	@go get github.com/mattn/memo
	@\cp -f make/envrc .envrc
	@direnv allow
	@git init
	@echo ""
	@echo "-> Setup direnv. See also: https://github.com/direnv/direnv#setup"
	@echo "-> Run: $ git remote add origin {{ your git repositor url }}"
	@echo "-> Usage mattn/memo See also: https://github.com/mattn/memo"
	@echo ""
	
list:
	@/bin/bash make/list | iconv -f UTF-8-MAC -t UTF-8

build:
	@gitbook build
	@rm -rf docs
	@mkdir docs
	@cp -f _book/index.html docs/
	@cp -f _book/search_index.json docs/
	@cp -fr _book/gitbook docs/
	@cp -fr _book/assets docs/
	@rm -rf docs/assets/*.md

deploy:
	@make build
	@git add -A
	@git commit -m 'Updated contents'
	@git push origin master

serve:
	@gitbook serve --open

.PHONY: all help install list build deploy serve
