"""
simulated customer changes 1
"""


records = []

secret_number = int(input('How many secrets do you want me to keep?\t'))
n = 1
while n <= secret_number:
    character = input(f'Let me store your secrets {n}:\t')
    if not character or character in records:
        print('Try again!')
    else:
        records.append(character)
        n = n + 1

print('\nYour inputs were:')
for record in records:
    print(record)
