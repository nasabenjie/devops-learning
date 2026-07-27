with open("demo.txt", "w") as f:
    f.write("Hello from Python\n")
    f.write("This is line 2\n")
    f.write("This is line 3\n")
print("Files written successfully")


with open("demo.txt","r") as f:
	content = f.read()
print("files contents:")
print(content)
