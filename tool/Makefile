all:
	@echo "Usage:"
	@echo "- setup:  Initialize git"
	@echo "- build:  Update SUMMARY.md with gitbook build"
	@echo "- deploy: Deploy to server"
	@echo "- serve:  Show contents on Local Server"

setup:
	@git init
	@echo "Run: $ git remote add origin {{ your git repositor url }}"

build:
	@mkdir -p build
	@python tools/build.py
	@gitbook build
	@rm -rf docs
	@rm -rf _book/docs
	@rm -rf _book/asstes
	@rm -rf _book/tools
	@rm -rf _book/Makefile
	@rm -rf _book/.gitignore
	@rm -rf _book/.gitkeep
	@mv _book docs

deploy:
	@make build
	@rm -rf build
	@git add -A
	@git commit -m 'Updated contents'
	@git push origin master

serve:
	@mkdir -p build
	@python tools/build.py
	@gitbook serve --open

.PHONY: all setup build deploy serve
