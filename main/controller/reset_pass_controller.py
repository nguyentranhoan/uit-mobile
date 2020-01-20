from common.controller import get, router, post
from request.create_user import CreateUserNormal
from request.reset_password import ResetPassword
from service.reset_pass_service import ResetPassService


@router('/reset/password', tags=['password'])
class ResetPassController:

    def __init__(self, reset_pass_service: ResetPassService) -> None:
        super().__init__()
        self.reset_pass_service = reset_pass_service

    @post("/?")
    def reset_password(self, request: ResetPassword):
        return self.reset_pass_service.reset_password(request=request)

    @get("/successful/?")
    def reset_password_successful(self):
        self.reset_pass_service.reset_pass_successful()
