"""
#
# Part : python JSON
# API = apprication programing interface
# 
"""

import json
#make a JSOn (dictionary string)
x = '{"name": "Jonh", "age": 20 , "city": "phuket"}'
print(x)

# parse
y = json.loads(x)

# python dictionary
print(y)
print(type(y))
print(y["city"])

# python dictionary
a = {
    "name": "Noa",
    "age": 20,
    "city": "phuket"
}

# convert to JSON (string)
b = json.dumps(a)

# JSOM string
print(b)


