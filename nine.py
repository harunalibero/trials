#CODE OFR NUMBER NINE
#CLUB        memebers       age     parental-permission   equipment                               
#volleyball   12            10>           notneeded        needed              
#physics      4             13>           needed           notneeded           
#spelling     6             6>            notneeded        notneeded                         
#boxing       7             15>           needed           needed 

spikers = 12
physicists = 4
spellers = 6
boxers = 7
#Desined by Libero.H
while True:
    #start by getting information on student.
    print("WECLOME TO AMPEX HIGH SCHOOL CLUB LOGIN,FOLLOW THE EASY STEPS TO JOIN;")
    choose = input("Would you like to sign up for a club (Y) or leave the site (N): ")
    if choose == "Y":
        name = input("What is your name: ")
        age = int(input("What is your age: "))
        print("SELECT A CLUB TO JOIN IN !")
        print("1.Volleyball \n 2.Physics \n 3.Spelling \n 4.Boxing")
        club = int(input("Which club would you love to join (select with the number code):"))
        if club == 1 :
            if spikers > 0 :
                spikers = spikers - 1        
                print("WELCOME TO THE VOLLEYBALL CLUB 🎈")
                if age < 10:
                    print("👶your still young to become a libero👶🏿young to join the volleyball club.")
                elif age >= 10:
                    print("You have a 50% chance of joining now.")
                    equipment1 = input("Do you have all the necessary equipment for volleyball yes ,(Y) or no (N); ")
                    if equipment1 =="Y":
                        print(f"Now {name}, you may join the volleyball club because you have the right age and you have all the equipment.")
                        print(f"This club only has {spikers}slots remaining. ")
                    else:
                        print("You do not have the equipment to participate in this activity") 
            elif spikers <=0:
                print("The club is full please try another club.")
                print(f"The Physics class has {physicists} places remaining.")
                print(f"The Spelling Club has {spellers} places remaining.")
                print(f"The Boxing Club has {boxers} places remaining.")
        if club == 2:
            if physicists > 0 :
                physicists= physicists - 1        
                print("WELCOME TO THE PHYSICS CLUB 🌠☀")
                if age < 13:
                    print("👶👶🏿 You still young to join the physics club things will be too hard.")
                elif age >= 13:
                    print("You have a 50% chance of joining now.")
                    parental1 = input("Did your parents allow you to participate in theoretical physics yes(Y) or no (N):")
                    if parental1 =="Y":
                        print(f"Now {name}, you may join the Physics club because you have the right age and your parents allowed you.")
                        print(f"This club only has {physicists} slots remaining. ")
                    else:
                        print("Your parents didn't allow you, go bavk and ask for permission before physics makes your head pain. ") 
            elif physicists <=0:
                print("The club is full please try another club.")
                print(f"The Volleyball has {spikers} spots remaining.")
                print(f"The Spelling Club has {spellers} places remaining.")
                print(f"The Boxing Club has {boxers} places remaining.")
        if club == 3:
            if spellers> 0 :
                spellers= spellers - 1        
                print("WELCOME TO THE SPELLER'S CLUB 👨‍👨‍👧‍👧")
                if age < 6:
                    print("👶👶🏿 You still young too even spell first grow.")
                elif age >= 13:
                    print("You have now joined the club.")
                    print(f"This club only has {spellers} slots remaining. ") 
            elif spellers <=0:
                print("The club is full please try another club.")
                print(f"The Volleyball has {spikers} spots remaining.")
                print(f"The Physicicts  have {physicists} places remaining.")
                print(f"The Boxing Club has {boxers} places remaining.")
        elif club == 4:
            if boxers > 0 :
                boxers = boxers - 1        
                print("WELCOME TO THE BOXER'S CLUB 👊🏿✊🏿")
                if age < 15 :
                    print("👶way too young to start boxers👶🏿 try something else.")
                elif age >= 15:
                    print("You have a 33.3% chance of joining now.")
                    parental2 = input("Did your parents allow you to participate boxing yes(Y) or no (N):")
                    equipment2 = input("Do you have all the necessary equipment for boxing yes ,(Y) or no (N); ")
                    if equipment2 =="Y" and parental2 == "Y":
                        print(f"Now {name}, you may join the boxer's club because you have all the equipment and yoyur parents allowed you tp get hit in the face.")
                        print(f"This club only has {boxers}slots remaining. ")
                    elif equipment2 == "N":
                        print("You dont have the boxing cloves")
                    elif parental2 =="N":
                        print("Your parents did not allow you to participate in boxing.......mbu your an egg.")
                        print("Try spelling.😁😂") 
            elif spikers <=0:
                print("The club is full please try another club.")
                print(f"The Physics class has {physicists} places remaining.")
                print(f"The Spelling Club has {spellers} places remaining.")
                print(f"The Boxing Club has {boxers} places remaining.")       
    elif choose == "N":
        break
    else :
        print("Wrong input.💢")




