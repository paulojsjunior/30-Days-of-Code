N = int(input())

for x in range(0, N):

    S = str(input())

    for i in range(0, len(S)):
        if i % 2 == 0:
            print(S[i], end='')

    for i in range(0, len(S)):
        if i % 2 != 0:
            print(S[i], end='')
