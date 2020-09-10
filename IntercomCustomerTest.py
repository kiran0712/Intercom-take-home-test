import unittest
from urllib.request import urlopen
from IntercomCustomer import IntercomCustomer


class IntercomCustomerTest(unittest.TestCase):

    def test_url(self):
        """Test function to check if the url is valid by matching the status code returned in the
            response header with 200, can also be worked with isurl fucntion from urllib.parse"""
        url = "https://s3.amazonaws.com/intercom-take-home-test/customers.txt"
        url_statuscode = urlopen(url).getcode()
        test_code = url_statuscode == 200
        print(test_code)

    def test_true_customer_list(self):
        """Test function to check list of customers who can be invited by passing list in which customers
        to be invited are present. The function also checks sorting order as the list returned by the function is sorted
        If the customers_invited lsit is unsorted, the test will fail"""
        test_obj = IntercomCustomer()
        customer_list = [{"latitude": "53.1302756", "user_id": 5, "name": "Nora Dempsey", "longitude": "-6.2397222"},
                         {"latitude": "53.4692815", "user_id": 7, "name": "Frank Kehoe", "longitude": "-9.436036"},
                         {"latitude": "52.986375", "user_id": 12, "name": "Christina McArdle", "longitude": "-6.043701"},]
        customers_invited = [{"latitude": "53.1302756", "user_id": 5, "name": "Nora Dempsey", "longitude": "-6.2397222"},
                             {"latitude": "52.986375", "user_id": 12, "name": "Christina McArdle", "longitude": "-6.043701"}]

        self.assertEqual(test_obj.customer_filter(customer_list), customers_invited)

    def test_none_customer_list(self):
        """Test function to check invite function by passing a list with no customers to be invited"""
        test_obj = IntercomCustomer()
        customer_list = [{"latitude": "51.92893", "user_id": 1, "name": "Alice Cahill", "longitude": "-10.27699"},
                         {"latitude": "52.2559432", "user_id": 9, "name": "Jack Dempsey", "longitude": "-7.1048927"},
                         {"latitude": "52.240382", "user_id": 10, "name": "Georgina Gallagher","longitude": "-6.972413"}
                         ]
        customers_invited = []
        self.assertEqual(test_obj.customer_filter(customer_list), customers_invited)

    def test_empty_customer_list(self):
        """Test function to check invite function by passing an empty"""
        test_obj = IntercomCustomer()
        customer_list = []
        customers_invited = []
        self.assertEqual(test_obj.customer_filter(customer_list),  customers_invited)

    def test_invalid_customer_list(self):
        """Test function to check invite function by passing a invalid lsit of customers"""
        test_obj = IntercomCustomer()
        customer_list = [{"latitude": "51.92893", "user_id": 29, "name": "Kiran Chandrasekaran", "longitude": "-10.27699"},
                         {"latitude": "52.8977", "user_id": 37, "name": "Dwight Schrute", "longitude": "-9.1047"}
                         ]
        customers_invited = []
        self.assertEqual(test_obj.customer_filter(customer_list), customers_invited)


if __name__ == '__main__':
    unittest.main()