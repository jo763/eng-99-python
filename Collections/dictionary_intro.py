d = {
    "course": "Engineering 99",
    "stream": "DevOps",
    "no. trainees": 11

}

print(d, type(d))

print(d["stream"])  # will return error if doesn't exist
print(d.get("stream"))  # will return "None" if doesn't exist

d["stream"] = "Data Engineering"
d.update({"stream": "Data Engineering"})

films = {"Cost_GBP": 8000000}

films['title'] = "HotFuzz"
films['director'] = "Edgar Wright"
films['cast leads'] = ["Simon Pegg", "Nick Frost"]
cast_to_be_added = ["Bill Nighy", "Olivia Colman", "Martin Freeman"]
for cast_member in cast_to_be_added:
    films['cast leads'].append(cast_member)

print(films)

print(films['cast leads'][0:2])

films.pop("director")
print(films)

del films["title"]
print(films)

print(films.keys())
print(films.values())
print(films.items())

