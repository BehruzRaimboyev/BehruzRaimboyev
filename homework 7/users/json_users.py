import json

try:
    with open('users_file.json','r') as f:
        data=json.loads(f.read())
    output=','.join([*data[0]])
    print(output)
    for obj in data:
        output += f"\n{obj['id']},{obj['name']},{obj['username']},{obj['email']},{obj['address'],['street'],['suite'],['city'],['zipcode'],['geo'],['lat'],['lng']},{obj['phone']},{obj['website']},{obj['company'],['name'],['catchPhrase'],['bs']}"
    print(output)
    with open('users_in.csv','w') as f:
        f.write(output)
except Exception as rr:
    print(f"Error:{str(rr)}")