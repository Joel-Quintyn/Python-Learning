import simplejson as json
import os

# newfile = open("./files/newfile.txt", "w+")
# string = "This content will be written to a text file"
# newfile.write(string)
# print(string)

if os.path.isfile("./files/ages.json") and os.stat("./files/ages.json").st_size != 0:
    old_file = open("./files/ages.json", "r+")
    data = json.loads(old_file.read())
    print(f"Current age is {data['age']} -- adding a year.")
    data["age"] += 1
    print(f"New age is {data['age']}")
else:
    old_file = open("./files/ages.json", "w+")
    data = {"name": "Joel", "age": 19}
    print(f"File not found, setting default data to -- {data}")

old_file.seek(0)
old_file.write(json.dumps(data))
