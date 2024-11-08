import json 


try:
    with open('todos_file.json','r') as f:
        data=json.loads(f.read())
    output=','.join([*data[0]])
    print(output)
    for obj in data:
        output += f"\n{obj['userId']},{obj['id']},{obj['title']},{obj['completed']}"
    print(output)
    with open('todos_in.csv','w') as f:
        f.write(output)
except Exception as rr:
    print(f"Error:{str(rr)}")