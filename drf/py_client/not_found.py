import requests
endpoint="http://127.0.0.1:8000/api/products/1293203/"
content=requests.get(endpoint)
print(content.json())