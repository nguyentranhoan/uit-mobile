class Choice(object):
    question_id: int
    question_content: str
    choice_type: str
    choice_content: str

    def __init__(self, question_id: int, question_content: str, choice_type: str, choice_content: str) -> None:
        self.question_id = question_id
        self.choice_type = choice_type
        self.choice_content = choice_content
        self.question_content = question_content


class ResultDetail(object):
    test_id: int
    test_title: str
    is_liked: bool
    answer_type: str

    def __init__(self, test_id: int, test_title: str, is_liked: bool, answer_type: str):
        self.test_id= test_id
        self.test_title = test_title
        self.is_liked = is_liked
        self.answer_type = answer_type
