import json
from pathlib import Path

script_location = Path(__file__).absolute().parent
file_location = script_location / 'db_db.json'

db = {}


def update_db():
    with open(file_location, 'w') as file:
        print(db)
        json.dump(db, file)


with open(file_location, 'r') as file:
    db = json.load(file)
#
# a = {'command': '00', 'body': {'id': 123, 'items': ['prikal']}}
# b = {'command': '01', 'body': 123}
#
# print(json.dumps(b))
# print(json.dumps(a))
