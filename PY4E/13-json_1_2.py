#Exercise combining the json1 and json2 tutorials about how json structurs the data 
import json #always needed in order to work with json files amd structurs

#Let's create some sample data ### SIMPLE STUCTURE = 1 ELEMENT WITH SUB-ARGUMENTS == PYTHON DICTIONARY style, key value pairs:

### 1 ### data in actual json format
data = '''
{
    "name" : "Rik",
    "phone" : {
        "type" : "int",
        "number" : "+393404843199"
    },
    "email" : {
        "hide" : "yes"
    }
}'''

### 2 ### load the data via the json library
myjsondata = json.loads(data)

### 3 ### select and print the data of interest
print('### 1 ###')
print('Name: ', myjsondata["name"])
print('Phone: ', myjsondata["phone"]["number"])

# or assign variables and then print - also possible to extract keys...
name = myjsondata["name"]
phone = myjsondata["phone"]
my_keys = list(myjsondata.keys())

print('### 2 ###')
print(f'{my_keys[0]}: ', name)

#NOW, LET'S CREATE A MORE COMPLEX STRUCTURE IN THE STYLE OF A PYTHON LIST CONTAINING DICTIONARIES

data2 = '''
[
    {
       "Id" : "726",
       "Name" : "Riccardo",
       "Surname" : "Pavia",
       "Nationality" : "Azerbaijanian"
    },
    {
        "Id" : "347",
        "Name" : "Bertoldo",
        "Surname" : "Da Pavia",
        "Nationality" : "Regno delle due Sicilie"
    }
]'''

myjsondata2 = json.loads(data2)

all_keys = []

# for index in myjsondata2 :
#     sec = index.keys()
#     #sec = myjsondata2[0].keys()
#     keys = list(sec)
#     all_keys.append(keys)
#
print('User Count: ', len(myjsondata2))

for item in myjsondata2 :
    sec = item.keys()
    keys = list(sec)
    all_keys.append(keys)
    print(all_keys[0], item["Id"])
    print(item["Name"])
    print(item["Surname"])
    print(item["Nationality"])

#print(all_keys[0][0])
#print(all_keys[1][0])
