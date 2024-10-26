# Função recursiva para soma da direita para a esquerda com exibição parcial
def soma_dir_esq(k, n, A):
    if k > n:
        print(f"soma_dir_esq({k}, {n}) = 0")
        return 0
    else:
        resultado_parcial = A[k-1] + soma_dir_esq(k+1, n, A)
        print(f"soma_dir_esq({k}, {n}) = {A[k-1]} + soma_dir_esq({k+1}, {n}) -> {resultado_parcial}")
        return resultado_parcial

# Função recursiva para soma da esquerda para a direita com exibição parcial
def soma_esq_dir(k, n, A):
    if k < 1:
        print(f"soma_esq_dir({k}, {n}) = 0")
        return 0
    else:
        resultado_parcial = A[k-1] + soma_esq_dir(k-1, n, A)
        print(f"soma_esq_dir({k}, {n}) = {A[k-1]} + soma_esq_dir({k-1}, {n}) -> {resultado_parcial}")
        return resultado_parcial

# Função principal para selecionar o método de soma
def calcular_soma():
    n = int(input("Digite o valor de n (tamanho da lista): "))
    A = list(range(1, n+1))  # Preenchendo a lista A com valores de 1 até n

    escolha = input("Escolha a direção da soma (esquerda para direita: 'E', direita para esquerda: 'D'): ").upper()

    if escolha == 'E':
        resultado = soma_esq_dir(n, n, A)
    elif escolha == 'D':
        resultado = soma_dir_esq(1, n, A)
    else:
        print("Escolha inválida!")
        return

    print(f"O resultado final da soma é: {resultado}")

# Executando a função principal
calcular_soma()
