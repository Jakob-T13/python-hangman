import random

words_list = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "NewHampshire", "NewJersey", "NewMexico", "NewYork", "NorthCarolina", "NorthDakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "RhodeIsland", "SouthCarolina", "SouthDakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "WestVirginia", "Wisconsin", "Wyoming"]

def GetRandomWord(lst):     #Choose a random word from a list of strings
    return lst[random.randint(0,len(lst)-1)]
    
def GameLoop():
    #game setup
    guesses = 0
    #answer = upper(GetRandomWord(words_list))
    answer = "TEXAS"    #static answer for testing
    display_string = []
    for i in answer:
        display_string += "_"
    guess_letters = []
    game_won = False
    
    #game loop
    while guesses < 7 and not game_won:
        print(' '.join(display_string))
        input_guess = str(input("Please guess a letter or the entire word: ")).upper()
        if len(input_guess) == 1:
            if input_guess in guess_letters:
                print("You've already guessed that letter. Try again.")
            else:
                guess_letters += input_guess
                if input_guess in answer:
                    for n in range(len(answer)):
                        if answer[n] == input_guess:
                            display_string[n] = input_guess
                else:
                    guesses += 1
                    print("'"+input_guess+"' is not in the word. You have "+str(7-guesses)+" wrong guesses remaining.")
        else:
            if input_guess == answer:
                game_won = True
            else:
                guesses += 1
                print("'"+input_guess+"' is not the correct answer. You have "+str(7-guesses)+" wrong guesses remaining.")
                
    #game end
    if game_won:
        print("Congratulations, you won!")
    else:
        print("Sorry, you lost. The word was '"+answer+"'.")
        
GameLoop()