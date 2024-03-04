
from random import randint

# 1:♣️ 2:♥️ 3:♠️ 4:♦️

valeurs = ['0', '0', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
groupes = ['♣️', '♥️', '♠️', '♦️']

#=====================================================================================

#Régles du jeu

print("Vous commencez avec 50 unités d'argent et vous disposez de 5 parties différentes")
print("Pour chaque partie gagnée, vous obtiendrais 1:1 de l'argent joué, dans le cas ou vous n'utilisiez pas d'aides, chaque une vous rendras 1/4 de l'argent joué (si vous gagnez)")

#=====================================================================================

class carte:
  def __init__(self, valeur = randint(0, 12), groupe = randint(0, 3)):                            #()
# carte aléatoire avec sa valeur et son groupe
    valeur = randint(2, 14)
    groupe = randint(0, 3)
    self.valeur = valeur
    self.groupe = groupe

  def GetCarte(self):                                                                             #()
# rend la carte (Ex: '4♠️')
    return valeurs[self.valeur] +  groupes[self.groupe]

  def GetValeur(self):                                                                            #()
# rend la valeur (Ex: pour 'K♠️', 13)
    return self.valeur
'''
  def gagnant(self, autre_carte):
# rend la valeur la plus grande entre 2 cartes (Ex: pour '10♦️' et '4♣️', '10♦️')
    if self.GetValeurStr(self.GetCarte) == autre_carte.GetValeurStr(autre_carte) :
      return 'Les deux cartes ont la même valeur :/'
    else:
      if self.GetValeurStr(self.GetCarte) > autre_carte.GetValeurStr(autre_carte) :
        return 'La premiere carte est la plus grande'
      else :
        return 'La deuxième carte est la plus grande'
'''
#=====================================================================================

class paquet_5:
# génère une liste de 10 cartes 
  def __init__(self):                                                                             #()
    c1 = carte()
    c2 = carte()
    c3 = carte()
    c4 = carte()
    c5 = carte()

    self.paquet = [c1, c2, c3, c4, c5]

  def GetCarte_paquet(self, pos_carte):                                                           #(int)
# renvoie une carte du paquet (J♣️)
    return self.paquet[pos_carte].GetCarte()

  def GetValeur_paquet(self, pos_carte):                                                          #(int)
# renvoie la valeur d'une carte du paquet (pour J♣️, 11)
    return self.paquet[pos_carte].GetValeur()

  def GetPaquet(self):                                                                            #()
# renvoie les cartes du paquet (['9♦️', '9♠️', '5♦️', '8♥️', 'J♣️'])
    L = []
    for i in range (len(self.paquet)):
      L.append(self.GetCarte_paquet(i))
    return L

  def GetPaquet_valeur(self):                                                                     #()
# renvoie la valeur de la somme du paquet (42)
    self.somme = 0
    for i in range (len(self.paquet)):
      self.somme += self.GetValeur_paquet(i)
    return self.somme

#=====================================================================================

class jeu:
  def __init__(self):
    self.paquet1 = paquet_5()
    self.paquet2 = paquet_5()
    self.paquet3 = paquet_5()
    self.paquet4 = paquet_5()
    self.aides = 2
    self.paquets = [None, self.paquet1, self.paquet2, self.paquet3, self.paquet4]

  def GetPaquet(self, numero_paquet):                                                             #(int)
    return self.paquets[numero_paquet]

  def voir_paquets(self):                                                                         #()
    print('Vous avez accés au 3 premières cartes de chaque paquet')
    print('Paquet 1: [', self.paquet1.GetCarte_paquet(0), self.paquet1.GetCarte_paquet(1), self.paquet1.GetCarte_paquet(2), '__ __ ]')
    print('Paquet 2: [', self.paquet2.GetCarte_paquet(0), self.paquet2.GetCarte_paquet(1), self.paquet2.GetCarte_paquet(2), '__ __ ]')
    print('Paquet 3: [', self.paquet3.GetCarte_paquet(0), self.paquet3.GetCarte_paquet(1), self.paquet3.GetCarte_paquet(2), '__ __ ]')
    print('Paquet 4: [', self.paquet4.GetCarte_paquet(0), self.paquet4.GetCarte_paquet(1), self.paquet4.GetCarte_paquet(2), '__ __ ]')
    print('Vous disposez de', self.aides, 'aides où vous pouvez révéler une carte ou en comparer 2.')
#    print('Pour révéler une carte vous devez écrire: nom_du_jeu.Revelation(numero de la carte, numero du paquet)')
#    print('Pour comparer deux carte vous devez écrire: nom_du_jeu.Comparation(numero de la carte 1, numero du paquet 1, numero de la carte 2, numero du paquet 2)')

  def RevelerCarte(self, num_carte, num_paquet):                                                  #(int, int)
# rend la carte qu'on souhaite connaître
    if self.aides != 0 :
      print('Aides:', self.aides, '-->', self.aides - 1)
      self.aides = self.aides - 1
      print('La carte', num_carte, 'du paquet', num_paquet, 'est:', self.paquets[num_paquet].GetCarte_paquet(num_carte - 1))
    else :
      return "Vous n'avez plus d'aides"

  def GetValeurStr(self, carte):                                                                  #(str)
# rend la valeur d'une carte (Ex: pour 'K♠️', 13)
    valeurss = ['0', '0', '2', '3', '4', '5', '6', '7', '8', '9', '1', 'J', 'Q', 'K', 'A']
    i = 0
    while valeurss[i] != carte[0] :
      i  += 1
    return i


  def ComparerCartes(self, num_carte1, num_paquet1, num_carte2, num_paquet2):                     #(int, int, int, int)
# rend la carte avec la valeur la plus grande
    if self.aides != 0 :
      print('Aides:', self.aides, '-->', self.aides - 1)
      self.aides = self.aides - 1
      if self.GetValeurStr(self.paquets[num_paquet1].GetCarte_paquet(num_carte1 - 1)) > self.GetValeurStr(self.paquets[num_paquet2].GetCarte_paquet(num_carte2 - 1)) :
        return 'La première carte a une plus grande valeur'
      elif self.GetValeurStr(self.paquets[num_paquet1].GetCarte_paquet(num_carte1 - 1)) < self.GetValeurStr(self.paquets[num_paquet2].GetCarte_paquet(num_carte2 - 1)) :
        return 'La deuxième carte a une plus grande valeur'
      else :
        return 'Les deux cartes ont la même valeur :/'
    else :
      return "Vous n'avez plus d'aides"

  def baraka(self, paquet):                                                                       #(class: paquet_5)
# rend si vous gagnez le jeu en fonction du paquet choisi
    somme = 0
    for i in range (1, 5):
      if self.paquets[i].GetPaquet_valeur() > somme :
        somme = self.paquets[i].GetPaquet_valeur()

    print('Les paquets étaient:')
    print('Paquet 1: [', self.paquet1.GetCarte_paquet(0), self.paquet1.GetCarte_paquet(1), self.paquet1.GetCarte_paquet(2), self.paquet1.GetCarte_paquet(3), self.paquet1.GetCarte_paquet(4), ']  Valeur:', self.paquet1.GetPaquet_valeur())
    print('Paquet 2: [', self.paquet2.GetCarte_paquet(0), self.paquet2.GetCarte_paquet(1), self.paquet2.GetCarte_paquet(2), self.paquet2.GetCarte_paquet(3), self.paquet2.GetCarte_paquet(4), ']  Valeur:', self.paquet2.GetPaquet_valeur())
    print('Paquet 3: [', self.paquet3.GetCarte_paquet(0), self.paquet3.GetCarte_paquet(1), self.paquet3.GetCarte_paquet(2), self.paquet3.GetCarte_paquet(3), self.paquet3.GetCarte_paquet(4), ']  Valeur:', self.paquet3.GetPaquet_valeur())
    print('Paquet 4: [', self.paquet4.GetCarte_paquet(0), self.paquet4.GetCarte_paquet(1), self.paquet4.GetCarte_paquet(2), self.paquet4.GetCarte_paquet(3), self.paquet4.GetCarte_paquet(4), ']  Valeur:', self.paquet4.GetPaquet_valeur())
    
    if paquet.GetPaquet_valeur() == somme :
      print('XD vous avez gagné !')
      return '✓'
    else :
      print('Vous avez perdu :(')
      return 'X'


#=====================================================================================

class casino:
  def __init__(self):
    self.argent = 50
    self.gagne = 0
    self.perdu = 0

    self.jeu_un = jeu()
    self.jeu_deux = jeu()
    self.jeu_trois = jeu()
    self.jeu_quatre = jeu()
    self.jeu_cinq = jeu()
    self.jeux = [None, self.jeu_un, self.jeu_deux, self.jeu_trois, self.jeu_quatre, self.jeu_cinq]

  def partie(self, pari, num):                                                                    #(int, int)
# execute une partie avec une somme d'argent
    if pari <= 0 :
      return '??'
    if pari > self.argent :
      return "Vous n'avez pas autant d'argent haha"
    else :
      self.pari = pari
      self.jeu = self.jeux[num]
      return self.jeu.voir_paquets()

  def Comparation(self, num_carte1, num_paquet1, num_carte2, num_paquet2):                        #(int, int, int, int)
# rend la carte avec la valeur la plus grande
    print(self.jeu.ComparerCartes(num_carte1, num_paquet1, num_carte2, num_paquet2))
  
  def Revelation(self, num_carte, num_paquet):                                                    #(int, int)
# rend la carte qu'on souhaite connaître
    print(self.jeu.RevelerCarte(num_carte, num_paquet))

  def BARAKA(self, numero_paquet):                                                                #(int)
# rend si vous gagnez en fonction du paquet choisi
    paquet = self.jeu.GetPaquet(numero_paquet)
#    print(self.jeu.baraka(paquet))
    if self.jeu.baraka(paquet) == '✓' :
      self.argent = self.argent + self.pari + (1/4*self.jeu.aides)*self.pari
      self.gagne = self.gagne + self.pari + (1/4*self.jeu.aides)*self.pari
    else :
      self.argent = self.argent - self.pari
      self.perdu = self.perdu + self.pari
    print('En total, voua avez:')
    print(self.argent, "unités d'argent")
    print('gagné:', self.gagne, "unités d'argent")
    print('et perdu:', self.perdu, "unités d'argent")

#=====================================================================================

def start():
    a = casino()
    i = 0
    while(i<5):
        print("Partie", i + 1, ":")
        if a.argent != 0 :
            parie = float(input("Pari:"))
            a.partie(parie,i+1)
            y = 2
            while y != 0 :
                mode = int(input("Comparation (1), Revelation (2) ou ne pas utiliser d'aides (3) ?"))
                if mode==1:
                    pos_carte1 = int(input("Position de la carte 1? "))
                    num_paquet1 = int(input("Numero du paquet? "))
                    pos_carte2 = int(input("Position de la carte 2? "))
                    num_paquet2 = int(input("Numero du paquet? "))
                    a.Comparation(pos_carte1, num_paquet1, pos_carte2, num_paquet2)
                    y = y - 1
                elif mode == 2:
                    pos_carte1 = int(input("Position de la carte ? "))
                    num_paquet1 = int(input("Numero du paquet? "))
                    a.Revelation(pos_carte1, num_paquet1)
                    y = y - 1
                else :
                    y = y - 1
            fin = int(input("Donnez le numéro du paquet dont vous pensez qu'il a la valeur la plus grande: "))
            a.BARAKA(fin)
            i += 1
            print("---------------")

start()
