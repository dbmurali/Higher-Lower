import random
from art import logo
from game_data import data

print(logo)
print("GUESS WHO HAS MORE INSTAGRAM FOLLOWERS")
# chose two random values from list
left=random.choice(data)
right=random.choice(data)


print(f"A: {left['name']},{left['description']},{left['country']}")
print(f"B: {right['name']},{right['description']},{right['country']}")

SCORE=0
is_user_correct=True
while is_user_correct:
        user_input=input("Enter A or B: ").upper()


        if user_input=="A":
             if left['follower_count'] > right['follower_count']:
               print(f"A: {left['name']},{left['description']},{left['country']},{left['follower_count']}")
               print(f"B: {right['name']},{right['description']},{right['country']},{right['follower_count']}")
               right = random.choice(data)
               print("CORRECT ANSWER")
               print("\n"*4)
               print(f"A: {left['name']},{left['description']},{left['country']}")
               print(f"B: {right['name']},{right['description']},{right['country']}")
               SCORE+=1
               print(f"YOUR SCORE= {SCORE}")
             else:
              print("WRONG ANSWER")
              print("game over")
              print(left)
              print(right)
              print(f"YOUR SCORE= {SCORE}")
              is_user_correct=False

        if user_input=="B":
            if left['follower_count']<right['follower_count']:
                print(f"A: {left['name']},{left['description']},{left['country']},{left['follower_count']}")
                print(f"B: {right['name']},{right['description']},{right['country']},{right['follower_count']}")
                left=random.choice(data)
                print("CORRECT ANSWER")
                print("\n" * 4)
                print(f"A: {left['name']},{left['description']},{left['country']}")
                print(f"B: {right['name']},{right['description']},{right['country']}")
                SCORE += 1
                print(f"YOUR SCORE= {SCORE}")
            else:
                print("WRONG ANSWER")
                print("game over")
                print(left)
                print(right)
                print(f"YOUR SCORE= {SCORE}")
                is_user_correct = False

