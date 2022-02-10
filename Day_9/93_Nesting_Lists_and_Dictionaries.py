# Nesting

capitals = {
    "France":"Paris",
    "The Netherlands":"Amsterdam",
    "England": "London",
    "Belgium": "Brussels",
    "Germany":"Berlin",
}

# Nesting a List in a Dictionary

major_cities = {
    "France": ["Paris","Lille","Marseille","Lyon"],
    "The Netherlands":["Amsterdam","Rotterdam","The Hague","Utrecht","Eindhoven"],
    "England": ["London","Liverpool","Manchester"],
    "Belgium": ["Brussels","Antwerp"],
    "Germany": ["Berlin","Hamburg","Leipzig"],
}

# Nesting a Dictionary in a Dictionary

travel_log = {
    "France": {"cities_visited":["Paris","Lille","Marseille","Lyon"], "total_visits":15},
    "The Netherlands": {"cities_visited":["Amsterdam","Rotterdam","The Hague","Utrecht","Eindhoven"], "total_visits":120},
    "England": {"cities_visited":["London","Liverpool","Manchester"], "total_visits":0},
    "Belgium": {"cities_visited":["Brussels","Antwerp"], "total_visits":3},
    "Germany": {"cities_visited":["Berlin","Hamburg","Leipzig"], "total_visits":6},
}

# Nesting a Dictionary in a List

travel_log = [
    {
        "country": "France", 
        "cities_visited": ["Paris","Lille","Marseille","Lyon"], 
        "total_visits": 15
    },
    {
        "country": "The Netherlands", 
        "cities_visited": ["Amsterdam","Rotterdam","The Hague","Utrecht","Eindhoven"], 
        "total_visits": 120
    },
    {
        "country": "England", 
        "cities_visited": ["London","Liverpool","Manchester"], 
        "total_visits": 0
    },
    {
        "country": "Belgium", 
        "cities_visited": ["Brussels","Antwerp"], 
        "total_visits": 3
    },
    {
        "country": "Germany", 
        "cities_visited": ["Berlin","Hamburg","Leipzig"], 
        "total_visits": 6
    },
]