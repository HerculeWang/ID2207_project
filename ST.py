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
        print("\nPlease decide a plan for the activity:")
        plan = input()
        appForm.add_plan(plan)
        print("Plan added.")
        while True:
            print("Would you like to require for extra budget? Type \"Y\" for Yes and \"N\" for No.")
            ext = input()
            if ext == "N":
                appForm.set_status("OPEN")
                print("Thank you.")
                break
            elif ext == "Y":
                appForm.set_status("OPEN")
                print("Please write done your extra requirements on budget:")
                comment = input()
                appForm.add_comment(comment)
                print("Comment added.")
                break
            else:
                print("Invalid input!")