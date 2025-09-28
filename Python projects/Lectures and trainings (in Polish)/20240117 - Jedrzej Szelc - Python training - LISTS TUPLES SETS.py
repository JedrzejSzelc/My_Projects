#########################################################
##### Date: 2024.01.17                              #####
##### Stream: Python Based Automation               #####
##### Author: jedrzej.szelc@capgemini.com           #####
##### Subject: Typy danych - Listy, Krotki, Zbiory  #####
#########################################################

print()

#######################################
### Punkt 1 - Listy w języku Python ###
#######################################

####################################
### Punkt 1.1 - Lista vs. indeks ###
####################################
print("Punkt 1.1 - Lista vs. indeks\n")

lista_liczb = [11, 22, 33, 44, 55]

print(lista_liczb)

# indeks_listy = 0
# print("Printuję element listy:", lista_liczb[indeks_listy], "pod indeksem:", indeks_listy)

exit()

#####################################
### Punkt 1.2 - Indeksowanie list ###
#####################################
print("Punkt 1.2 - Indeksowanie list\n")

lista_liczb = [11, 22, 33, 44, 55]

print("Printuję dwa elementy listy:", lista_liczb[2:4])

# indeks_start = 2
# indeks_stop = 4
# print("Printuję elementy z listy:", lista_liczb[indeks_start:indeks_stop],
#       "\ngdzie 'indeks_start' to:", indeks_start, ", a 'indeks_stop' to:", indeks_stop,
#       "\nprzy czym ostatnim elementem na liście jest:", lista_liczb[4])

exit()

#########################################
### Punkt 1.3 - Zmiana elementu listy ###
#########################################
print("Punkt 1.3 - Zmiana elementu listy\n")

lista_liczb = [11, 22, 33, 44, 55]

lista_liczb[3] = 77

print("Printuję listę po zmianie:", lista_liczb)

exit()

########################################
### Punkt 1.4 - Typy danych w liście ###
########################################
print("Punkt 1.4 - Typy danych w liście\n")

lista_roznych_typow_danych = [54321, "Jędrzej", "jest 'gópi'...", 12345]

print("Printuję listę różnych typów danych:", lista_roznych_typow_danych)

# lista_z_zagniezdzona_lista = [lista_roznych_typow_danych, "Ta lista zawiera listę."]
# print("Lista z zagnieżdżoną listą:", lista_z_zagniezdzona_lista)

# print("Element zagnieżdżonej listy, czyli zagnieżdżona lista:", lista_z_zagniezdzona_lista[0])

# pierwszy_element_zagniezdzonej_listy = lista_z_zagniezdzona_lista[0]
# print("Pierwszy element zagnieżdżonej listy, czyli zagnieżdżona lista:", pierwszy_element_zagniezdzonej_listy)

# print("Działanie dwuwymiarowe:", lista_z_zagniezdzona_lista[0][1])

exit()

##########################################
### Punkt 1.5 - Negatywne indeksowanie ###
##########################################
print("Punkt 1.5 - Negatywne indeksowanie\n")

lista_liczb = [11, 22, 33, 44, 55]

indeks_listy = -1
print("Printuję element listy:", lista_liczb[indeks_listy], "pod indeksem:", indeks_listy)

# indeks_stop = -3
# indeks_start = -1
# print("Printuję elementy z listy:", lista_liczb[indeks_stop:indeks_start],
#       "\ngdzie 'indeks_stop' to:", indeks_stop, ", a 'indeks_start' to:", indeks_start,
#       "\nprzy czym ostatnim elementem na liście jest:", lista_liczb[-1])

exit()

##########################################
### Punkt 1.6 - Tworzenie pustej listy ###
##########################################
print("Punkt 1.6 - Tworzenie pustej listy\n")

pusta_lista_1 = []
pusta_lista_2 = list()

print("Pusta lista nr 1:", pusta_lista_1)
print("Pusta lista nr 2:", pusta_lista_2)

exit()

####################################################################
### Punkt 1.7 - Dodawanie elementów do listy - metoda 'append()' ###
####################################################################
print("Punkt 1.7 - Dodawanie elementów do listy - metoda 'append()'\n")

pusta_lista = []
lista_liczb = [11, 22, 33, 44, 55]

# pusta_lista[0] = 11

# lista_liczb[5] = 66

# print("Pusta lista przed użyciem metody 'append()':\n", pusta_lista)
# pusta_lista.append(66)
# # pusta_lista.append(77)
# # # pusta_lista.append(88)
# print()
# print("Metoda 'append()' umożliwia dokładanie elementów do już istniejącej, pustej listy:\n", pusta_lista)

