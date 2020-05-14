from common.controller import get, router
from service.news_service import NewsService


@router('/news', tags=['news'])
class NewsController:

    def __init__(self, news_service: NewsService) -> None:
        super().__init__()
        self.news_service = news_service

    @get("/?")
    def list_news(self):
        return self.news_service.list_news()

    @get("/{news_id}/?")
    def get_news_detail(self, news_id: int):
        return self.news_service.get_news_detail(news_id)

    @get("/hot/?")
    def get_liked_news(self):
        return self.news_service.list_liked_news()



