from src.kripke import *

def main():
    # Charge la structure de Kripke de l'exclusion mutuelle dans le fichier in.txt
    K = charger_kripke()
    # Charge la formule CTL dans le fichier in.txt
    formule = charger_formule()

    # prop est une liste qui va stocker les éléments de la formule
    prop = []
    # tmp est une liste qui va stocker les derniers résultats
    tmp = []
    # res est le résultat
    res = {}
    while(len(formule) > 0):
        # On regarde le dernier élément de la formule
        i = formule.pop()
        # C'est un True
        if i == "True":
            print("BOOL : True")
            # On construit un dictionnaire de booléen True
            prop.append(KS_bool(K.nb_etats(), True))
        # C'est un False
        elif i == "False":
            print("BOOL : False")
            # On construit un dictionnaire de booléen False
            prop.append(KS_bool(K.nb_etats(), False))
        # C'est un not
        elif i == "not":
            print("NOT")
            # La liste prop n'est pas vide
            if len(prop) > 0:
                elem = prop.pop()
                # On va faire not(elem)
                res = K.check_not(elem)
            # La liste prop est vide
            else:
                elem = tmp.pop()
                # On va faire not(res)
                res = K.check_not(elem)
            tmp.append(res)
        # C'est un and
        elif i == "and":
            print("AND")
            # La liste prop est vide, on va regarder dans la liste tmp, et on prend les deux dernier résultats
            if len(prop) == 0:
                elem1 = tmp.pop()
                elem2 = tmp.pop()
                res = K.check_and(elem1, elem2)
            # Un seul élément dans prop, donc il va falloir faire and(elem, res)
            if len(prop) == 1:
                elem1 = prop.pop()
                elem2 = tmp.pop()
                res = K.check_and(elem1, elem2)
            # On a au moins deux éléments, on va faire and(elem1, elem2)
            elif len(prop) > 1:
                elem1 = prop.pop()
                elem2 = prop.pop()
                res = K.check_and(elem1, elem2)
            tmp.append(res)
        # C'est un next
        elif i == "next":
            print("NEXT")
            # La liste prop n'est pas vide
            if len(prop) > 0:
                elem = prop.pop()
                # On va faire next(elem)
                res = K.check_next(elem)
            # La liste prop est vide
            else:
                elem = tmp.pop()
                # On va faire next(res)
                res = K.check_next(res)
            tmp.append(res)
        # C'est un euntil
        elif i == "euntil":
            print("EUNTIL")
            # La liste prop est vide, on va regarder dans la liste tmp, et on prend les deux dernier résultats
            if len(prop) == 0:
                elem1 = tmp.pop()
                elem2 = tmp.pop()
                res = K.check_euntil(elem1, elem2)
            # Un seul élément dans prop, donc il va falloir faire euntil(elem, res)
            if len(prop) == 1:
                elem1 = prop.pop()
                elem2 = tmp.pop()
                res = K.check_euntil(elem1, elem2)
            # On a au moins deux éléments, on va faire euntil(elem1, elem2)
            elif len(prop) > 1:
                elem1 = prop.pop()
                elem2 = prop.pop()
                # On met à jour res et on pop deux éléments dans prop
                res = K.check_euntil(elem1, elem2)
            tmp.append(res)
        # C'est un auntil
        elif i == "auntil":
            print("AUNTIL")
            # La liste prop est vide, on va regarder dans la liste tmp, et on prend les deux dernier résultats
            if len(prop) == 0:
                elem1 = tmp.pop()
                elem2 = tmp.pop()
                res = K.check_auntil(elem1, elem2)
            # Un seul élément dans prop, donc il va falloir faire auntil(elem, res)
            if len(prop) == 1:
                elem1 = prop.pop()
                elem2 = tmp.pop()
                res = K.check_auntil(elem1, elem2)
            # On a au moins deux éléments, on va faire auntil(elem1, elem2)
            elif len(prop) > 1:
                elem1 = prop.pop()
                elem2 = prop.pop()
                # On met à jour res et on pop deux éléments dans prop
                res = K.check_auntil(elem1, elem2)
            tmp.append(res)
        # C'est une proposition
        else:
            print("PROP : {}".format(i))
            # On ajoute celle-ci dans la liste prop
            prop.append(i)
        print("formule : {}".format(formule))
        print("prop : {}".format(prop))
        print("tmp : {}".format(tmp))
        print("res : {}".format(get_etats_verifie(res)))
        print("-----------------")
    # La formule CTL est composé d'une seul proposition
    if len(prop) > 0:
        elem = prop.pop()
        if isinstance(elem, str):
            res = K.check_prop(elem)
        else:
            res = elem

    # Affichage du résultat
    print("Voici les états qui vérifient la formule CTL : {}".format(get_etats_verifie(res)))

def KS_bool(size, b):
    """
    True partout
    @param size: la taille du dictionnaire
    @param b: un booléen
    @return dict de taille size ou tous les éléments sont b
    """
    res = {}
    for i in range(size):
        res[i] = b
    return res

def charger_kripke():
    """
    Charge la structure de Kripke à partir du fichier in.txt
    @return la structure de Kripke correspondant
    """
    K = Kripke()
    f = open("./in.txt", "r")
    for line in f:
        l = line.strip().split(' ')
        if l[0] == 'e':
            liste = []
            for i in range(2, len(l)):
                liste.append(l[i])
            K.add_etat(Etat(int(l[1]), liste))
        elif l[0] == 't':
            K.add_transition(Transition(int(l[1]), int(l[2])))
        elif l[0] == 'f':
            print("La formule CTL : {}".format(l[1::]))
        else:
            raise Exception('Erreur, dans le fichier in.txt !')
    f.close()
    return K

def charger_formule():
    """
    Charge la formule à partir du fichier in.txt (dernière ligne)
    @return une liste
    """
    res = []
    f = open("./in.txt", "r")
    res = f.readlines()[-1].split(' ')
    return res[1::]

def get_etats_verifie(l):
    """
    Renvoie un ensemble d'états qui sont vrais
    @param l: un dictionnaire
    @return un ensemble d'états
    """
    res = set()
    if isinstance(l, dict):
        for i, j in l.items():
            if j == True:
                res.add(i)
    return res

if __name__ == "__main__":
    main()