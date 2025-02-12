#Library calculator
name = input("What is the name of the book that you are returning: ")
days = int(input("How many days have passed: "))
if days <= 7:
    charge = days * 0.5
    print(f"Your charge is ${charge}charge.As you were charged $0.5 for each day.")
elif days > 7 and days <=14 :
    days_over_week = days - 7
    charge = 7 * 0.5 + days_over_week * 1
    print(f"Your charge is ${charge},because of:")
    print("For 1 week - $0.5 \n week and above - $1")
elif days > 14 :
    days_over_week = days - 14
    charge = 7 * 0.5 + 7 * 1 + days_over_week * 2 + 10
    print(f"Your charge is ${charge},because of: ")
    print("For 1 week - $0.5 \n week and above - $1 \n a fortnight and above - $2 \n plus $10")
print("THANK YOU COME AGAIN ❕❕ we hope to see you soon.")
