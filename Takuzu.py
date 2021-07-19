from upemtk import *  

CHEMIN_VERS_FICHIER = 'puzzle.txt'

def puzzle(CHEMIN_VERS_FICHIER):
    '''
    Fonction qui va parcourir le fichier texte puzzle et va renvoyer ce dernier sous forme d'une liste de listes
    :Param CHEMIN_VERS_FICHIER: Chemin du fichier texte puzzle
    :Return value: ListePuzzle, une liste de listes représentant le puzzle
    >>>puzzle(CHEMIN_VERS_FICHIER)
    (lorsque puzzle.txt :
     1 0
      0 
     0  
    11   )
    [[' ', '1', ' ', '0'], [' ', ' ', '0', ' '], [' ', '0', ' ', ' '], ['1', '1', ' ', ' ']]
    '''
    f = open(CHEMIN_VERS_FICHIER)
    ListePuzzle = []
    lst2 = []
    
    for ligne in f:
        lst2 = []
        ligne = ligne.replace('\n','')
        for e in ligne:
            lst2.append(e)
        ListePuzzle.append(lst2)
    
    return ListePuzzle

def remplir_case(yCase, xCase, Valeur, LstPuzNMod, LstPuzMod):
    '''
    Fonction qui modifie la valeur d'une case et ne la modifie que si cette valeur est modifiable.
    :Param xCase, yCase: Coordonnées de xCase et yCase en case
    :Param Valeur: Valeur que l'utilisateur souhaite assigner à la case
    :Param LstPuzNMod: Une liste de listes représentant le puzzle initial
    :Param LstPuzMod: Une liste de listes représentant le puzzle actuel    
    :Return value: ListePuzMod, une liste de listes représentant le puzzle actuel modifié
    >>>remplir_case(2, 3, 1, LstPuzNMod, LstPuzMod)
    ( lorsque LstPuzMod = 
    [' ', '1', ' ', '0']
    [' ', ' ', '0', ' ']
    [' ', '0', ' ', ' ']
    ['1', '1', ' ', ' ']
    
    [' ', '1', ' ', '0']
    [' ', ' ', '0', ' ']
    [' ', '0', ' ', ' ']
    ['1', '1', '1', ' ']
    
    >>>remplir_case(1, 0, 1, LstPuzNMod, LstPuzMod)
    ( lorsque LstPuzMod = 
    [' ', '1', ' ', '0']
    [' ', ' ', '0', ' ']
    [' ', '0', ' ', ' ']
    ['1', '1', ' ', ' ']
    
    [' ', '1', ' ', '0']
    [' ', ' ', '0', ' ']
    [' ', '0', ' ', ' ']
    ['1', '1', ' ', ' '] )
    
    '''
    if LstPuzNMod[xCase][yCase] != '1' and LstPuzNMod[xCase][yCase] != '0':
            if Valeur == '1' or Valeur == '0' or Valeur == ' ':
                LstPuzMod[xCase][yCase] = Valeur
            else:
                print('Valeur incorrecte!')
    else:
        print('Vous ne pouvez pas modifier cette valeur!')
    return LstPuzMod

def lst_colonnes(LstPuzMod):
    '''
    Fonction qui renvoie une liste de listes représentant les colonnes du puzzle.
    :Param LstPuzMod: Une liste de listes représentant le puzzle actuel 
    :Return value: lst_colonnes, une liste de listes représentant les colonnes du puzzle
    >>>lst_colonnes(LstPuzMod)
    ( lorsque LstPuzMod = 
    [' ', '1', ' ', '0']
    [' ', ' ', '0', ' ']
    [' ', '0', ' ', ' ']
    ['1', '1', ' ', ' ']
    
    [[' ', ' ', ' ', '1'], ['1', ' ', '0', '1'], [' ', '0', ' ', ' '], ['0', ' ', ' ', ' ']]
    '''
    i = 0
    lst_colonnes = []
    while i < len(LstPuzMod):
        j = 0
        colonne = []
        while j < len(LstPuzMod):
            a = LstPuzMod[j]
            colonne.append(a[i])
            j += 1
        lst_colonnes.append(colonne)
        i += 1
    return lst_colonnes
    
