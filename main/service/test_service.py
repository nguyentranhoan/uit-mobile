from injector import inject, singleton

from component.database import MasterDatabase
from request.create_user import CreateUserNormal
from response.test import Test, Question, Choice


@inject
@singleton
class TestService:

    def __init__(self, master_database: MasterDatabase):
        super().__init__()
        self.master_database = master_database

    def list_tests(self):
        with self.master_database.session() as db:
            list_test = []
            info = db.execute(f"""
                        SELECT 
                            id,
                            title,
                            image
                        FROM 
                            test
                        ORDER BY
                            id  DESC""").fetchall()
            if len(info) == 0:
                return 0
            else:
                for data in info:
                    list_test.append(Test(test_id=data.id,
                                          title=data.title,
                                          image=data.image))
                return list_test

    def get_question_detail(self, test_id: int):
        with self.master_database.session() as db:
            list_question = []
            info = db.execute(f"""
                        SELECT 
                            question.id,
                            question.question_content
                        FROM 
                            question                    
                        WHERE 
                            question.test_id = {test_id}""").fetchall()
            if len(info) == 0:
                return 0
            else:
                for data in info:
                    list_choice = []
                    question_content = ''
                    choices = db.execute(f"""
                        SELECT 
                            is_typed,
                            choice_content
                        FROM 
                            choice                    
                        WHERE 
                            test_id = {test_id}
                            AND question_id = {data.id}""").fetchall()
                    for choice in choices:
                        question_content = data.question_content
                        list_choice.append(Choice(value=choice.is_typed,
                                                  label=choice.choice_content))
                    list_question.append(Question(question_id=data.id,
                                                  question_content=question_content,
                                                  choices=list_choice))
                return list_question

    def list_liked_tests(self):
        with self.master_database.session() as db:
            list_test = []
            info = db.execute(f"""
                        SELECT 
                            test.id,
                            test.title,
                            test.image,
                            SUM( CASE
                                    WHEN
                                        taken_test.is_liked = True
                                    THEN
                                        1
                                    WHEN
                                        taken_test.is_liked = False
                                    THEN
                                        0
                                    END) AS "liked_test"
                        FROM 
                            test JOIN taken_test ON test.id = taken_test.test_id
                        GROUP BY
                            test.id,
                            test.title,
                            test.image
                        ORDER BY
                            liked_test DESC;""").fetchall()
            if len(info) == 0:
                return 0
            else:
                for data in info:
                    list_test.append(Test(test_id=data.id,
                                          title=data.title,
                                          image=data.image))
                return list_test

    def search_tests(self, key_word: str):
        with self.master_database.session() as db:
            list_test = []
            info = db.execute(f"""
                        SELECT 
                            test.id,
                            test.title,
                            test.image                            
                        FROM 
                            test     
                        WHERE
                            test.title LIKE '%{key_word[0].capitalize()}%'
                            OR test.title LIKE '%{key_word[0]}%'
                        ORDER BY
                            test.title DESC;""").fetchall()
            if len(info) == 0:
                return 0
            else:
                for data in info:
                    list_test.append(Test(test_id=data.id,
                                          title=data.title,
                                          image=data.image))
                return list_test
