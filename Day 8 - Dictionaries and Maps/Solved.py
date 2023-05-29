N = int(input())
phoneBook = {}

for i in range(N):
    contactName, phoneNumber = input().split(' ')
    phoneBook[contactName] = phoneNumber

while True:
    try:
        name = input()
    except E0FError:
        break

    if name in phoneBook.keys():
        print(f'{name}={phoneBook[phoneNumber]}')
    else:
        print('Not found.')
