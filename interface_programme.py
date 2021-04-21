from tkinter import *


def programme():
    def generate():
        #pour l'instant generate renvoie la liste des positions des muscles dans la Listbox
        print("les muscles sont :",Lb_Muscle_travail.curselection(),"la difficulté est : ", Lb_difficulty.curselection())
        
        
    #creation format fenetre
    window = Tk()
    window.title("Programme")
    window.geometry("1080x720")
    window.iconbitmap("logo.ico")
    window.config(background="#2C2F33")
    
    #creation frame mere
    frame = Frame(window, bg ="#2C2F33")
    #creation frame des muscles
    muscle_frame = Frame(frame, bg = "#2C2F33")
    #creation frame de la difficulte
    diff_frame = Frame(frame, bg = "#2C2F33")
    
    #creation de la liste des muscles que nous allons travailler et son label
    label_muscle = Label(muscle_frame, text = "Quels muscles voulez vous travailler : ", font = ("Helvetica", 10), bg = '#2C2F33', fg ="white")
    
    Lb_Muscle_travail = Listbox(muscle_frame, width = 20, height = 5 ,selectmode = "multiple" , selectbackground ="grey", exportselection = 0, activestyle = 'none')
    Lb_Muscle_travail.insert(1, "Jambe")
    Lb_Muscle_travail.insert(2, "Abdos")
    Lb_Muscle_travail.insert(3, "Bras")
    Lb_Muscle_travail.insert(4, "Dos")
    Lb_Muscle_travail.insert(5, "Epaule")
    
    #creation liste difficulte pour la seance
    label_difficulty = Label(diff_frame, text = "Difficulté de la séance : ", font = ("Helvetica", 10), bg = '#2C2F33', fg ="white" )

    yDefilB = Scrollbar(diff_frame, orient='vertical')
    yDefilB.grid(row =1, column=1)

    Lb_difficulty = Listbox(diff_frame, width = 20, height = 1 ,selectmode = "single" , selectbackground ="grey",exportselection = 0, activestyle = 'none',yscrollcommand=yDefilB.set)
    Lb_difficulty.insert(1, "Très facile")
    Lb_difficulty.insert(2, "Facile")
    Lb_difficulty.insert(3, "Normal")
    Lb_difficulty.insert(4, "Difficile")
    Lb_difficulty.insert(5, "Très difficile")
    
    yDefilB['command'] = Lb_difficulty.yview  
    
    #creation menu déroulant pour les notices exerices
    menu_barre = Menu(window)
    file_menu = Menu(menu_barre, tearoff=0)
    file_menu.add_command(label="Nouveau")
    #file_menu.add_command(label = "Exercices", command = notice_exercice)
    file_menu.add_command(label="Quitter", command=window.quit)
    menu_barre.add_cascade(label="fichier", menu=file_menu)
    
    #config fenetre pour avoir cette barre
    window.config(menu=menu_barre)
    
    #creation bouton pour generer la seance
    button_generate = Button(frame, text = "Generer", font=("Helvetica", 10), command = generate)
    
    label_difficulty.grid(row=0,column=0)
    Lb_difficulty.grid(row=1, column=0)
    
    label_muscle.pack()
    Lb_Muscle_travail.pack()
    
    
    muscle_frame.grid(row = 0, column = 0, sticky = W)
    diff_frame.grid(row = 0, column = 2, sticky = E)
    button_generate.grid(row=5,column = 1)

    
    frame.pack(expand=YES)
    
    window.mainloop()
    
    
#programme()
