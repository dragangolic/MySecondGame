print("Welcome to my world")
name = input("What is your name? ")
age = int(input("What is your age? "))
print("Hello", name, "you are", age, "years old.")
is_older = age >= 18
health = 10
print("You are starting with", health, "health")
if age >= 18:
    print("You are old enough to play!")
    wants_to_play = input("Do you want to play(yes/no)").lower()
    if wants_to_play == "yes":
        print("Let's play")
        left_or_right = input("First choose...Left or Right").lower()
        if left_or_right == "left":
            ans = input("Nice, you follow the path and reach the lake..Do you want to (swim/dive)").lower()

            if ans == "swim":
                print("Great, Just go ahead")
            elif ans == "dive":
                print("You managed somehow, but you lost 5 health!")
                health -= 5
                ans = input("You notice a house and a river. Which do you go to(river/house)?")
                if ans == "house":
                    print("Go to the house and are greeted by the owner.He didn't like you and \
                    you lose another 5 health. ")
                    health -= 5
                    if health <= 0:
                        print("You now have 0 health and you lost the game...")
                    else:
                        print("You have survived this time")

                else:
                    print("You lose! ")
        else:
            print("Oh, you lost")

    else:
        print("Cya...")
elif age >= 14:
    print("You can play with supervision")
else:
    print("You are not old enough!")
