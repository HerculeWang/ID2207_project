class SeniorCustomerService:
    def __init__(self) -> None:
        pass
    def reviewFromCS(self, requestForm):
        if requestForm.get_status() != "REQUEST_FILLED":
            print("No request form available!")
            return
        print("Here are the client's requests:")
        print(requestForm.get_request())
        while True:
            print("Please type \"A\" to approve, or \"D\" to decilne.")
            revResult = input()
            if revResult == "A":
                requestForm.set_status("SCS_APPROVE")
                print("Request approved.")
                break
            elif revResult == "D":
                requestForm.set_status("SCS_DECLINE")
                print("Request declined.")
                break
            else:
                print("Invalid input!")
    def reviewFromAM(self, requestForm):
        if requestForm.get_status() not in ["AM_APPROVE", "AM_DECLINE"]:
            print("No request form available!")
            return
        print("Here is the decision from Adminstration Manager:")
        print("%s"%("Approve." if requestForm.get_status() == "AM_APPROVE" else "Decline."))
        print("Please inform the client.")