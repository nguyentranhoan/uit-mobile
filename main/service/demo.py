from injector import inject, singleton

from component.database import MasterDatabase
from request.create_user import CreateUserNormal


@inject
@singleton
class DemoService:

    def __init__(self, master_database: MasterDatabase):
        super().__init__()
        self.master_database = master_database

    def list(self):
        with self.master_database.session() as db:
            def register_normal(request: CreateUserNormal):
                db.execute(f"""
                            INSERT INTO user_account (
                                                    first_name,
                                                    midle_name,
                                                    last_name,
                                                    normal_account,
                                                    password,
                                                    email,
                                                    avatar)
                                            VALUES (
                                                    '{request.first_name}',
                                                    '{request.midle_name}',
                                                    '{request.last_name}',
                                                    '{request.normal_account}',
                                                    '{request.password}',
                                                    '{request.email}',
                                                    '{request.avatar}')""")
                db.commit()
                return 1
