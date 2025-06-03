def recursive_sum(a, i=0):
    if i == len(a):
        return 0
    if a[i] < 9:
        return a[i] + recursive_sum(a, i+1)
    else:
        return recursive_sum(a, i+1)

a = [2, 34, 56, 7, 86, 9]
result = recursive_sum(a)
print("Sum of elements < 9:", result)