import os
from CS import CustomerService
from RF import RequestForm
from SCS import SeniorCustomerService
from FM import FinancialManager
from AM import AdministrationManager
from DM import DepartmentManager
from ST import SubTeam
from AF import ApplicationForm

passwdDict = {
    "CS": "CS123",
    "SCS": "SCS123",
    "FM": "FM123",
    "AM": "AM123",
    "SM": "SM123",
    "PM": "PM123",
    "SST": "SST123",
    "PST": "PST123"
}

prompt = """
Welcome, %s!
Please select a workflow:

%s

Enter a number to continue, type "Q" to logout.
"""

csPrompt  = prompt%("Customer Service",         "  1) Fill client's request.")
scsPrompt = prompt%("Senior Customer Service",  "  1) Review form from Customer Service.\n  2) Review form from Administration Manager.")
fmPrompt  = prompt%("Financial Manager",        "  1) Review form from Senior Customer Service.")
amPrompt  = prompt%("Administration Manager",   "  1) Review form from Financial Manager.")
dmTaskPrompt = "  1) Fill an application with client's needs.\n  2) Review plan and comments from sub-team."
stTaskPrompt = "  1) Decide a plan for the activity."


if __name__ == "__main__":
    custServ = CustomerService()
    reqFrom = RequestForm()
    seCusServ = SeniorCustomerService()
    finMan = FinancialManager()
    admMan = AdministrationManager()
    servMan = DepartmentManager("Service Manager")
    prodMan = DepartmentManager("Production Manager")
    servST = SubTeam("Sub-team of Service")
    prodST = SubTeam("Sub-team of production")
    DMs = {"SM": servMan, "PM": prodMan}
    STs = {"SST": servST, "PST": prodST}
    servAppForm = ApplicationForm()
    prodAppForm = ApplicationForm()
    AFs = {"SM": servAppForm, "SST": servAppForm, "PM": prodAppForm, "PST": prodAppForm}

    while True:
        os.system("pause")
        os.system("cls")
        userName = input("Username: ")
        password = input("Password: ")
        if userName not in passwdDict.keys():
            print("User does not exist!")
            continue
        if password != passwdDict[userName]:
            print("Password error!")
            continue
        print("Login Success!")

        os.system("pause")
        os.system("cls")
    
        if userName == "CS":
            # Customer Service
            while True:
                print(csPrompt)
                wkType = input()
                if wkType == "Q":
                    break
                if wkType == "1":
                    # Fill client's request
                    os.system("cls")
                    custServ.fillRequest(reqFrom)
                else:
                    print("Invalid input!")
                os.system("pause")
                os.system("cls")
            os.system("cls")
        
        elif userName == "SCS":
            # Senior Customer Service:
            while True:
                print(scsPrompt)
                wkType = input()
                if wkType == "Q":
                    break
                if wkType == "1":
                    # Review form from Customer Service
                    os.system("cls")
                    seCusServ.reviewFromCS(reqFrom)
                elif wkType == "2":
                    # Review form from Administration Manager
                    os.system("cls")
                    seCusServ.reviewFromAM(reqFrom)
                else:
                    print("Invalid input!")
                os.system("pause")
                os.system("cls")
            os.system("cls")
        
        elif userName == "FM":
            # Financial Manager:
            while True:
                print(fmPrompt)
                wkType = input()
                if wkType == "Q":
                    break
                if wkType == "1":
                    # Review form from Senior Customer Service
                    os.system("cls")
                    finMan.reviewFromSCS(reqFrom)
                else:
                    print("Invalid input!")
                os.system("pause")
                os.system("cls")
            os.system("cls")
        
        elif userName == "AM":
            # Administration Manager:
            while True:
                print(amPrompt)
                wkType = input()
                if wkType == "Q":
                    break
                if wkType == "1":
                    # Review form from Financial Manager
                    os.system("cls")
                    admMan.reviewFromFM(reqFrom)
                else:
                    print("Invalid input!")
                os.system("pause")
                os.system("cls")
            os.system("cls")

        elif userName == "SM" or userName == "PM":
            # Service Manager or Production Manager
            while True:
                user = DMs[userName]
                print(prompt%(user.get_name(), dmTaskPrompt))
                wkType = input()
                if wkType == "Q":
                    break
                if wkType == "1":
                    # Fill an application with client's needs 
                    os.system("cls")
                    user.fill_app(AFs[userName])
                elif wkType == "2":
                    # Review plan and comments from sub-team
                    os.system("cls")
                    user.review_plan(AFs[userName])
                else:
                    print("Invalid input!")
                os.system("pause")
                os.system("cls")
            os.system("cls")
        
        elif userName == "SST" or userName == "PST":
            # Service Sub-team or Production Sub-team
            while True:
                user = STs[userName]
                print(prompt%(user.get_name(), stTaskPrompt))
                wkType = input()
                if wkType == "Q":
                    break
                if wkType == "1":
                    # Decide a plan for the activity.
                    os.system("cls")
                    user.start_task(AFs[userName])
                else:
                    print("Invalid input!")
                os.system("pause")
                os.system("cls")
            os.system("cls")
        