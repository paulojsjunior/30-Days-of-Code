N = int(input())
phoneBook = {}

for i in range(N):
    contactName, phoneNumber = input().split(' ')
    phoneBook[contactName] = phoneNumber
