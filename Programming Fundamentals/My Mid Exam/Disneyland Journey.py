"""
Create a program that checks if you can save money for a Disneyland's journey. You have a certain number of months during which you can collect the money.
At the end of each month, you save 25% of the cost of the journey.
At the beginning of every odd month (except the first one) you spent 16% of the money collected so far on clothes and shoes.
Every 4th (fourth) month at the beginning of the month your boss gives you а bonus. It is 25% of the money collected so far.
If you save enough money for the journey, calculate how much money will be left for the souvenirs. Then print the following:
"Bravo! You can go to Disneyland and you will have {money}lv. for souvenirs."
If the money saved is less, you need to calculate how much money you need. Then print the following:
"Sorry. You need {money}lv. more."
Both numbers should be formatted to the 2nd decimal place.
Input
•	On the 1st line, you will receive how much the journey will cost – a real number in the range [500.0…10000.0]
•	On the 2nd line, you will receive the number of months for which you have to collect money – an integer number in the range [1…12]
"""

journey_cost = int(input())
months = int(input())
money = 0

for month in range(1, months + 1):
    if month % 2 != 0 and month != 1:
        money -= money * 0.16
    elif month % 4 == 0:
        money += money * 0.25
    money += journey_cost * 0.25

for_souvenirs = abs(money - journey_cost)
if money >= journey_cost:
    print(f"Bravo! You can go to Disneyland and you will have {for_souvenirs:.2f}lv. for souvenirs.")
else:
    print(f"Sorry. You need {for_souvenirs:.2f}lv. more.")