#Lists: Storing multiple values in order
# favgames=["Halo","Mario Kart","Elden Ring"]

# #index a list
# #Indexing a list just means outputting or searching for one value in the list
# print(favgames[2])
# print(favgames[0:2])

# #using Len() we can find out how many total items are in a list
# print(len(favgames))

# #adding items to a list
# #append() adds to the end of a list
# #insert() adds items to a specific position

# favgames.append("DarkSouls")
# print(favgames)
# favgames.insert(0, "LoL")
# print(favgames)

# #Common list methods
# #Count() counts how many times a value appears
# #remove() removes a specific item
# #sort() puts the list in a sorted order
# #reverse() flips the current order of the list

# #Count example
# print(favgames.count("LoL"))
# #remove() example
# favgames.remove("DarkSouls")
# print(favgames)
# #sort() example
# favgames.sort()
# print(favgames)
# #reverse() example
# favgames.reverse()
# print(favgames)

#loop through the items in my list
# favgames=["Halo","Mario Kart","Elden Ring"]

# for games in favgames:
#   print(games)

#Dictionaries: Stores labeled information
#A dictionary store data in key value pairs
#Dictionaries are useful when a label matters more than a position

#make a dictionary that is called playerstats

player_stats={
  #Dictionary values must be health, mana, level, gold
  #word;value
  "health":100,
  "mana":40,
  "level":15,
  "gold":25,

}

# #Lists vs dictionaries
# #We use a list when order matters and we want a collection of items
# #A dictionary is used when labels matter and you want to look things up by name

# #Accessing a dictionary
# print(f"you have {player_stats["health"]} health left!")

# #what if we want to update dictionary values?
# #You can add a new key-value pair by assigning the value to a new key
# #You can also update an existing value or increase it

# player_stats["Strength"]=15
# player_stats["health"]-=15
# print(player_stats)

#Keys() and Values()

#keys() shows all dictionary values
#Values() shows all dictionary values

# print(player_stats.keys())
# print(player_stats.values())

#How we can loop through our dictionaries
#We can loop through the keys or the values or both
#items() is often the most readable way to  show everything in a dictionary

#Loop through the keys
# for stats in player_stats.keys():
#   print(stats)

# #Loop through the values
# for values in player_stats.values():
#   print(values)

# #Loop through both keys and values
# for stats, values in player_stats.items():
#   print(f"{stats} [{values}]")

#Nested Dictionaries
students={
  "001":{
    "Name": "Ana",
    "Major":"Programming",
    "Credits": 6
  },
  "002":{
    "Name":"Joe",
    "Major":"Cyber",
    "Credits": 15
  }
}

#how do we access nested data?
#to access nested data we go one level at a time

print(students["002"]["Major"])

#Nested Structures can mix lists and dictionaries
#Programs often combine multiple data structures together
#An inner dictionary can contain a list as one of its values

students={
  "005":{
    "Name":"Sebastian"
    "Classes"["Math","Hacking","Linux"],
    "GPA": 4.0
  }
}

