"""
Ascii art 
"""


#### Fonctions secondaires


def artcode_i(s):
    """Ascii art algorithme itératif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    o = [1]
    c = [s[0]]
    n = len(s)
    for k in range(1,n) :
        if s[k] == s[k-1] :
            o[-1]+=1
        else :
            c.append(s[k])
            o.append(1)
    return list(zip(c,o))


def artcode_r(s):
    """ascii art algorithme récursif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    n=len(s)
    # cas de base
    if n == 0 :
        return []
    # recherche nombre de caractères identiques au premier
    i = 1
    while i<n and s[i] == s[0]:
        i+=1
    tup = (s[0],i)
    # appel récursif
    return [tup] + artcode_r(s[i:])

#### Fonction principale

def main():
    """
    Fonction maingit
    """
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
