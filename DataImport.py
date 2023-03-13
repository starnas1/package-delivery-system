
import csv
from Package import Package


# Imports data from the package file
def import_package_data(package_hash):
    package_file = open("csv/Packages.csv")
    package_data = csv.reader(package_file)
    for row in package_data:
        package_id = int(row[0])
        package_address = row[1]
        package_city = row[2]
        package_state = row[3]
        package_zip_code = row[4]
        package_deadline = row[5]
        package_weight = row[6]
        package_status = "At Hub"

        package = Package(package_id, package_address, package_city, package_state, package_zip_code, package_deadline,
                          package_weight, package_status)

        package_hash.insert(package_id, package)


# Imports data from the address file
def get_address(address):
    address_file = open("csv/Address Table.csv")
    address_data = csv.reader(address_file)
    for row in address_data:
        if address in row[1]:
            return int(row[0])


# Calculates the distance between two addresses
def calculate_distance(address1, address2):
    distance_file = open("csv/Distance Data.csv")
    distance_data = list(csv.reader(distance_file))
    distance = distance_data[address1][address2]
    return float(distance)
