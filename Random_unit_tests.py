import string
import random
import json

def AWS_AWI_check(raw_json):

    #by default, we want to return True
    result = True

    #load json file
    try:
        Loaded_json = json.load(raw_json)
    except:
        print("Loading failed. Check if your file format is JSON.")

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

f = open("test.json")
file = json.load(f)
for m in range(1000):
    x = random.randint(1,1000)
    wanted_result = True
    word = ''.join(random.choices(string.ascii_uppercase + string.digits, k=x))
    if word == "*":
        wanted_result = False
    file['PolicyDocument']['Statement'][0]["Resource"] = word
    json_update = open("test.json", "w+")
    json_update.write(json.dumps(file))
    json_update.close()
    f = open("test.json")
    AWS_AWI_check(f)


