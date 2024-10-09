import sys

class SubTeam:
    name = ""
    
    def __init__(self, name) -> None:
        self.name = name
    
    def get_name(self):
        return self.name
    
    def start_task(self, appForm):
        if appForm.get_status() != "NEEDS_ADDED":
            print("No application form available!")
            return
        print("Here are the client's needs:")
        print(appForm.get_need())
        print("\nPlease decide a plan for the activity, press Ctrl+Z to end input.")
        plan = sys.stdin.readlines()
        appForm.add_plan(''.join(plan))
        print("Plan added.")
        while True:
            ext = input("Would you like to require for extra budget? Type \"Y\" for Yes and \"N\" for No.")
            if ext == "N":
                appForm.set_status("OPEN")
                print("Thank you.")
                break
            elif ext == "Y":
                appForm.set_status("OPEN")
                print("Please write done your extra requirements on budget, press Ctrl+Z to end input.")
                comment = sys.stdin.readlines()
                appForm.add_comment(''.join(comment))
                print("Comment added.")
                break
            else:
                print("Invalid input!")