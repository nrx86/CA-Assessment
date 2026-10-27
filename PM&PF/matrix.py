
matrix = []

for i in range(3):
    values = input().split()
    row = [int(values[0]), int(values[1]), int(values[2])]
    matrix.append(row)

r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())

r1 = r1 - 1
c1 = c1 - 1
r2 = r2 - 1
c2 = c2 - 1

temp = matrix[r1][c1]
matrix[r1][c1] = matrix[r2][c2]
matrix[r2][c2] = temp

for row in matrix:
    print(" ".join(map(str, row)))

    