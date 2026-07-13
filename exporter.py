def show(articles):

    print("Articles found:\n")

    for article in articles:
        print(article)

    print("\n" + "-" * 22)

    print(
        f"Total Articles: {len(articles)}"
    )
