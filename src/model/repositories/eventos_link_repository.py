import random
from src.model.entities.eventos_link import EventosLink
from src.model.entities.eventos import Eventos
from src.model.configs.connection import DBConnectionHandler
from .interface.eventos_link_repository import EventosLinkRepositoryInterface
import string
from typing import Optional, List

class EventosLinkRepository(EventosLinkRepositoryInterface):
    def insert(self, inscrito_id: int, evento_id: int) -> str:
        with DBConnectionHandler() as db:
            try:
                link_final = ''.join(random.choices(string.ascii_letters + string.digits, k=7))
                formatted_link = f'nlw.connect_{link_final}'

                new_event = EventosLink(inscrito_id=inscrito_id, evento_id=evento_id, link=formatted_link)
                db.session.add(new_event)
                db.session.commit()

                return formatted_link
            except Exception as exception:
                db.session.rollback()
                raise exception

    def select_event(self, event_name: str) -> Optional[Eventos]:
        with DBConnectionHandler() as db:
            data = (
                db.session
                .query(Eventos)
                .filter(Eventos.nome == event_name)
                .one_or_none()
            )
            return data

    def select_link(self, link: str) -> List[EventosLink]:
        with DBConnectionHandler() as db:
            try:
                data = (
                    db.session
                    .query(EventosLink)
                    .filter(EventosLink.link == link)
                    .all()
                )
                return data
            except Exception as exception:
                db.session.rollback()
                raise exception

    def select_event_link(self, event_id: int, subscriber_id: int) -> Optional[EventosLink]:
        with DBConnectionHandler() as db:
            try:
                data = (
                    db.session
                    .query(EventosLink)
                    .filter(
                        EventosLink.evento_id == event_id,
                        EventosLink.inscrito_id == subscriber_id
                    )
                    .one_or_none()
                )
                return data
            except Exception as exception:
                db.session.rollback()
                raise exception