def check_lignes(LstPuzMod):
    '''
    Fonction qui pour chaque ligne du puzzle si elle est remplie ou non.
    :Param LstPuzMod: Une liste de listes représentant le puzzle actuel 
    :Return value: ligne_remplie, une liste de listes représentant le puzzle avec : la ligne si elle est remplie, ou l'élement vide ( ' ' ) si elle ne l'est pas.
    >>>check_lignes(LstPuzMod)
    ( lorsque LstPuzMod = 
    [' ', '1', ' ', '0']
    [' ', ' ', '0', ' ']
    ['1', '0', ' ', ' ']
    ['1', '1', ' ', ' '] )
    
    [' ', ' ', ' ', ' ']
    
    >>check_lignes(LstPuzMod)
    ( lorsque LstPuzMod =
    [' ', '1', ' ', '0']
    [' ', ' ', '0', ' ']
    ['1', '0', ' ', ' ']
    ['1', '1', '0', '0'] )
    
    [' ', ' ', ' ', ['1', '1', '0', '0']]
    '''
    i = 0
    ligne_remplie = []
    while i < len(LstPuzMod):
        if ' ' not in LstPuzMod[i]:
            ligne_remplie.append(LstPuzMod[i])
        else:
            ligne_remplie.append(' ')
        i += 1
    return ligne_remplie

def check_colonnes(LstPuzMod):
    '''
    Fonction qui verifie si une colonne est remplie ou non.
    :Param LstPuzMod: Une liste de listes représentant le puzzle actuel 
    :Return value: colonne_remplie, une liste de listes représentant le puzzle avec : la colonne si elle est remplie, ou l'élement vide ( ' ' ) si elle ne l'est pas.
    >>>check_colonnes(LstPuzMod)
    ( lorsque LstPuzMod = 
    [' ', '1', ' ', '0']
    ['0', ' ', '0', ' ']
    ['1', '0', ' ', ' ']
    ['1', '1', ' ', ' '] )
    
    [' ', ' ', ' ', ' ']
    >>>check_colonnes(LstPuzMod)
    ( lorsque LstPuzMod =
    ['0', '1', ' ', '0']
    ['0', ' ', '0', ' ']
    ['1', '0', ' ', ' ']
    ['1', '1', ' ', ' ']
    [' ', ' ', ' ', ' '] )
    
    [['0', '0', '1', '1'], ' ', ' ', ' ']
    
    '''
    i = 0
    colonne_remplie = []
    while i < len(LstPuzMod):
        j = 0
        colonne = []
        while j < len(LstPuzMod):
            a = LstPuzMod[j]
            colonne.append(a[i])
            j += 1
        if ' ' not in colonne:
            colonne_remplie.append(colonne)
        else:
            colonne_remplie.append(' ')
        i += 1
    return colonne_remplie

def check_plateau(LignesRemplies):
    '''
    Fonction qui verifie si le plateau est remplie ou non.
    :LignesRemplies: La liste représentant le plateau avec les lignes remplies ainsi que les lignes non remplies (représentés par l'élement vide ( ' ' )).
    :Return value: True si le plateau est remplie sinon False.
    >>>check_plateau(LignesRemplies)
    ( lorsque LstPuzMod =
    [' ', '1', ' ', '0']
    [' ', ' ', '0', ' ']
    ['1', '0', ' ', ' ']
    ['1', '1', ' ', ' '] )
    False
    >>>check_plateau(LignesRemplies)
    ( lorsque LstPuzMod =
    ['0', '1', '1', '0']
    ['0', '1', '0', '1']
    ['1', '0', '1', '0']
    ['1', '1', '0', '0'] )
    True
    '''
    v = False
    if ' ' not in LignesRemplies:
        print('Plateau remplie')
        v = True
    return v
        

