from tkinter import *
from programme import *

def logging_hub():
  def verification_mdp_and_users():
      user = user_entry.get()
      password = password_entry.get()
      fichier = open("mdp_and_users.txt", "r")
      logs = "(" + user + "," + password + ")"
      if logs in fichier.read():
        print("Valide")
        window.quit()
        programme()
        return 1
        
      else:
        print("Non valide")
        return 0

  #creer la fenetre
  window = Tk()
  window.title("Logging hub")
  window.geometry("720x480")
  window.iconbitmap("logo.ico")
  window.config(background="#2C2F33")

  #creation frame principal
  frame = Frame(window, bg="#2C2F33")

  #def verification_password():
  #creation image
  width = 200
  height = 200
  image = PhotoImage(file="fond.png")
  canvas = Canvas(frame, width=width, height = height, bg = '#2C2F33', bd=0, highlightthickness = 0)
  canvas.create_image(width/2, height/2, image=image)
  canvas.grid(row = 0, column = 0, sticky=W)

  #creer une sous boite
  right_frame = Frame(frame, bg= "#2C2F33")


  #creer un titre
  label_utilisateur = Label(right_frame, text = "Utilisateur:", font =("Helvetica", 20), bg ="#2C2F33", fg = 'white')
  label_utilisateur.pack()

  #creer un champ utilisateur
  user_entry = Entry(right_frame, font=("Helvetica", 20), bg = "White", fg = '#2C2F33')
  user_entry.pack()

  #creer un titre
  label_password = Label(right_frame, text = "Mot de passe:", font =("Helvetica", 20), bg ="#2C2F33", fg = 'white')
  label_password.pack()

  #creer un champ mot de passe
  password_entry = Entry(right_frame, font=("Helvetica", 20), bg = "White", fg = '#2C2F33')
  password_entry.pack()

  #bouton validation
  button_validation_password = Button(right_frame, text = "Verifier", font=("Helvetica", 20), bg = "White", fg = '#2C2F33', command = verification_mdp_and_users)
  
  button_validation_password.pack(fill=X)

  #création barre de menu
  menu_barre = Menu(window)

  #creer un menu
  file_menu = Menu(menu_barre, tearoff=0)
  file_menu.add_command(label="Nouveau")
  file_menu.add_command(label="Quitter", command=window.quit)
  menu_barre.add_cascade(label="fichier", menu=file_menu)
  #config fenetre pour avoir cette barre
  window.config(menu=menu_barre)



  #on place la frame a droite de la frame principale
  right_frame.grid(row=0,column=1, sticky=E)
  #afficher frame
  frame.pack(expand=YES)
  #afficher la fenetre
  window.mainloop()
  
 
