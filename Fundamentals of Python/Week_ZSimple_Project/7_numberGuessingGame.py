import random

while True:
    random_num = random.randint(1,10)
    attempt =  0
    max_attempt = 10

    
    print("New Game Started !! Guess the number between 1 to 100")
    
    while attempt < max_attempt:
        user_guess = int(input("Enter a number:"))
        attempt +=1
        if  user_guess == random_num:
            print(f"Congrulations! you won in {attempt} attempts")
            break
        elif user_guess < random_num:
            print("Go higher!")
        else:
            print("Go Lower!")
        print(f"Chances left :{max_attempt - attempt}")
        
    if attempt == max_attempt & user_guess !=random_num:
        print(f"Game over !The number was {random_num}")
        
    if input("Play again? (y/n): ").lower() != 'y':
        break
print("Thanks for playing")