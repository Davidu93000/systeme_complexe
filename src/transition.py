class Transition:
    """
    Une transition est un couple d'entier positifs représentant les états source et destination
    """
    def __init__(self, a, b):
        """
        @param a: un entier correspondant à l'état source.
        @param b: un entier correspondant à l'état destination.
        """
        # Les états doivent être des entiers
        if isinstance(a, int) and isinstance(b, int):
            # Les états doivent être positif ou null
            if a >= 0 and b >= 0:
                self.src = a
                self.dest = b
            else:
                raise ValueError("Les états source et destination doivent être positifs !")
        else:
            raise TypeError("Les états source et destination doivent être des entiers !")

    def get_source(self):
        """
        @return int: Renvoie l'état source de la transition
        """
        return self.src

    def get_destination(self):
        """
        @return int: Renvoie l'état destination de la transition
        """
        return self.dest

    def print_transition(self):
        """
        Affiche la transition sous forme: Transition(src, dest)
        """
        print("Transition({}, {})".format(self.src, self.dest))

    def __eq__(self, transition):
        """
        Test si une transition t1 est égale à une autre transition t2.
        Elles sont égales si les états source et destination sont les mêmes.
        @param transition: une transition
        @return bool: True si les transitions sont les mêmes, False sinon.
        """
        # transition est bien une Transition
        if isinstance(transition, Transition):
            # Les états source et destination sont identiques
            if self.src == transition.src and self.dest == transition.dest:
                return True
            else:
                return False
        else:
            raise TypeError("Ce n'est pas une transition !")

    def __hash__(self):
        return hash((self.src, self.dest))