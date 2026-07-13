from models import Article


def build_articles(titles):

    articles = []

    for title in titles:

        articles.append(
            Article(title)
        )

    return articles
