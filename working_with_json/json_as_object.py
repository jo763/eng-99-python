import json

class Film:
    def __init__(self, filepath):
        film_info = self.open_json_file(filepath)
        self.name = film_info.get("name")
        self.seasons = film_info.get("seasons")
        self.film_sequel = film_info.get("film_sequel")
        self.production_company = film_info.get("production_company")
        self.ratings = film_info.get("ratings")
        pass

    @staticmethod
    def open_json_file(filepath):
        with open(filepath) as film_file:
            return json.load(film_file)

    def get_average_rating(self):
        # returns avegae of all ratings in self.ratings
        average_rating = 0
        ratings = self.ratings.values()
        for i in ratings:
            average_rating += i
        return average_rating/len(ratings)

firefly = Film("shrek.json")
print(firefly.name)
print(firefly.seasons)
print(firefly.film_sequel)
print(firefly.production_company)
print(firefly.get_average_rating())
