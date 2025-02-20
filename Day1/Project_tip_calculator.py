#Project TIP Calculator

print("Welcome to project tip Calculator!!")
bill = float(input("Enter the total bill: $"))
discount = float(input("How much discount do you want to get: "))
split = int(input("Enter the number of people to split the bill among: "))

bill_post_discount = bill-bill*discount/100
#print(bill_post_discount)
after_bill = round(bill_post_discount/split,2)
print(f"Each person would have to pay: {after_bill}$")
