import xml.etree.ElementTree as ET
input = '''<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Riccardo</name>
        </user>
        <user x="7">
            <id>004</id>
            <name>Felix</name>
        </user>
    </users>
</stuff>'''
stuff = ET.fromstring(input)
#print(stuff[:])
out = ET.tostring(stuff, encoding='unicode')
print(input)
print('\n\n')
print(out)
print('\n\n')
list=stuff.findall('users/user')
print('list: ', list)
print('\n\n')
users_nr = len(list)
print(f'Number of users found: {users_nr}')
print('\n\n')
for item in list :
    name=item.find('name').text
    print(f'Name: {name}')
    id=item.find('id').text
    print(f'ID: {id}')
    attr=item.get('x')
    print(f'Attribute: {attr}')
