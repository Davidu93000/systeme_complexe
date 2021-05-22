from .etat import *
from .transition import *

class Kripke:
    """
    Une structure de Kripke est représenté par un couple d'ensemble de transitions et d'états
    """
    def __init__(self):
        self.etats = set()
        self.transitions = set()
                    
    def get_etats(self):
        """
        @return set: l'ensemble des états.
        """
        return self.etats

    def get_transitions(self):
        """
        @return set: l'ensemble des transitions.
        """
        return self.transitions

    def add_etat(self, etat):
        """
        Ajoute un état à la structure de Kripke.
        @param etat: l'état que l'on ajoute.
        """
        # etat est bien un Etat
        if isinstance(etat, Etat):
            self.etats.add(etat)
        else:
            raise TypeError("L'argument entré n'est pas un Etat !")

    def add_transition(self, transition):
        """
        Ajoute une transition à la structure de Kripke.
        @param transition: la transition que l'on ajoute
        """
        # transition est bien une Transition
        if type(transition) is Transition:
            # Les états source et destination existent
            if self.transition_in(transition) == True:
                self.transitions.add(transition)
            else:
                raise ValueError("Les états source et destination doivent exister !")
        else:
            raise TypeError("L'argument entré n'est pas une Transition !")

    def nb_etats(self):
        """
        @return int: le nombre d'états.
        """
        return len(self.etats)

    def nb_transitions(self):
        """
        @return int: le nombre de transitions.
        """
        return len(self.transitions)

    # Test si notre état existe dans la liste des états dans la structure de Kripke
    def etat_in(self, etat):
        """
        Test si notre état est dans l'ensemble d'états.
        @param etat: l'état que l'on test.
        @return bool: True si l'état est dans l'ensemble d'états.
        """
        # etat est bien un Etat
        if type(etat) is Etat:
            for i in self.etats:
                if etat.get_etat() == i.get_etat():
                    return True
        return False

    # Test si notre transition les états source et destination existent dans la liste des états dans la structure de Kripke
    def transition_in(self, transition):
        """
        Test si notre transition est dans l'ensemble des transitions.
        @param transition: la transition que l'on test.
        @return bool: True si la transition est dans l'ensemble des transitions.
        """
        # transition est bien une Transition
        if type(transition) is Transition:
            # Parcours les états de la structure de Kripke
            for i in self.etats:
                # On a trouvé l'état source il existe
                if transition.get_source() == i.get_etat():
                    # On reparcours la liste pour trouver l'état destination
                    for j in self.etats:
                        # On a trouvé l'état destination il existe
                        if transition.get_destination() == j.get_etat():
                            return True
        return False

    # Affiche tout les états
    def print_etats(self):
        """
        Affiche les états.
        """
        for i in self.etats:
            i.print_etat()

    # Affiche tout les transitions
    def print_transitions(self):
        """
        Affiche les transitions.
        """
        for i in self.transitions:
            i.print_transition()

    # Affiche la structure de Kripke
    def print_kripke(self):
        """
        Affiche la structure de Kripke (affiche les états et transitions)
        """
        print("Liste des états : ")
        self.print_etats()
        print("Liste des transitions : ")
        self.print_transitions()

    # OK
    def check_prop(self, prop):
        """
        Cas 1
        @param prop: la proposition à vérifier.
        @return res: un dict (etat: bool)
        """
        res = {}
        # Pour tous les états
        for e in self.etats:
            # prop est dans la liste des propositions atomiques donc True
            if prop in e.get_props():
                res[e.get_etat()] = True
            # prop n'est pas dans la liste des propositions atomiques donc False
            else:
                res[e.get_etat()] = False
        return res

    # OK
    def check_not(self, prop):
        """
        Cas 2
        @param prop: la proposition à vérifier ou un dict
        @return res: un dict (etat: bool)
        """
        res = {}
        # prop est une proposition
        if isinstance(prop, str):
            # On transforme prop en un dict (marking(phi))
            prop = self.check_prop(prop)
        # On parcours tous les propositions de prop
        for i, j in prop.items():
            # On a un True donc on aura False
            if j == True:
                res[i] = False
            # On a False donc on aura True
            else:
                res[i] = True
        return res

    # OK
    def check_and(self, prop1, prop2):
        """
        Cas 3
        @param prop1: la proposition à vérifier ou un dict.
        @param prop2: la proposition à vérifier ou un dict.
        @return res: un dict (etat: bool)
        """
        res = {}
        # prop1 est une proposition
        if isinstance(prop1, str):
            # On transforme prop1 en un dict (marking(phi1))
            prop1 = self.check_prop(prop1)
        # prop2 est une proposition
        if isinstance(prop2, str):
            # On transforme prop2 en un dict (marking(phi2))
            prop2 = self.check_prop(prop2)
        # On parcours tout prop1 (on peut faire par prop2 cela ne change rien)
        for i, j in prop1.items():
            res[i] = prop1[i] and prop2[i]        
        return res

    # OK
    def check_next(self, prop):
        """
        Cas 4
        @param prop: la proposition à vérifier ou un dict.
        @return res: un dict (etat: bool)
        """
        res = {}
        # On initialise tous à False
        for i in self.etats:
            res[i.get_etat()] = False
        # prop est une proposition
        if isinstance(prop, str):
            # On transforme prop en un dict (marking(phi))
            prop = self.check_prop(prop)
        # On parcours les transitions
        for t in self.transitions:
            # On a trouvé une transition qui à l'état destination à vrai
            if prop[t.get_destination()] == True:
                res[t.get_source()] = True
        return res

    # OK
    def check_euntil(self, prop1, prop2):
        """
        Cas 5
        @param prop1: la proposition à vérifier ou un dict.
        @param prop2: la proposition à vérifier ou un dict.
        @return res: un dict (etat: bool)
        """
        res = {}
        L = []
        seenbefore = {}
        # Initialise tout à False et seenbefore à False
        for q in self.etats:
            res[q.get_etat()] = False
            seenbefore[q.get_etat()] = False
        # prop1 est une proposition
        if isinstance(prop1, str):
            # On transforme prop1 en un dict (marking(phi1))
            prop1 = self.check_prop(prop1)
        # prop2 est une proposition
        if isinstance(prop2, str):
            # On transforme prop2 en un dict (marking(phi2))
            prop2 = self.check_prop(prop2)
        # On parcours tous les états
        for q in self.etats:
            # L'état q est vrai dans prop2 (phi2)
            if prop2[q.get_etat()] == True:
                # On ajout l'état q dans la liste L
                L.append(q.get_etat())
        # On parcours la liste l tant qu'elle n'est pas vide
        while len(L) != 0:
            # On prend un état q dans la liste L
            for q in L:
                # On met à True
                res[q] = True
                # On parcours tous les transitions
                for t in self.transitions:
                    # On a trouve une transition entrant vers q
                    if t.get_destination() == q:
                        if seenbefore[t.get_source()] == False:
                            seenbefore[t.get_source()] = True
                            if prop1[t.get_source()] == True:
                                L.append(t.get_source())
            # On enlève q de la liste L
            L.pop(-1)
        return res

    # OK
    def check_auntil(self, prop1, prop2):
        """
        Cas 6
        @param prop1: la proposition à vérifier ou un dict.
        @param prop2: la proposition à vérifier ou un dict.
        @return res: un dict (etat: bool)
        """
        res = {}
        L = []
        degree = {}
        # Initialise tout à False et les degrés de tous les états
        for q in self.etats:
            res[q.get_etat()] = False
            degree[q.get_etat()] = self.get_degree(q.get_etat())
        # prop1 est une proposition
        if isinstance(prop1, str):
            # On transforme prop1 en un dict (marking(phi1))
            prop1 = self.check_prop(prop1)
        # prop2 est une proposition
        if isinstance(prop2, str):
            # On transforme prop2 en un dict (marking(phi2))
            prop2 = self.check_prop(prop2)
        # On parcours tous les états
        for q in self.etats:
            # L'état q est vrai dans prop2 (phi2)
            if prop2[q.get_etat()] == True:
                # On ajout l'état q dans la liste L
                L.append(q.get_etat())
        # On parcours la liste l tant qu'elle n'est pas vide
        while len(L) != 0:
            # On prend un état q dans la liste L
            for q in L:
                # On met à True
                res[q] = True
                # On parcours tous les transitions
                for t in self.transitions:
                    # On a trouve une transition entrant vers q
                    if t.get_destination() == q:
                        # On décrémente son dégré
                        degree[t.get_source()] -= 1
                        if degree[t.get_source()] == 0 and prop1[t.get_source()] == True and res[t.get_source()] == False:
                            L.append(t.get_source())
                # On enlève q de la liste L
                L.pop(0)
        return res

    def get_degree(self, n):
        """
        Calcul le degrée d'un état
        @param n: un entier correspondant à l'état
        @return int: le degré sortant
        """
        res = 0
        if isinstance(n, int):
            for i in self.transitions:
                if i.get_source() == n:
                    res += 1
        else:
            raise TypeError("L'argument n'est pas un entier !")
        return res