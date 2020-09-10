#!/bin/python3
import json
import math
from urllib.request import urlopen

"""
This program has been written to read the customers file from the url provided and calculate the distance of the customers
from the Intercom Dublin office and invite only customers within a 100km radius to a food and drinks party.

Author: Kiran Chandrasekaran
"""


class IntercomCustomer:

    """Declaring the location of Intercom Dublin office and radius of earth"""
    icom_off_lat = math.radians(53.339428)
    icom_off_lon = math.radians(-6.257664)
    radius_earth = 6371

    def customer_distance(self, data):
        """Function to calculate the distance between a given point and
           the co-ordinates of the Intercom Dublin Office using the
           Great Circle distance formula"""
        customer_lat = math.radians(float(data['latitude']))
        customer_long = math.radians(float(data['longitude']))
        del_long = math.fabs(customer_long - self.icom_off_lon)

        """ Great circle distance formula can be found here: 
            https://en.wikipedia.org/wiki/Great-circle_distance """

        eq1 = (math.sin(customer_lat) * math.sin(self.icom_off_lat))
        eq2 = math.cos(customer_lat) * math.cos(self.icom_off_lat) * math.cos(del_long)

        del_sig = math.acos(eq1 + eq2)
        distance = self.radius_earth * del_sig
        return distance

    def customer_filter(self, data):
        """Function to filter list of customers within 100 km
           to the Dublin office, sorted in ascending order of their IDs
           Using lambda to simplify the filter and sort operations"""

        distance = lambda dist: self.customer_distance(dist) < 100
        cust_invited = [cust_invite for cust_invite in data if distance(cust_invite)]
        sort_customer = sorted(cust_invited, key=lambda x: x['user_id'])
        return sort_customer

    def customer_invite(self, cust_file):
        """Function to reads the customer json file, convert it to a iterable list
           and prints the customers to be invited within 100 km radius"""
        customer_list = ""
        with open(cust_file) as custfile:
            for line in custfile:
                customer_list += line.replace('\n', ',')
                if 'str' in line: break

        cust_list = '[' + customer_list[:len(customer_list)] + ']'

        final_cust = self.customer_filter(json.loads(cust_list))
        output_file = '/Volumes/BooksandEverything/intercom/output.txt'

        """Code to ensure that each time the program is run, the output file gets cleared, this is done to reduce 
        redundancy in the file"""
        op_file = open(output_file, 'r+')
        op_file.seek(0)
        op_file.truncate()
        for i in final_cust:
            print(i['user_id'], i['name'])
            with open(output_file, 'a') as output:
                output.write(str(i['user_id'])+" "+i['name']+"\n")
            output.close()


if __name__ == '__main__':
    customerobj = IntercomCustomer()
    customer_file = '/Volumes/BooksandEverything/intercom/customers.txt'
    with open(customer_file, 'w') as customers:
        customers.write(urlopen("https://s3.amazonaws.com/intercom-take-home-test/customers.txt").read().decode('utf-8'))
    customerobj.customer_invite(customer_file)
