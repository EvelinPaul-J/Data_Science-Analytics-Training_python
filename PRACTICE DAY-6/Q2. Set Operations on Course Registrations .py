A = {101, 102, 103, 105}
B = {102, 104, 105, 106}
print("Both courses:", sorted(A & B))
print("Only Course A:", sorted(A - B))
print("Either course:", sorted(A | B))
