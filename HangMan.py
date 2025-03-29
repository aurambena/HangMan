import random
import os

def ahorcado (c, guess, dict_guess, dict_compare, compare, random_word_list1,longitud,letter, random_word_list):
    if c==1:
        print("   _---_    ")
        print("  /     \   ")
        print("  \     /   ")
        print("   \_v_/    \n")
    elif c==2: 
        print("   _---_    ")
        print("  /     \   ")
        print("  \     /   ")
        print("   \_v_/    ")
        print("     |      ")
        print("     |      ")
        print("     |      ")
        print("     |      \n")
    elif c==3:
        print("   _---_    ")
        print("  /     \   ")
        print("  \     /   ")
        print("   \_v_/    ")
        print("     |      ")
        print("     |      ")
        print("     |      ")
        print("     |      ")
        print("    /       ")
        print("   /        ")
        print("  /         \n")
    elif c==4:
        print("   _---_    ")
        print("  /     \   ")
        print("  \     /   ")
        print("   \_v_/    ")
        print("     |      ")
        print("     |      ")
        print("     |      ")
        print("     |      ")
        print("    / \      ")
        print("   /   \     ")
        print("  /     \    \n")
    elif c==5:
        print("   _---_    ")
        print("  /     \   ")
        print("  \     /   ")
        print("   \_v_/    ")
        print("     |      ")
        print("     |      ")
        print("     |      ")
        print("     |      ")
        print("    / \      ")
        print("   /   \     ")
        print("  /     \    ")
        print(" /__     \  \n")
    elif c==6:
        print("   _---_    ")
        print("  /     \   ")
        print("  \     /   ")
        print("   \_v_/    ")
        print("     |      ")
        print("     |      ")
        print("     |      ")
        print("     |      ")
        print("    / \      ")
        print("   /   \     ")
        print("  /     \    ")
        print(" /__     \__ \n")
    elif c==7:
        print("   _---_    ")
        print("  /     \   ")
        print("  \     /   ")
        print("   \_v_/    ")
        print("     |      ")
        print("   / |      ")
        print("  /  |      ")
        print("  \_ |      ")
        print("    / \      ")
        print("   /   \     ")
        print("  /     \    ")
        print(" /__     \__ \n")
    elif c==8:
        print("   _---_    ")
        print("  /     \   ")
        print("  \     /   ")
        print("   \_v_/    ")
        print("     |      ")
        print("   / | \    ")
        print("  /  |  \   ")
        print("  \_ |   \_ ")
        print("    / \      ")
        print("   /   \     ")
        print("  /     \    ")
        print(" /__     \__ \n")
    elif c==9:
        print("  |            ")
        print("  |   _---_    ")
        print("  |  /     \   ")
        print("  |  \     /   ")
        print("  |   \_v_/    ")
        print("  |     |      ")
        print("  |   / | \    ")
        print("  |  /  |  \   ")
        print("  |  \_ |   \_ ")
        print("  |    / \      ")
        print("  |   /   \     ")
        print("  |  /     \    ")
        print("__| /__     \__ \n") 
    elif c==10:
        print("   _______     ")
        print("  |   _---_    ")
        print("  |  /     \   ")
        print("  |  \     /   ")
        print("  |   \_v_/    ")
        print("  |     |      ")
        print("  |   / | \    ")
        print("  |  /  |  \   ")
        print("  |  \_ |   \_ ")
        print("  |    / \      ")
        print("  |   /   \     ")
        print("  |  /     \    ")
        print("__| /__     \__ \n") 
    elif c==11:
        print("   ______      ")
        print("  |   _-|-_    ")
        print("  |  /  |  \   ")
        print("  |  \  |  /   ")
        print("  |   \_v_/    ")
        print("  |     |      ")
        print("  |   / | \    ")
        print("  |  /  |  \   ")
        print("  |  \_ |   \_ ")
        print("  |    / \      ")
        print("  |   /   \     ")
        print("  |  /     \    ")
        print("__| /__     \__ \n") 
    elif c==12:
        print("\n PERDISTE!")
        print("   ______      ")
        print("  |   _-|-_    ")
        print("  |  / X|X \   ")
        print("  |  \  |  /   ")
        print("  |___\_O_/___ ")
        print("  |     |      ")
        print("  |   / | \    ")
        print("  |  /  |  \   ")
        print("  |  \_ |   \_ ")
        print("  |    / \      ")
        print("  |   /   \     ")
        print("  |  /     \    ")
        print("__| /__     \__ \n")
        # print("La palabra era: " (random_word_list)) 

    input_letter(c,guess, dict_guess, dict_compare,compare, random_word_list1,longitud,random_word_list)    # validation(c,dict_guess,longitud,letter,random_word_list1, compere, dict_compare)
    
