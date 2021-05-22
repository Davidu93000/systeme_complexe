# Model Checker

* [Consignes](#Consignes)
* [Pré-requis](#Pré-requis)
* [Contenu](#Contenu)
* [Le rapport](#Le-rapport)
* [Le fichier in.txt](#Le-fichier-intxt)
* [Le fichier main.py](#Le-fichier-mainpy)
* [Le fichier test.py](#Le-fichier-testpy)
* [Amélioration](#Amélioration)

# Consignes

L'objectif de ce mini-projet est de développer un model checker pour la logique CTL. Partant des algorithmes de vérification vus en cours (Slides 56-63), il vous est demandé  d'implémenter, dans un langage de programmation de votre choix, un model checker CTL ayant comme entrée un fichier contenant une description textuelle d'une structure de Kripke (KS) et une formule CTL. En sortie, on a une réponse quant à la satisfaction de la formule donnée par le système représenté par la structure de Kripke. Vous devez choisir les structures de données adéquates pour représenter les deux formalismes en question (KS et formule CTL).

Pour les plus avancés, l'implémentation peut être adaptée au modèle des réseaux de Petri :  La structure de Kripke peut dans ce cas représenter le graphe des marquages du réseau de Petri donné en entrée.

Ce projet peut être fait en binômes. La deadline pour rendre votre projet est le 15 janvier 2021.

# Pré-requis

- [Python](https://www.python.org/).
- Notions [CTL](https://en.wikipedia.org/wiki/Computation_tree_logic), [LTL](https://en.wikipedia.org/wiki/Linear_temporal_logic), [Model-checking](https://en.wikipedia.org/wiki/Model_checking), [Structure de Kripke](https://en.wikipedia.org/wiki/Kripke_structure_(model_checking))

## Contenu

- Un rapport expliquant les structures de données utilisées, choix d'implémentations, perspectives d'amélioration et application sur quelques exemples.
- Un fichier README.MD contenant les instructions.
- Un dossier `src` contenant les codes en python
    - `kripke.py`
    - `etat.py`
    - `transition.py`
- Deux fichiers python
    - `main.py`
    - `test.py`
- Un dossier `images` contenant des captures d'écran.
- Un fichier `in.txt` qui aura comme contenu la structure de Kripke et la formule CTL.
- Un fichier `in.txt.bak` pour permettre de revenir avec la structure de Kripke par défaut.

## Afficher un graphe

Installer `pip3`

```shell
sudo apt install pip3
```

Puis installer le package `igraph`

```
pip3 install igraph
```

## Le rapport

Pour générer le rapport en pdf

```
latex rapport.tex
```

## Le fichier `in.txt`

C'est dans ce fichier que nous allons mettre notre structure de Kripke ainsi qu'une formule CTL.

Dans le fichier `in.txt`, il s'agit de l'exemple de l'exclusion mutuelle vu en cours.

On peut modifier notre structure de Kripke en changeant le contenu de ce fichier.

Sur chaque ligne, on va commencer par mettre une lettre qui indique si la ligne est un état ou une transition (`e` pour un état, `t` pour une transition, `f` pour la formule).

La dernière ligne de ce fichier sera la formule CTL.

- Pour les états, on va mettre un entier qui sera le numéro de l'état, puis une suite de propositions atomiques qui sont vérifiés dans cet état.
- Pour les transitions, on va mettre deux entiers, le premier pour l'état source, et la deuxième pour l'état destination.
- Pour la formule, on mettra la séquence d'exécution de notre model checker.

Pour les formules : on utilise les mots-clés qui sont :
- `True`
- `False`
- `not` pour le non logique
- `and` pour le et logique
- `next` pour le next
- `euntil` pour le exist until
- `auntil` pour le always until

Voici un exemple :

```
e 1 p q
e 2 p
e 3 q
t 1 2
t 2 3
t 3 3
f and p q
```
La formule ici correspond à $p \land q$

## Le fichier `main.py`

C'est là que nous allons tester la structure de Kripke entré dans le fichier `in.txt`

Dans un terminal, tapez `python3 main`

## Le fichier `test.py`

Il s'agit des tests sur les différents cas de notre model checker. Les cas utilisés sont dans le rapport.

Dans un terminal, tapez `python3 test.py`

## Amélioration
- Visualisation des structures de Kripke avec un graphe (utilisation du package igraph)
- Vérifier que la formule CTL entré est syntaxiquement correcte ($p \land q \land$ n'est pas valide)
- La conversion automatique des formules CTL (transformation des $\Rightarrow$, $\lor$, etc.)
- Faire un model checker sur les formules LTL
- Essayer de faire ce projet avec des réseaux de pétri
- Améliorer du code
- Afficher la structure de Kripke avec un graphe