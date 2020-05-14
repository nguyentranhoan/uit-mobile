from injector import inject, singleton

from component.database import MasterDatabase
from request.login_user import LoginUserNormal, LoginUserEmail, LoginUserFacebook


@inject
@singleton
class LoginService:

    def __init__(self, master_database: MasterDatabase):
        super().__init__()
        self.master_database = master_database

    def login_normal(self, request: LoginUserNormal):
        with self.master_database.session() as db:
            info = db.execute(f"""  
                        SELECT id 
                        FROM 
                            user_account
                        WHERE
                            normal_account = '{request.normal_account}'
                            AND password = '{request.password}'""").fetchone()
            if info is None:
                return 0
            else:
                return info.id

    def login_email(self, request: LoginUserEmail):
        with self.master_database.session() as db:
            info = db.execute(f"""
                        SELECT 
                            id 
                        FROM 
                            user_account
                        WHERE
                            email = '{request.email}'""").fetchone()
            if info is None:
                db.execute(f"""
                        INSERT INTO user_account (
                                                email)
                                        VALUES (                                        
                                                '{request.email}')""")
                db.commit()

                new_user = db.execute(f"""
                        SELECT id 
                        FROM 
                            user_account
                        WHERE
                            email = '{request.email}'""").fetchone()
                return new_user.id
            else:
                return info.id

    def login_facebook(self, request: LoginUserFacebook):
        with self.master_database.session() as db:
            info = db.execute(f"""
                        SELECT 
                            id 
                        FROM 
                            user_account
                        WHERE
                            facebook_account = '{request.facebook_account}'""").fetchone()
            if info is None:
                db.execute(f"""
                        INSERT INTO user_account (
                                                facebook_account)
                                        VALUES (                                        
                                                '{request.facebook_account}')""")
                db.commit()

                new_user = db.execute(f"""
                                SELECT 
                                    id 
                                FROM 
                                    user_account
                                WHERE
                                    facebook_account = '{request.facebook_account}'""").fetchone()
                return new_user.id
            else:
                return info.id
