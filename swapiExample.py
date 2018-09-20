import swapi

empire = swapi.get_film(2)

empirePlanets = empire.get_planets()

for planet in empirePlanets.order_by("population"):
    print(planet.name, planet.population)
