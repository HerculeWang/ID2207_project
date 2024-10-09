import sys

class FinancialManager:
    
    def __init__(self) -> None:
        pass
    
    def review_from_SCS(self, requestForm):
        if requestForm.get_status() != "SCS_APPROVE":
            print("No request form available!")
            return
        print("Here are the client's requests:")
        print(requestForm.get_request())
        print("The Senior Customer Service has approved this request.")
        print("Please write your feedback on budget, press Ctrl+Z to end input.")
        feedback = sys.stdin.readlines()
        requestForm.add_comment(''.join(feedback))
        requestForm.set_status("COMMENT_ADDED")
        print("Thank you for your feedback.")
    
    def review_budg_nego(self, budNegForm):
        if budNegForm.get_status() != "REQ_ADDED":
            print("No request form available!")
            return
        print("Here is the budget negotiation request from %s:"%budNegForm.get_name())
        print(budNegForm.get_requirements())
        print("Please negotiate with the client and write down the result of negotiation, press Ctrl+Z to end input.")
        res = sys.stdin.readlines()
        budNegForm.add_result(''.join(res))
        budNegForm.set_status("DECIDED")
        print("Result of negotiation added.")