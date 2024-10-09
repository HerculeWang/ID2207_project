import sys

class HumanResource:
    
    def __init__(self) -> None:
        pass
    
    def recruit_staff(self, hrForm):
        if hrForm.get_status() != "INSUFF":
            print("No application form available!")
            return
        print("Here is the request for additional resources from %s:"%hrForm.get_name())
        print(hrForm.get_shortage())
        print("Please recruit new employees to solve the shortage of their team.")
        print("After finishing recruitment, please write names and types(long-term/outsourcing) of the new employees.")
        print("Press Ctrl+Z to end input.")
        solu = sys.stdin.readlines()
        hrForm.add_solution(''.join(solu))
        hrForm.set_status("RECRUIT")
        print("New employees added.")
