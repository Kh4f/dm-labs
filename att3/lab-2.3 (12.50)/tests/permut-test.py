from itertools import permutations

with open('../input.txt', 'r') as file:
    N = int(file.readline().strip())

# Генерация всех возможных перестановок списка размера N
all_permutations = [list(p) for p in permutations(list(range(1, N + 1)))]

for perm in all_permutations:
    print(perm)

print(len(all_permutations))

