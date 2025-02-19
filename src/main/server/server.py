from flask import Flask
from src.main.routes.events import events_route_bp
from src.main.routes.subscribers import subscribers_route_bp
from src.main.routes.events_link import events_link_route_bp
from src.model.configs.connection import DBConnectionHandler

app = Flask(__name__)

app.register_blueprint(events_route_bp)
app.register_blueprint(subscribers_route_bp)
app.register_blueprint(events_link_route_bp)

with DBConnectionHandler() as db:
    pass

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000, debug=True)