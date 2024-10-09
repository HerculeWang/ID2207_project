class BudgetNegotiationForm:
    teamName = ""
    status = ""
    requirements = ""
    result = ""
    
    def __init__(self, teamName):
        self.status = "INIT"
        self.teamName = teamName
    
    def set_status(self, status):
        self.status = status
    
    def add_requirements(self, requirements):
        self.requirements = requirements
    
    def add_result(self, result):
        self.result = result
    
    def get_name(self):
        return self.teamName
    
    def get_status(self):
        return self.status
    
    def get_requirements(self):
        return self.requirements
    
    def get_result(self):
        return self.result