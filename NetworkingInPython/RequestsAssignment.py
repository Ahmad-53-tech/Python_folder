import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
print(response.status_code)
data = response.json()
title = data["title"]
completed = data["completed"]
if completed:
    print(f"{title} has been completed")
else:
    print(f"{title} is still pending")