import json

with open("demo.json") as jsonfile:
    # demo = json.load(jsonfile)
    # print(demo)
    # print(type(demo))
    read_file = jsonfile.read()
    demo = json.loads(read_file)
    print(demo)
    print(type(demo))


# Create a Python dict
# with info about
# favour film/tx series

film = {
    "name": "Firefly",
    "seasons": 1,
    "film_sequel": True,
    "Production_company": "Fox"
}

# film_json_string = json.dumps(film)
# print(film_json_string)
# print(type(film_json_string))
#
# with open("shrek.json", "w") as shrekfile:
#     shrekfile.write(film_json_string)

with open("shrek2.json", "w") as shrekfile:
    json.dump(film, shrekfile)
