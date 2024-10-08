class CustomerService:
    def __init__(self) -> None:
        pass
    def fillRequest(self, requestForm):
        if requestForm.get_status() != "INIT":
            print("No request form available!")
            return
        clientRequest = input("Please fill the client's requests:\n")
        requestForm.add_request(clientRequest)
        requestForm.set_status("REQUEST_FILLED")
        print("Request added!")