import re


def parse(html):

    return re.findall(
        r"<h2>(.*?)</h2>",
        html
    )
