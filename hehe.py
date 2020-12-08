import json 

# when you found another converting problem, just add in here
def fixer(e, data):
    if "Expecting ',' delimiter" in str(e):
        fix_data = data+"}"
    elif "Unterminated string" in str(e):
        fix_data = data+'"'
    elif "Expecting value" in str(e):
        fix_data = data+'"null"'
    elif "Expecting ':' delimiter" in str(e):
        fix_data = data+':'
    elif "Expecting property name enclosed in double quotes" in str(e):
        fix_data = data+'"' 
    else:
        fix_data = "unfix"
    return fix_data

# function to validate the json string, and fix it over and over again until able to convert to jsonObj
def validation(string):
    data = string
    while True:
        try: 
            jsonObj = json.loads(data)
            return jsonObj
            break
        except Exception as e:
            data = fixer(e, data)

js = {
    "asep" : "asep",
    "foo" : "bar",
    "nani" : "hahay",
}

string = json.dumps(js) # convert json object to json string, its a should when in the future u need to send a json.
missing_string = string[:-18] # this variable used to test the function by define how much char is missing. 

print('missing string:', missing_string) # we print the rest string

try:
    jsob = json.loads(missing_string)
    print(jsob)
except Exception as e:
    print(e)
    res = validation(missing_string)
    print(res)
