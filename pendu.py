solution = input("Entrer votre mot : ")
tentatives = 8
affichage = ""
lettres_trouvees = ""

for l in solution:
  affichage = affichage + "_ "

print(">> Bienvenue dans le pendu <<")

while tentatives > 0:
  print("\nMot à deviner : ", affichage)
  proposition = input("proposez une lettre : ")[0:1].lower()

  if proposition in solution:
      lettres_trouvees = lettres_trouvees + proposition
      print("-> Bien vu!")
  else:
    tentatives -= 1
    print("-> Non\n")
    if tentatives==0:
        print(" ==========Y= ")
    if tentatives<=1:
        print(" ||/       |  ")
    if tentatives<=2:
        print(" ||/       |  ")
    if tentatives<=3:
        print(" ||        0  ")
    if tentatives<=4:
        print(" ||       /|\ ")
    if tentatives<=5:
        print(" ||       /|\ ")
    if tentatives<=6:                    
        print("/||           ")
    if tentatives<=7:
        print("==============\n")

  affichage = ""
  for x in solution:
      if x in lettres_trouvees:
          affichage += x + " "
      else:
          affichage += "_ "

  if "_" not in affichage:
      print(">>> Vous avez Gagné! <<<")
      break
     
print("\n    * Fin de la partie *	")