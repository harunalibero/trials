menu = ("1.Pizza - $10 \n 2.Burger -$5 \n 3.Pasta -$7 ")
print(menu)
meal = int(input("By putting in the number of the meal, which meal would you like: "))
if meal == 1 :
    print("You have ordered for Pizza which cost $10 per slice.🍕")
elif meal == 2 :
    print("You have ordered for burger which cost $5 🍔")
elif meal == 3:
    print("You have ordered for Pasta which is $ 7 per bowl.🍜")
else:
    print("Invalid meal.❌")


