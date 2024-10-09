class HRForm:
    teamName = ""
    status = ""
    shortage = ""
    solution = ""
    
    def __init__(self, teamName) -> None:
        self.status = "INIT"
        self.teamName = teamName
    
    def set_status(self, status):
        self.status = status
    
    def add_shortage(self, shortage):
        self.shortage = shortage
    
    def add_solution(self, solution):
        self.solution = solution
    
    def get_name(self):
        return self.teamName
    
    def get_status(self):
        return self.status
    
    def get_shortage(self):
        return self.shortage
    
    def get_solution(self):
        return self.solution