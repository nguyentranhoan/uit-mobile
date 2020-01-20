from common.controller import router, post
from request.login_user import LoginUserNormal, LoginUserFacebook, LoginUserEmail
from service.login_service import LoginService


@router('/login', tags=['login'])
class LoginController:

    def __init__(self, login_service: LoginService) -> None:
        super().__init__()
        self.login_service = login_service

    @post("/normal/?")
    def login_normal(self, request: LoginUserNormal):
        return self.login_service.login_normal(request)

    @post("/facebook/?")
    def login_facebook(self, request: LoginUserFacebook):
        return self.login_service.login_facebook(request)

    @post("/email/?")
    def login_email(self, request: LoginUserEmail):
        return self.login_service.login_email(request)
