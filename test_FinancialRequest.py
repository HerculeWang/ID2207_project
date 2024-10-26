import sys
import io
from DM import DepartmentManager
from FM import FinancialManager
from BNF import BudgetNegotiationForm

if __name__ == "__main__":

    origStdout = sys.stdout

    servMan = DepartmentManager("Service Manager")
    finMan = FinancialManager()

    budNegForm = BudgetNegotiationForm("Service Team")
    assert budNegForm.get_status() == "INIT"

    # Service Manager sends a budget negotiation
    sys.stdin = io.StringIO("$100 extra budget.")
    sys.stdout = io.StringIO()
    servMan.send_budg_nego(budNegForm)
    assert sys.stdout.getvalue() == "Please enter your requirements on budget, press Ctrl+Z to end input.\nRequirements added!\n"
    assert budNegForm.get_status() == "REQ_ADDED"
    assert budNegForm.get_requirements() == "$100 extra budget."

    # Financial Manager reviews the budget negotiation
    sys.stdin = io.StringIO("OK.")
    sys.stdout = io.StringIO()
    finMan.review_budg_nego(budNegForm)
    assert sys.stdout.getvalue() == "Here is the budget negotiation request from Service Team:\n$100 extra budget.\nPlease negotiate with the client and write down the result of negotiation, press Ctrl+Z to end input.\nResult of negotiation added.\n"
    assert budNegForm.get_status() == "DECIDED"
    assert budNegForm.get_result() == "OK."

    # Service Manager reviews the result.
    sys.stdout = io.StringIO()
    servMan.review_neg_result(budNegForm)
    assert sys.stdout.getvalue() == "Here is the result of negotiation:\nOK.\n"

    sys.stdout = origStdout
    print("Test Finished.")