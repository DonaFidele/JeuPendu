#coding:utf-8

from random import randrange
import os ,time

#gestion des mots depuis le fichier mots.txt
def get_words(filename):
    with open(filename, "r") as words_file:
        word_list = words_file.readlines()
    word_list_clean = []
    for word in word_list:
        if word.endswith('\n'):
            word_list_clean.append(word.split('\n')[0])
        else:
            word_list_clean.append(word)

    return word_list_clean

#gestion du choix de mots
def generate_random_word(words):
        return words[randrange(len(words))]

#gestion des scores
def write_score(name, score):
    print("Writing score...")
    content = get_words("scores.txt")
    score_dict = {}
    for line in content:
        name_user, score_user = line.split(":")
        score_dict[name_user] = int(score_user)
    if name in score_dict.keys():
        score_dict[name]+=score
    else:
        score_dict[name] = score
    with open("scores.txt", "w") as filename:
        pass
    with open("scores.txt", "a") as filename:
        for name_key, value in score_dict.items():
            filename.write(name_key + ":" + str(value) + "\n")



def fin():
    os.system("clear")
    print("""
    
    
                                                                     /$$$$$$$$ /$$$$$$ /$$   /$$
                                                                    | $$_____/|_  $$_/| $$$ | $$
                                                                    | $$        | $$  | $$$$| $$
                                                                    | $$$$$     | $$  | $$ $$ $$
                                                                    | $$__/     | $$  | $$  $$$$
                                                                    | $$        | $$  | $$\  $$$
                                                                    | $$       /$$$$$$| $$ \  $$
                                                                    |__/      |______/|__/  \__/    
    
    """ )

def welcome():    
    
    print("""

                                                         /$$                                            
                                                        | $$                                            
                                 /$$  /$$  /$$  /$$$$$$ | $$  /$$$$$$$  /$$$$$$  /$$$$$$/$$$$   /$$$$$$ 
                                | $$ | $$ | $$ /$$__  $$| $$ /$$_____/ /$$__  $$| $$_  $$_  $$ /$$__  $$
                                | $$ | $$ | $$| $$$$$$$$| $$| $$      | $$  \ $$| $$ \ $$ \ $$| $$$$$$$$
                                | $$ | $$ | $$| $$_____/| $$| $$      | $$  | $$| $$ | $$ | $$| $$_____/
                                |  $$$$$/$$$$/|  $$$$$$$| $$|  $$$$$$$|  $$$$$$/| $$ | $$ | $$|  $$$$$$
                                 \_____/\___/  \_______/|__/ \_______/ \______/ |__/ |__/ |__/ \_______/
                                                                                                        
                                                                        
                                                                        

                                                                                            
    """)  

    time.sleep(1)     
    print("""


                                                            $$\                                          
                                                            $$ |              
                                                            $$$$$$\ $$$$$$\  
                                                          \_$$  _|  $$  __$$\ 
                                                            $$ |    $$ /  $$ |
                                                            $$ |$$\ $$ |  $$ |
                                                           \$$$$  |\$$$$$$  |
                                                            \____/  \______/ 
                                                                                                
                    
    """)

    time.sleep(1)                                                           
    
    print("""

                             /$$$$$$$                           /$$                  /$$$$$$                                   
                            | $$__  $$                         | $$                 /$$__  $$                                  
                            | $$  \ $$ /$$$$$$  /$$$$$$$   /$$$$$$$ /$$   /$$      | $$  \__/  /$$$$$$  /$$$$$$/$$$$   /$$$$$$ 
                            | $$$$$$$//$$__  $$| $$__  $$ /$$__  $$| $$  | $$      | $$ /$$$$ |____  $$| $$_  $$_  $$ /$$__  $$
                            | $$____/| $$$$$$$$| $$  \ $$| $$  | $$| $$  | $$      | $$|_  $$  /$$$$$$$| $$ \ $$ \ $$| $$$$$$$$
                            | $$     | $$_____/| $$  | $$| $$  | $$| $$  | $$      | $$  \ $$ /$$__  $$| $$ | $$ | $$| $$_____/
                            | $$     |  $$$$$$$| $$  | $$|  $$$$$$$|  $$$$$$/      |  $$$$$$/|  $$$$$$$| $$ | $$ | $$|  $$$$$$$
                            |__/      \_______/|__/  |__/ \_______/ \______/        \______/  \_______/|__/ |__/ |__/ \_______/
                                                                                                                                                                                                                                                                                                                                                                                 

    """)              



def good_luck(name):
        print(f"""  
    


  ,----..                                            ,--,                                 ,-.         
 /   /   \                            ,---,        ,--.'|                             ,--/ /|         
|   :     :    ,---.     ,---.      ,---.'|        |  | :            ,--,           ,--. :/ |         
.   |  ;. /   '   ,'\   '   ,'\     |   | :        :  : '          ,'_ /|           :  : ' /          
.   ; /--`   /   /   | /   /   |    |   | |        |  ' |     .--. |  | :    ,---.  |  '  /           
;   | ;  __ .   ; ,. :.   ; ,. :  ,--.__| |        '  | |   ,'_ /| :  . |   /     \ '  |  :           
|   : |.' .''   | |: :'   | |: : /   ,'   |        |  | :   |  ' | |  . .  /    / ' |  |   \          
.   | '_.' :'   | .; :'   | .; :.   '  /  |        '  : |__ |  | ' |  | | .    ' /  '  : |. \         
'   ; : \  ||   :    ||   :    |'   ; |:  |        |  | '.'|:  | : ;  ; | '   ; :__ |  | ' \ \        
'   | '/  .' \   \  /  \   \  / |   | '/  '        ;  :    ;'  :  `--'   \'   | '.'|'  : |--'         
|   :    /    `----'    `----'  |   :    :|        |  ,   / :  ,      .-./|   :    :;  |,'            
 \   \ .'                        \   \  /           ---`-'   `--`----'     \   \  / '--'              
  `---`                           `----'                                    `----'                    

                            {name.upper()} 

    
     
    """)

