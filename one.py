#PIN ENTRY
name = input("What is your name: ")
your_pin = 3464
#No. of trials 3
trials = 3

while trials > 0:
    enter_pin = int(input("Tell us your pin :"))
    if enter_pin == your_pin:
        print(f"{name} ,access has been granted to your account.")
        break
    else:
        trials = trials - 1
        if trials > 0:
            print(f"Wrong pin entered and now you have {trials} attempts remaining.")
        else:
            print(f"Hey, {name} you have tried 3 times and now your account is blocked.Contact services now!")




