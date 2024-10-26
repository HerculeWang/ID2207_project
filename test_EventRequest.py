import sys
import io
from CS import CustomerService
from SCS import SeniorCustomerService
from FM import FinancialManager
from AM import AdministrationManager
from RF import RequestForm


if __name__ == "__main__":

    origStdout = sys.stdout

    custServ = CustomerService()
    seCusServ = SeniorCustomerService()
    finMan = FinancialManager()
    admMan = AdministrationManager()

    reqFrom = RequestForm()
    assert reqFrom.get_status() == "INIT"

    # Customer Service fills the request form
    sys.stdin = io.StringIO("I want an apple.")
    sys.stdout = io.StringIO()
    custServ.fillRequest(reqFrom)
    assert sys.stdout.getvalue() == "Please fill the client's requests, Press Ctrl+Z to end input.\nRequest added!\n"
    assert reqFrom.get_status() == "REQUEST_FILLED"
    assert reqFrom.get_request() == "I want an apple."

    # Senior Customer Service reviews form
    sys.stdin = io.StringIO("A")
    sys.stdout = io.StringIO()
    seCusServ.reviewFromCS(reqFrom)
    assert sys.stdout.getvalue() == "Here are the client's requests:\nI want an apple.\nPlease type \"A\" to approve, or \"D\" to decilne.Request approved.\n"
    assert reqFrom.get_status() == "SCS_APPROVE"

    # Financial Manager adds comment
    sys.stdin = io.StringIO("I agree.")
    sys.stdout = io.StringIO()
    finMan.review_from_SCS(reqFrom)
    assert sys.stdout.getvalue() == "Here are the client's requests:\nI want an apple.\nThe Senior Customer Service has approved this request.\nPlease write your feedback on budget, press Ctrl+Z to end input.\nThank you for your feedback.\n"
    assert reqFrom.get_status() == "COMMENT_ADDED"
    assert reqFrom.get_comment() == "I agree."

    # Administration Manager reviews form
    sys.stdin = io.StringIO("A")
    sys.stdout = io.StringIO()
    admMan.reviewFromFM(reqFrom)
    assert sys.stdout.getvalue() == "These are the client's requests:\nI want an apple.\n\nThis is feedback from Financial Manager:\nI agree.\n\nPlease type \"A\" to approve, or \"D\" to decilne: Request approved.\n"
    assert reqFrom.get_status() == "AM_APPROVE"

    # Senior Customer Service review form
    sys.stdout = io.StringIO()
    seCusServ.reviewFromAM(reqFrom)
    assert sys.stdout.getvalue() == "Here is the decision from Adminstration Manager:\nApprove.\nPlease inform the client.\n"

    sys.stdout = origStdout
    print("Test Finished.")