#def find_max_value(numbers):
   # max_value = numbers[0]
   # for i in range(len(numbers)):
    #    if numbers[i] > max_value:
     #       max_value = numbers[i]
   # return max_value

#def find_min_value(numbers):
 #   min_value = numbers[0]
  #  for i in range(len(numbers)):
   #     if numbers[i] < min_value:
    #        min_value = numbers[i]
   # return min_value

#numbers = [4, 1, 7, 3, 9, 2]

#max_num = find_max_value(numbers)
#min_num = find_min_value(numbers)

#print("Maximum number:", max_num)
#print("Minimum number:", min_num)

# link to chagpt convo
# https://chatgpt.com/c/67bea211-d844-8010-a868-34f4a6fa6d26


# new refactored code
def find_max_value(numbers):
    """Returns the maximum value from a list of numbers."""
    return max(numbers)

def find_min_value(numbers):
    """Returns the minimum value from a list of numbers."""
    return min(numbers)

# Sample list of numbers
numbers = [4, 1, 7, 3, 9, 2]

# Find maximum and minimum numbers
max_num = find_max_value(numbers)
min_num = find_min_value(numbers)

# Print results
print("Maximum number:", max_num)
print("Minimum number:", min_num)