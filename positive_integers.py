def print_positive_numbers(numbers):
    positive_numbers = []
    for num in numbers:
        if num > 0:
            positive_numbers.append(num)
    print(positive_numbers)

list1 = [12, -7, 5, 64, -14]
print_positive_numbers(list1)

list2 = [12, 14, -95, 3]
print_positive_numbers(list2)
