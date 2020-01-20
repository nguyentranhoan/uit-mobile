from injector import inject, singleton

from component.database import MasterDatabase


@inject
@singleton
class RecommendService:

    def __init__(self, master_database: MasterDatabase):
        super().__init__()
        self.master_database = master_database

    def list_similar_user(self):
        with self.master_database.session() as db:
            pass
