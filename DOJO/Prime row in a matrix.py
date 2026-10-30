from sqlite3 import Row


matrix=[ 
    [1,8,1],
    [4,5,7],
    [8,9,3]
    ]
prime_count=0
for i in matrix:
    for j in i:
        is_prime=j>=2
        for divisor in range(2,j):
            if j%divisor==0:
                is_prime=False
                break
            if is_prime:
                prime_count +=1
print(prime_count)
