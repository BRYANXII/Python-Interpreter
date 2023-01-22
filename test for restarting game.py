import random
 
 
def main(): 
    print('Hello! What is your name?')
    myName = input()
    play = "yes"
    while play == "yes":
        game(myName)
        play = input("Type yes to play again and no to quit: ").lower()
    print("Thank you for playing.")
         
 
def game(myName):
    guessesTaken = 0
    number = random.randint(1, 10)
    print('Well, ' + myName + ', I am thinking of a number between 1 and 10.')
    guess = ""
    while guess != number:
        print('Take a guess.') 
        guess = input("> ")
        guess = int(guess)
        guessesTaken = guessesTaken + 1                                 
 
        if guess < number:
            print('Your guess is too low.') 
        elif guess > number:
            print('Your guess is too high.')
        else:
            guessesTaken = str(guessesTaken)
            print('Good job, '+ myName + '! You guessed my number in '
                + guessesTaken + ' guesses!')
            break
 
  
main()