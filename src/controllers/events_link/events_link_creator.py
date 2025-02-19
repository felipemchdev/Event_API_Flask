from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse
from src.model.repositories.interface.eventos_link_repository import EventosLinkRepositoryInterface

class EventsLinkCreator:
    def __init__(self, eventos_link_repository: EventosLinkRepositoryInterface) -> None:
        self.__eventos_link_repository = eventos_link_repository

    def create_event_link(self, http_request: HttpRequest) -> HttpResponse:
        try:
            event_link_info = http_request.body["data"]
            inscrito_id = event_link_info["inscrito_id"]
            evento_id = event_link_info["evento_id"]

            link_info = self.__eventos_link_repository.insert(inscrito_id, evento_id)

            return HttpResponse(
                status_code=201,
                body={
                    "data": {
                        "type": "eventos_link",
                        "id": link_info["creator_id"],
                        "attributes": {
                            "creator_id": link_info["creator_id"],
                            "creator_name": link_info["creator_name"],
                            "event_id": link_info["event_id"],
                            "link": link_info["link"]
                        }
                    }
                }
            )
        except Exception as exception:
            return HttpResponse(
                status_code=500,
                body={"errors": [{"title": "Server Error", "detail": str(exception)}]}
            )