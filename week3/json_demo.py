import json

# A Python dictionary
server = {
    "hostname": "web-server-01",
    "ip": "192.168.1.100",
    "port": 443,
    "status": "running",
    "services": ["nginx", "python", "postgresql"]
}

# Convert dictionary to JSON and save to file
with open("server.json", "w") as f:
    json.dump(server, f, indent=4)

print("JSON file created")

# Read JSON file back
with open("server.json", "r") as f:
    data = json.load(f)

print(f"Server name: {data['hostname']}")
print(f"Server IP: {data['ip']}")
print(f"Services running: {data['services']}")
