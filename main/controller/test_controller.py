from common.controller import get, router
from service.test_service import TestService


@router('/tests', tags=['tests'])
class TestController:

    def __init__(self, test_service: TestService) -> None:
        super().__init__()
        self.test_service = test_service

    @get("/?")
    def list_tests(self):
        return self.test_service.list_tests()

    @get("/{test_id}/detail/?")
    def get_question_detail(self, test_id: int):
        return self.test_service.get_question_detail(test_id)

    @get("/hot/?")
    def get_liked_test(self):
        return self.test_service.list_liked_tests()

    @get("/search//?")
    def search_tests(self, key_word: str):
        return self.test_service.search_tests(key_word=key_word)


