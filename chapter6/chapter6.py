# Dictionaries

# my_dict={}
# my_dict=dict()

# my_dict = {
#    "key":"value"
# }

# my_dict = dict(key="value")

from multiprocessing.sharedctypes import Value


steve={
    "name":"Steve",
    "weight":155.5,
    "height":70,
    "foods":["country fried steak", "fried chicken", "collards"],
    "ice_cream":{
        "vanilla":False,
        "chocolate":True,
        "coffee":False
    },
    10 : "this has an integer key" 
}
# name_of_dict[KEY]
print(steve.get("candies", "No Candy List"))
steve["name"]="Joe"
print(steve)
steve.update({
    "candies":["snickers", "mars", "m&ms"]
})
print(steve)
del steve["candies"]
print(steve)

# Looping over dictionary

for key in steve:
    print(key)
    print(type(key))
    print(steve[key])

print(steve.values())
for value in steve.values():
    print(value)
    print(type(value))

print(steve.items())
for tup in steve.items():
    print(tup) 

print(steve.items())
for key, value in steve.items():
    print(key, end=" ")
    print(value)  

print(steve.items())
for key, value in steve.items():
    if isinstance(value,list):
        print(f"The list is at {key}")
       