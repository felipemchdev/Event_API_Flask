from src.model.repositories.interface.subscribers_repository import SubscribersRepositoryInterface
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse

class SubscribersCreator:
    def __init__(self, subscribers_repo: SubscribersRepositoryInterface):
        self.__subscribers_repo = subscribers_repo
    
    def create_subscriber(self, http_request: HttpRequest) -> HttpResponse:
        subscriber_info = http_request.body["data"]
        name = subscriber_info["name"]
        email = subscriber_info["email"]
        link = subscriber_info.get("link")
        evento_id = subscriber_info["evento_id"]

        self.__check_subscriber(email, evento_id)
        self.__insert_subscriber(name, email, link, evento_id)
        return self.__format_response(name, email, link, evento_id)

    def __check_subscriber(self, email: str, evento_id: int) -> None:
        response = self.__subscribers_repo.select_subscriber(email, evento_id)
        if response: 
            raise Exception("Subscriber already exists")

    def __insert_subscriber(self, name: str, email: str, link: str, evento_id: int) -> None:
        self.__subscribers_repo.insert(name, email, link, evento_id)

    def __format_response(self, name: str, email: str, link: str, evento_id: int) -> HttpResponse:
        return HttpResponse(
            body={
                "data": {
                    "type": "Subscriber",
                    "count": 1,
                    "attributes": {
                        "name": name,
                        "email": email,
                        "link": link,
                        "evento_id": evento_id
                    }
                }
            },
            status_code=201
        )