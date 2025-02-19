import random
from src.model.entities.eventos_link import EventosLink
from src.model.entities.eventos import Eventos
from src.model.entities.inscritos import Inscritos
from src.model.configs.connection import DBConnectionHandler
from .interface.eventos_link_repository import EventosLinkRepositoryInterface
import string
from typing import Optional, List, Dict, Any
from sqlalchemy.orm import joinedload

class EventosLinkRepository(EventosLinkRepositoryInterface):
    def insert(self, inscrito_id: int, evento_id: int) -> Dict[str, Any]:
        with DBConnectionHandler() as db:
            try:
                link_final = ''.join(random.choices(string.ascii_letters + string.digits, k=7))
                formatted_link = f'mch.connect_{link_final}'

                new_event = EventosLink(inscrito_id=inscrito_id, evento_id=evento_id, link=formatted_link)
                db.session.add(new_event)
                db.session.commit()

                # Get creator's information
                creator = (
                    db.session
                    .query(Inscritos)
                    .filter(Inscritos.id == inscrito_id)
                    .one()
                )

                return {
                    "link": formatted_link,
                    "creator_id": inscrito_id,
                    "creator_name": creator.nome,
                    "event_id": evento_id
                }
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

    def select_link(self, link: str) -> List[Dict[str, Any]]:
        with DBConnectionHandler() as db:
            try:
                data = (
                    db.session
                    .query(EventosLink, Inscritos)
                    .join(Inscritos, EventosLink.inscrito_id == Inscritos.id)
                    .filter(EventosLink.link == link)
                    .all()
                )
                
                return [{
                    "id": link.id,
                    "creator_id": link.inscrito_id,
                    "creator_name": inscrito.nome,
                    "event_id": link.evento_id,
                    "link": link.link
                } for link, inscrito in data]
            except Exception as exception:
                db.session.rollback()
                raise exception

    def select_event_link(self, event_id: int, subscriber_id: int) -> Optional[Dict[str, Any]]:
        with DBConnectionHandler() as db:
            try:
                result = (
                    db.session
                    .query(EventosLink, Inscritos)
                    .join(Inscritos, EventosLink.inscrito_id == Inscritos.id)
                    .filter(
                        EventosLink.evento_id == event_id,
                        EventosLink.inscrito_id == subscriber_id
                    )
                    .first()
                )
                
                if result:
                    link, inscrito = result
                    return {
                        "id": link.id,
                        "creator_id": link.inscrito_id,
                        "creator_name": inscrito.nome,
                        "event_id": link.evento_id,
                        "link": link.link
                    }
                return None
            except Exception as exception:
                db.session.rollback()
                raise exception