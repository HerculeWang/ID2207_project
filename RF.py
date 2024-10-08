class RequestForm:
    clientRequest = ""
    comment = ""
    status = ""
    def __init__(self) -> None:
        self.status = "INIT"
    def add_request(self, request):
        self.clientRequest = request
    def add_comment(self, comment):
        self.comment = comment
    def set_status(self, status):
        self.status = status
    def get_request(self):
        return self.clientRequest
    def get_comment(self):
        return self.comment
    def get_status(self):
        return self.status