import requests
headers={'Authorization': 'Bearer 93187851db5ac21c05b2f206ecd21e42a00e0958'}
endpoint="http://127.0.0.1:8000/api/products/"
data={
    'title':'this field is done',
    'price':32.99
}
content=requests.post(endpoint,json=data,headers=headers)
print(content.json())