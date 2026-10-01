def odd_or_even(number):
    if number % 2 == 0:
        return "even"
    return "odd"

number = int(input('enter a number:' ))
print(odd_or_even(number))