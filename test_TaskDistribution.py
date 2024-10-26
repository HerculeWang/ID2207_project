import sys
import io
from DM import DepartmentManager
from ST import SubTeam
from AF import ApplicationForm


if __name__ == "__main__":

    origStdout = sys.stdout

    servMan = DepartmentManager("Service Manager")
    servST = SubTeam("Sub-team of Service")

    appForm = ApplicationForm()
    assert appForm.get_status() == "INIT"

    # Service Manager fills form
    sys.stdin = io.StringIO("The client wants an apple.")
    sys.stdout = io.StringIO()
    servMan.fill_app(appForm)
    assert sys.stdout.getvalue() == "Please fill the client's needs, press Ctrl+Z to end input.\nClient's needs added!\n"
    assert appForm.get_status() == "NEEDS_ADDED"
    assert appForm.get_need() == "The client wants an apple."

    # Service Team decides a plan
    sys.stdin = io.StringIO("Y\n$100\nBuy an apple.")
    sys.stdout = io.StringIO()
    servST.start_task(appForm)
    assert sys.stdout.getvalue() == "Here are the client's needs:\nThe client wants an apple.\nWould you like to require for extra budget? Type \"Y\" for Yes and \"N\" for No.Please write done your extra requirement: Comment added.\n\nPlease decide a plan for the activity, press Ctrl+Z to end input.\nPlan added.\n"
    assert appForm.get_status() == "OPEN"
    assert appForm.get_plan() == "Buy an apple."
    assert appForm.get_comment() == "$100"

    # Service Manager reviews from sub-team
    sys.stdout = io.StringIO()
    servMan.review_plan(appForm)
    assert sys.stdout.getvalue() == "Here is the plan from your sub-team:\nBuy an apple.\nYour sub-team also required for extra budget, here are their requirements:\n$100\n"

    sys.stdout = origStdout
    print("Test Finished.")