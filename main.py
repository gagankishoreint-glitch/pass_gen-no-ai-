# 1)first take input from user based on choice ->1.strong and also rememberable 2.GAGU-algorithm 3.random 
# 2)check length of the password itself 
# 3)inclusions of special characters
# 5)check if user needs some special keywords/characters they wants to include 
# 4)verify with user else generate another random 

# algo1: Diceware for rememberable ( again hackers are human so it should have a keyword from user which is not their name,location,related to their personal information)
# algo2: Gagu algorithm 
# algo3: random 

import random
import string
import time
import subprocess
import secrets

special_characters=["!","@","#","$","%","^","&","*","`","~","/","?","-"]
gagu_algorithm=("reverse","skip","change-to-special_characters")
def s_r():
    def dice_map_loader():  # Renamed 
        dice_map = {}
        try:
            with open("dice.txt", "r") as file:
                for line in file:
                    parts = line.split()
                    if len(parts) == 2:
                        dice_map[parts[0]] = parts[1]
        except FileNotFoundError:
            print("Error: 'dice.txt' file was not found!")
        return dice_map
    dice_map = dice_map_loader()
    if not dice_map:
        return "Failed to start Diceware."

    num_words = int(input("\nHow many words do you want?: "))
    password_pieces = []

    for _ in range(num_words):
        five_digit_roll = "".join(secrets.choice("123456") for _ in range(5))
        matched_word = dice_map[five_digit_roll]
        password_pieces.append(matched_word)

    return "-".join(password_pieces)
def gagu():
    time.sleep(1)
    print("-----GAGU-ALGO-PROCESSING-----")
    word_count = int(input("Enter word-count: "))
    password_divided = []
    for i in range(word_count):
        while True:
            keyword = input("Please enter keyword that is not your name,number,address or so......(#smgcatchyy): ").strip()
            
            time.sleep(0.5)
            if not keyword or len(keyword) <= 2:
                print("----Checking----")
                print("oops, enter valid keyword")
                continue
            break
        word = random.choice(gagu_algorithm)
        if word == "reverse":
            modified_keyword = keyword[::-1]
            password_divided.append(modified_keyword)
        elif word == "skip":
            continue
        elif word == "change-to-special_characters":
            modified_keyword = random.choice(special_characters)
            password_divided.append(modified_keyword)
        else:
            print("....sus....")
    final_password = "".join(password_divided)
    return final_password
def random_password(length, spec):
    password_pieces = []
    string_set = string.ascii_letters + string.digits
    
    if spec == "yes":
        take_special = input("Enter your special character (or) characters: ")
        string_set = string_set + take_special
    else:
        print("okay.......")
        time.sleep(0.5)
    for _ in range(length):
        picked_char = secrets.choice(string_set)
        password_pieces.append(picked_char)
    final_password = "".join(password_pieces)
    return final_password
print("Welcome ###### , We will generate a password based on your choice\n1)Strong and can be remembered sort\n2)GAGU-ALG(no remembrance)\n3)something random ")
time.sleep(0.9)
choice=int(input("Type -> 1 for option one (or) Type -> 2 for option two (or) Type -> 3 for option three\nOption:"))
if choice == 1 :
    time.sleep(0.8)
    print("Ah! I see you want strong pass which can sit tight in your ape-brain 🧠")
    time.sleep(1)
    subprocess.run(["bash" ,"rolling_dice.sh"])
    print("password that can be remembered is: ",s_r())
elif choice == 2 :
    time.sleep(0.8)
    print("Noice-picko user ###### 🤞")
    time.sleep(1)
    print("Alright so gagu algorithm is unique in its own way so you user ##### are required to specify the word count in it(word not character)\nLet's Start")
    time.sleep(1)
    print("Your password is :" ,gagu())
        #if random is skip then we skip the word typed
        #if random is reverse then we reverse the word typed
        #if random is change then we change the typed word in special character
    #reverse , skip , change 
elif choice == 3 :
    time.sleep(0.8)
    print("Random can be guessed cause computer generated random have a pattern, proceed with caution")
    check=input("Are you sure ?").lower().strip()
    if check == "yes" :
        time.sleep(0.8)
        length=int(input("Enter the length:"))
        spec=input("Do you need special characters in this password?").lower()
        print("...generating....")
        time.sleep(1)
        print(random_password(length,spec))
    elif check == "no":
        updated_choice=int(input("Enter updated choice:"))
        if updated_choice == 2:
            print(gagu())
        elif updated_choice == 1:
            print(s_r())
        else:
            print("you need therapy for your EYES (3 Options only exist)") 
else:
    time.sleep(1)
    print("Why? , What is wrong with you.....👀")