from src.model.repositories.interface.subscribers_repository import SubscribersRepositoryInterface
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse
from src.model.entities.inscritos import Inscritos
from typing import List, Tuple, Any

class SubscribersManager:
    def __init__(self, subscribers_repo: SubscribersRepositoryInterface):
        self.__subscribers_repo = subscribers_repo

    def get_subscribers_by_link(self, http_request: HttpRequest) -> HttpResponse:
        try:
            event_id = http_request.params["event_id"]
            link = http_request.params.get("link")  # Using get() to make link optional
            subs = self.__subscribers_repo.select_subscribers_by_link(link, event_id)
            return self.__format_subs_by_link(subs)
        except KeyError as e:
            return HttpResponse(
                body={"error": f"Missing required parameter: {str(e)}"},
                status_code=400
            )
        except Exception as e:
            return HttpResponse(
                body={"error": str(e)},
                status_code=500
            )

    def get_event_ranking(self, http_request: HttpRequest) -> HttpResponse:
        try:
            event_id = http_request.params["event_id"]
            event_ranking = self.__subscribers_repo.get_ranking(event_id)
            return self.__format_event_ranking(event_ranking)
        except KeyError as e:
            return HttpResponse(
                body={"error": f"Missing required parameter: {str(e)}"},
                status_code=400
            )
        except Exception as e:
            return HttpResponse(
                body={"error": str(e)},
                status_code=500
            )

    def __format_subs_by_link(self, subs: List[Inscritos]) -> HttpResponse:
        formatted_subscribers = []
        for sub in subs:
            try:
                formatted_subscribers.append({
                    "type": "subscriber",
                    "id": sub.id,
                    "attributes": {
                        "name": sub.nome,  
                        "email": sub.email,
                        "link": sub.link
                    }
                })
            except AttributeError as e:
                return HttpResponse(
                    body={"error": f"Invalid subscriber data: {str(e)}"},
                    status_code=500
                )
        return HttpResponse(
            body={
                "data": {
                    "type": "Subscribers",
                    "count": len(formatted_subscribers),
                    "subscribers": formatted_subscribers
                }
            },
            status_code=200
        )

    def __format_event_ranking(self, event_ranking: List[Tuple[str, int]]) -> HttpResponse:
        formatted_event_ranking = []
        for position in event_ranking:
            try:
                formatted_event_ranking.append({
                    "link": position[0],  
                    "total_subscribers": position[1]
                })
            except (IndexError, TypeError) as e:
                return HttpResponse(
                    body={"error": f"Invalid ranking data: {str(e)}"},
                    status_code=500
                )
        return HttpResponse(
            body={
                "data": {
                    "type": "Ranking",
                    "count": len(formatted_event_ranking),
                    "ranking": formatted_event_ranking
                }
            },
            status_code=200
        )