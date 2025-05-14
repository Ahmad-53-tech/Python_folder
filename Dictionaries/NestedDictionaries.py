# Nested dictionary: having a list inside a dictionary OR having a dictionary inside another dictionary.
 

# list in a dictionary
# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Stuttgart", "Berlin"]
# }


# # Accessing berlin
# print(travel_log["Germany"][1])




#dictionary in a dictionary
travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_cities": 12
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    },
}
# Accessing lille
print(travel_log["France"]["cities_visited"])