
number_of_questions = input("How many questions do you want to play? ")

import urllib.request, json 
with urllib.request.urlopen(f"https://opentdb.com/api.php?amount={number_of_questions}&category=21&type=boolean") as url:
    data = json.loads(url.read().decode())

opentdb_results = data["results"]

print(data["results"][0]["question"])