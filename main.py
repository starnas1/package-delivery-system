
import datetime

from DataImport import *
from HashTable import *
from Truck import *

# Instantiate a hash table for all packages
package_hash = HashTable()
import_package_data(package_hash)

# Test package hash table creation
# print(package_hash.search(40))

# Create truck objects
truck1 = Truck('Truck 1', 16, 18, '4001 S 700 E', datetime.timedelta(hours=8, minutes=0, seconds=0),
               [1, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40])
truck2 = Truck('Truck 2', 16, 18, '4001 S 700 E', datetime.timedelta(hours=9, minutes=5, seconds=0),
               [3, 5, 6, 8, 12, 17, 18, 25, 26, 28, 32, 36, 38])
truck3 = Truck('Truck 3', 16, 18, '4001 S 700 E', datetime.timedelta(hours=10, minutes=20, seconds=0),
               [2, 4, 7, 9, 10, 11, 21, 22, 23, 24, 27, 33, 35, 39])


# Creates function to deliver packages. This function calls the determine_nearest_neighbor function to determine the
# nearest package to the current location. The function then updates the truck's current location, current time,
# miles traveled, and package status. The function then adds the package from the truck's package list and removes it
# from the packages to deliver list.
def deliver_packages(truck):
    # Set the current time to the start time of the truck
    truck.current_time = truck.start_time

    # Create a list of packages to be delivered from the truck's package list
    packages_to_deliver = truck.package_list[:]

    # print(packages_to_deliver)
    # print(truck.package_list)

    # Clear the truck's package list in preparation for sorting and delivery
    truck.package_list.clear()

    # print(truck.package_list)
    while packages_to_deliver:
        distance_next_address, next_package = determine_nearest_neighbor(truck.location, packages_to_deliver)
        truck.package_list.append(next_package.package_id)
        # print(truck.package_list)
        packages_to_deliver.remove(next_package.package_id)
        # print(packages_to_deliver)
        truck.location = next_package.address
        truck.miles_traveled += distance_next_address
        truck.current_time += datetime.timedelta(hours=distance_next_address / truck.speed)
        next_package.start_time = truck.start_time
        next_package.delivery_time = truck.current_time


# While there are packages remaining in the packages to deliver list, the algorithm reviews each package and returns
# the nearest package and the distance to that package's address
def determine_nearest_neighbor(current_location, packages_to_deliver):
    distance_next_address = 1000000
    next_package = None
    for package in packages_to_deliver:
        curr_package = package_hash.search(package)
        # print(curr_package)
        package_distance = calculate_distance(get_address(current_location), get_address(curr_package.address))
        # print(package_distance)
        if package_distance <= distance_next_address:
            distance_next_address = package_distance
            # print(distance_next_address)
            next_package = curr_package
            # print(next_package)
    return distance_next_address, next_package


deliver_packages(truck1)
deliver_packages(truck2)

package_to_update = package_hash.search(9)
package_to_update.address = '410 S State St'
package_to_update.zip_code = '84111'

deliver_packages(truck3)


# print(truck1)
# print(truck2)
# print(truck3)
# print(package_hash.search(1))

# The Main class is the entry point and command line interface for the program
class Main:
    print('**********************************************************')
    print('Welcome to the Western Governors University Parcel Service')
    print('**********************************************************')
    print('Please select from the following options:')
    print('1 - Status of an individual package at a specified time')
    print('2 - Status of all packages at a specified time')
    print('3 - Total miles drive by all trucks')
    print('4 - Exit the program')
    print('**********************************************************')
    user_selection = int(input('Please enter your selection: '))

    if user_selection == 1:
        print('You have selected option 1')
        print('Please enter the package ID')
        package_id = int(input('Package ID: '))
        print('Please enter the time you would like to check the status of the package')
        time = input('Time in format (HH:MM:SS): ')

        if package_id > 40:
            print('Package ID does not exist')
        else:

            package = package_hash.search(package_id)
            (h, m, s) = time.split(':')
            converted_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            package.update_status(converted_time)

            print('Package ID: ', package_id)
            print('Time: ', time)
            print('Status: ', package.status)
            if package.status == 'Delivered':
                print('Delivery Time: ', package.delivery_time)
            print('Delivery Deadline: ', package.deadline)
            print('Delivery Address: ', package.address)
            print('Delivery City: ', package.city)
            print('Delivery State: ', package.state)
            print('Delivery Zip: ', package.zip_code)
            print('Package Weight: ', package.weight, 'kgs')

    elif user_selection == 2:
        print('You have selected option 2')
        print('Please enter the time you would like to check the status of all packages')
        time = input('Time in format (HH:MM:SS): ')
        (h, m, s) = time.split(':')
        converted_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

        for i in range(1, package_hash.size + 1):
            package = package_hash.search(i)
            package.update_status(converted_time)
            print('ID:', package.package_id, '| Status:', package.status, end=" ")
            if package.status == 'Delivered':
                print('| Delivery Time:', package.delivery_time, end=" ")
            print('| Deadline:', package.deadline,
                  '| Address:', package.address, '| City:', package.city,
                  '| State:', package.state, '| Zip:', package.zip_code, '| Weight:', package.weight)

    elif user_selection == 3:
        print('You have selected option 3')
        print('Total miles driven by all trucks: ', truck1.miles_traveled + truck2.miles_traveled +
              truck3.miles_traveled)

    elif user_selection == 4:
        print('You have selected option 4')
        print('Thank you for using the Western Governors University Parcel Service')
        print('Goodbye')
        exit(0)
