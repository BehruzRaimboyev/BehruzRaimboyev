import requests

url='http://jsonplaceholder.typicode.com/posts'

res=requests.get(url)

print(res.text)