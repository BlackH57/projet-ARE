def initialise_series():
    fichier = open("data.txt", "w")
    fichier.write("[]\n")
    fichier.close()


def add_fichier():
    text = input("que veut tu écrires dans le fichier :\n")
    fichier = open("data.txt", "a")
    fichier.write(text)
    fichier.close()

def read_fichier():
    fichier = open("data.txt", "r")
    text = fichier.read()
    print(text)
    fichier.close()


def add_value_fichier():
    fichier = open("data.txt", "r")
    value = input("quelle est la valeur ajouter: ")
    text = fichier.read()

    if text == "[]\n":
        text = "["+value+"]"
    else:
        i = 0
        while text[i] != ']':
            i += 1
        text = text[:i] + ", " + value + text[i:]
    
    fichier.close()
    fichier = open("data.txt", "w")
    fichier.write(text)
    fichier.close()

def est_chiffre(i):
    if i == '0' or i == '1' or i == '2' or i == '3' or i == '4' or i == '5' or i == '6' or i == '7' or i == '8' or i == '9':
        return 1
    else:
        return 0

def convert_txt_to_list(text):
    list_res = []
    i = 0
    text = text[1:]
    nombre = ''
    while text[i] != ']':        
        if est_chiffre(text[i]):
            nombre = nombre + text[i]
            
        if text[i]==',':
            i+=1
            
        if text[i] ==' ' :
            list_res.append(int(nombre))
            nombre = ''
        i += 1
        
    list_res.append(int(nombre))
    return list_res

#permet juste de pas avoir à ouvrir et fermer le fichier pour utiliser convert_txt_to_list
def list_from_fichiertxt():
    fichier = open("data.txt", "r")
    text = fichier.read()
    L = convert_txt_to_list(text)
    fichier.close()
    return L
