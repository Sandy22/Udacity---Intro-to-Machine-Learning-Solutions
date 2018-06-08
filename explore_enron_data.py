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

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
# How many data points (people) are in the dataset?
print (len(enron_data.keys()))
print (len(enron_data.values()[0]))
count = 0
for i in enron_data.keys():
    if enron_data[i]["poi"] == True:
       count += 1
print "POIs: "
print count

# How Many POIs Exist?
namesfile = open("../final_project/poi_names.txt", "r")
names = namesfile.readlines()
print len(names[2:])
namesfile.close()

print enron_data.keys()

# What is the total value of the stock belonging to James Prentice?
print enron_data["PRENTICE JAMES"]["total_stock_value"]

# How many email messages do we have from Wesley Colwell to persons of interest?
print enron_data["COLWELL WESLEY"]
print enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]

# Whats the value of stock options exercised by Jeffrey Skilling?
print enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]

# How much money did that person get?
print enron_data["LAY KENNETH L"]["total_payments"]

# How many folks in this dataset have a quantified salary?
# What about a known email address?
countNaNSalary = 0
countKnownEmail = 0
for i in enron_data.keys():
    print enron_data[i]["salary"]
    if enron_data[i]["salary"] != "NaN":
        countNaNSalary += 1
    if enron_data[i]["email_address"] != "NaN":
        countKnownEmail += 1
print countNaNSalary
print countKnownEmail

# How many people in the E+F dataset (as it currently exists) have NaN for their total payments?
# What percentage of people in the dataset as a whole is this?
count = 0
for i in enron_data.keys():
    if enron_data[i]["total_payments"] == "NaN":
       count += 1
print count
print len(enron_data.keys())
print count*100/len(enron_data.keys())

# How many POIs in the E+F dataset have NaN for their total payments?
# What percentage of POIs as a whole is this?
count = 0
for i in enron_data.keys():
    if enron_data[i]["poi"] == True and enron_data[i]["total_payments"] == "NaN":
            count += 1
print count
print len(enron_data.keys())
print count*100/len(enron_data.keys())
