

# Creating the class for a package
class Package:
    def __init__(self, package_id, address, city, state, zip_code, deadline, weight, status):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline = deadline
        self.weight = weight
        self.status = status
        self.start_time = None
        self.delivery_time = None

    def __str__(self):
        return "Package: %s, Address: %s, City: %s, State: %s, Zip Code: %s, Deadline: %s, Weight: %s, Status: %s, " \
               "Start Time: %s, Delivery Time: %s" % (self.package_id, self.address, self.city, self.state,
                                                      self.zip_code, self.deadline, self.weight, self.status,
                                                      self.start_time, self.delivery_time)

    # Creating a function for updating the status of a package
    def update_status(self, current_time):
        if self.delivery_time < current_time:
            self.status = "Delivered"
        elif self.start_time < current_time:
            self.status = "En Route"
        else:
            self.status = "At Hub"