def input_letter(c,guess, dict_guess, dict_compare,compare, random_word_list1,longitud,random_word_list):
    
    if dict_guess != random_word_list1:
        
        print("Adivina la palabra! \n")
        #print(random_word_list1)
        print(' '.join(map(str, guess)))
        letter = input("\nIngresa una letra: ")
        # os.system("cls")
        # ahorcado (c, guess, dict_guess, dict_compare, compere, random_word_list1,longitud,letter)
        validation (c,dict_guess, longitud, letter, random_word_list, compare, dict_compare,random_word_list1)
    elif dict_guess == random_word_list1:
        os.system("cls")
        print("Adivina la palabra! \n")
        print(' '.join(map(str, guess)))
        print("\n GANASTE!")
    
def validation (c,dict_guess, longitud, letter, random_word_list,compare, dict_compare,random_word_list1):
   

    compare= []
    i=0
    while i<longitud:
        if letter != random_word_list[i]:
            compare.append("_ ",)
            
        else:
            compare.append(random_word_list[i])
        i=i+1
    i=0
    contador=[]
    while i<longitud:
        contador.append("_ ",)
        i=i+1

    if compare == contador:
        c=c+1

    dict_compare={}
    for k, v in enumerate(compare):
        f"key {k}: value = {v}"
        dict_compare[k]=v    
   
 
    compare_plus(c,dict_guess, dict_compare, compare, random_word_list,longitud,letter,random_word_list1)
    
def compare_plus(c,dict_guess, dict_compare, compare, random_word_list,longitud,letter,random_word_list1):
    
    guess=[]
    i=0
    while i<longitud:
        if dict_compare[i] != dict_guess[i]:
            
            if dict_compare[i] != ("_ "):
                guess.append(dict_compare[i])
            elif dict_guess[i] != ("_ "):
                guess.append(dict_guess[i])
            
        elif dict_compare[i] == ("_ ") and dict_guess[i] == ("_ "):
            guess.append("_ ")
            
        else:
            if dict_compare[i] != ("_ "):
                guess.append(dict_compare[i])
            elif dict_guess [i] != ("_ "):
                guess.append(dict_guess[i])
        i=i+1
    
    dict_guess={}
    for k, v in enumerate(guess):
        f"key {k}: value = {v}"
        dict_guess[k]=v    
    os.system("cls")
    
    ahorcado (c, guess, dict_guess, dict_compare, compare, random_word_list,longitud,letter,random_word_list1)
    # input_letter(c, guess, dict_guess, dict_compare, compare, random_word_list,longitud)

def data():

    #abro el archivo con las palabras
    data = []
    random_word_list = []
    with open("./files/data.txt","r", encoding="utf-8") as f:
        for line in f:
            data.append(str(line))
    #print(data)
    #seleccionar una palabra aleatoria
    random_word = random.choice(data)
    #cuento cuantas letras tiene
    longitud = len(random_word)-1
    
    random_word_list = [i for i in random_word]
    random_word_list.pop(longitud)
    
    random_word_list1={}
    for k, v in enumerate(random_word_list):
        f"key {k}: value = {v}"
        random_word_list1[k]=v 
    
    compare= [longitud]
    dict_compare={}
    for k, v in enumerate(compare):
        f"key {k}: value = {v}"
        dict_compare[k]=v 
    guess=[]
    i=0
    while i < len(random_word_list):
        guess.append("_ ",)
        i=i+1
   
    dict_guess={}
    for k, v in enumerate(guess):
        f"key {k}: value = {v}"
        dict_guess[k]=v    
    c=0
    input_letter(c,guess,dict_guess, dict_compare, compare, random_word_list1,longitud,random_word_list)
    
         
if __name__ == "__main__":
    data()