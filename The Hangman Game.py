import random
def hangman():
    name= input("what's your name?")
    print( "welcome" , name , ", try to not let the hangman die!")
    print(" you have 10 attempts")
    words_available=["bangladesh","farm","wall","robotics","mouse","cow"]
    word=random.choice(words_available)
    chances=10
    guessmade=""
    valid_letters= set("abcdefghijklmnopqrstuvwxyz")
    letters_game=set(word)
    letters_used=set()

    while len(word)>0:
        if letters_used in letters_game:
            used_character= letters_game-letters_used
            print(used_character)
            break
        
        main_word=""
        for letter in word:
            if letter in guessmade:
                main_word=main_word+letter
            else:
                main_word=main_word+" _ "
        if main_word==word:
            print("the correct word is ",main_word , "!")
            print(" well done! you saved the hangman")
            break
            
        
        print("guess the word",main_word)
        guess=input()
        print("you have used:",guess)
        if guess in valid_letters:
            guessmade=guessmade+guess
        else:
            print(" enter a valid character")
            guess=input()

        if guess not in word:
            chances=chances-1
            if chances==9:
                print("you have 9 chances to save the hangman")

            if chances==8:
                print("you have 8 chances to save the hangman")
            if chances==7:
                print("you have 7 chances to save the hangman")
            if chances==6:
                print("you have 6 chances to save the hangman")
            if chances==5:
                print("you have 5 chances to save the hangman")
            if chances==4:
                print("you have 4 chances to save the hangman")
            if chances==3:
                print("you have 3 chances to save the hangman")
            if chances==2:
                print("you have 2 chances to save the hangman")
            if chances==1:
                print("you have 1 chances to save the hangman")
            if chances==0:
                print("You let the hangman die...")
                print("the correct word is:", used_character)
                break
                



hangman()
