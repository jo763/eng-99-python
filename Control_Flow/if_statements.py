film_rating = "PG"


def rate_film(film_rating):
    if film_rating == "18":
        print("You must be 18 or older to view this film")
    elif film_rating == "15":
        print("You must be 15 or older to view this film")
    elif film_rating == "12" or film_rating == "12A":
        print("You must be 12 or older to view this film")
    elif film_rating == "PG":
        print("Parental guidance is advised")
    else:
        print("Film is suitable for all audiences")


film_rating = "PG"
rate_film(film_rating)

film_rating = "U"
rate_film(film_rating)

film_rating = "12"
rate_film(film_rating)

film_rating = "12A"
rate_film(film_rating)

film_rating = "15"
rate_film(film_rating)

film_rating = "18"
rate_film(film_rating)