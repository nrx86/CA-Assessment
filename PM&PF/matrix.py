
# matrix = []

# for i in range(3):
#     values = input().split()
#     row = [int(values[0]), int(values[1]), int(values[2])]
#     matrix.append(row)

# r1, c1 = map(int, input().split())
# r2, c2 = map(int, input().split())

# r1 = r1 - 1
# c1 = c1 - 1
# r2 = r2 - 1
# c2 = c2 - 1

# temp = matrix[r1][c1]
# matrix[r1][c1] = matrix[r2][c2]
# matrix[r2][c2] = temp

# for row in matrix:
#     print(" ".join(map(str, row)))


# # Read the size of the matrix
# n = int(input())

# # Create an empty matrix
# grid = []

# # Read the matrix rows
# for i in range(n):
#     row = list(map(int, input().split()))
#     grid.append(row)

# # Store the sum of each row and column
# row_totals = []
# col_totals = []

# # Calculate the sum of each row
# for r in range(n):
#     row_total = 0
#     for c in range(n):
#         row_total += grid[r][c]
#     row_totals.append(row_total)

# # Calculate the sum of each column
# for c in range(n):
#     col_total = 0
#     for r in range(n):
#         col_total += grid[r][c]
#     col_totals.append(col_total)

# # Calculate the main diagonal sum
# diagonal_total = 0
# for i in range(n):
#     diagonal_total += grid[i][i]

# # Print the row totals
# print("Rows:")
# for total in row_totals:
#     print(total)

# # Print the column totals
# print("Columns:")
# for total in col_totals:
#     print(total)

# # Print the main diagonal total
# print("Main diagonal:")
# print(diagonal_total)

# # Calculate and print row total minus column total
# print("Balance:")
# for i in range(n):
#     print(row_totals[i] - col_totals[i])

# nums=[23,45,65,70,89]
# target=65
# for i in range(len(nums)):
#     if nums[i]==target:
#         print(i)
#         break


    