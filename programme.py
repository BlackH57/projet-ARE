from tkinter import *
from random import random
from tkinter import Tk, ttk, StringVar, Label
from functools import partial
from time import sleep
from winsound import Beep

Jambe = [[("jambe1",10,20),("test",10,20)],[("jambe2",10,20)],[("jambe3",10,20)],[("jambe4",10,20)],[("jambe5",10,20)]]
Abdos = [[("abdos1",10,20)],[("abdos2",10,20)],[("abdos3",10,20)],[("abdos4",10,20)],[("abdos5",10,20)]]
Bras = [[("bras1",10,20)],[("bras2",10,20)],[("bras3",10,20)],[("bras4",10,20)],[("bras5",10,20)]]
Dos = [[("dos1",10,20)],[("dos2",10,20)],[("dos3",10,20)],[("dos4",10,20)],[("dos5",10,20)]]
Epaule = [[("Epaule1",10,20)],[("Epaule2",10,20)],[("Epaule3",10,20)],[("Epaule4",10,20)],[("Epaule5",10,20)]]

def barre_de_progression_chrono(window, action, seconde):

    
    root = Frame(window, bg = "#2C2F33")
    
    label_exercice = Label(root, text = '\n' + action +' :', font = "Helvetica", bg = "#2C2F33", fg = "White" )
    label_exercice.pack()
    
    progress = ttk.Progressbar(root, length=400, maximum=seconde*100)
    progress.pack(pady=30)
    
    progress.start(10)
    
    message = StringVar()
    w = Label(root, textvariable = message , font='Helvetica', bg = "#2C2F33", fg="White")
    w.pack()
    
    seconds = 0
    delay = 1000
    
    
    def anim(ms):
        #soundtime = 250
        message.set("Il reste :" +str(seconde - ms // 1000)+ " secondes")
        root.after(delay, anim, ms + delay)
        print(message.get())
        time = seconde-ms//1000
        # if time == seconde / 2:
        #     Beep(1000,soundtime)
        # else:
        #     if time <=5 and time != 0 : 
        #         Beep(1000,soundtime)
        if time <= 0:
            # Beep(1250,soundtime)
            progress.stop()
            root.destroy()
    
    anim(0)
    
    root.pack(expand=YES)

def randrange(debut, fin):
    return int(random()*(fin-debut+1)+debut)

def choix_exercice():
    def ensemble_exercice_possible():
        gr_Muscle = [muscle for muscle in Lb_Muscle_travail.curselection()] #transformation tuple en liste
        #print(gr_Muscle, len(gr_Muscle))
        
        ln = len(gr_Muscle) #longueur de la liste gr_Muscle
        
        diff = [diff for diff in Lb_difficulty.curselection()][0]   #difficulté de la séance
        #print(diff)
        gr_exercice = []    #groupe d'exercice à la fin
        #print(type(gr_Muscle))
        
        #Proportion du/des muscles dans la liste des exercices possible
        if ln == 1:
            quota = 10
        if ln == 2:
            quota = 5
        if ln == 3:
            quota = 4
        if ln == 4:
            quota = 3
        if ln == 5:
            quota = 2
        
        for i in range(0,quota):
            if 0 in gr_Muscle:
                gr_exercice.append(Jambe[diff])
            if 1 in gr_Muscle:
                gr_exercice.append(Abdos[diff])
            if 2 in gr_Muscle:
                gr_exercice.append(Bras[diff])
            if 3 in gr_Muscle:
                gr_exercice.append(Dos[diff])
            if 4 in gr_Muscle:
                gr_exercice.append(Epaule[diff])
                
        #gr_exercice = [exercice for ens in gr_exercice for exercice in ens]
        #print("\navant ajout exercice complémentaire :\n", gr_exercice, len(gr_exercice))
        
        ex_complementaire = [Jambe[diff],Abdos[diff],Bras[diff],Dos[diff],Epaule[diff]]
        
        gr_exercice = gr_exercice + ex_complementaire   #pour permettre d'avoir du repos pour les muscles. En faible proportion.
        #print("\naprès ajout exercice complémentaire :\n", gr_exercice, len(gr_exercice))
        
        return gr_exercice
        
    def sortie_exo_unique(liste_exercice):
        ln_ex = len(liste_exercice)
        rn1 = randrange(0,ln_ex-1)
        rn2 = randrange(0,len(liste_exercice[rn1])-1)
        exo_add = liste_exercice[rn1][rn2]
        
        return exo_add  
    
    def color():
        couleurs = ["pink", "lightgreen", "orange", "purple", "yellow", "red"]
        return couleurs[randrange(0,5)]
        
    def affichage_tableau_exercice(seance_int, liste_exercice, colonne):
        couleur = "#2C2F33"     #si on veut des couleurs plus funky on peut ecrire couleurs = color()
        taille = 20
        exercice_tuple = liste_exercice[colonne]
        exercice, effort, repos = exercice_tuple
        
        frame_exercice = Frame(seance_int, bg = couleur)
        frame_separation = Frame(seance_int, bg = "white")
        
        separation_hor1 = Label(frame_exercice, text= "----------", font = ("Helvetica", taille), bg = couleur, fg= "White")
        separation_hor2 = Label(frame_exercice, text= "----------", font = ("Helvetica", taille), bg = couleur, fg= "White")
        
        separation_vert = Label(frame_separation, text= "|\n|\n|\n|\n|\n|", font = ("Helvetica", taille), bg = couleur, fg= "White")


        label_exercice = Label(frame_exercice, text = exercice, font = ("Helvetica", taille), bg = couleur, fg = "White")
        label_effort = Label(frame_exercice, text = str(effort),font = ("Helvetica", taille), bg = couleur, fg = "White")
        label_repos = Label(frame_exercice, text = str(repos),font = ("Helvetica", taille), bg = couleur, fg = "White")
        
        label_exercice.pack()
        separation_hor1.pack()
        label_effort.pack()
        separation_hor2.pack()
        label_repos.pack()
        frame_exercice.grid(row = 0, column = 2*colonne)
        
        separation_vert.pack()
        frame_separation.grid(row = 0, column = 2*colonne+1)
        
        
    def exercice_launch(Seance, seance, n, nb_exercice):  #nom initiale exercice_launch
        if nb_exercice > n:            
            exercice,effort,repos = seance[n]
            # effort = 1
            # repos = 1
            barre_de_progression_chrono(Seance, exercice, effort)
            Seance.after(effort*1000, barre_de_progression_chrono, Seance, "repos", repos)
            Seance.after((repos+effort)*1000+2,exercice_launch, Seance,seance,n+1, nb_exercice)
        else:
            label_finish = Label(Seance, text = "La séance est finie !" , font = ('Helvetica',40),bg = "#2C2F33", fg = "White")
            label_finish.pack()
    
            
    def seance_lancement(frame, seance,nb_exercice):

        exercice_launch(frame, seance, 0, nb_exercice)
        # Seance = Tk()
        # action ="squat"
        # effort = 5
        # barre_de_progression_chrono(Seance, action, effort)
        # Seance.mainloop()
        
  
    def generate():
        """retourne une séance d'exercice (pour l'instant seulement les exercice sans temps d'effort ni de repos)"""
        #print("les muscles sont :",Lb_Muscle_travail.curselection(),"la difficulté est : ", Lb_difficulty.curselection())
        liste_exercice = ensemble_exercice_possible()
        ln_ex = len(liste_exercice)
        seance = []
        nb_exercice = 10
        
        seance_int = Tk()
        seance_int.title("Séance")
        seance_int.iconbitmap("logo.ico")
        seance_int.config(background = "#2C2F33")
        
        frame_seance = Frame(seance_int, bg = "#2C2F33")
        
        for i in range(0,nb_exercice):
            exo_add = sortie_exo_unique(liste_exercice)
            seance.append(exo_add)
            affichage_tableau_exercice(frame_seance, seance, i)
            
        #print("la séance est :\n " , seance, len(seance))
        seance_lancement_with_arg = partial(seance_lancement,seance_int, seance,nb_exercice)
        
        bouton_lancement_seance = Button(master = seance_int, text = "Lancer la séance", font=("Helvetica", 20), command = seance_lancement_with_arg)   
        
        frame_seance.pack(expand=YES)
        bouton_lancement_seance.pack()
        seance_int.mainloop()
   
        
        
    #creation format fenetre
    window = Tk()
    window.title("Programme")
    window.geometry("720x480")
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
    notice = Menu(menu_barre, tearoff = 0)
    notice.add_command(label = "Jambe")
    notice.add_command(label = "Bras")
    notice.add_command(label = "Abdos")
    notice.add_command(label = "Epaule")
    notice.add_command(label = "Dos")
    menu_barre.add_cascade(label= "notice", menu = notice)
    
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
