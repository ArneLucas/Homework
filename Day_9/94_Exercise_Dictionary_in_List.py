travel_log = [
    {
        "country": "France", 
        "cities": ["Paris","Lille","Marseille","Lyon"], 
        "visits": 15
    },
    {
        "country": "The Netherlands", 
        "major_cities": ["Amsterdam","Rotterdam","The Hague","Utrecht","Eindhoven"], 
        "visits": 120
    },
    {
        "country": "England", 
        "major_cities": ["London","Liverpool","Manchester"], 
        "visits": 0
    },
    {
        "country": "Belgium", 
        "major_cities": ["Brussels","Antwerp"], 
        "visits": 3
    },
    {
        "country": "Germany", 
        "major_cities": ["Berlin","Hamburg","Leipzig"], 
        "visits": 6
    },
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

# above is 1 list, with 4 nested dictionaries, each containging 3 keys (one key containing a list as a value)

def add_new_country(country_visited, nr_of_visits, major_cities):
    travel_log.append({
        "country": country_visited, 
        "major_cities": major_cities, 
        "visits": nr_of_visits,         
        })


#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)