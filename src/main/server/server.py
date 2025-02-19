from flask import Flask
from src.main.routes.event import event_route_bp
from src.model.configs.connection import DBConnectionHandler
from src.main.routes.subs import subscribers_route_bp
from src.main.routes.events_link import event_link_route_bp

app = Flask(__name__)

app.register_blueprint(event_route_bp)
app.register_blueprint(subscribers_route_bp)
app.register_blueprint(event_link_route_bp)

with DBConnectionHandler() as db:
    pass

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000, debug=True)