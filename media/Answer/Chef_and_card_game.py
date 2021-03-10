from sys import stdin, stdout
for _ in range(int(stdin.readline())):
    n=int(stdin.readline())
    chef=[0 for i in range(n)]
    morty = [0 for i in range(n)]
    for testing in range(n):
        chef[testing], morty[testing] = list(map(str,stdin.readline().split()))
    print(chef,morty)
    chef_power = 0
    morty_power = 0
    for i in range(n):
        if len(chef[i]) > 1:
            while len(chef[i])!=1:
                digit = 0
                for j in chef[i]:
                    digit = digit + int(j)
                chef[i] = str(digit)
            print(chef[i])
        if len(morty[i]) > 1:
            while len(morty[i])!=1:
                digit = 0
                for j in morty[i]:
                    digit = digit + int(j)
                morty[i] = str(digit)
            print(morty[i])
        if int(chef[i]) > int(morty[i]):
            chef_power = chef_power +1
        elif int(chef[i]) < int(morty[i]):
            morty_power = morty_power +1
        else:
            chef_power = chef_power +1
            morty_power = morty_power +1
    if chef_power > morty_power:
        print("0",chef_power)
    elif morty_power>chef_power:
        print("1",morty_power)
    else:
        print("2",morty_power)