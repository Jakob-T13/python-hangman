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
        print(str(display_string))
        input_guess = str(input("Please guess a letter or the entire word: "))
        if len(input_guess) == 1:
            