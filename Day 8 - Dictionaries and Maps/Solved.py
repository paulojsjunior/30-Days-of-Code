N = int(input())
phoneBook = {}

for i in range(N):
    contactName, phoneNumber = input().split(' ')
    phoneBook[contactName] = phoneNumber

for j in range(N):
    name = input()

    if name in phoneBook.keys():
        print(f'{name}={phoneBook[phoneNumber]}')
    else:
        print('Not found.')
