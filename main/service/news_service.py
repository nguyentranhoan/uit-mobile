from injector import inject, singleton

from component.database import MasterDatabase
from response.news import News, NewsContent


@inject
@singleton
class NewsService:

    def __init__(self, master_database: MasterDatabase):
        super().__init__()
        self.master_database = master_database

    def list_news(self):
        with self.master_database.session() as db:
            list_news = []
            info = db.execute(f"""
                        SELECT 
                            id,
                            title,
                            image
                        FROM 
                            news
                        ORDER BY
                            id DESC""").fetchall()
            if len(info) == 0:
                return 0
            else:
                for data in info:
                    list_news.append(News(news_id=data.id,
                                          title=data.title,
                                          image=data.image))
                return list_news

    def get_news_detail(self, news_id: int):
        with self.master_database.session() as db:
            list_news = []
            info = db.execute(f"""
                        SELECT 
                            id,
                            title, 
                            content
                        FROM 
                            news                    
                        WHERE 
                            news.id = {news_id}""").fetchall()
            if len(info) == 0:
                return 0
            else:
                for data in info:
                    list_news.append(NewsContent(news_id=data.id,
                                                 title=data.title,
                                                 content=data.content))
                return list_news

    def list_liked_news(self):
        with self.master_database.session() as db:
            list_news = []
            info = db.execute(f"""
                        SELECT 
                            news.id,
                            news.title,
                            news.image,
                            SUM( CASE
                                    WHEN
                                        taken_news.is_liked = True
                                    THEN
                                        1
                                    WHEN
                                        taken_news.is_liked = False
                                    THEN
                                        0
                                    END) AS "liked_news"
                        FROM 
                            news JOIN taken_news ON news.id = taken_news.news_id
                        GROUP BY
                            news.id,
                            news.title,
                            news.image
                        ORDER BY
                            liked_news DESC""").fetchall()
            if len(info) == 0:
                return 0
            else:
                for data in info:
                    list_news.append(News(news_id=data.id,
                                          title=data.title,
                                          image=data.image))
                return list_news
