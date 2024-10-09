import sys
class CustomerService:
    def __init__(self) -> None:
        pass
    def fillRequest(self, requestForm):
        if requestForm.get_status() != "INIT":
            print("No request form available!")
            return
        print("Please fill the client's requests, Press Ctrl+Z to end input.")
        clientRequest = sys.stdin.readlines()
        requestForm.add_request(''.join(clientRequest))
        requestForm.set_status("REQUEST_FILLED")
        print("Request added!")