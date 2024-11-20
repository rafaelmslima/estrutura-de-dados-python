def binary_search(arr, start, end, key):
    while start <= end:
        mid = start + (end - start) // 2  # Use // para divisão inteira
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            start = mid + 1
        else:
            end = mid - 1
    return -1  # Esse retorno estava dentro do `else` e foi corrigido

arr = ['arroz', 'feijao', 'batata', 'queijo','picles', 'pao', 'piroca']
arr.sort()
x = 'piroca'
result = binary_search(arr, 0, len(arr) - 1, x)
print(result)