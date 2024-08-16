[LEN, PERG] = input().split(" ")
lista = [int(x) for x in input().split(" ")]

store = {}
def potencial(l: int, r: int, key: str) -> int:
    if key in store:
        return store[key]
    
    p = 0
    i = l
    while i <= r:
        j = l
        while j <= r:
            if j != i: 
                p += (lista[i]*10) + lista[j]
            j += 1
        i += 1

    store[key] = p
    return p

for _ in range(int(PERG)):
    [start, end] = input().split(" ")
    print(potencial(int(start)-1, int(end)-1, start+end))
