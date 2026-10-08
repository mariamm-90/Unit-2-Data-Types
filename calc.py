#challenge 1
""" def odd_or_even(number):
    if number % 2 == 0:
        return "even"
    return "odd"

number = int(input('enter a number:' ))
print(odd_or_even(number))


day_of_week = input("what day is it? ")
if day_of_week == "Thursday":
    print("correct")
else:
    print("incorrect") """


#cheat sheet index card permitted concepts
#sample call function
#sample define function
#sample loop




x = int(input("Enter a positive number"))
y = int(input("Enter another positive number"))
def greatest_common_factor():
    while x:
        number1, number2 = number2, number1 % number2
print(f"The greatest common factor is {greatest_common_factor(x,y)}")


















""" # Greatest Common Factor (GCF)
def greatest_common_factor(num1, num2):
    a = abs(num1)
    b = abs(num2)

    while b != 0:
        a, b = b, a % b

    return a

# Example usage
print(greatest_common_factor(48, 18)) """