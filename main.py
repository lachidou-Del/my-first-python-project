print("==============================")
print("   PERSONAL MONEY ASSISTANT")
print("==============================")

name = input("What is your name? ")
income = float(input("How much money do you earn per month (€)? "))
expenses = float(input("How much do you spend per month (€)? "))

remaining = income - expenses

print()
print("Hello,", name)
print("Your monthly income:", income, "euros")
print("Your monthly expenses:", expenses, "euros")
print("Money remaining:", round(remaining, 2), "euros")

if remaining > 0:
    print("Great! You have money left to save.")
elif remaining == 0:
    print("Your income exactly covers your expenses.")