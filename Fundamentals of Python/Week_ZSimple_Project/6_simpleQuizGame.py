score = 0       #Initialize score as 0
total_questions = 3  # Define total questions

#Q1
print("Q1: Which programming language has rich frameworks?:")
ans = input().strip().lower() 

if ans == "python":
    score += 1         #every time answer is corrected score update by 1
    print("Correct!")
else:
    print("Wrong answer")

#Q2
print("Q2: Which is the Backend Framework of Python")
ans2 = input().strip().lower()

if ans2 == "django":  # Fixed: should be lowercase to match .lower()
    score += 1
    print("Correct!")
else:
    print("Wrong answer")
    
#Q3
print("Q3: List is Mutable or Immutable?:")
ans3 =input().strip().lower()

if ans3 == "Mutable":
    score += 1
else:
    print("Wrong answer")

print(f"Your score: {score}/{total_questions}")








