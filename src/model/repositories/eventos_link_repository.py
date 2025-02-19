import random
from src.model.entities.eventos_link import EventosLink
from src.model.configs.connection import DBConnectionHandler
from .interface.eventos_link_repository import EventosLinkRepositoryInterface
import string

class EventosLinkRepository(EventosLinkRepositoryInterface):
    def insert(self, inscrito_id: int, evento_id: int) -> str:
        with DBConnectionHandler() as db:
            try:
                link_final = ''.join(random.choices(string.ascii_letters + string.digits, k=7))
                formatted_link = f'evento_{evento_id}/{inscrito_id}_{link_final}'

                new_event = EventosLink(inscrito_id=inscrito_id, evento_id=evento_id, link=formatted_link)
                db.session.add(new_event)
                db.session.commit()

                return formatted_link
            except Exception as exception:
                db.session.rollback()
                raise exception

    def select_event(self, event_name: str) -> Eventos:
        with DBConnectionHandler() as db:
            data = (
                db.session
                .query(Eventos)
                .filter(Eventos.nome == event_name)
                .one_or_none()
            )
            return data