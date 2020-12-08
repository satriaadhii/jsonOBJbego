import json 

def fixer(e, data):
    if "Expecting ',' delimiter" in str(e):
        fix_data = data+"}"
        #print('fixed delimeter')
    elif "Unterminated string" in str(e):
        fix_data = data+'"'
        #print('fixed unterminated string')
    elif "Expecting value" in str(e):
        fix_data = data+'"null"'
        #print('fixed expecting value')
    elif "Expecting ':' delimiter" in str(e):
        fix_data = data+':'
        #print('fixed ":" delimeter')
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
ilang = string[:-15]
print(ilang)
try:
    jsob = json.loads(ilang)
    print(jsob)
except Exception as e:
    print(e)
    res = validation(ilang)
    print(res)
    



#print("tipe: {} | isi: {} ".format(type(string), string))
#print("ilang: {}\n".format(ilang))

#try:
#    print('try seg')
#    jsonObj = json.loads(ilang)
#
#except Exception as e:
#    print("\nexc seg")
#    print("| error detail: {}".format(e))
#    ilang = checking(e, ilang)
#    print(ilang)
#
#finally:
#    print('\nfin seg')
#    fin = json.loads(ilang)
#    print("tipe: {} | isi: {}".format(type(fin), fin))
