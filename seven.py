#CAR PARKING
print("ENTER IN 24  CLOCK SYSTEM (0 - 24 HOURS ) .5 for 30 past and .25 for quarter past . ")
entry_time = int(input("At what time did you enter the car parking: "))
now = int(input("What is the time right now: "))
weekend_status = input("Is it a weekend ,Y for yes and N for no: ") 
time_spent = now - entry_time
ticket = input("Do you have your ticket, Y for yes and N for no; ") 
if ticket == "Y":
    print("You will have to pay $25 for losing the ticket.")
elif weekend_status == "Y":
    print("Since its weekend you will be paying $10.")
elif entry_time < 9.5:
    print("Your gonna be charged $10 for being an early bird.")
else:
    duration = entry_time - now
    if duration <= 2:
        fee = duration * 4
        print(fee)
    elif duration <= 5:
        fee = (duration - 2 ) * 3 + 8
        print(fee)
    else: 
        fee = (duration - 5 ) * 2 + 17
        print(fee)


