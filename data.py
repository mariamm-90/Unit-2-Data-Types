#tip calculator
""" bill = input("How much was the bill? ")
tip = input("What percentage tip would you like to give? ")
bill = float(bill)
tip = int(tip)
total = bill + (bill * tip / 100)
print(f"The total bill, including tip, is: ${total:.2f}") """


#Challenge 1 word counter
#1. ask user to input sentence
#2. develop a function that accepts the user input and will tell you how many words are in that string
""" def count_words(user_sentence):
    word_list = user_sentence.split()
    total_words = len(word_list)
    print(f"There are {total_words} words in your sentence.")
user_input = input("enter a sentence: ")
count_words(user_input) """


#2. Mad Libs Challenge
""" adjective = input("Enter an adjective: ")     #descriptive word that describes a noun
noun = input("Enter a noun: ")     #person, place, thing
verb = input("Enter a verb: ")     #an acton word; something physcially done
place = input("Enter a place: ")
print(f"Today at Staten Island Tech, a very {adjective} student brought a {noun} to class.")
print(f"It suddenly broke and {verb} all the way down the {place}.") """


#Challenge 3 create a function that determines if number is odd or even
""" def odd_or_even(number):
    if number % 2 == 0:
        return "even"
    return "odd"
number = int(input('enter a number:' ))
print(odd_or_even(number)) """


#Challenge 4 create function that accepts a "bill" value and offer tip of 0%, 15%, 20% or 25% depending on if the service 
# was "bad, okay, good , or great 
""" def calculate_tip(bill, service):
    tip_rates = {
        "bad": 0.00,
        "okay": 0.15,
        "good": 0.20,
        "great": 0.25,
    }
    if service not in tip_rates:
        return "Invalid service level"
    tip_amount = bill * tip_rates[service]
    return bill + tip_amount
user_bill = float(input("Enter the bill amount: "))
user_service = input("How was the service? (bad, okay, good, great): ")
final_amount = calculate_tip(user_bill, user_service)
print(f"The total bill, including tip, is: ${final_amount:.2f}") """


#Challenge 5 create function that accepts an input and determines all factors of the number
""" def find_factors(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors
num = int(input("Enter a number to find its factors: "))
print(find_factors(num)) """


#Challenge 6 create function that accepts two numbers and returns the greatest common factor of the two numbers
""" def find_gcf(num1, num2):
    gcf = 1
    for i in range(1, num1 + 1):
        if num1 % i == 0 and num2 % i == 0:
            gcf = i
    return gcf
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print(find_gcf(num1, num2)) """