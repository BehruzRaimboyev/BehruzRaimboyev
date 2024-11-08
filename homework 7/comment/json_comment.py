import json

try:
    with open('comment_file.json','r') as f:
        data=json.loads(f.read())
    output=','.join([*data[0]])
    print(output)
    for obj in data:
        output +=f"\n{obj['postId']},{obj['id']},{obj['name']},{obj['email']},{obj['body']}"
    print(output)
    with open('comment_in.csv',mode='w') as f:
        f.write(output)
except Exception as ex:
    print(f'Error:{str(ex)}')
    