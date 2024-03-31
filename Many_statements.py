import json
import argparse

my_file = open("Test_many_policies.json")


def AWS_AWI_check_multi_stat(raw_json, stat_number):
    #by default, we want to return True
    result = True

    #check, if the second var type is correct
    if type(stat_number) != int:
        print("Please, provide an integer as second var.")

    #load json file
    try:
        Loaded_json = json.load(raw_json)
    except:
        print("Loading failed. Check of your file format is JSON.")
        return None

    print(len(Loaded_json['PolicyDocument']['Statement']))
    if len(Loaded_json['PolicyDocument']['Statement']) - 1 < stat_number:
        raise ValueError('Index out of range.')

    #find field resources
    try:
        resources = Loaded_json['PolicyDocument']['Statement'][stat_number]["Resource"]
    except:
        print("Your file doesn't even contains field Resources.")
        return None

    #check value of "Resource" field
    if (resources) == '*':
        result = False

    print(result)
    return result

#parser- to give possibility to provide variables from command line
parser = argparse.ArgumentParser()
parser.add_argument("--File", type=str, default="test.json")
parser.add_argument("--Stat", type = int, default="0")

args = parser.parse_args()
file = open(args.File)

#function calling
AWS_AWI_check_multi_stat(file, args.Stat)