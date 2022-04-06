import random

file_path = (r'words.txt')          #path for file with words
words_file = open(file_path, "r")   #open words file with read-only permissions
words_list = words_file.readlines() #read words into a list
words_file.close()                  #close the file when done

#words_list = ["APPLE", "ORANGE"]   #debug word list

game_states = []
for i in range(7+1):
    state_path = str("state"+str(i)+".txt")
    state_file = open(state_path, "r")
    state_txt = state_file.read()
    game_states.append(state_txt)
    state_file.close()

for x in range(len(words_list)-1):      #strip newlines from words
    words_list[x]=words_list[x].strip()

def GetRandomWord(lst):     #Choose a random word from a list of strings and remove it from the list
    word_index = random.randint(0,len(lst)-1)   #random int for index of word to be chosen
    returnval = lst[word_index]                 #word to be returned
    del(words_list[word_index])                 #delete the word from the original list
    return returnval
    
    
def GameLoop():
    is_running = True
    record = {
        "wins": 0,
        "losses": 0
    }
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
            print(game_states[guesses])
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
            record["wins"] += 1
            print("Congratulations, you won! The word was '"+answer+"'.")
        else:
            record["losses"] += 1
            print(game_states[guesses])
            print("Sorry, you lost. The word was '"+answer+"'.")
        print("You have won "+str(record["wins"])+" times and lost "+str(record["losses"])+" times.")
        if words_list != []:
            play_again = input("Would you like to play again? (y/n) ")
            if play_again != "y":
                is_running = False
        else:
            print("You've played with all the words in the list!")
            is_running = False

GameLoop()
