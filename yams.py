import random

des = []
des_completes_adversaire = []
des_completes_joueur = []

tableau_score_adversaire = {}
tableau_score_joueur = {}


def jet_des():
    """Génère aléatoirement 5 dés entre 1 et 6"""
    while len(des) < 5:
        jet = random.randint(1, 6)
        des.append(jet)


def comparaison(des):
    """Compare les dés jetés aux dés déjà complétés"""
    if (des in des_completes_adversaire):
        return False
    else:
        return True


def filtrage(des):
    """Filtre les dés en fonction de leur présence dans la liste"""
    global des_selectionnes
    des_selectionnes = list(filter(comparaison, des))


def des_plus_frequent(des):
    """Détermine la valeur de dé la plus occurente"""
    if des:
        return max(set(des), key=des.count)


def compte_des(des, des_manche):
    """Compte le nombre d'occurence de la valeur selectionnée"""
    if des:
        return des.count(des_manche)


def tour_adversaire():
    """Fais jouer la manche de l'adversaire"""
    global des
    global total_adversaire
    for i in range(3):

        jet_des()
        print("Tour de l'adversaire", des)

        filtrage(des)
        des = des_selectionnes  # réassigne la valeur des dés jeté à dé
        des_manche = (des_plus_frequent(des))  # dé manche est dé le + fréquent

        compte_des(des, des_manche)
        occurences_des = des.count(des_manche)

        des.clear()
        for i in range(occurences_des):
            des.append(des_manche)

    # si il y a au moins un dé égal à une valeur non attribuée après 3 lancers
    # ajouter la valeur du dé aux valeurs non utilisables et attribuer le score
    if des_manche is not None:
        des_completes_adversaire.append(des_manche)
        score_manche = occurences_des*des_manche
    # si aucune valeur utilisable,  0 dans la valeur la + faible non utilisée
    else:
        score_manche = 0
        des_manche = 1
        while des_manche in des_completes_adversaire:
            des_manche = des_manche+1

    # attribuer la valeur de score de cette manche à la valeur
    tableau_score_adversaire[des_manche] = score_manche
    total_adversaire = 0

    for i in tableau_score_adversaire.values():
        total_adversaire += i

    print("Les valeurs de dés déjà lancées par l'adversaire", des_completes_adversaire)
    print("Le tableau des scores de l'adversaire est", tableau_score_adversaire, " et son score total est", total_adversaire)


def tour_joueur():
    """Lance la manche de l'utilisateur"""
    global des
    global total_joueur
    for i in range(3):

        jet_des()
        print("Votre main :", des)

        des_manche = 0

        while des_manche == 0:
            choix = input("Quelle valeur souhaitez-vous sauvegarder pour cette manche?")

            try:
                choix = int(choix)

                if choix in des_completes_joueur:
                    print("Choisissez une valeur non utilisée")

                elif choix > 6 or choix < 1:
                    print("Choisissez une valeur entre 1 et 6")

                else:
                    des_manche = int(choix)

            except ValueError:
                print("Choisissez un chiffre")

        compte_des(des, des_manche)
        occurences_des = des.count(des_manche)

        des.clear()
        for i in range(occurences_des):
            des.append(des_manche)

    # ajouter le dé utilisé à la liste des dés complétés
    des_completes_joueur.append(des_manche)
    print("Les valeurs de dés déjà lancées par vous", des_completes_joueur)

    # calcul du score pour cette manche et ajout du score dans la liste
    score_tot = occurences_des*des_manche
    tableau_score_joueur[des_manche] = score_tot
    total_joueur = 0
    for i in tableau_score_joueur.values():
        total_joueur += i
    print("Tableau des scores:", tableau_score_joueur, "Score total est", total_joueur)


for i in range(6):
    tour_adversaire()
    des.clear()
    tour_joueur()
    des.clear()

if total_joueur > total_adversaire:
    print("Vous avez gagné")
else:
    print("L'adversaire a gagné")
