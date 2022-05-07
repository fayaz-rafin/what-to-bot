# Python program to read
# json file


import json

with open('main/food.json') as f:
  data = json.load(f)

print(data)