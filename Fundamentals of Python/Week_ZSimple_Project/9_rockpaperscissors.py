# Rock Paper Scissor Game:
# get input form 2 user (r,p,s)
# you can use nested if-else or other logic to determine the winner

# user1 and user 2 input same--> Tie

# r,p ---> p wins
# r,s ---> r wins
# p,s ---> s wins

user_1 = input("User 1 input--> Enter any one from options ('r','p','s')?:").strip().lower()
user_2 = input("User 2 input -->Enter any one from options ('r','p','s')?:").strip().lower()

if user_1 == user_2:
    print("Game Tie !")
else:
    if user_1 == 'r':
        if user_2 == 'p':
            print(f"User 2  wins in r,p ---> p wins")
        else:                                          #user 2 becomes s 
            print(f"User 1  wins in r,s ---> r wins")
            
    elif user_1 == 'p':
        if user_2 == 's':
            print(f"User 2  wins in p,s ---> s wins")
        else:                                          #user 2 becomes r
            print(f"User 1  wins in p,r ---> p wins") 
    
    elif user_1 == 's':
        if user_2 == 'r':
            print(f"User 2  wins in s,r ---> r wins")
        else:                                          #user 2 becomes p
            print(f"User 1  wins in s,p ---> s wins") 
    else:
        print("invalid input from user ")
    
    