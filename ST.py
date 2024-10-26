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
        
        while True:
            ext = input("Would you like to require for extra budget? Type \"Y\" for Yes and \"N\" for No.")
            if ext == "N":
                break
            elif ext == "Y":
                comment = input("Please write done your extra requirement: ")
                appForm.add_comment(comment)
                print("Comment added.")
                break
            else:
                print("Invalid input!")
        
        appForm.set_status("OPEN")
        print("\nPlease decide a plan for the activity, press Ctrl+Z to end input.")
        plan = sys.stdin.readlines()
        appForm.add_plan(''.join(plan))
        print("Plan added.")