import random
from statistics import mode

#valeurs prises par les dés jetés
des=[]

#valeurs déjà présentes dans le tableau des scores de l'adversaire et du joueur
des_completes_adversaire=[]
des_completes_joueur=[]

#dictionnaires contenant les scores de l'adversaire et du joueur
dic_score_adversaire= {}
dic_score_joueur= {}

#fonction permettant de générer aléatoirement 5 valeurs de dés entre 1 et 6
def jet_des ():
    while len(des) < 5:
        jet=random.randint(1,6)
        des.append(jet)

#fonction donnant la condition de comparaison (si la valeur est dans la liste)
def comparaison (des):
    if (des in des_completes_adversaire):
        return False
    else:
        return True
    
#fonction permettant de filtrer les dés selon la condition établie précedemment
def filtrage (des):
    global des_selectionnes
    des_selectionnes=list(filter(comparaison, des))

#fonction permettant de déterminer la valeur la + occurente dans la liste (si la liste n'est pas vide)
def des_plus_frequent(des):
    if des:
        return max(set(des), key = des.count)
    
# fontion permettant de compter le nombre d'occurences de cette valeur (si la liste n'est pas vide)
def compte_des(des, des_manche):
    if des:
        return des.count(des_manche)

def tour_adversaire ():
    global des
    global total_adversaire
    for i in range (3):

        jet_des()
        print("Les dés jetés par l'adversaire:",des)

        #vérifier que la valeur du dé choisi est toujours disponible
        filtrage(des)
        des=des_selectionnes

        #valeur sélectionnée pour cette manche (la + occurente)
        des_manche = (des_plus_frequent(des))

        compte_des(des,des_manche)

        #nombre de fois où cette valeur apparaît
        occurences_des=des.count(des_manche)

        #supprimer les valeurs non sélectionnées pour ne garder que les valeurs à conserver pour le prochain jet
        des.clear()

        for i in range (occurences_des):
            des.append(des_manche)
    
    #si il y a au moins un dé correspondant à une valeur non attribuée au terme des 3 lancers :
    #ajouter la valeur du dé aux valeurq non utilisables et attribuer le score 
    if des_manche:
        des_completes_adversaire.append(des_manche)
        score_manche = occurences_des*des_manche
    #si aucune valeur n'est utilisable, mettre 0 dans la valeur la plus faible non utilisée
    else:
        score_manche=0
        des_manche=1
        while des_manche in des_completes_adversaire:
            des_manche=des_manche+1
    
    #attribuer la valeur de score de cette manche à la valeur
    dic_score_adversaire[des_manche] = score_manche

    total_adversaire=0

    #somme total du score
    for i in dic_score_adversaire.values():
        total_adversaire += i

    print("Les valeurs de dés déjà lancées par l'adversaire",des_completes_adversaire)
    print("Le tableau des scores de l'adversaire est",dic_score_adversaire," et son score total est",total_adversaire)

def tour_joueur ():
    global des
    global total_joueur
    for i in range (3):

        jet_des()
        
        print("Les dés jetés par vous :",des)

        demande_des_manche = input("Quelle valeur souhaitez vous sauvegarder pour cette manche?")

        des_manche = int(demande_des_manche)

        while des_manche in des_completes_joueur:
            print ("Cette valeur a déjà été attribuée, veuillez en choisir une autre")
            demande_des_manche = input("Quelle valeur souhaitez vous sauvegarder?")
            des_manche = int(demande_des_manche)
        
        while des_manche>6 or des_manche<1:
            print ("Veuillez choisir une valeur entre 1 et 6")
            demande_des_manche = input("Quelle valeur souhaitez vous sauvegarder?")
            des_manche = int(demande_des_manche)

        compte_des(des,des_manche)

        occurences_des=des.count(des_manche)

        des.clear()

        for i in range (occurences_des):
            des.append(des_manche)

    #ajouter le dé utilisé à la liste des dés complétés
    des_completes_joueur.append(des_manche)
    print("Les valeurs de dés déjà lancées par vous",des_completes_joueur)
    
    #calcul du score pour cette manche et ajout du score dans la liste
    score_tot = occurences_des*des_manche
    dic_score_joueur[des_manche] = score_tot
    total_joueur=0
    for i in dic_score_joueur.values():
        total_joueur += i
    print("Votre tableau des scores",dic_score_joueur," et votre score total est",total_joueur)

for i in range(6):
    tour_adversaire()
    des.clear()
    tour_joueur()
    des.clear()

if total_joueur>total_adversaire:
    print("Vous avez gagné")
else:
    print("L'adversaire a gagné")