"""
simulated customer changes 2
"""


records = set()

secret_number = int(input('How many secrets do you want me to keep?\t'))
n = 1
while n <= secret_number:
    character = input(f'Let me store your secrets {n}:\t')
    records.add(character)
    n = n + 1

print('\nYour inputs were:')
for record in records:
    print(record)
