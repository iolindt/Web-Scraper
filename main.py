from settings import APP_NAME
from settings import SEPARATOR

from fetcher import download
from parser import parse
from extractor import build_articles
from exporter import show

print(SEPARATOR)
print(APP_NAME)
print(SEPARATOR)
print()

html = download()

titles = parse(html)

articles = build_articles(
    titles
)

show(articles)
