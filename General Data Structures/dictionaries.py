dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print "dict['Name']: ", dict['Name']
print "dict['Age']: ", dict['Age']

# Output
# dict['Name']:  Zara
# dict['Age']:  7

# Update Dictionary
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
dict['Age'] = 8; # update existing entry
dict['School'] = "DPS School"; # Add new entry

print "dict['Age']: ", dict['Age']
print "dict['School']: ", dict['School']

# Output
# dict['Age']:  8
# dict['School']:  DPS School

# Delete Dictionary Elements
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
del dict['Name']; # remove entry with key 'Name'
dict.clear();     # remove all entries in dict
del dict ;        # delete entire dictionary

# Iterate through Dictionary
dic = {}
for key, value in dic

# Check for existence of a key in a dictionary
dict = {}
if key in dict:
    # If key is in the dictionary, perform something.

if value in dict.values():
    # If value is in the dictionary, perform something.
