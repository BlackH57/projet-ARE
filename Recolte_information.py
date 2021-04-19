#demande de la difficulte

def diff_deb():

   print("Quel difficulté de programme voulez vous suivre :")
   print("1   2   3\n")
   n = int(input("Indiquez le numero: \n"))

   return n

def diff_fin():
    print("La séance était-elle dur :\n")
    prinmusclet("1   2   3\n")
    n = int(input("Indiquez le numero:\n"))
    
    return n
  
#donne utilisateur
def entree_donnee_utilisateur():
   prenom = input("\nQuel est ton prénom :") #demande d'écrire "prenom"
   age = int(input("Quel est ton age : "))
   taille = float(input("Quelle est ta taille : "))
   pratique_sport = reg_sport()
   print ("Bonjour"+prenom+"!")
   #print ("Tu as",age,"ans et tu mesures",taille,"m.")

   return (prenom,age,taille,pratique_sport)
