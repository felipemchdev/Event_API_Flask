from src.model.configs.connection import DBConnectionHandler
from src.model.entities.inscritos import Inscritos
from .interface.subscribers_repository import SubscribersRepositoryInterface
from sqlalchemy import func, desc
from typing import List, Optional, Tuple

class SubscribersRepository(SubscribersRepositoryInterface):
    def insert(self, name: str, email: str, link: str, evento_id: int) -> None:
        with DBConnectionHandler() as db:
            try:
                new_subscriber = Inscritos(
                    nome=name,
                    email=email, 
                    link=link,
                    evento_id=evento_id
                )
                db.session.add(new_subscriber)
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception

    def select_subscriber(self, email: str, evento_id: int) -> Optional[Inscritos]:
        with DBConnectionHandler() as db:
            data = (
                db.session
                .query(Inscritos)
                .filter(Inscritos.email == email)
                .filter(Inscritos.evento_id == evento_id)
            .one_or_none()
            )
            return data

    def select_subscribers_by_link(self, link: Optional[str], event_id: int) -> List[Inscritos]:
        with DBConnectionHandler() as db:
            query = (
                db.session
                .query(Inscritos)
                .filter(Inscritos.evento_id == event_id)
            )
            
            if link:
                query = query.filter(Inscritos.link == link)
            
            return query.all()

    def get_ranking(self, event_id: int) -> List[Tuple[str, int]]:
        with DBConnectionHandler() as db:
           result = (
            db.session
                .query(Inscritos.link,
                func.count(Inscritos.id).label("total")
                )
                .filter(Inscritos.evento_id == event_id)
                .group_by(Inscritos.link)
                .order_by(desc("total"))
                .all()
           )
           return result