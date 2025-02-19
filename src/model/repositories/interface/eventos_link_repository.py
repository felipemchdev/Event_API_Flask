from abc import ABC, abstractmethod
from src.model.entities.eventos_link import EventosLink

class EventosLinkRepositoryInterface(ABC):

    @abstractmethod
    def insert(self, inscrito_id: int, evento_id: int) -> str: pass

    @abstractmethod
    def select_link(self, inscrito_id: int, evento_id: int) -> EventosLink: pass