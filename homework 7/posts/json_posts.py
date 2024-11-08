import json

try:
    with open('posts_file.json','r') as f:
        data=json.loads(f.read())
    output=','.join([*data[0]])
    print(output)
    for obj in data:
        output +=f"\n{obj['userId']},{obj['id']},{obj['title']},{obj['body']}"
    print(output)
    with open('post_in.csv',mode='w') as f:
        f.write(output)
except Exception as ex:
    print(f'Error:{str(ex)}')
