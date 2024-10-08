class FinancialManager:
    def __init__(self) -> None:
        pass
    def reviewFromSCS(self, requestForm):
        if requestForm.get_status() != "SCS_APPROVE":
            print("No request form available!")
            return
        print("Here are the client's requests:")
        print(requestForm.get_request())
        print("The Senior Customer Service has approved this request, please write your feedback on budget:")
        feedback = input()
        requestForm.add_comment(feedback)
        requestForm.set_status("COMMENT_ADDED")
        print("Thank you for your feedback.")