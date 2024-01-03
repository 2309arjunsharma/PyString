import random
name = str(input("Enter your name: "))
print("Good luck",name)
print("You have to guess the word")
words = ["rainbow", "fish", "car", "black", "glue", "dog", "coin", "water", "action", "hero", "god", "alien", "movement", "nuerologist", "surgeon", "steryotype", "death", "llama", "spanish"]
word  = random.choice(words)
print("Guess the letter from a-z(in lower case letters)")
guesses = ''
turns = 10
while turns > 0:
    lost_turn = 0
    for a in word:
        #print(a,"_", word)
        if a in guesses:
            #print(a, "_",guesses)
            print(a, end="")
        else:
            print("_")
            #print("_",lost_turn)
            lost_turn = lost_turn + 1

    if(lost_turn==0):
        print("\nGood job! You Win")
        print("The word was",word)
        break

    print()
    guess = str(input("Guess a letter: "))
    guesses += guess
    if(guess not in word):
        turns = turns - 1
        print("You are wrong")
        print("You have", + turns, 'more guesses')

    if(turns==0):
        print("You lose!")
        print("Try again next time!")

            
