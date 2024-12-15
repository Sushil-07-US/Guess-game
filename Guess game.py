# FIRST PROJECT OF PYTHON 
# GUESSING GAME

import random


name = input("Enter your name: ")
mode= int(input("Enter game Mode: \n 1 Easy \n 2 Medium \n 3 Hard\n Mode = "))

if mode == 1:
    num = random.randint(1, 51)
    guess = int(input("Enter guess number (1, 50): "))
    guess_count = 1
    guess_limit = 10

  
    

        

    while guess != num and guess_count != guess_limit:

        if guess < 1:
            print("Please enter the number from 1 to 50")
            break

        if guess > 50:
            print("Please enter the number between 1 to 50.")
            break

        print("Level: Easy")
        print(f"Your guess: {guess}")

        print("Your guess is wrong.")


    
        print  (f"{name} You did {guess_count } attempt out of 10")
        guess_count +=1

    

        Ques = input (f" {name} Do you want to play again Y/N: ")

        if Ques == "Y" or Ques=="y":
            guess = int(input("Enter your guess again: "))
        

        elif Ques == "N" or Ques=="n":
            break

        else:
            print("Please type Y to continue game")
            break


        if guess_count == guess_limit:
            print(f"{name} you are out of attempt")
            print(f"Computer guess: {num}")
            break
    
    
        if guess == num:
            print(f"Congratulation! {name} You guess number successfully")
            break



elif mode == 2:
    num = random.randint(1, 101)
    guess = int(input("Enter your guess number (1, 100): "))
    guess_count = 1
    guess_limit = 7



    while guess != num and guess_count != guess_limit:

        if guess < 1:
            print("You have to enter value from 1 to 100") 
            break

        if guess > 100:
            print("Please enter the number between 1 to 100.")
            break



        print("Level: Medium")
        

        print(f"Your guess: {guess}")

        print("your guess is wrong.")

        if guess < num :
            print("Your guess number is low")

        else:
            print("Your guess number is high")
        


    
        print  (f"You did {guess_count } attempt out of 7")
        guess_count +=1

    

        Ques = input ("Do you want to play again Y/N: ")

        if Ques == "Y" or Ques=="y":
            guess = int(input("Enter your guess again: "))
        

        elif Ques == "N" or Ques=="n":
            break

        else:
            print("Please type Y to continue game")
            break

        if guess_count == guess_limit:
            print("You are out of attempt")
            print(f"Computer guess: {num}")
            break
    
    
        if guess == num:
            print(f"Congratulation!{name} You guess number successfully")
            break



elif mode == 3:
    
    num = random.randint(1, 201)
    guess = int(input("Enter your guess number (1, 200): "))
    guess_count = 1
    guess_limit = 5



    while guess != num and guess_count != guess_limit:

        if guess < 1:
            print("You have to enter value from 1 to 200") 
            break

        if guess > 201:
            print("Please enter the number between 1 to 50.")
            break

        print("Level: Hard")

        print(f"Your guess: {guess}") 

        print("Your guess is wrong.")

        if num % 2== 0 and guess % 2 != 0:
            print("Hint : Number is even")

        else:
            print("Hint : Number is odd")
         
    


    
        print  (f"You did {guess_count } attempt out of 5 ")
        guess_count +=1

    

        Ques = input ("Do you want to play again Y/N: ")

        if Ques == "Y" or Ques=="y":
            guess = int(input("Enter your guess again: "))
        

        elif Ques == "N" or Ques=="n":
            break

        else:
            print("Please type Y to continue game")
            break

        if guess_count == guess_limit:
            print(f"{name} you are out of attempt")
            print(f"Computer guess: {num}")
            break
    
    
        if guess == num:
            print(f"Congratulation! {name} You guess number successfully")
            break

else:
    print(" Please make sure to Enter number 1, 2 and 3")


    

print(f"Thank you! {name} See you again.....")
