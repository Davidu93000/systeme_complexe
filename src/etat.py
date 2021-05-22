class Etat:
    """
    Un état est un couple contenant un entier positif et un ensemble de proposition atomique qui sont vérifiées.
    """
    def __init__(self, etat, props):
        """
        @param etat: le numéro de l'état.
        @param props: une liste de propositions (liste de string).
        """
        # etat est bien un entier
        if isinstance(etat, int):
            # etat est bien positif
            if etat >= 0:
                self.etat = etat
                self.props = set()
                # props est bien une liste
                if isinstance(props, list):
                    # On parcours la liste des propositions
                    for i in props:
                        # La proposition est bien un string
                        if isinstance(i, str):
                            self.props.add(i)
                        else:
                            raise TypeError("Les propositions doivent être des strings !")
                else:
                    raise TypeError("La liste prop doit être une liste !")
            else:
                raise ValueError("L'état doit être un entier positif !")
        else:
            raise TypeError("L'état doit être un entier !")
    
    def get_etat(self):
        """
        Renvoie l'état
        @return int: Renvoie le numéro de l'état
        """
        return self.etat
    
    # Renvoie la liste des propositions
    def get_props(self):
        """
        @return set: Renvoie l'ensemble des propositions
        """
        return self.props

    # Affiche l'état
    def print_etat(self):
        """
        Affiche l'état sous forme: Etat(etat, props)
        """
        print("Etat({}, {})".format(self.etat, self.props))

    # Test si un état est égale à un autre état
    def __eq__(self, etat):
        """
        Test si deux états e1 est égale à un autre état e2.
        On considère que deux états sont égaux si elles ont le même numéro.
        @param etat: un etat
        @return bool: True si les états sont les mêmes, False sinon.
        """
        # etat est bien un Etat
        if isinstance(etat, Etat):
            # On considère que deux états sont égaux si elles ont le même numéro
            if self.etat == etat.etat:
                return True
            else:
                return False
        else:
            raise TypeError("Ce n'est pas un état !")

    def __hash__(self):
        return hash(self.etat)