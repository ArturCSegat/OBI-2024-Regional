input()
alienigena = input()
msg = input()

for c in msg:
    if c not in alienigena:
        print('N')
        exit()
print('S')