def condition1(LstPuzMod):
    '''
    Fonction qui va vérifier si il y a 3 cases identiques alignés ou non sur chaques lignes et chaques colonnes
    :Param LstPuzMod: Une liste de listes représentant le puzzle actuel 
    :Return value V: False si il y a 3 cases identiques alignés sinon True
    :Return value coor_cond1Ligne: Liste de listes représentant les coordonnées en cases des 3 cases identiques alignés sur une ligne
    :Return value coor_cond1Col: Liste de listes représentant les coordonnées en cases des 3 cases identiques alignés sur une colonne
    >>>condition1(LstPuzMod)
    ( où LstPuzMod =
    [' ', '1', ' ', '0']
    [' ', ' ', '0', ' ']
    [' ', '0', ' ', ' ']
    ['1', '1', ' ', ' '] )
    True [] []
    >>>condition1(LstPuzMod)
    ( où LstPuzMod =
    [' ', '1', ' ', '0']
    [' ', ' ', '0', ' ']
    [' ', '0', ' ', ' ']
    ['1', '1', '1', ' '] )
    False [[0, 3], [1, 3], [2, 3]] []
    >>>condition1(LstPuzMod)
    ( où LstPuzMod =
    [' ', '1', ' ', '0']
    ['1', ' ', '0', ' ']
    ['1', '0', ' ', ' ']
    ['1', '1', ' ', ' '] )
    False [] [[0, 1], [0, 2], [0, 3]]
    '''
    i = 0
    a = 0
    v = True
    coor_cond1Ligne = []
    while a < len(LstPuzMod[0]):
        i = 0
        while i < len(LstPuzMod[0])//2:
            if LstPuzMod[a][i] == '0' and LstPuzMod[a][i+1] == '0' and LstPuzMod[a][i+2] == '0':
                v = False
                coor_cond1Ligne.append([i, a])
                coor_cond1Ligne.append([i+1, a])
                coor_cond1Ligne.append([i+2, a])
                print('3 valeurs similaires sur la ligne ' + str(a) + '!')
            if LstPuzMod[a][i] == '1' and LstPuzMod[a][i+1] == '1' and LstPuzMod[a][i+2] == '1':
                v = False
                coor_cond1Ligne.append([i, a])
                coor_cond1Ligne.append([i+1, a])
                coor_cond1Ligne.append([i+2, a])
                print('3 valeurs similaires sur la ligne ' + str(a) + '!')
            i += 1
        a += 1
        
        
    i = 0
    a = 0
    v = True
    coor_cond1Col = []
    while a < len(LstPuzMod):
        i = 0
        while i < len(LstPuzMod[0])//2:
            if LstPuzMod[i][a] == '0' and LstPuzMod[i+1][a] == '0' and LstPuzMod[i+2][a] == '0':
                v = False
                coor_cond1Col.append([a, i])
                coor_cond1Col.append([a, i+1])
                coor_cond1Col.append([a, i+2])
                print('3 valeurs similaires sur la colonne ' + str(a) + '!')
            if LstPuzMod[i][a] == '1' and LstPuzMod[i+1][a] == '1' and LstPuzMod[i+2][a] == '1':
                v = False
                coor_cond1Col.append([a, i])
                coor_cond1Col.append([a, i+1])
                coor_cond1Col.append([a, i+2])
                print('3 valeurs similaires sur la colonne ' + str(a) + '!')
            i += 1
        a += 1
    return v, coor_cond1Ligne, coor_cond1Col
    
    
def condition2(LignesRemplies, ColonnesRemplies, LstPuzMod):
    '''
    Fonction qui va vérifier si il y a ou non autant de 1 que de 0 dans chaque lignes et colonnes
    :LignesRemplies: La liste représentant le plateau avec les lignes remplies ainsi que les lignes non remplies (représentés par l'élement vide ( ' ' )).
    :ColonnesRemplies: La liste représentant le plateau avec les colonnes remplies ainsi que les colonnes non remplies représentés par l'élement vide ( ' ' ).
    :Param LstPuzMod: Une liste de listes représentant le puzzle actuel 
    :Return value V : False si il n'y a pas autant de 1 que de 0
    :Return value coor_cond2: Une liste de listes sous forme [[x], [y]] avec x représentant le numéro de la ligne ne respectant pas la condition ( x étant vide si la condition est respecté ) et de même y pour la colonne ne respectant pas la condition.
    >>>condition2(LignesRemplies, ColonnesRemplies, LstPuzMod)
    ( où LstPuzMod =
    [' ', '1', ' ', '0']
    [' ', ' ', '0', ' ']
    [' ', '0', ' ', ' ']
    ['1', '1', ' ', ' '] )
    True [[], []]
    >>>condition2(LignesRemplies, ColonnesRemplies, LstPuzMod)
    ( où LstPuzMod =
    [' ', '1', ' ', '0']
    [' ', ' ', '0', ' ']
    ['1', '0', '1', '1']
    ['1', '1', ' ', ' '] )
    False [[2], []]
    '''
    
    i = 0
    j = 0
    v = True
    coor_cond2 = []
    lst = []
    while i < len(LignesRemplies):
        nb_un = 0
        lgn = LignesRemplies[i]
        nb_un = lgn.count('1')
        if nb_un != len(LstPuzMod)/2 and lgn != ' ':
            print("Il n'y a pas autant de 1 que de 0 dans la ligne " + str(i) + '!')
            lst.append(i)
            v = False
        i += 1
    coor_cond2.append(lst)
    lst = []
    while j < len(ColonnesRemplies):
        nb_un = 0
        lgn = ColonnesRemplies[j]
        nb_un = lgn.count('1')
        if nb_un != len(LstPuzMod)/2 and lgn != ' ':
            print("Il n'y a pas autant de 1 que de 0 dans la colonne " + str(j) + '!')
            lst.append(j)
            v = False
        j += 1
    coor_cond2.append(lst)
    return v, coor_cond2

