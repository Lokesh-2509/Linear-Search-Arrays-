def count_occurrences(arr, target):
    count = 0
    for num in arr:
        if num == target:
            count += 1
    return count
A = [1, 2, 2]
B = 2
result = count_occurrences(A, B)
print("Number of occurrences of", B, "in A:", result)
A = [1, 2, 1]
B = 3
result = count_occurrences(A, B)
print("Number of occurrences of", B, "in A:", result)
