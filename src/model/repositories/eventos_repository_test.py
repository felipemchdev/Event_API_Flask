from src.model.repositories.eventos_repository import EventosRepository

def test_insert_eventos():
    event_name = "eventoTeste2"
    event_repo = EventosRepository()
    
    event_repo.insert(event_name)