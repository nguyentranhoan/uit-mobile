from common.controller import get, router, post
from request.create_user import CreateUserNormal
from service.register_service import RegisterService


@router('/register', tags=['register'])
class RegisterController:

    def __init__(self, register_service: RegisterService) -> None:
        super().__init__()
        self.register_service = register_service

    @post("/normal/?")
    def register_normal(self, request: CreateUserNormal):
        return self.register_service.register_normal(request=request)

    @get("/successful/?")
    def validate_user_email(self):
        self.register_service.register_normal_successful()
