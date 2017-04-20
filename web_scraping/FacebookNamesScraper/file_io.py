import string
import random
def read_file(file_name):
    file = open(file_name,"r")
    text = file.read()
    liste = text.split("\n")
    return  liste

def heal_name(name):
    char = name
    liste = char.split("'")
    if(len(liste)>1):
        new_char = liste[0] + liste[1]
        return(new_char)
    else:
        return(name)



def login_generator(name):
    try:
        test_liste = name.split()
        for i in range(0,len(test_liste)):
            test_liste[i] = heal_name(test_liste[i])
        if (len(test_liste) > 2):
            first_name = test_liste[0] + "_" + test_liste[1]
            return(first_name + "." + test_liste[2])
        else:
            return(test_liste[0] + "." + test_liste[1])
    except IndexError:
        pass


def password_generator(size=6,chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def creat_accounts(file):
    liste = read_file(file)
    dico = {}
    for i in range(0, len(liste)):
        dico[login_generator(liste[i])] = password_generator()
    for i in dico.keys():
        print("--LOGIN--: "+i+"         --PASSWORD-- "+dico[i] )

print(creat_accounts("names.txt"))
