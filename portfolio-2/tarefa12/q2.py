def algo(n):
    if n == 0:
        return 0
    else:
        return algo(n - 1) + 2 * n - 1

# Função fechada
def F(n):
    return n ** 2

# Teste
n = 5
print(f"Valor calculado recursivamente: {algo(n)}")
print(f"Valor pela fórmula fechada: {F(n)}")