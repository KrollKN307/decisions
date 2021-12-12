with open('v23.txt', 'r') as file:
    lines = [[float(y) for y in x.strip().split(' ')] for x in file.readlines()]

print("Вхідні дані:")
print("Koef   A   B   C   D   E")
for line in lines: print("%.2f  %2d  %2d  %2d  %2d  %2d" % (line[0], line[1], line[2], line[3], line[4], line[5]))
print("\nОбчислені параметри в залежності від коефіцієнтів:")
print("Koef    A     B     C     D     E")
sumOfColumns = [0, 0, 0, 0, 0]
for line in lines:
    print("%.2f  %1.2f  %1.2f  %1.2f  %1.2f  %1.2f" % (
    line[0], line[0] * line[1], line[0] * line[2], line[0] * line[3], line[0] * line[4], line[0] * line[5]))
    sumOfColumns[0] += line[0] * line[1]
    sumOfColumns[1] += line[0] * line[2]
    sumOfColumns[2] += line[0] * line[3]
    sumOfColumns[3] += line[0] * line[4]
    sumOfColumns[4] += line[0] * line[5]

print("      %1.2f  %1.2f  %1.2f  %1.2f  %1.2f" % (
sumOfColumns[0], sumOfColumns[1], sumOfColumns[2], sumOfColumns[3], sumOfColumns[4]))
print("Найкращий вибір: ", sumOfColumns.index(max(sumOfColumns)) + 1, chr(65 + sumOfColumns.index(max(sumOfColumns))))
