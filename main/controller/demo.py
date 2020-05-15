from common.controller import get, router, post
from service.demo import DemoService


# i makes some changes here to check as flag

@router('/demos', tags=['demo'])
class DemoController:

    def __init__(self, demo_service: DemoService) -> None:
        super().__init__()
        self.demo_service = demo_service

    @get("/?")
    def list(self):
        return self.demo_service.list()
