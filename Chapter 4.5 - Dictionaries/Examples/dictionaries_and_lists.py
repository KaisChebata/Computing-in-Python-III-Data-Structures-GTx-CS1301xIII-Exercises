classes = {"Math" : ["David", "Lucy", "Dana"],
           "Physics" : ["Addison", "Vrushali", "Bilbo"],
           "Chemistry" : ["Sara", "Lugos", "Mireia", "Perle"],
           "Computing" : ["Partha", "Venijamin", "Terra", "Sofia"],
           "History" : ["Tryphon", "Gevorg", "Raza", "Rein"]}
print('Students in Computer Science:', classes['Computing'])
classes['History'].append('Francis')
print('Students in History:', classes['History'])

print('---------------------------------------------------------')
addressBook = {"David": ("555 Home St", "4045551234", "david@david.com"),
               "Lucy" : ("555 Home St", "4045555678", "lucy@lucy.com"),
               "Dana" : ("123 There Rd", "4045559101", "dana@dana.net")}
print('David infos:', addressBook['David'])
print('Dana phone number:', addressBook['Dana'][1])