def play_game(afficher_welcome=True):
    if afficher_welcome==True:
        welcome()  
    time.sleep(1)
    os.system("clear")
    name = input("Name: ")#nom du joueur
    os.system("clear")    
    recommandation="You will only have to guess the hidden word\nEight chances you have been granted to find it"
    print("*".join(recommandation))
    Name=name.title()
    time.sleep(7)
    os.system("clear")
    good_luck(Name)
    time.sleep(2)
    os.system("clear")
    n=8 #nombre de chance
    word_list = get_words("mots.txt")#renvoie la liste des mots
    chosen_word = generate_random_word(word_list)#renvoie le mot aleatoire
    my_list=[]
    for i in chosen_word:
        my_list+="*"
    print(*my_list)#affiche le mot à deviner masqué sous les étoiles

    for i in range(0,n):
        try:
            char_guess=input("Guess the letter of the word \n")
            while char_guess.isdecimal():# releve une exception d'erreur de valeur(l'utilisateur ne doit pas entrer un chiffre)
                char_guess=input("Please,enter letters!!!")
                os.system("clear")
                n-=1
            while len(char_guess)!=1:# vérifie le nombre de lettre entré par le joueur:pas au delà de 1
                char_guess=input("you can guess only one letter at a time")
                os.system("clear") 
                n-=1
        except:
            print("Guess the letter of the word ")
        os.system("clear")

        if char_guess in my_list:#signale une  la lettre  déjà trouvée
            print("This letter is already found")
            time.sleep(1)
            os.system("clear")
        else:
            for index, value in enumerate(chosen_word):
                if value ==char_guess :#affiche un lettre trouvée
                    my_list[index]=char_guess 
                    print("Yeah!!!Good game!!!")
                    time.sleep(1)
                    os.system("clear")
        print(*my_list) 
        
        n-=1
        print(f"you still have {n} chances")#renseignement sur le nombre de chances

        list_join = "".join(my_list)#ramène le mot qui était en liste en string
        score = ((len(my_list)- my_list.count("*")) / len(my_list)) * 100 # (nbre_caractere_trouve / nbre_caractere_total_du_mot) * 100 ; nbre_caractere_trouve = nbre_caractere_total_du_mot - nbre_detoile_dans_le_mot
        score = int(score)
        
        if n<1 :
            print(f"Le score est : {score}")
            try:
                write_score(name, score)
            except:
                pass
            continue_jeu = input(" you are out of luck\nPress -1 for a new game\nPress 2 to quit\nyour answer:")
            if continue_jeu=="1":
                play_game(False)           
            else:
                fin()
                return 0

        elif list_join == chosen_word:
            print(f"yeah!!!The hidden word was {chosen_word}")
            print(f"Le score est : {score}")
            write_score(name, score)
            
            print("""
                          /$$$$$$                                                     /$$               /$$             /$$     /$$                                     /$$ /$$
                         /$$__  $$                                                   | $$              | $$            | $$    |__/                                    | $$| $$
                        | $$  \__/  /$$$$$$  /$$$$$$$   /$$$$$$   /$$$$$$  /$$$$$$  /$$$$$$   /$$   /$$| $$  /$$$$$$  /$$$$$$   /$$  /$$$$$$  /$$$$$$$   /$$$$$$$      | $$| $$
                        | $$       /$$__  $$| $$__  $$ /$$__  $$ /$$__  $$|____  $$|_  $$_/  | $$  | $$| $$ |____  $$|_  $$_/  | $$ /$$__  $$| $$__  $$ /$$_____/      | $$| $$
                       &œ | $$      | $$  \ $$| $$  \ $$| $$  \ $$| $$  \__/ /$$$$$$$  | $$    | $$  | $$| $$  /$$$$$$$  | $$    | $$| $$  \ $$| $$  \ $$|  $$$$$$       |__/|__/
                        | $$    $$| $$  | $$| $$  | $$| $$  | $$| $$      /$$__  $$  | $$ /$$| $$  | $$| $$ /$$__  $$  | $$ /$$| $$| $$  | $$| $$  | $$ \____  $$              
                        |  $$$$$$/|  $$$$$$/| $$  | $$|  $$$$$$$| $$     |  $$$$$$$  |  $$$$/|  $$$$$$/| $$|  $$$$$$$  |  $$$$/| $$|  $$$$$$/| $$  | $$ /$$$$$$$/       /$$ /$$
                         \______/  \______/ |__/  |__/ \____  $$|__/      \_______/   \___/   \______/ |__/ \_______/   \___/  |__/ \______/ |__/  |__/|_______/       |__/|__/
                                                       /$$  \ $$                                                                                                               
                                                      |  $$$$$$/                                                                                                              
                                                       \______/                                                                                                                
                """)

            continue_jeu = input("You win the game\nPress 1 for a new game\nPress 2 to quit\nyour ans : ")
            if continue_jeu=="1":
                play_game(False)
            else:
                fin()
                return 0
    
            