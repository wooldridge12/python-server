class Customer():
    '''Class'''

    def __init__(self, id, name, address, email = "", password = ""):
        self.id = id
        self.name = name
        self.address = address
        self.email = email
        self.password = password

new_customer = Customer(1, "Hannah Hall", "7002 Chestnut Ct", "www.sdsd.com")
