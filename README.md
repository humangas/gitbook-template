# gitbook-template
Easy setup of gitbook template (defualt, faq, api with include some plugins) .

## Installation (for Mac)
```
$ curl -L https://raw.githubusercontent.com/humangas/gitbook-template/master/install | bash
```

### Select theme
You can select the theme under [template](https://github.com/humangas/gitbook-template/tree/master/template) directory.

```
$ export THEME=api && curl -L https://raw.githubusercontent.com/humangas/gitbook-template/master/install | bash
$ export THEME=faq && curl -L https://raw.githubusercontent.com/humangas/gitbook-template/master/install | bash
...
```

### Force Update depecies software
With the UPDATE option, you can force update the dependent software (if it is not installed, it will be installed).

```
$ export UPDATE=1 && curl -L "https://raw.githubusercontent.com/humangas/gitbook-template/master/install -U" | bash
```


## Usage
After installing, please execute the following.

```
$ mv your_book {{ your book name }}
$ cd {{ your book name }}
$ gitbook serve --open
```

To make it easier... See Makefile

## Install Software
Refer to the following for installed software.

- [software](https://github.com/humangas/gitbook-template/blob/master/install#L37)

## Include Gitbook Plugins
It mainly includes the following plugins.

- [gitbook-plugin-search-languages](https://www.npmjs.com/package/gitbook-plugin-search-languages)
- [gitbook-plugin-toc](https://github.com/whzhyh/gitbook-plugin-toc)
- [gitbook-plugin-uml](https://plugins.gitbook.com/plugin/uml)
- [gitbook-plugin-mermaid-gb3](https://plugins.gitbook.com/plugin/mermaid-gb3)
- [gitbook-plugin-graph](https://github.com/cjam/gitbook-plugin-graph)

