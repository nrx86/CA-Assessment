# integers = [500, 450, 200, 300, 250]
# integers.append(100)
# integers.extend([200,300])

# integers.insert(1,50)
# integers.pop()
# integers.sort()
# print(integers)

times=[45, 32, 50, 28, 40]
times.append(35)
times.extend([25, 60])
times.insert(2, 30)
times.remove(50)
times.sort()

print(times)
print("Length: ", len(times))
print("Minimum: ", min(times))
print("Maximum: ", max(times))
print("Total: ", sum(times))
print("Average: ", sum(times)/len(times))
