# matrix=[ 
#     [1,8,1],
#     [4,5,7],
#     [8,9,3]
#     ]
# prime_count=0
# for i in matrix:
#     for j in i:
#         is_prime=j>=2
#         for divisor in range(2,j):
#             if j%divisor==0:
#                 is_prime=False
#                 break
#             if is_prime:
#                 prime_count +=1
# print(prime_count)

dimensions = input().split()
rows = int(dimensions[0])
columns = int(dimensions[1])
board = []
for _ in range(rows):
    pieces = input().split()
    row = []
    for column in range(columns):
        row.append(int(pieces[column]))
    board.append(row)

qualifying_rows = 0
first_row = -1
for row_index in range(rows):
    # Write code here: Check this row and update qualifying_rows and first_row.
    has_prime = False

    for number in board[row_index]:

        if number > 1:
            is_prime = True

            for divisor in range(2, number):
                if number % divisor == 0:
                    is_prime = False
                    break

            if is_prime:
                has_prime = True
                break

    if has_prime:
        qualifying_rows += 1

        if first_row == -1:
            first_row = row_index


    pass

print("Qualifying rows:", qualifying_rows)
print("First qualifying row:", first_row)
