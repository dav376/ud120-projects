#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
import pandas

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
print(len(enron_data))

#df = pandas.read_pickle("../final_project/final_project_dataset.pkl")

total_poi = 0
have_qualified_salary = 0
known_email_address = 0
missing_total_payments = 0
missing_total_payments_poi = 0
for key, value in enron_data.iteritems():
    if value['poi'] == True:
        total_poi = total_poi + 1
        if value['total_payments'] == 'NaN':
            missing_total_payments_poi = missing_total_payments_poi + 1
    if value['salary'] != 'NaN':
        have_qualified_salary = have_qualified_salary + 1
    if value['email_address'] != 'NaN':
        known_email_address = known_email_address + 1
    if value['total_payments'] == 'NaN':
        missing_total_payments = missing_total_payments + 1


print(enron_data["LAY KENNETH L"]["total_payments"])
print(enron_data["SKILLING JEFFREY K"]["total_payments"])
print(enron_data["FASTOW ANDREW S"]["total_payments"])

print(have_qualified_salary)
print(known_email_address)
print(missing_total_payments)

print(total_poi)
print(missing_total_payments_poi)