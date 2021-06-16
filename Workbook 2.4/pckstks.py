matchsticks = 27   
while matchsticks > 0:    
    while True:
        try:
            one = int(input("Player one, take 1-3 matchsticks: "))
            
            if one < 1 or one > 3:
                raise ValueError 
            break
        except ValueError:
            print("Oh no you can only pick up 1-3 sticks at a time")
            
    matchsticks = matchsticks - one
    if matchsticks < 0:
        break
    
    print("There are",matchsticks,"matchsticks remaining")
    

    if matchsticks == 1:
        print("WOW you win, the computer now has to take the last matchstick.")
        
    if matchsticks < 1:
        print("Oh no you lose, have taken the last matchstick!")
        
    
    print("Player two, take 1-3 matchsticks: ")
    

    import random
    two = random.randint(1,3)
    print("player two takes",two,)
    
        
    matchsticks = matchsticks - two

    print("There are",matchsticks,"matchsticks")
    

    if matchsticks == 1:
        print("Oh no you lose, You have taken the last matchstick!")
        
       
    if matchsticks < 1:
        print("WOW You win, the computer has taken the last matchstick.")
        

    if matchsticks < 0:
        break

