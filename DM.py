import sys
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
        print("Please fill the client's needs, press Ctrl+Z to end input.")
        clientNeed = sys.stdin.readlines()
        appForm.add_need(''.join(clientNeed))
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
    def check_staffing(self, hrForm):
        if hrForm.get_status() != "INIT":
            print("No application form available!")
            return
        print("Please check the staff availablity of your team.")
        while True:
            avail = input("Type \"S\" if your team has a sufficient number of employees, and type \"I\" if insufficient: ")
            if avail == "S":
                hrForm.set_status("SUFF")
                print("Thank you.")
                break
            elif avail == "I":
                hrForm.set_status("INSUFF")
                print("A request for additional resources will be sent to the HR team.")
                print("Please write down your requests, press Ctrl+Z to end input.")
                req = sys.stdin.readlines()
                hrForm.add_shortage(''.join(req))
                print("The request has been sent.")
                break
            else:
                print("Invalid input!")
    def rev_rec_res(self, hrForm):
        if hrForm.get_status() != "RECRUIT":
            print("No application form available!")
            return
        print("Here is the recruitment result from HR team:")
        print(hrForm.get_solution())