from injector import inject, singleton

from component.database import MasterDatabase
from request.create_user import CreateUserNormal
from mail.sending_email import validate_user_mail


@inject
@singleton
class RegisterService:

    def __init__(self, master_database: MasterDatabase):
        super().__init__()
        self.master_database = master_database

    def register_normal(self, request: CreateUserNormal):
        with self.master_database.session() as db:
            db.execute(f"""
                    DELETE FROM
                        authentication""")

            db.execute(f"""
                        INSERT INTO authentication (                                                
                                                user_name,
                                                password,
                                                email)
                                        VALUES (                                                
                                                '{request.normal_account}',
                                                '{request.password}',
                                                '{request.email}')""")
            db.commit()
            validate_user_mail(request.email)

    def register_normal_successful(self):
        with self.master_database.session() as db:
            response = 'successful!'
            request = db.execute(f"""
                        SELECT
                            user_name,
                            password,
                            email
                        FROM
                            authentication""").fetchone()
            db.execute(f"""
                        INSERT INTO user_account (
                                                normal_account,
                                                password,
                                                email)
                                        VALUES (
                                                '{request.user_name}',
                                                '{request.password}',
                                                '{request.email}')""")
            return response
