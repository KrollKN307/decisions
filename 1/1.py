def read_matrix():
    matrix = []
    with open("v23.txt", "r") as f:
        rows = f.readlines()
        for row in rows:
            to_add = row.replace('\n', '')
            matrix.append([int(numeric_string) for numeric_string in to_add.split(' ')])
    return matrix


def print_matrix(matrix):
    for i in range(len(matrix)):
        to_print = []
        for j in range(len(matrix[i])):
            to_print.append(str(matrix[i][j]))
        print('', '|'.join(to_print))


def walds(matrix):
    min_in_rows = []
    for row in matrix:
        min_in_rows.append(min(row))
    max_val = max(min_in_rows)
    print("Найменші значення рядків:", min_in_rows)
    print("Найбільше з найменших значень у рядках:", max_val)
    return min_in_rows.index(max_val)


def laplace(matrix):
    avg_in_rows = []
    for row in matrix:
        avg_in_rows.append(sum(row) / len(row))
    max_val = max(avg_in_rows)
    print("Середнє у рядках", [round(x, 2) for x in avg_in_rows])
    print("Найбільше з середніх значень у рядках", round(max_val, 2))
    return avg_in_rows.index(max_val)


def hurwitz(matrix, coef):
    result = []
    for i in range(len(matrix)):
        result.append(coef * min(matrix[i]) + (1 - coef) * max(matrix[i]))
    print("Коеф.:", coef)
    print("Отримані значення:", result)
    return result.index(max(result))


def bayes_laplace(matrix, coefs):
    result = [0 for x in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            result[i] += coefs[j] * matrix[i][j]
    print("Коеф.:", coefs)
    print("Отримані значення:", result)
    return result.index(max(result))


lines = read_matrix()
print("Matrix")
print_matrix(lines)
print("\nКритерій Вальда:")
index = walds(lines)
print("Оптимальна стратегія:", lines[index])
print("\nОцінка Лапласа:")
index = laplace(lines)
print("Оптимальна стратегія:", lines[index])
print("\nКритерій Гурвіца:")
index = hurwitz(lines, 0.8)
print("Оптимальна стратегія:", lines[index])
print("\nКритерій Байєса-Лапласа:")
index = bayes_laplace(lines, [0.55, 0.3, 0.15])
print("Оптимальна стратегія:", lines[index])
