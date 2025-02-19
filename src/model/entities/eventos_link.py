from src.model.configs.base import Base
from sqlalchemy import Column, Integer, String, ForeignKey

class EventosLink(Base):
    __tablename__ = "Eventos_link"

    id = Column(Integer, primary_key=True, autoincrement=True)
    inscrito_id = Column(Integer, ForeignKey("Inscritos.id"), nullable=False)
    evento_id = Column(Integer, ForeignKey("Eventos.id"), nullable=False)
    link = Column(String, nullable=True)