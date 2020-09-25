"""
Exercise 3.17 (Nested Loops)
Write a script that displays the following triangle patterns seperately, one below the other. Seperate each pattern from the next one by one blank line.
Use for loops to generate the patterns. Display all asterisks(*) with a single statement of the form
print('*',end='')
which causes the asterisks to display side by side
"""

print('(a)')
for num in range(1,11):
    for _ in range(num,0,-1):
        print('*',end = '')
    print()

# Seperator   
print('\n')

print('(b)')
for num in range(10):
    for _ in range(num,10,1):
        print('*',end = '')
    print()

# Seperator   
print('\n')

print('(c)')
for num in range(0,10):
    for _ in range(0,num,1):
        print(' ',end='')
    for _ in range(num,10,1):
        print('*',end = '')
    print()

# Seperator   
print('(d)')
for num in range(0,11):
    for _ in range(10,num,-1):
        print(' ',end='')
    for _ in range(0,num,1):
        print('*',end = '')
    print()