def condition3(colonnes, LstPuzMod):
    '''
    Fonction qui verifie si il y a des lignes qui se ressemblent ou des colonnes qui se ressemblent.
    :Param LstPuzMod: Une liste de listes représentant le puzzle actuel 
    :Param colonnes, une liste de listes représentant les colonnes du puzzle
    :Return value v: False si il y a des lignes qui se ressemblent entre eux ou si il y a des colonnes qui se ressemblent entre eux, sinon True.
    :Return value coor_cond3: Une liste de listes où les lignes qui n'ont pas de doublons sont représentés avec un vide ( ' ' ).
    >>>condition3(colonnes, LstPuzMod) 
    ( où LstPuzMod =
    [' ', '1', ' ', '0']
    [' ', ' ', '0', ' ']
    [' ', '0', ' ', ' ']
    ['1', '1', ' ', ' '] )
    True, [' ', ' ', ' ', ' ']
    >>>condition3(colonnes, LstPuzMod) 
    ( où LstPuzMod =
    ['1', '1', '0', '0']
    [' ', ' ', '0', ' ']
    [' ', '0', ' ', ' ']
    ['1', '1', '0', '0'] )
    False, [['1', '1', '0', '0'], ' ', ' ', ['1', '1', '0', '0']]
    
    
    '''
    i = 0
    v = True
    v1 = True
    v2 = True
    coor_cond3 = []
    lst = []
    while i < len(LstPuzMod):
        if LstPuzMod.count(LstPuzMod[i]) != 1:
            v1 = False
            lst.append(i)
        i += 1
    i = 0
    coor_cond3.append(lst)
    lst = []
    while i < len(colonnes):
        if colonnes.count(colonnes[i]) != 1:
            v2 = False
            lst.append(i)
        i += 1
    coor_cond3.append(lst)
    if v2 == False:
        print('Des colonnes sont similaires!')
    if v1 == False:
        print('Des lignes sont similaires!')
    v = v1 and v2
    return v, coor_cond3

#Programme principale

choix = int(input("Choissez entre jouer sur le mode graphique (1) et le mode terminal (0) : "))
while choix != 1 and choix != 0:
    print('Mauvaise saisie')
    choix = int(input("Choissez entre jouer sur le mode graphique et le mode terminal: "))

if choix == 0 : 
    LstPuzMod = puzzle(CHEMIN_VERS_FICHIER)
    LstPuzNMod = puzzle(CHEMIN_VERS_FICHIER)
    i = 0   
    while i < len(LstPuzMod):
        print(LstPuzMod[i])    
        i += 1     
    while True:
        print()  
        xCase = int(input('Entrez xCase: '))
        yCase = int(input('Entrez yCase: '))
        Valeur = input('Entrez Valeur: ')
        remplir_case(yCase, xCase, Valeur, LstPuzNMod, LstPuzMod)
        colonnes = lst_colonnes(LstPuzMod)
        LignesRemplies = check_lignes(LstPuzMod)
        ColonnesRemplies = check_colonnes(LstPuzMod)
        rempli = check_plateau(LignesRemplies)
        print()
        i = 0   
        while i < len(LstPuzMod):
            print(LstPuzMod[i])    
            i += 1 
        v1, coor_cond1Ligne, coor_cond1Col = condition1(LstPuzMod)
        v2, coor_cond2 = condition2(LignesRemplies, ColonnesRemplies, LstPuzMod)
        if rempli == True:
            v3, coor_cond3 = condition3(colonnes, LstPuzMod)
            if v1 and v2 and v3 == True:
                print('Partie gagnée!')
                break

 
### Mode Graphique

def init_plateau(n):
    '''
    Fonction initialisant un plateau
    :Param n: n (int) longueur d'une case
    '''
    lst = []
    y = 0
    while y < TAILLE_FENETRE:
        x = 0
        while x < TAILLE_FENETRE:
            rectangle(x, y, x + n, y + n, couleur = 'black', remplissage = 'snow', epaisseur = 1, tag = '')
            x += n
        y += n



    
