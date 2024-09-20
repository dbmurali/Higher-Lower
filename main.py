import random
from art import logo
from game_data import data

print(logo)
print("GUESS WHO HAS MORE INSTAGRAM FOLLOWERS")

B=random.choice(data)
A = random.choice(data)
score=0
to_run=True

while to_run:

        def print_details(datas):
           return  {datas['name'],datas['description'],datas['country']}
        if A==B:
            B=random.choice(data)

        print(print_details(A))
        print("------VS-------")
        print(print_details(B))

        a_followers=A['follower_count']
        b_followers=B['follower_count']

        user_choice=input("choose \"A\" or \"B\":  ").upper()

        if a_followers>b_followers and user_choice=="A":
            score += 1
            print(F"correct  your score: {score}")
            B = random.choice(data)


        elif b_followers>a_followers and user_choice=="B":
            score += 1
            print(F"correct  your score: {score}")
            A=B
            B=random.choice(data)

        else:

            print(f"wrong  final score: {score}")
            to_run=False
