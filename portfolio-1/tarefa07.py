def soma(n, v):
    s = 0
    if n == 0:
        s += 0
    else:
        s += soma(n-1, v) + v[n]
    return s

n = int(input("Escolha e digite 50 ou 100 para execução: "))
v = [i for i in range(n + 1)]

res = soma(n, v)
print(res)