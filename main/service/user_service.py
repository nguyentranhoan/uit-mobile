from injector import inject, singleton

from component.database import MasterDatabase
from mail.sending_email import recommend_friend_from, recommend_friend_to
from request.create_user import UpdateUserInfo
from request.result import Result
from request.test import Feedback
from response.result import ResultDetail, Choice
from response.test import Answer
from response.user import UserInfo


@inject
@singleton
class UserService:

    def __init__(self, master_database: MasterDatabase):
        super().__init__()
        self.master_database = master_database

    def update_user_info(self, user_id: int, request: UpdateUserInfo):
        with self.master_database.session() as db:
            db.execute(f"""
                    UPDATE 
                        user_account
                    SET 
                        first_name = '{request.first_name}',
                        midle_name = '{request.midle_name}',
                        last_name = '{request.last_name}',
                        password = '{request.password}'
                    WHERE
                        id = {user_id}""")
            db.commit()
            return 1

    def get_user_info(self, user_id: int):
        with self.master_database.session() as db:
            info = db.execute(f"""
                        SELECT 
                            first_name, 
                            midle_name,
                            last_name,
                            facebook_account,
                            email,
                            normal_account,
                            avatar
                        FROM 
                            user_account
                        WHERE
                            id = {user_id}""").fetchone()
            if info is None:
                return 0
            else:
                return UserInfo(first_name=info.first_name,
                                midle_name=info.midle_name,
                                last_name=info.last_name,
                                facebook_account=info.facebook_account,
                                email=info.email,
                                normal_account=info.normal_account,
                                avatar=info.avatar)

    def read_news(self, user_id: int, news_id: int):
        with self.master_database.session() as db:
            info = db.execute(f"""
                        SELECT 
                            news_id
                        FROM 
                            taken_news
                        WHERE
                            user_id = {user_id}
                            AND news_id = {news_id}""").fetchone()
            if info.news_id is not None:
                return 1
            else:
                db.execute(f"""
                        INSERT INTO 
                            taken_news(
                                    user_id,
                                    news_id,
                                    is_liked)
                            VALUES(
                                    {user_id},
                                    {news_id},
                                    {False})""")
                db.commit()
                return 1

    def get_news_taken(self, user_id: int):
        with self.master_database.session() as db:
            info = db.execute(f"""
                            SELECT
                                taken_news.user_id,
                                taken_news.news_id,
                                news.title AS news_title,
                                news.image AS news_image,
                                taken_news.is_liked
                            FROM 
                                taken_news JOIN news ON taken_news.news_id = news.id
                            WHERE
                                taken_news.user_id = {user_id}""").fetchall()
            if len(info) == 0:
                return 0
            else:
                return info

    def update_news_liked(self, user_id: int, news_id: int):
        with self.master_database.session() as db:
            info = db.execute(f"""
                            SELECT 
                                is_likeds
                            FROM
                                taken_news
                            WHERE
                                user_id = {user_id}
                                AND news_id = {news_id}""").fetchone()
            if not info.is_liked:
                i = 2
            else:
                i = 1
            if i%2 != 0:
                is_liked = False
            else:
                is_liked = True
            db.execute(f"""
                    UPDATE 
                        taken_news
                    SET 
                        is_liked = '{is_liked}'
                    WHERE
                        user_id = {user_id} 
                        AND news_id = {news_id};""")
            db.commit()
            return 1

    def submit_test(self, user_id: int, test_id: int, request: Result):
        with self.master_database.session() as db:
            if user_id == -1:
                db.execute(f"""DELETE FROM taken_test WHERE user_id = {-1}""")
                db.execute(f"""DELETE FROM test_result WHERE user_id = {-1}""")
                db.execute(f"""DELETE FROM previous_test WHERE user_id = {-1}""")
                db.execute(f"""DELETE FROM user_account WHERE id = {-1}""")

                db.execute(f"""INSERT INTO user_account(id) VALUES(-1)""")

            db.execute(f"""
                    DELETE FROM 
                        previous_test
                    WHERE 
                        test_id = {test_id}
                        AND user_id = {user_id}""")

            db.execute(f"""
                    DELETE FROM 
                        taken_test
                    WHERE 
                        test_id = {test_id}
                        AND user_id = {user_id}""")

            db.execute(f"""
                    DELETE FROM 
                        test_result
                    WHERE 
                        test_id = {test_id}
                        AND user_id = {user_id}""")
            # db.commit()

            db.execute(f"""
                        INSERT INTO taken_test (
                                                user_id,
                                                test_id,
                                                is_liked)
                                        VALUES (                                        
                                                {user_id},
                                                {test_id},
                                                {False})""")

            for choice in request.choices:
                info = db.execute(f"""
                            SELECT
                                choice.id as choice_id
                            FROM
                                choice
                            WHERE
                                test_id = {test_id}
                                AND question_id = {choice.question_id}
                                AND is_typed = '{choice.type}'""").fetchone()
                db.execute(f"""
                        INSERT INTO previous_test (
                                                user_id,
                                                test_id,
                                                question_id,
                                                choice_id,
                                                choice_type)
                                        VALUES (                                        
                                                {user_id},
                                                {test_id},
                                                {choice.question_id},
                                                {info.choice_id},
                                                '{choice.type}')""")
                # db.commit()

            data_input = db.execute(f"""
                            select
                                previous_test.user_id,
                                previous_test.test_id,
                                SUM (
                                    CASE
                                    WHEN previous_test.choice_type = 'a'
                                    THEN
                                    1
                                    ELSE
                                    0
                                    END
                                    )*1 
                                    +
                                SUM (
                                    CASE
                                    WHEN previous_test.choice_type = 'b'
                                    THEN
                                    1
                                    ELSE
                                    0
                                    END
                                    )*2 
                                    +
                                SUM (
                                    CASE
                                    WHEN previous_test.choice_type = 'c'
                                    THEN
                                    1
                                    ELSE
                                    0
                                    END
                                    )*3 AS "total_point"
                            from 
                                previous_test
                            where
                                previous_test.test_id = {test_id}
                            group by
                                previous_test.user_id,
                                previous_test.test_id;""").fetchone()

            answer = db.execute(f"""
                            SELECT 
                                id AS answer_id,
                                is_typed, 
                                description,
                                image
                            FROM 
                                answer
                            WHERE 
                                test_id = {test_id}
                                AND point > {data_input.total_point}
                            ORDER BY
                                point""").fetchone()
            # db.commit()

            db.execute(f"""
                INSERT INTO
                    test_result(
                            user_id,
                            test_id,
                            answer_id,
                            answer_type,
                            answer_description)
                    VALUES(
                            {user_id},
                            {test_id},
                            {answer.answer_id},
                            '{answer.is_typed}',
                            '{answer.description}');""")
            db.commit()

            result = db.execute(f"""
                        SELECT DISTINCT
                            test_result.answer_id,
                            test_result.answer_type,
                            test_result.answer_description,
                            answer.image
                        FROM 
                            test_result JOIN answer ON test_result.answer_id = answer.id
                        WHERE
                            test_result.user_id = {user_id}
                            AND test_result.test_id ={test_id}""").fetchone()
            if result is None:
                return 0
            else:
                return Answer(answer_id=result.answer_id,
                              answer_type=result.answer_type,
                              answer_description=result.answer_description,
                              image=result.image)

    def get_tests_taken(self, user_id: int):
        with self.master_database.session() as db:
            list_taken_tests = []
            info = db.execute(f"""
                        SELECT DISTINCT
                            test.id AS test_id,
                            test.title AS test_title,
                            test.image as test_image,
                            taken_test.is_liked,
                            test_result.answer_type
                        FROM 
                            test JOIN test_result ON test.id = test_result.test_id
                            JOIN taken_test ON test.id = taken_test.test_id
                        WHERE
                            test_result.user_id = {user_id}""").fetchall()
            # no taken tests
            if len(info) == 0:
                return 0
            else:
                for data in info:
                    list_taken_tests.append(ResultDetail(test_id=data.test_id,
                                                         test_title=data.test_title,
                                                         test_image=data.test_image,
                                                         is_liked=data.is_liked,
                                                         answer_type=data.answer_type))

                return list_taken_tests

    def get_test_result(self, user_id: int, test_id: int):
        with self.master_database.session() as db:
            result = db.execute(f"""
                        SELECT DISTINCT
                            test_result.user_id,
                            test_result.test_id,
                            test.title AS test_title,
                            test_result.answer_type,
                            test_result.answer_description,
                            answer.image,
                            taken_test.is_liked
                        FROM 
                            test_result 
                            JOIN test ON test_result.test_id = test.id
                            JOIN taken_test ON test_result.test_id = taken_test.test_id
                            JOIN answer ON test_result.answer_id = answer.id
                        WHERE
                            test_result.user_id = {user_id}
                            AND test_result.test_id ={test_id}""").fetchone()
            if result is None:
                return 0
            else:
                return result

    def get_result_detail(self, user_id: int, test_id: int):
        with self.master_database.session() as db:
            list_detail = []
            results = db.execute(f"""
                        SELECT 
                            previous_test.question_id,
                            question.question_content,
                            previous_test.choice_type,
                            choice.choice_content
                        FROM 
                            previous_test JOIN question ON previous_test.question_id = question.id
                            JOIN choice ON previous_test.choice_id = choice.id
                        WHERE
                            previous_test.user_id = {user_id}
                            AND previous_test.test_id ={test_id}""").fetchall()
            if len(results) == 0:
                return 0
            else:
                for result in results:
                    list_detail.append(Choice(question_id=result.question_id,
                                              question_content=result.question_content,
                                              choice_type=result.choice_type,
                                              choice_content=result.choice_content))
                return list_detail

    def update_test_feedback(self, user_id: int, test_id: int, request: Feedback):
        with self.master_database.session() as db:
            db.execute(f"""
                    UPDATE 
                        taken_test
                    SET 
                        feedback = '{request.feedback}'
                    WHERE
                        user_id = {user_id} 
                        AND test_id = {test_id};""")
            db.commit()
            return 1

    def update_test_liked(self, user_id: int, test_id: int):
        with self.master_database.session() as db:
            info = db.execute(f"""
            SELECT 
                is_liked
            FROM
                taken_test
            WHERE
                user_id = {user_id}
                AND test_id = {test_id}""").fetchone()
            if not info.is_liked:
                i = 2
            else:
                i = 1
            if i%2 != 0:
                is_liked = False
            else:
                is_liked = True
            db.execute(f"""
                    UPDATE 
                        taken_test
                    SET 
                        is_liked = '{is_liked}'
                    WHERE
                        user_id = {user_id} 
                        AND test_id = {test_id};""")
            db.commit()
            return 1

    def recommend_friend(self, user_id: int, test_id: int):
        with self.master_database.session() as db:
            test_result = db.execute(f"""
                                SELECT DISTINCT
                                    test_result.answer_id,
                                    user_account.email
                                FROM 
                                    test_result JOIN user_account ON test_result.user_id = user_account.id
                                WHERE
                                    test_result.user_id = {user_id}
                                    AND test_result.test_id = {test_id}""").fetchone()
            if test_result.email is None:
                return 0
            else:

                list_friends = db.execute(f"""
                                    SELECT DISTINCT
                                        user_account.email
                                    FROM 
                                        test_result JOIN user_account ON test_result.user_id = user_account.id
                                    WHERE
                                        test_result.user_id != {user_id}
                                        AND test_result.answer_id = {test_result.answer_id}
                                        AND test_result.test_id = {test_id}""").fetchall()
                if len(list_friends) == 0:
                    return 2
                else:
                    for friend in list_friends:
                        recommend_friend_to(to=friend.email,from_whom=test_result.email)
                        recommend_friend_from(to=friend.email, from_whom=test_result.email)
                    return 1
