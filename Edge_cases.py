import json
import argparse

import os

def AWS_AWI_check(raw_json):

    #by default, we want to return True
    result = True

    #load json file
    try:
        Loaded_json = json.load(raw_json)
    except:

        print("Loading failed. Check of your file format is JSON.")
        print(result)
        return result

    #find field resources
    try:
        resources = Loaded_json['PolicyDocument']['Statement'][0]["Resource"]
    except:
        print("Your file doesn't even contains field Resources.")
        print(result)
        return result

    # check value of "Resource" field
    if (resources) == '*':
        result = False

    print(result)
    return result

for filename in os.listdir("Edge_cases_test"):
    f = open("Edge_cases_test/" + filename)
    AWS_AWI_check(f)