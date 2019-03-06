'''
Represents good use case of when to NOT use else when working with if statements
'''

'''
In the first example, it's okay to not have else: return False because it'll break
out of the loop when it hits the if statement.
'''

for i in range(10):
    if x in asdf:
        return True
    return False

'''
In this example, we need the else statement because we're not returning in the if.
'''

for i in range(10):
    if x in asdf:
        y = someval
    else:
        x = someval2

'''CANNOT BE'''
for i in range(10):
    if x in asdf:
        y = someval
    x = someval2
