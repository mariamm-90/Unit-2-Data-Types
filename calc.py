#challenge 1
def odd_or_even(number):
    if number % 2 == 0:
        return "even"
    return "odd"

number = int(input('enter a number:' ))
print(odd_or_even(number))

""" day_of_week = input("what day is it? ")
if day_of_week == "Thursday":
    print("correct")
else:
    print("incorrect") """