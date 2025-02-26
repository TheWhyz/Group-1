def find_duplicates(lst):
    duplicates = set()
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] == lst[j]:
                duplicates.add(lst[i])
    return list(duplicates)

# Example usage
numbers = [1, 2, 3, 4, 5, 2, 3, 6, 7, 8, 1]
print("Duplicates:", find_duplicates(numbers))

#refactored version
def find_duplicates(lst):
    seen = set()
    duplicates = set()
    
    for num in lst:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    
    return list(duplicates)

# Example usage
numbers = [1, 2, 3, 4, 5, 2, 3, 6, 7, 8, 1]
print("Duplicates:", find_duplicates(numbers))