def pixel_vers_case(x, y):   
    '''
    Fonction qui transforme les coordonées en pixels d'une case en ses coordonées en case
    :Param x, y: Coordonnées x, y en pixels
    :Return value x, y: Coordonnées x, y en cases
    >>>pixel_vers_case(150, 50)
    1, 0
    >>>pixel_vers_case(323, 390)
    3, 3
    '''
    i = int(x // n)
    j = int(y // n)
    return i, j
    
def init_valeur_case(LstPuzMod):
    '''
    Fonction qui va retourner une liste de listes représentant les coordonnées de chaque case avec sa valeur.
    :Param LstPuzMod: Une liste de listes représentant le puzzle actuel 
    :Return value: Une liste de listes avec chaque élément sous la forme [x, y, v] où x et y sont les coordonnées en cases de la case et v sa valeur.
    >>>init_valeur_case(LstPuzMod) ( où LstPuzMod est le puzzle initial )
    [[[0, 0, ' '], [1, 0, '1'], [2, 0, ' '], [3, 0, '0']], [[0, 1, ' '], [1, 1, ' '], [2, 1, '0'], [3, 1, ' ']], [[0, 2, ' '], [1, 2, '0'], [2, 2, ' '], [3, 2, ' ']], [[0, 3, '1'], [1, 3, '1'], [2, 3, ' '], [3, 3, ' ']]]
    '''
    i = 0
    case_valeurs = []
    while i < len(LstPuzMod):
        j = 0
        lst2 = []
        while j < len(LstPuzMod):
            lst = []
            a = LstPuzMod[i]
            lst.append(j)
            lst.append(i)
            lst.append(a[j])
            lst2.append(lst)
            j += 1
        case_valeurs.append(lst2)
        i += 1
    return case_valeurs
    
def case_valeur(i, j, valeur_des_cases):
    '''
    Fonction qui va retourner la valeur de la case en paramètre
    :Param i, j: Coordonnée (x, y) en case
    :Param valeur_des_cases : Une liste de listes avec chaque élément sous la forme [x, y, v] où x et y sont les coordonnées en cases de la case et v sa valeur.
    :Return value: La valeur de la case
    >>>case_valeur(0, 0, valeur_des_cases)
    ' '
    >>>case_valeur(1, 0, valeur_des_cases)
    '1'
    '''
    valeur = valeur_des_cases[j][i][2]
    return valeur
    
def change_valeur(valeur_case):
    '''
    Fonction qui va changer la valeur de la case dans l'ordre : ' ', '0', '1'
    :Param valeur_case: La valeur actuelle de la case
    :Return value: La nouvelle valeur de la case
    >>>change_valeur(' ')
    '0'
    >>>change_valeur('0')
    '1'
    >>>change_valeur('1')
    ' '
    '''
    while True:
        if valeur_case == ' ':
            valeur_case = '0'
            break
        if valeur_case == '0':
            valeur_case = '1'
            break
        if valeur_case == '1':  
            valeur_case = ' '
            break
    return valeur_case

def remplace_valeur(i, j, LstPuzMod, nouvelle_valeur, NMod):
    '''
    Fonction qui remplace la valeur de la case seulement si elle est modifiable
    :Param i, j: Coordonnée (x, y) en case
    :Param LstPuzMod: Une liste de listes représentant le puzzle actuel 
    :Param nouvelle_valeur: La nouvelle valeur de la case
    :Param NMod: Liste de listes représentant le puzzle initial
    '''
    if NMod[j][i] != '1' and NMod[j][i] != '0':
        LstPuzMod[j][i] = nouvelle_valeur

def dessin(LstPuzMod, n, NMod):
    '''
    Fonction qui va afficher les valeurs de chaque case sur le plateau
    :Param LstPuzMod: Une liste de listes représentant le puzzle actuel 
    :Param n: Longueur d'une case
    :Param NMod: Liste de listes représentant le puzzle initial
    '''
    i = 0
    while i < len(LstPuzMod):
        j = 0
        while j < len(LstPuzMod):
            if NMod[j][i] == '1' or NMod[j][i] == '0':
                if LstPuzMod[j][i] == '1':
                    image(i*n+n/2, j*n+n/2, '11.png', ancrage='center')
                if LstPuzMod[j][i] == '0':
                    image(i*n+n/2, j*n+n/2, '01.png', ancrage='center')
            else:
                if LstPuzMod[j][i] == '1':
                    image(i*n+n/2, j*n+n/2, '1.png', ancrage='center')
                if LstPuzMod[j][i] == '0':
                    image(i*n+n/2, j*n+n/2, '0.png', ancrage='center')
            j += 1
        i += 1
        
def dessin_cond1(coor_cond1Ligne, coor_cond1Col):
    '''
    Fonction qui va barrer les 3 cases alignés ne respectant pas la condition.
    :Param value coor_cond1Ligne: Liste de listes représentant les coordonnées en cases des 3 cases identiques alignés sur une ligne
    :Param value coor_cond1Col: Liste de listes représentant les coordonnées en cases des 3 cases identiques alignés sur une colonne
    '''
    if len(coor_cond1Ligne) >= 3:
        image(((coor_cond1Ligne[1][0])*100)+50,((coor_cond1Ligne[1][1])*100)+50, 'underline_horizontale.png', ancrage='center')
        
    if len(coor_cond1Col) >= 3:
        image(((coor_cond1Col[1][0])*100)+50,((coor_cond1Col[1][1])*100)+50, 'underline_verticale.png', ancrage='center')
    
def dessin_cond2(coor_cond2, n):
    '''
    Fonction qui va hachurer la ligne ou la colonne où il n'y a pas autant de 1 que de 0.
    :Param coor_cond2: Une liste de listes sous forme [[x], [y]] avec x représentant le numéro de la ligne ne respectant pas la condition ( x étant vide si la condition est respecté ) et de même y pour la colonne ne respectant pas la condition.
    :Param n: La longueur d'une case
    '''  
    if coor_cond2[0] != []:
        i = 0
        while i < len(coor_cond2[0]):
            x = coor_cond2[0][i]*n
            y = x + n/2
            x = 0
            while x != TAILLE_FENETRE:
                image(x+n/2, y, 'hachure.png', ancrage='center')
                x += n
            i += 1
    
    if coor_cond2[1] != []:
        i = 0
        while i < len(coor_cond2[1]):
            y = coor_cond2[1][i]*n
            x = y + n/2
            y = 0
            while y != TAILLE_FENETRE:
                image(x, y+n/2, 'hachure.png', ancrage='center')
                y += n
            i += 1
            
            
if choix == 1:
    LstPuzMod = puzzle(CHEMIN_VERS_FICHIER)
    NMod = puzzle(CHEMIN_VERS_FICHIER)
    TAILLE_FENETRE = 400
    n = TAILLE_FENETRE/len(LstPuzMod)
    cree_fenetre(TAILLE_FENETRE, TAILLE_FENETRE)
    valeur_des_cases = init_valeur_case(LstPuzMod)
    init_plateau(n)
    dessin(LstPuzMod, n, NMod)
    while True:
        ev = donne_ev()
        if type_ev(ev) == "ClicGauche":
            efface_tout()
            x = abscisse(ev)
            y = ordonnee(ev)
            i, j = pixel_vers_case(x, y)
            valeur_des_cases = init_valeur_case(LstPuzMod)
            valeur_case = case_valeur(i, j, valeur_des_cases)
            nouvelle_valeur = change_valeur(valeur_case) 
            remplace_valeur(i, j, LstPuzMod, nouvelle_valeur, NMod)
            colonnes = lst_colonnes(LstPuzMod)
            init_plateau(n)
            dessin(LstPuzMod, n, NMod)
            LignesRemplies = check_lignes(LstPuzMod)
            ColonnesRemplies = check_colonnes(LstPuzMod)
            rempli = check_plateau(LignesRemplies)
            v1, coor_cond1Ligne, coor_cond1Col = condition1(LstPuzMod)
            v2, coor_cond2 = condition2(LignesRemplies, ColonnesRemplies, LstPuzMod)
            dessin_cond1(coor_cond1Ligne, coor_cond1Col)
            dessin_cond2(coor_cond2, n)
            if rempli == True:
                v3, coor_cond3 = condition3(colonnes, LstPuzMod)
                if v1 and v2 and v3 == True:
                    texte(TAILLE_FENETRE//2, TAILLE_FENETRE//2, 'GAGNÉ !', couleur='green', ancrage='center')
                    attend_fermeture()
        if type_ev(ev) == "ClicDroit":
            break
        mise_a_jour()
    ferme_fenetre()