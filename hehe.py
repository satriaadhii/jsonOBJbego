import json 

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

def validation(string):
    data = string
    while True:
        try: 
            jsonObj = json.loads(data)
            return jsonObj
            break
        except Exception as e:
            data = fixer(e, data)

json_awal = {
    "asep" : "asep",
    "foo" : "bar",
    "nani" : "hahay",
}

string = json.dumps(json_awal)
missing_string = string[:-18]
print('missing string:', missing_string)
try:
    jsob = json.loads(missing_string)
    print(jsob)
except Exception as e:
    print(e)
    res = validation(missing_string)
    print(res)
