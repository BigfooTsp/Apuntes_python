from collections import defaultdict

def gen_raices4(min, max):
    diccionario = defaultdict(list)
    for e1 in range(1, int(max**0.5)):
        r1 = e1**2
        for e2 in range(e1, int((max-e1**2)**0.5)+1):
            r2 = e2 ** 2
            diccionario[r1+r2].append((r1, r2))
    return diccionario