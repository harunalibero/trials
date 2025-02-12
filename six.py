#ORDERING JAZZ!
main =("pizza \n burger \n salad") 
side =("fruit \n yorghurt \n vegetables \n chips")
drinks =("water \n juice \n milk")

print("CHOOSE THE MAIN DISH FROM HERE ")
print(main)
dish = input("What is your main dish for today: ")
if dish in main :
    print(f"Your dish is {dish}.")

    if "salad" in dish :
        print("You are gonna get a free fruit.")
    print(" CHOOSE A SIDE DISH")
    print(side)
    sid1 = input("Whatis your first side dish for today: ")
    sid2 = input("What is your second side dish: ")
    if sid1 == "chips" and sid2 == "chips":
        print("You can't have chips twice in a meal.It's not healthy.")
    else:
        print(f"Your side dishes for today are {sid1} and {sid2}.")
        print("CHOOSE DRINKS THAT YOU NEED: ")
        print(drinks)
        drink = input("Which drinks would you take: ")
        if drink in drinks:
            print(f"Your drink for today is {drink} .")
        else:
            print("Select a drink that is in the list.")
    print("THAK YOU FOR COMPLING 💨")
else:
    print("Please pick a meal thats on the menu.")








