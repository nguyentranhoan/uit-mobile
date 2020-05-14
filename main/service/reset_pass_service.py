from injector import inject, singleton

from component.database import MasterDatabase
from mail.sending_email import reset_pass_mail
from request.reset_password import ResetPassword


@inject
@singleton
class ResetPassService:

    def __init__(self, master_database: MasterDatabase):
        super().__init__()
        self.master_database = master_database

    def reset_password(self, request: ResetPassword):
        with self.master_database.session() as db:
            db.execute(f"""
                    DELETE FROM
                        authentication""")

            info = db.execute(f"""
                    SELECT
                        user_account.id,
                        user_account.normal_account,
                        user_account.email
                    FROM
                        user_account
                    WHERE
                        user_account.email = '{request.email}'""").fetchone()

            if info is None:
                return 0
            else:
                db.execute(f"""
                            INSERT INTO
                                authentication (
                                        id,
                                        user_name,
                                        password,
                                        email)
                                VALUES (
                                        {info.id},
                                        '{info.normal_account}',
                                        '{request.new_password}',
                                        '{request.email}')""")
                db.commit()
                reset_pass_mail(request.email, info.normal_account)
                return info.normal_account

    def reset_pass_successful(self):
        with self.master_database.session() as db:
            response = 'successful!'
            info = db.execute(f"""
                        SELECT
                            id,
                            user_name,
                            password,
                            email
                        FROM
                            authentication""").fetchone()

            db.execute(f"""
                            UPDATE user_account
                            SET
                                password = '{info.password}'
                            WHERE
                               email = '{info.email}'""")
            db.commit()
            return response
