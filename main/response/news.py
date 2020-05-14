class News(object):
    news_id: int
    title: str
    image: str

    def __init__(self, news_id: int, title: str, image: str):
        self.news_id = news_id
        self.title = title
        self.image = image


class NewsContent(object):
    news_id: int
    title: str
    content: str

    def __init__(self, news_id: int, title: str, content: str):
        self.news_id = news_id
        self.title = title
        self.content = content
