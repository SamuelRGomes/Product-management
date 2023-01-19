# import requests
# endpoint="http://127.0.0.1:8000/api/"
# content=requests.post(endpoint,json={"title":"Hello World"})
# print(content.json())

import dotenv
import os
dotenv.read_dotenv()
print(str(os.environ.get('APPLICATION_ID')))
print(str(os.environ.get('API_KEY')))
# print(content.status_code)
# print(content.headers)
# print(content.text)
