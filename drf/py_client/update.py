import requests
endpoint="http://127.0.0.1:8000/api/products/1/update/"
data={
    "title":"Hello world my friend",
    "price":129.99
}
content=requests.put(endpoint,json=data)
print(content.json())