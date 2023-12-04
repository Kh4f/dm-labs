def determinant():
    # Условие остановки
    if len(matrix) == 1:
        return matrix[0][0]
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    # Шаг рекурсии
    new_det = 0
    for i in range(len(matrix)):
        submatrix = [row[:i] + row[i + 1:] for row in matrix[1:]]
        new_det += ((-1) ** i) * matrix[0][i] * determinant()
    return new_det


with open("input.txt", "r") as inputFile:
    matrix = [list(map(int, line.split())) for line in inputFile.readlines()]

det = determinant()

with open("output.txt", "w") as outputFile:
    outputFile.write(str(det))
print(det)

# Слолжность O(n!), где n — размерность матрицы.
# Используется  рекурсивный процесс, который для каждого элемента
# первой строки матрицы вычисляет определитель подматрицы, размер которых уменьшается на один с каждым шагом,
# ведущего к факториальному числу операций.
