#### Imports et définition des variables globales


#### Fonctions secondaires


def artcode_i(s):
    """retourne la liste de tuples encodant une chaîne de caractères passée en argument selon un algorithme itératif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    
    # votre code ici
    l = []
    i = 1
    while(s[i]==s[0]):
        i+=1
    ev = (s[0],i)
    l.append(ev)
    return l.append(artcode_i(s[i:]))


def artcode_r(s):
    """retourne la liste de tuples encodant une chaîne de caractères passée en argument selon un algorithme récursif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    
    # votre code ici
    l = []
    i = 0
    while (s[i]==s[0]):
        i+=1
    ev = (s[0],i)
    l.append(ev)
    return l.append(artcode_i(s[i:]))
    # cas de base
    # recherche nombre de caractères identiques au premier
    # appel récursif

    return []
    

#### Fonction principale


def main():
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
