import requests
id=input('Enter the id of the product you are looking for \n')
endpoint=f"http://127.0.0.1:8000/api/products/{id}/"
content=requests.get(endpoint)
print(content.json())