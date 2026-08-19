import json

fruits =["apples","pineapple","strawaberry","tomatoes", "kiwi"]
for fruit in fruits:
        print(fruit)


with open("devops_tools.json", "w") as f:
	json.dump(fruits, f, indent=4)
print("saved to JSON")

with open("devops_tools.json", "r") as f:
	data = json.load(f)

print("Read back  from JSON")
print(data)
