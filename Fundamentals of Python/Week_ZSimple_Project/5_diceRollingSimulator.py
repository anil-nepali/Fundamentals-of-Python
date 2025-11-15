#in the dice rolling simulator.. we simply wanted to get random number
import random

dice_faces={
    1 :   """
                    ╭───────╮
                    │       │
                    │   0   │
                    │       │
                    ╰───────╯
            """,
    2 :   """
                    ╭───────╮
                    │ 0     │
                    │       │
                    │     0 │
                    ╰───────╯ 
 
            """,
    3 :   """
                    ╭───────╮
                    │ 0     │
                    │   0   │
                    │     0 │
                    ╰───────╯

            """,
    4 :   """
                    ╭───────╮
                    │ 0   0 │
                    │       │
                    │ 0   0 │
                    ╰───────╯

            """,
    5 :   """
                    ╭───────╮
                    │ 0   0 │
                    │   0   │
                    │ 0   0 │
                    ╰───────╯

             """,
    6:    """
                    ╭───────╮
                    │ 0   0 │
                    │ 0   0 │
                    │ 0   0 │
                    ╰───────╯

            """    
}

# Convert dictionary values to a list for random selection        
outcomes = list(dice_faces.values())

x="y"
while x.lower()=="y":
    rand_outcome = random.sample(outcomes,1)
    for outcome in rand_outcome:
        print(outcome)
    x=input("print y for rolling dice:")