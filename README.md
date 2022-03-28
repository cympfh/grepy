# grepy: CommandLine web-grep.py

Re-implementation [web-grep](https://github.com/cympfh/web-grep) with Python3,  
Scraping HTML or XML with simple Patterns like `grep -o`.

```bash
# Requires Python3
$ pip install git+https://github.com/cympfh/grepy
$ which grepy
$ curl -sL https://example.com/xxx | grepy '<a href={}></a>'
```
