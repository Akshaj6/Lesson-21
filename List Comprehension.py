l = int(input("Enter a number :"))
if l <= 0:
    print("Enter a number which is greater than 0 and positive")
else:
    odd_numbers = [num for num in range(l) if num % 2 != 0]
    print("List of odd numbers : {odd_numbers}")
    list_odd = [num for num in range(1, l, 2)]
    print("2nd list of odd numbers : {list_odd}")
fruits = ["apple", "banana", "mango", "pear", "dragonfruit", "strawberry", "guava"]
print("List of fruits : {fruits}")
caps = [fruit.capitalize() for fruit in fruits]
print("List with 1st letter capital : {caps}")