class AdministrationManager:
    def __init__(self) -> None:
        pass
    def reviewFromFM(self, requestForm):
        if requestForm.get_status() != "COMMENT_ADDED":
            print("No request form available!")
            return
        print("These are the client's requests:\n%s\n"%requestForm.get_request())
        print("This is feedback from Financial Manager:\n%s\n"%requestForm.get_comment())
        while True:
            revResult = input("Please type \"A\" to approve, or \"D\" to decilne: ")
            if revResult == "A":
                requestForm.set_status("AM_APPROVE")
                print("Request approved.")
                break
            elif revResult == "D":
                requestForm.set_status("AM_DECLINE")
                print("Request declined.")
                break
            else:
                print("Invalid input!")