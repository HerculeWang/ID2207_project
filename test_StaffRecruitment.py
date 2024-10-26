import sys
import io
from DM import DepartmentManager
from HR import HumanResource
from HRF import HRForm

if __name__ == "__main__":

    origStdout = sys.stdout

    servMan = DepartmentManager("Service Manager")
    humRes = HumanResource()

    hrForm = HRForm("Service Team")
    assert hrForm.get_status() == "INIT"

    # Service Manager applies for additional resource
    sys.stdin = io.StringIO("I\nWe need 1 more employee.")
    sys.stdout = io.StringIO()
    servMan.check_staffing(hrForm)
    assert sys.stdout.getvalue() == "Please check the staff availablity of your team.\nType \"S\" if your team has a sufficient number of employees, and type \"I\" if insufficient: A request for additional resources will be sent to the HR team.\nPlease write down your requests, press Ctrl+Z to end input.\nThe request has been sent.\n"
    assert hrForm.get_status() == "INSUFF"
    assert hrForm.get_shortage() == "We need 1 more employee."

    # Human Resource manages recruitment
    sys.stdin = io.StringIO("Jack, outsourcing")
    sys.stdout = io.StringIO()
    humRes.recruit_staff(hrForm)
    assert sys.stdout.getvalue() == "Here is the request for additional resources from Service Team:\nWe need 1 more employee.\nPlease recruit new employees to solve the shortage of their team.\nAfter finishing recruitment, please write names and types(long-term/outsourcing) of the new employees.\nPress Ctrl+Z to end input.\nNew employees added.\n"
    assert hrForm.get_status() == "RECRUIT"
    assert hrForm.get_solution() == "Jack, outsourcing"

    # Service Manager checks recruitment result
    sys.stdout = io.StringIO()
    servMan.rev_rec_res(hrForm)
    assert sys.stdout.getvalue() == "Here is the recruitment result from HR team:\nJack, outsourcing\n"

    sys.stdout = origStdout
    print("Test Finished.")