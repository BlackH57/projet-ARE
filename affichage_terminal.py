#Je me prend (Henri) comme exemple pour l'affichage d'une personne
#à utiliser avec la base de donnée et les diverses fonctions écrites
print("\n\n\n")
print("------------- Moyennes Henri ------------- ")
print("Squat : ", moyenne(Henri_squat))
print("Relevé militaire : ", moyenne(Henri_releve))
print("Twist : ", moyenne(Henri_twist))
print("Dips : ", moyenne(Henri_dips))
print("Pont fessier jambe gauche : ", moyenne(Henri_pont_fessier_g))
print("Pont fessier jambe droite : ", moyenne(Henri_pont_fessier_d))
print("Equilibre unipodale jambe gauche : ", moyenne(Henri_equilibre_g))
print("Equilibre unipodale jambe droite : ", moyenne(Henri_equilibre_d))
print("Souplesse ischios : ", moyenne(Henri_souplesse_ischios))
print("Souplesse adducteurs : ", moyenne(Henri_souplesse_adducteurs))
print("------------------------------------------ ")

print("\n\n\n")
print("------------- Medianne Henri ------------- ")
print("Squat : ", mediane(Henri_squat))
print("Relevé militaire : ", mediane(Henri_releve))
print("Twist : ", mediane(Henri_twist))
print("Dips : ", mediane(Henri_dips))
print("Pont fessier jambe gauche : ", mediane(Henri_pont_fessier_g))
print("Pont fessier jambe droite : ", mediane(Henri_pont_fessier_d))
print("Equilibre unipodale jambe gauche : ", mediane(Henri_equilibre_g))
print("Equilibre unipodale jambe droite : ", mediane(Henri_equilibre_d))
print("Souplesse ischios : ", mediane(Henri_souplesse_ischios))
print("Souplesse adducteurs : ", mediane(Henri_souplesse_adducteurs))
print("------------------------------------------ ")

print("\n\n\n")
print("------------- Moyennes groupes ------------- ")
print("Squat : ", moyenne_dict(Squat))
print("Relevé militaire : ", moyenne_dict(Releve_militaire))
print("Twist : ", moyenne_dict(Twist))
print("Dips : ", moyenne_dict(Dips))
print("Pont fessier jambe gauche : ", moyenne_dict(Pont_fessier_g))
print("Pont fessier jambe droite : ", moyenne_dict(Pont_fessier_d))
print("Equilibre unipodale jambe gauche : ", moyenne_dict(Equilibre_g))
print("Equilibre unipodale jambe droite : ", moyenne_dict(Equilibre_d))
print("Souplesse ischios : ", moyenne_dict(Souplesse_ischios))
print("Souplesse adducteurs : ", moyenne_dict(Souplesse_adducteur))
print("------------------------------------------ ")
print("\n\n\n")
print("------------- Medianes groupes ------------- ")
print("Squat : ", mediane(dict_to_list(Squat)))
print("Relevé militaire : ", mediane(dict_to_list(Releve_militaire)))
print("Twist : ", mediane(dict_to_list(Twist)))
print("Dips : ", mediane(dict_to_list(Dips)))
print("Pont fessier jambe gauche : ", mediane(dict_to_list(Pont_fessier_g)))
print("Pont fessier jambe droite : ", mediane(dict_to_list(Pont_fessier_d)))
print("Equilibre unipodale jambe gauche : ", mediane(dict_to_list(Equilibre_g)))
print("Equilibre unipodale jambe droite : ", mediane(dict_to_list(Equilibre_d)))
print("Souplesse ischios : ", mediane(dict_to_list(Souplesse_ischios)))
print("Souplesse adducteurs : ", mediane(dict_to_list(Souplesse_adducteur)))
print("------------------------------------------ ")