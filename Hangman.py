from random import choice
from time import sleep
import hm_resource as hmr

hint = choice(list(hmr.words.keys()))

find_word = choice(list(hmr.words[hint]))

blank = ['_']*len(find_word)

wrong_letters=[]

print(hmr.title)
print("______________________________________________________")
present_stage=0
flag=0
print(f"\n\nLET'S START THE GAME!!!!")
print(f"\n\nYou have to guess a {len(find_word)} letter word")
print(*blank)
print("\n\n______________________________________________________")
while(True):
    print("\n\n------>hint : " + hint)
    print("\nword:",end="")
    print(*blank)
    check=1
    while(check):
        letter=input("\nGuess a letter : ")
        if letter.isalpha() and len(letter)==1:
            letter=letter.lower()
            check=0
        else:
            print("Enter letter only")
    if(letter in find_word and letter not in blank):
        print("\nWow, you guessed it correct!!!\n")
        for i in range(len(find_word)):
            if(letter == find_word[i]):
                blank[i]=letter
        if('_' not in blank):
            break
    elif(letter in wrong_letters or letter in blank):
        print("You have already guessed that letter")
        print("try a new letter!!")
    else:
            if(present_stage==7):
                flag=1
                print(f"\n\nThe correct word is : {find_word}")
                print("\nYou didn't guessed the word correctly!!!!")
                print("You Lost all the chances!!!")
                print("You are hanged ☠️ ☠️ ☠️ ☠️")
                print(hmr.lose)
                break
            print(hmr.stage[present_stage])
            print("\nOh NO!!, you guessed it wrong")
            print(f"\nRemaining chances : {7-present_stage}\n\n")
            wrong_letters.append(letter)
            present_stage+=1
    if(len(wrong_letters)):
        print(f"Wrong letters : {(wrong_letters)}")
    print("______________________________________________________")

if(flag==0):
    print("Congratulations!!!!!!")
    print("You guessed the word correctly")
    print(f"\n\nThe correct word is : {find_word}")
    print("\n____________YOU WON____________")
    print(hmr.win)
    print("You saved Your Life🥳🥳🥳🥳🥳")
print(hmr.game_over)
sleep(20)






