"""
the computer is going to ask for n unique characters one at a time
the computer will tell me if the character has already been used
computer will then store the unique character
after this has been done n times, a list of used characters will be printed
"""


records = []

n = 3
while n > 0:
    character = input('Let me store your secrets:\t')
    if not character or character in records:
        print('Try again!')
    else:
        records.append(character)
        n = n - 1

print('\nYour inputs were:')
for record in records:
    print(record)
