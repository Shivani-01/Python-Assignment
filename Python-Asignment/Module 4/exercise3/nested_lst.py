matrix=[[j for j in range(10)] for i in range(5)]
print(matrix)
print()
flatten_list=[i for j in matrix for i in j]
print(flatten_list)
print()
flatten_lower=[i for j in matrix for i in j if i<6]
print(flatten_lower)
