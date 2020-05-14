from typing import List


class Test(object):
    test_id: int
    title: str
    image: str

    def __init__(self, test_id: int, title: str, image: str):
        self.test_id = test_id
        self.title = title
        self.image = image


class Choice(object):
    value: str
    label: str

    def __init__(self, value: str, label: str):
        self.value = value
        self.label = label


class Question(object):
    question_id: int
    question_content: str
    choices: List[Choice]

    def __init__(self, question_id: int, question_content: str, choices: List[Choice]):
        self.question_id = question_id
        self.question_content = question_content
        self.choices = choices


class Answer(object):
    answer_id: int
    answer_type: str
    answer_description: str
    image: str

    def __init__(self, answer_id: int, answer_type: str, answer_description: str, image: str):
        self.answer_id = answer_id
        self.answer_type = answer_type
        self.answer_description = answer_description
        self.image = image
