class HttpRequest:
    def __init__(self, body: dict = None, params: dict = None) -> None:
        self.params = params
        self.body = body