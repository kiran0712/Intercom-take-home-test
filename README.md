# Intercom-take-home-test
Files contains intercom take home test solutions

This readme file is to be used as a guide when executing the Intercom take home test python file. Written by: Kiran Chandrasekaran

Objective: We have some customer records in a text file (customers.txt) -- one customer per line, JSON
lines formatted. We want to invite any customer within 100km of our Dublin office for some food
and drinks on us. Write a program that will read the full list of customers and output the names
and user ids of matching customers (within 100km), sorted by User ID (ascending).


There are two main files in this folder:

1.IntercomCustomer.py : This file contains the code that does the following: 
a) fetch the data at the given url, save it into a text file, 
b) read the json data from the file ‘customers.txt’ 
C) calculate distances of each customer in the file with Intercom Dublin office
D) return the customers located within 100km of the Intercom office to be invited for the party 
E) Save the output in a file ‘output.txt’ and print the output

2. IntercomCustomerTest.py: This file contains various test cases to test the code written in the above file.

Requirements to successfully run the code:

1. Python 3 environment: can be downloaded using anaconda environment. The documentation to help with this can be found here: https://docs.anaconda.com/anaconda/install/

2. Suitable IDE to run the code: This code has been developed on Pycharm IDE. This can be found here: https://www.jetbrains.com/pycharm/

3. The files can be run using the command: python <filename>.py in the console, or if using IDE, you can run the files by creating a configuration to run the file each time. 

4. Make sure to check the path of the .txt files to ensure that the system can find the files to write to and read from. 
