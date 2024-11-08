import json

try:
    with open('photos_file.json',mode='r') as f:
        data=json.loads(f.read())
    output=','.join([*data[0]])
    print(output)
    for obj in data:
        output += f"\n{obj['albumId']},{obj['id']},{obj['title']},{obj['url']},{obj['thumbnailUrl']}"
    print(output)
    with open('photos_in.csv',mode='w') as f:
        f.write(output)
except Exception as rr:
    print(f"Error:{str(rr)}")