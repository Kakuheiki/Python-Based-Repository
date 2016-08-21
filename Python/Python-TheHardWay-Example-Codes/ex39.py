things = ["a", "b", "c", "d"]
print things[0]

things[1] = "Z"
print things[1]

print things



stuff = {"Name": "Gilbert", "Age": "15", "height": 6*12+2}

print stuff["Name"]
print stuff["Age"]
print stuff["height"]

stuff["city"] = "Santo Domingo"
print stuff["city"]

print stuff

stuff[1] = "Wow"
stuff[2] = "Neato"
print stuff[1]
print stuff[2]

print stuff

del stuff['city']
del stuff[1]
del stuff[2]
print stuff


states = {
"Oregon" : "OR",
"Florida" : "FL",
"California" : "NY",
"Michigan" : "MI"
}

cities = {
"MI" : "Detroit",
"CA" : "San Francisco",
"FL" : "Jacksonville"
}


cities["OR"] = "Portland"
cities["NY"] = "New York"

print "_" * 10
print "NY State has: ", cities["NY"]
print "OR State has: ", cities["OR"]

print "_" * 10
print "Michigan's abbreviation is: ", states["Michigan"]
print "Florida's abbreviation is: ", states["Florida"]

print "_" * 10
for state, abbrev in states.items():
    print "%s is abbreviated %s" % (state, abbrev)

print "_" * 10
for abbrev,  city in cities.items():
    print "%s has the citiy %s" % (abbrev, city)

print "_" * 10
for state, abbrev in states.items():
    print "%s is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev])

print '_' * 10
state = states.get ("Texas", None)

if not states:
    print "Sorry, no Texas."

city = cities.get("TX", "Does not exist")
print "The city for the state 'TX' is: %s" % city
