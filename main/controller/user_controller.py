from common.controller import get, router, put
from request.create_user import UpdateUserInfo
from request.result import Result
from request.test import IsLiked, Feedback
from service.user_service import UserService


@router('/users', tags=['users'])
class UserController:

    def __init__(self, user_service: UserService) -> None:
        super().__init__()
        self.user_service = user_service

    @put("/{user_id}/update/?")
    def update_user_info(self, user_id: int, request: UpdateUserInfo):
        return self.user_service.update_user_info(user_id, request)

    @get("/{user_id}/info/?")
    def get_user_info(self, user_id: int):
        return self.user_service.get_user_info(user_id)

    @put("/{user_id}/news/{news_id}/taken/?")
    def read_news(self, user_id: int, news_id: int):
        return self.user_service.read_news(user_id, news_id)

    @get("/{user_id}/news/taken/?")
    def get_news_taken(self, user_id: int):
        return self.user_service.get_news_taken(user_id)

    @get("/{user_id}/news/{news_id}/liked/?")
    def update_news_liked(self, user_id: int, news_id: int, request: IsLiked):
        return self.user_service.update_news_liked(user_id, news_id)

    @put("/{user_id}/tests/{test_id}/submit/?")
    def submit_test(self, user_id: int, test_id: int, request: Result):
        return self.user_service.submit_test(user_id, test_id, request)

    @get("/{user_id}/tests/taken/?")
    def get_tests_taken(self, user_id: int):
        return self.user_service.get_tests_taken(user_id)

    @get("/{user_id}/tests/{test_id}/result/?")
    def get_test_result(self, user_id: int, test_id: int):
        return self.user_service.get_test_result(user_id, test_id)

    @get("/{user_id}/tests/{test_id}/result/detail/?")
    def get_result_detail(self, user_id: int, test_id: int):
        return self.user_service.get_result_detail(user_id,test_id)

    @put("/{user_id}/tests/{test_id}/feedback/?")
    def update_test_feedback(self, user_id: int, test_id: int, request: Feedback):
        return self.user_service.update_test_feedback(user_id, test_id, request)

    @get("/{user_id}/tests/{test_id}/liked/?")
    def update_test_liked(self, user_id: int, test_id: int):
        return self.user_service.update_test_liked(user_id, test_id)

    @get("/{user_id}/tests/{test_id}/friend/?")
    def recommend_friend(self, user_id: int, test_id: int):
        return self.user_service.recommend_friend(user_id,test_id)

