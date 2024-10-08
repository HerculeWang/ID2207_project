class DepartmentManager:
    name = ""
    def __init__(self, name):
        self.name = name
    def get_name(self):
        return self.name
    def fill_app(self, appForm):
        if appForm.get_status() != "INIT":
            print("No application form available!")
            return
        clientNeed = input("Please fill the client's needs:\n")
        appForm.add_need(clientNeed)
        appForm.set_status("NEEDS_ADDED")
        print("Client's needs added!")
    def review_plan(self, appForm):
        if appForm.get_status() != "OPEN":
            print("No application form available!")
            return
        print("Here is the plan from your sub-team:")
        print(appForm.get_plan())
        if appForm.get_comment() != "":
            print("Your sub-team also required for extra budget, here are their requirements:")
            print(appForm.get_comment())
