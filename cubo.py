N = int(input())

total = N ** 3
face = N ** 2

pintado1 = ((N-2)**2) * 6
pintado2 = (((N-2)*4)*6) / 2
pintado3 = 8

nao_pintado = total - pintado1 - pintado2 - pintado3

if nao_pintado < 0:
    nao_pintado = 0

print(int(nao_pintado))
print(int(pintado1))
print(int(pintado2))
print(int(pintado3))
