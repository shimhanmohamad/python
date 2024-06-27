travel_log = {
    "france" : {"city" :["paris","lille","dijion"],"total" : [1,2,3]},
    "UK" : "london",
    "USA"  : ["Newyork","washigton"]
}


# print(travel_log["UK"])
# print(travel_log["france"])

# for city in travel_log:
#     print(travel_log[city])

for ci in travel_log:
    for ty in "france":
        print(travel_log[ci][ty])