# print("Już istniejąca lista przed użyciem metody 'append()':\n", lista_liczb)
# lista_liczb.append(66)
# # lista_liczb.append(77)
# # # lista_liczb.append(88)
# print()
# print("Metoda 'append()' umożliwia dokładanie elementów do już istniejącej listy:\n", lista_liczb)

exit()

####################################################################
### Punkt 1.8 - Dodawanie elementów do listy - metoda 'insert()' ###
####################################################################
print("Punkt 1.8 - Dodawanie elementów do listy - metoda 'insert()'\n")

pusta_lista = []
lista_liczb = [11, 22, 33, 44, 55]

print("Pusta lista przed użyciem metody 'insert()':\n", pusta_lista)
pusta_lista.insert(0, "Pierwsza wartość listy")
print()
print("Metoda 'insert()' umożliwia wstawianie elementów do już istniejącej, pustej listy:\n", pusta_lista)

# print("Już istniejąca lista przed użyciem metody 'insert()':\n", lista_liczb)
# lista_liczb.insert(1, "Pierwszy string!")
# # lista_liczb.insert(2, 66)
# # # lista_liczb.insert(5, "Jeszcze jeden string...")
# print()
# print("Metoda 'insert()' umożliwia wstawianie elementów pod wybranym indeksem w już istniejącej liście:\n", lista_liczb)

exit()

##################################################################
### Punkt 1.9 - Usuwanie elementów z listy - metoda 'remove()' ###
##################################################################
print("Punkt 1.9 - Usuwanie elementów z listy - metoda 'remove()'\n")

lista_liczb = [11, 22, 33, 44, 55]
lista_roznych_typow_danych = [54321, "Jędrzej", "jest 'gópi'...", 12345]

lista_liczb.remove(22)
print("Usuwanie elementów z listy liczb przy pomocy metody 'remove()':", lista_liczb)

# lista_roznych_typow_danych.remove("jest 'gópi'...")
# print("Usuwanie elementów z listy różnych typów danych przy pomocy metody 'remove()':", lista_roznych_typow_danych)

exit()

################################################################
### Punkt 1.10 - Usuwanie elementów z listy - metoda 'pop()' ###
################################################################
print("Punkt 1.10 - Usuwanie elementów z listy - metoda 'pop()'\n")

lista_liczb = [11, 22, 33, 44, 55]
lista_roznych_typow_danych = [54321, "Jędrzej", "jest 'gópi'...", 12345]

print("Już istniejąca lista liczb przed użyciem metody 'pop()':\n", lista_liczb)
ostatni_element_listy = lista_liczb.pop()
print()
print("Użycie metody 'pop()' skutkuje skróceniem listy liczb:", lista_liczb,
      "\noraz zwróceniem elementu 'ściąganego' z listy liczb:", ostatni_element_listy)

# print("Już istniejąca lista różnych typów danych przed użyciem metody 'pop()':\n", lista_roznych_typow_danych)
# ostatni_element_listy = lista_roznych_typow_danych.pop()
# print()
# print("Użycie metody 'pop()' skutkuje skróceniem listy różnych typów danych:", lista_roznych_typow_danych,
#       "\noraz zwróceniem elementu 'ściąganego' z listy różnych typów danych:", ostatni_element_listy)

exit()

#########################################################################################
### Punkt 1.11 - Metody i funkcje 'len()', 'max()', 'min()', 'sort()' oraz 'sorted()' ###
#########################################################################################
print("Punkt 1.11 - Metody i funkcje 'len()', 'max()', 'min()', 'sort()' oraz 'sorted()'\n")

lista_liczb = [22, 11, 55, 44, 33]

print("Długość listy liczb:", len(lista_liczb))

# print("Maksymalna wartość w liście liczb:", max(lista_liczb))
# print("Minimalna wartość w liście liczb:", min(lista_liczb))

# lista_liczb.sort()
# print("Lista posortowana 'in-place' metodą 'sort()':", lista_liczb)

# lista_posortowanych_liczb = sorted(lista_liczb)
# print("Oryginalna lista liczb:", lista_liczb)
# print("Nowa lista posortowana metodą 'sorted()':", lista_posortowanych_liczb)

exit()

########################################################
### Punkt 2 - Krotki (ang. 'tuples') w języku Python ###
########################################################

