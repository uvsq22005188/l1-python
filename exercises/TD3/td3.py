temps = (4, 23, 1, 34)


def tempsEnSeconde(temps):
    """ Renvoie la valeur en seconde de temps donné comme jour,
     heure, minute, seconde."""
    tempsEnSeconde = temps[3] + temps[2] * 60 + temps[1] * 60 * 60 + temps[0] * 60 * 60 * 24
    return(tempsEnSeconde)


print(tempsEnSeconde(temps), "secondes")


seconde = 100000

def secondeEnTemps(seconde):
    """Renvoie le temps (jour, heure, minute, seconde)
     qui correspond au nombre de seconde passé en argument"""
    jour, seconde = divmod(seconde, 86400)
    heure, seconde = divmod(seconde, 3600)
    minute, seconde = divmod(seconde, 60)
    return (jour , heure, minute, seconde)


print(secondeEnTemps(seconde))


listejhms = ["Jour", "Heure", "Minute", "Seconde"]
liste_jhms_pluriel = []
tempsliste = []

def ajoutListe(temps):
    '''Enleve l'unité si égal à 0'''
    for c in range(1):
        if c != 0:
            tempsliste.append(temps[c])


def pluriels(temps):
    '''Met les mots au pluriels ou laisse au singulier'''
    for i in range(4):
        if temps[i] == 1:
            liste_jhms_pluriel.append(listejhms[i])
            tempsliste.append(temps[i])
        elif temps[i] > 1:
            liste_jhms_pluriel.append(listejhms[i] + "s")
            tempsliste.append(temps[i])
        pass


def afficheTemps(temps):
    '''Affiche le temps'''
    ajoutListe(temps)
    print(pluriels(temps))
    for x in range(len(tempsliste)):
        print(tempsliste[x], liste_jhms_pluriel[x], end=(", "))
    print("")
    return demandeTemps(temps)


def demandeTemps(temps):
    '''demande un temps et verifie qu'il soit valable'''
    temps=[]
    temps = str(input("Entrez une date avec des espaces: "))
    temps = temps.split()
    tempsint = []
    for p in range(4):
        tempsint.append(int(temps[p]))
    if tempsint[1] > 24:
        print("Heures supérieur à 24 !")
        tempsint[1] = int(input("Entrez une heure valide: "))
    if tempsint[2] > 60:
        print("Minutes supérieur à 60 !")
        tempsint[2] = int(input("Entrez une minute valide: "))
    if tempsint[3] > 60:
        print("Secondes supérieur à 60 !")
        tempsint[3] = int(input("Entrez une seconde valide: "))
    temps = tempsint
    return temps

print(afficheTemps(temps))

def sommeTemps(temps1, temps2):
    return secondeEnTemps(tempsEnSeconde(temps1) + tempsEnSeconde(temps2))

print(sommeTemps((2,3,4,25),(1,2,3,4)))