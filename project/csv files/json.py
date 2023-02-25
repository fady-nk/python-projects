import json

collage = {
    "collage": "cs collage",
    "objectives": "to learn computer science",
    "departments": {
        "dep1": "computer science",
        "dep2": "cyber security",
    },
    "years": [
        "first year",
        "second year",
        "third year",
        "fourth year",
    ],
    "numbers": [1, 2, 3, 4],
    "ID": [10, 20, 30, 40]
}
3
json.dump(collage, open("collage.json", "w"))

new_collage = json.load(open("collage.json", "r"))
