import random

file_path = (r'words.txt')
words_file = open(file_path, "r")
words_list = words_file.readlines()
words_file.close()

for x in range(len(words_list)-1):
    words_list[x]=words_list[x].strip()

def GetRandomWord(lst):     #Choose a random word from a list of strings and remove it from the list
    word_index = random.randint(0,len(lst)-1)
    returnval = lst[word_index]
    del(words_list[word_index])
    return returnval
    
    
def GameLoop():
    is_running = True
    wins = 0
    losses = 0
    while is_running:
        #game setup
        guesses = 0
        answer = GetRandomWord(words_list).upper()
        #answer = "MINNESOTA"    #static answer for testing
        print(answer) #print for debug
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
                        if '_' not in display_string:
                            game_won = True
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
            wins += 1
            print("Congratulations, you won! The word was '"+answer+"'.")
        else:
            losses += 1
            print("Sorry, you lost. The word was '"+answer+"'.")
        print("You have won "+str(wins)+" times and lost "+str(losses)+" times.")
        if words_list != []:
            play_again = input("Would you like to play again? (y/n) ")
            if play_again != "y":
                is_running = False
        else:
            print("You've played with all the words in the list!")

GameLoop()
