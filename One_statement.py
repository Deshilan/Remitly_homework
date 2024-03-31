import json
import argparse


def AWS_AWI_check(raw_json):

    #by default, we want to return True
    result = True

    #load json file
    try:
        Loaded_json = json.load(raw_json)
    except:
        print("Loading failed. Check of your file format is JSON.")

    #find field resources
    try:
        resources = Loaded_json['PolicyDocument']['Statement'][0]["Resource"]
    except:
        print("Your file doesn't even contains field Resources.")
        return result

    # check value of "Resource" field
    if (resources) == '*':
        result = False

    print(result)
    return result

#parser- to give possibility to provide variables from command line
parser = argparse.ArgumentParser()
parser.add_argument("Name", default="test.json")
args = parser.parse_args()
file = open(args.Name)

#function calling
AWS_AWI_check(file)