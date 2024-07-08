#!/usr/bin/env python

import csv

with open('yaml_automation_staging.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)
    #to avoid reading first line of csv i.e: fields name
    next(csv_reader)
    for line in csv_reader:
        print(line)