import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
data = response.json()
print("Fetched Data:", data)
