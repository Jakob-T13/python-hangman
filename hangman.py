import random

file_path = (r'words.txt')          #path for file with words
words_file = open(file_path, "r")   #open words file with read-only permissions
words_list = words_file.readlines() #read words into a list
words_file.close()                  #close the file when done

#words_list = ["APPLE", "ORANGE"]   #debug word list

game_states = []                            #list for game state strings
for i in range(7+1):                        #for each of the 7 game states:
    state_path = str("state"+str(i)+".txt") #build the filename (state<i>.txt)
    state_file = open(state_path, "r")      #open the file
    state_txt = state_file.read()           #read its contents into a var
    game_states.append(state_txt)           #copy that var into the list
    state_file.close()                      #close the file

for x in range(len(words_list)-1):      #strip newlines from words
    words_list[x]=words_list[x].strip()

def GetRandomWord(lst):     #Choose a random word from a list of strings and remove it from the list
    word_index = random.randint(0,len(lst)-1)   #random int for index of word to be chosen
    returnval = lst[word_index]                 #word to be returned
    del(words_list[word_index])                 #delete the word from the original list
    return returnval
    
    
def GameLoop():         #the actual game
    is_running = True   #maintains the main loop
    record = {          #win/loss record
        "wins": 0,
        "losses": 0
    }
    while is_running:   #main loop
        #game setup
        guesses = 0     #number of wrong attempts
        answer = GetRandomWord(words_list).upper()      #get a word and convert it to UPPERCASE
        #answer = "MINNESOTA"    #static answer for testing
        #print(answer) #print for debug
        display_string = []     #list for the characters of the answer to display, since strings can't be modified
        for i in answer:        #for each letter in the answer word
            display_string += "_"   #place an _ in the display word
        guess_letters = []      #list to store already-guessed letters
        game_won = False        #maintains game loop
    
        #game loop
        while guesses < 7 and not game_won:     #while at fewer than 7 wrong guesses and haven't won yet:
            print(game_states[guesses])         #display the current game state
            print(' '.join(display_string))     #display current progress on the correct answer
            input_guess = str(input("Please guess a letter or the entire word: ")).upper()  #prompt user for input, convert input to a string, convert input to UPPERCASE
            if len(input_guess) == 1:           #if input is a single character:
                if input_guess in guess_letters:    #if user has already guessed that character:
                    print("You've already guessed that letter. Try again.") #tell them to try again
                else:
                    guess_letters += input_guess    #add the letter to the list
                    if input_guess in answer:       #if input is in the answer:
                        for n in range(len(answer)):    #for each character in the display list
                            if answer[n] == input_guess:    #if the input letter matches the nth letter in the word
                                display_string[n] = input_guess #change the underscore at that position to the letter
                        if '_' not in display_string:   #if all the underscores are filled
                            game_won = True         #all letters have been found, game is won
                    else:
                        guesses += 1        #add to count of incorrect guesses
                        print("'"+input_guess+"' is not in the word. You have "+str(7-guesses)+" wrong guesses remaining.")     #tell the user they're wrong
            elif len(input_guess) > 1:
                if input_guess == answer:   #if user guesses the word correctly
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
