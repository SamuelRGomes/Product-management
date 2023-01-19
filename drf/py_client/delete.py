import requests
product_id=input("What is the product id you want to use?\n")
try:
    product_id=int(product_id)
except: 
    product_id=None
    print(f"{product_id} is not a valid id")
if product_id:
    endpoint=f"http://127.0.0.1:8000/api/products/{product_id}/delete/"


content=requests.delete(endpoint)
print(content.status_code,content.status_code==204)