#####################################################
### Punkt 2.1 - Prawie jak listy, choć niezmienne ###
#####################################################
print("Punkt 2.1 - Prawie jak listy, choć niezmienne\n")

krotka_liczb = (11, 22, 33, 44, 55)
krotka_roznych_typow_danych = (54321, "Jędrzej", "jest 'gópi'...", 12345)

indeks_krotki = 2

print("Printuję element krotki liczb:", krotka_liczb[indeks_krotki],
      "pod indeksem:", indeks_krotki)
print("Printuję element krotki różnych typów danych:",
      krotka_roznych_typow_danych[indeks_krotki],
      "pod indeksem:", indeks_krotki)

# krotka_liczb[3] = 77

exit()

###########################################
### Punkt 2.2 - Tworzenie pustej krotki ###
###########################################
print("Punkt 2.2 - Tworzenie pustej krotki\n")

pusta_krotka_1 = ()
pusta_krotka_2 = tuple()

print("Pusta krotka nr 1:", pusta_krotka_1)
print("Pusta krotka nr 2:", pusta_krotka_2)

exit()

############################################
### Punkt 2.3 - Do listy i z powrotem... ###
############################################
print("Punkt 2.3 - Do listy i z powrotem...\n")

krotka_liczb = (11, 22, 33, 44, 55)

lista_liczb = list(krotka_liczb)
lista_liczb[3] = 77
krotka_liczb = tuple(lista_liczb)

print("Printuję krotkę liczb po konwersji z krotki do listy, "
      "\nzmianie wartości i powrotnej konwersji z listy do krotki:", krotka_liczb)

exit()

######################################################
### Punkt 3 - Zbiory (ang. 'sets') w języku Python ###
######################################################

################################################################
### Punkt 3.1 - Zbiory są nieindeksowalne i nieuporządkowane ###
################################################################
print("Punkt 3.1 - Zbiory są nieindeksowalne i nieuporządkowane\n")

zbior_liczb = {11, 22, 33, 44, 55}
zbior_roznych_typow_danych = {54321, "Jędrzej", "jest 'gópi'...", 12345}

zbior_liczb[2]
# zbior_roznych_typow_danych[2]

# print("Printuję zbiór liczb:", zbior_liczb)
# print("Printuję zbiór różnych typów danych:", zbior_roznych_typow_danych)

exit()

###############################################################################
### Punkt 3.2 - Zbiory są trudne do zmiany - metody 'add()' oraz 'remove()' ###
###############################################################################
print("Punkt 3.2 - Zbiory są trudne do zmiany - metody 'add()' oraz 'remove()'\n")

zbior_liczb = {11, 22, 33, 44, 55}
zbior_roznych_typow_danych = {54321, "Jędrzej", "jest 'gópi'...", 12345}

# zbior_liczb[3] = 77
# zbior_roznych_typow_danych[2] = "jest bardzo 'gópi'..."

# zbior_liczb.add(77)
# zbior_roznych_typow_danych.add(67890)

# zbior_liczb.remove(22)
# zbior_roznych_typow_danych.remove("Jędrzej")

print("Printuję zbiór liczb:", zbior_liczb)
print("Printuję zbiór różnych typów danych:", zbior_roznych_typow_danych)

exit()

####################################################################################################
### Punkt 3.3 - Zastosowania zbiorów: usuwanie duplikatów, część wspólna, różnica i suma zbiorów ###
####################################################################################################
print("Punkt 3.3 - Zastosowania zbiorów: usuwanie duplikatów, część wspólna, różnica i suma zbiorów\n")

### Usuwanie duplikatów
zbior_liczb = {11, 22, 33, 44, 55, 11, 22}
print("Printuję zbiór liczb:", zbior_liczb)

# ### Część wspólna dwóch zbiorów
# zbior_liczb_1 = {11, 22, 33, 44, 55}
# zbior_liczb_2 = {66, 77, 33, 44, 55}
# print("Część wspólna dwóch zbiorów:", zbior_liczb_1.intersection(zbior_liczb_2))

# ### Różnica dwóch zbiorów
# zbior_liczb_1 = {11, 22, 33, 44, 55}
# zbior_liczb_2 = {66, 77, 33, 44, 55}
# print("Różnica dwóch zbiorów:", zbior_liczb_1.difference(zbior_liczb_2))

# ### Suma dwóch zbiorów
# zbior_liczb_1 = {11, 22, 33, 44, 55}
# zbior_liczb_2 = {66, 77, 33, 44, 55}
# print("Suma dwóch zbiorów:", zbior_liczb_1.union(zbior_liczb_2))