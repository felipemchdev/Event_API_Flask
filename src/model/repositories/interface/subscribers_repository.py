from abc import ABC, abstractmethod
from src.model.entities.inscritos import Inscritos


class SubscribersRepositoryInterface(ABC):
    
    @abstractmethod
    def insert(self, name: str, email: str, link: str, evento_id: int) -> None: pass


    @abstractmethod
    def select_subscriber(self, email: str) -> Inscritos: pass