

# Creating the class for a delivery truck
class Truck:
    def __init__(self, name, capacity, speed, location, start_time, package_list):
        self.name = name
        self.capacity = capacity
        self.speed = speed
        self.location = location
        self.start_time = start_time
        self.current_time = start_time
        self.package_list = package_list
        self.miles_traveled = 0

    def __str__(self):
        return "Truck %s, capacity: %s, speed: %s, location: %s, start time: %s, current time: %s, package list: %s, " \
               "miles traveled: %s" % (self.name, self.capacity, self.speed, self.location, self.start_time,
                                       self.current_time, self.package_list, self.miles_traveled)
