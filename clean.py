import csv
import json
import pandas as pd

# df = pd.read_json("./drug1.json")

datas = json.load(open("./drug1.json"))['results']

# df = pd.DataFrame(data["results"])

count = 0

for data in datas:
    count+= 1

print(count)