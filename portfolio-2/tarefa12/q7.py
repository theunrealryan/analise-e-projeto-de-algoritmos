def f(n):
    if n == 0:
        return 1
    else:
        return n * f(n - 1)

# Teste
n = 5
print(f"f({n}) = {f(n)}")
