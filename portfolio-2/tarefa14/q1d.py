def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
        left_half = merge_sort(arr[:mid])
        right_half = merge_sort(arr[mid:])
        return merge(left_half, right_half)

def merge(left, right):
    sorted_array = []
    i = j = 0
    # Comparação e fusão das metades
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1
    # Adiciona os elementos restantes
    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])
    return sorted_array

# Testando a função com um array de tamanho n
import random
import time

n = 1024  # Tamanho do array
arr = [random.randint(0, 1000) for _ in range(n)]
start_time = time.time()
sorted_arr = merge_sort(arr)
end_time = time.time()
print(f"Tempo de execução para n={n}: {end_time - start_time} segundos")
