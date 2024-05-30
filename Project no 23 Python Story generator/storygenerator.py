import random
print("Hello Reader")

readername = input("What is your name? ")

print("Hello " + readername)

names = ["zara", "ben", "Esme", "Andrew","Aisha"]
Places = ["Karachi", "Lahore", "Islamabad", "Rawalpindi","Faslabad","Multan"]
quests = ["City of lights","City of food","Beauty of the city","City of saints"]
roles = ["Text Pay City","Knight","Amazon warrior","orgre","witch"]

randomname = random.choice(names)
randomPlaces = random.choice(Places)
randomquests = random.choice(quests)
randomrole = random.choice(roles)

story = "once upon a time there was a " + randomrole + "called" + randomname + "use to live in " + randomPlaces + "that use to be called as" + randomquests + "that city gave us" 
print(story)