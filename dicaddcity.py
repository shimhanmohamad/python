travel_log = [
    {"country": "france",
     "visits" :12,
      "cities": ["paris","lille","dijion"]
    },
    {
        "country": "germany",
        "visits" : 5,
        "cities": ["berlin","hamburg","stuttgrat"]
    }
]

def add_new_country(country_visited,time_visited,cities_visisted):
    travel = {}
    travel["country"] = country_visited
    travel["visists"] = time_visited
    travel["cities"] = cities_visisted
    travel_log.append(travel)


add_new_country("russia",2,["moscow","yagu"])
add_new_country("srilanka",3,["kandy","colombo"])

print(travel_log)