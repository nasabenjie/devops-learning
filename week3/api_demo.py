import json
import urllib.request

# Call a free public API that returns random user data
url = "https://jsonplaceholder.typicode.com/users/1"

with urllib.request.urlopen(url) as response:
    data = json.loads(response.read())

print("API Response received")
print(f"Name: {data['name']}")
print(f"Email: {data['email']}")
print(f"City: {data['address']['city']}")
print(f"Company: {data['company']['name']}")
