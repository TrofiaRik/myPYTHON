import json
data = '''{
    "name" : "Rick",
    "phone" : {
        "type" : "intl",
        "number" : "+39 355 355 024"
    },
    "email" : {
        "hide" : "yes"
    }
}'''
infos = json.loads(data)
print('Name:', infos["name"])
print('Hide:', infos["email"]["hide"])
print(infos)

input2 = '''[
    {"id" : "001",
     "x" : "2",
     "name" : "chuck"
    },
    {"id" : "009",
     "x" : "7",
     "name" : "Chuck"
    }
]'''
infos2 = json.loads(input2)
print(infos2)
print(f'Records Count: {len(infos2)}')
for el in infos2:
    print('id:',el['id'])
    print('x:',el['x'])
    print('name:',el['name'])
