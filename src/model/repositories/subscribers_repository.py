from src.model.configs.connection import DBConnectionHandler
from src.model.entities.inscritos import Inscritos
from .interface.subscribers_repository import SubscribersRepositoryInterface

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

    def select_subscriber(self, email: str) -> Inscritos:
        with DBConnectionHandler() as db:
            data = (
                db.session
                .query(Inscritos)
                .filter(Inscritos.email == email)
                .first()
            )
            return data