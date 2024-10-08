class ApplicationForm:
    clientNeeds = ""
    plan = ""
    comment = ""
    status = ""
    def __init__(self) -> None:
        self.status = "INIT"
    def add_need(self, clientNeeds):
        self.clientNeeds = clientNeeds
    def add_plan(self, plan):
        self.plan = plan
    def add_comment(self, comment):
        self.comment = comment
    def set_status(self, status):
        self.status = status
    def get_need(self):
        return self.clientNeeds
    def get_plan(self):
        return self.plan
    def get_comment(self):
        return self.comment
    def get_status(self):
        return self.status