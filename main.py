import os

from CS import CustomerService
from RF import RequestForm
from SCS import SeniorCustomerService
from FM import FinancialManager
from AM import AdministrationManager
from DM import DepartmentManager
from ST import SubTeam
from AF import ApplicationForm
from HR import HumanResource
from HRF import HRForm
from BNF import BudgetNegotiationForm

passwdDict = {
    "CS" : "CS123",
    "SCS": "SCS123",
    "FM" : "FM123",
    "AM" : "AM123",
    "SM" : "SM123",
    "PM" : "PM123",
    "SST": "SST123",
    "PST": "PST123",
    "HR" : "HR123"
}

prompt = """
Welcome, %s!
Please select a workflow:

%s

Enter a number to continue, type "Q" to logout.
"""

csPrompt  = prompt%("Customer Service",         "  1) Fill client's request.")
scsPrompt = prompt%("Senior Customer Service",  "  1) Review form from Customer Service.\n  2) Review form from Administration Manager.")
fmPrompt  = prompt%("Financial Manager",        "  1) Review form from Senior Customer Service.\n  2) Review budget negotiation from Service Manager.\n  3) Review budget negotiation from Production Manager.")
amPrompt  = prompt%("Administration Manager",   "  1) Review form from Financial Manager.")
hrPrompt  = prompt%("Human Resource Team",      "  1) Manage recruitment for the Service Team.\n  2) Manage recruitment for the Production Team.")
dmTaskPrompt = "  1) Fill an application with client's needs.\n  2) Review plan and comments from sub-team.\n  3) Manage staffing issues.\n  4) Review recruitment result from HR team.\n  5) Send a budget negotiation to Financail Manager.\n  6) Review the negotiation result from Finicail Manager."
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
    humRes = HumanResource()
    servHrForm = HRForm("Service Team")
    prodHrForm = HRForm("Production Team")
    HRFs = {"SM": servHrForm, "PM": prodHrForm}
    servBudNegForm = BudgetNegotiationForm("Service Team")
    prodBudNegForm = BudgetNegotiationForm("Production Team")
    BNFs = {"SM": servBudNegForm, "PM": prodBudNegForm}

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
                    finMan.review_from_SCS(reqFrom)
                elif wkType == "2":
                    # Review budget negotiation from Service Manager
                    os.system("cls")
                    finMan.review_budg_nego(BNFs["SM"])
                elif wkType == "3":
                    # Review budget negotiation from Production Manager.
                    os.system("cls")
                    finMan.review_budg_nego(BNFs["PM"])
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
                elif wkType == "3":
                    # Manage staffing issues
                    os.system("cls")
                    user.check_staffing(HRFs[userName])
                elif wkType == "4":
                    # Review recruitment result from HR team
                    os.system("cls")
                    user.rev_rec_res(HRFs[userName])
                elif wkType == "5":
                    # Send a budget negotiation to Financail Manager
                    os.system("cls")
                    user.send_budg_nego(BNFs[userName])
                elif wkType == "6":
                    # Review the negotiation result from Finicail Manager
                    os.system("cls")
                    user.review_neg_result(BNFs[userName])
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
        
        elif userName == "HR":
            # Human Resource
            while True:
                print(hrPrompt)
                wkType = input()
                if wkType == "Q":
                    break
                if wkType == "1":
                    # Manage recruitment for the Service Team
                    os.system("cls")
                    humRes.recruit_staff(HRFs["SM"])
                elif wkType == "2":
                    # Manage recruitment for the Production Team
                    os.system("cls")
                    humRes.recruit_staff(HRFs["PM"])
                else:
                    print("Invalid input!")
                os.system("pause")
                os.system("cls")
            os.system("cls")