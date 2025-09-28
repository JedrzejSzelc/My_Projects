#############################################################
##### Date: 2024.02.28                                  #####
##### Stream: Python Based Automation                   #####
##### Author: jedrzej.szelc@capgemini.com               #####
##### Subject: Instrukcje warunkowe (if, elif, else...) #####
#############################################################

print()

##############################################
### Punkt 1 - Warunek 'if' w języku Python ###
##############################################

#####################################################
### Punkt 1.1 - Podstawowa struktura warunku 'if' ###
#####################################################
print("Punkt 1.1 - Podstawowa struktura warunku 'if'\n")

a = -1
b = 5

if a > b:
    print("Warunek 'if' został spełniony.")
print("Kod poza warunkiem 'if'.")

exit()

########################################################
### Punkt 1.2 - Warunek 'if' vs. operatory relacyjne ###
########################################################
print("Punkt 1.2 - Warunek 'if' vs. operatory relacyjne\n")

# '>' - większy
# '>=' - większy-równy
# '<' - mniejszy
# '<=' - mniejszy-równy
# '==' - równy
# '!=' - nierówny

a = 5
b = 5

if a > b:
    print("Warunek 'if' został spełniony.")
print("Kod poza warunkiem 'if'.")

exit()

##################################################
### Punkt 1.3 - Instrukcja 'else' warunku 'if' ###
##################################################
print("Punkt 1.3 - Instrukcja 'else' warunku 'if'\n")

a = 5
b = 4

if a >= b:
    print("Warunek 'if' został spełniony.")
else:
    print("Warunek 'if' nie został spełniony.")

exit()

###############################################################
### Punkt 1.4 - Zagnieżdżanie instrukcji 'if', czyli 'elif' ###
###############################################################
print("Punkt 1.4 - Zagnieżdżanie instrukcji 'if', czyli 'elif'\n")

a = 4
b = 4

if a >= b:
    print("Gałąź: a >= b")
elif a < b:
    print("Gałąź: a < b")
else:
    print("Żaden z warunków 'if' nie został spełniony.")

# if a >= b:
#     print("Gałąź: a >= b")
#     if a >= 110:
#         print("Zmienna 'a' ma wartość większą-równą od 110.")
# elif a < b:
#     print("Gałąź: a < b")
# else:
#     print("Żaden z warunków 'if' nie został spełniony.")

exit()

###########################################################
### Punkt 1.5 - Instrukcja wyboru 'Switch' w Python...? ###
###########################################################
print("Punkt 1.5 - Instrukcja wyboru 'Switch' w Python...?\n")

# jakas_zmienna = 10
#
# switch (jakas_zmienna):
#     case -1:
#         print("jakas zmienna == -1")
#     case 10:
#         print("jakas zmienna == 10")
#     case 123
#         print("jakas zmienna == 123")

a = 10

if a == -1:
    print("Wartość 'a' wynosi: -1")
elif a == 10:
    print("Wartość 'a' wynosi: 10")
elif a == 123:
    print("Wartość 'a' wynosi: 123")
else:
    print("Jędrzej jest 'gópi'.")

exit()

#########################################################################
### Punkt 1.6 - Przykład praktyczny: Sprawdź czy liczba jest parzysta ###
#########################################################################
print("Punkt 1.6 - Przykład praktyczny: Sprawdź czy liczba jest parzysta\n")

dzielna = 10
dzielnik = 2

# Modulo:
# 10 / 2 == (2 * 5 + 0), czyli reszta z dzielenia 10 przez 2 wynosi 0
# 11 / 2 == (2 * 5 + 1), czyli reszta z dzielenia 11 przez 2 wynosi 1
# 5 / 3 == (1 * 3 + 2), czyli reszta z dzielenia 5 przez 3 wynosi 2

# Operator modulo: % - reszta z dzielenia
reszta_z_dzielenia = dzielna % dzielnik

if reszta_z_dzielenia == 0:
    print("Liczba jest PARZYSTA!")
else:
    print("Liczba jest NIEPARZYSTA!")

exit()

#####################################################
### Punkt 2 - Warunek 'if' vs. operatory logiczne ###
#####################################################

###########################################
### Punkt 2.1 - Operator logiczny 'and' ###
###########################################
print("Punkt 2.1 - Operator logiczny 'and'\n")

a = 10
logged_in = True

if a == 10 and logged_in:
    print("Obydwa warunki są jednocześnie spełnione.")
else:
    print("Jeden z warunków nie jest spełniony.")

exit()

##########################################
### Punkt 2.2 - Operator logiczny 'or' ###
##########################################
print("Punkt 2.2 - Operator logiczny 'or'\n")

a = 10
logged_in = True

if a == 10 or logged_in:
    print("Przynajmniej jeden z warunków jest spełniony.")
else:
    print("Żaden z warunków nie jest spełniony.")

exit()

###########################################################
### Punkt 3 - Warunek 'if' vs. operatory przynależności ###
###########################################################

################################################
### Punkt 3.1 - Operator przynależności 'in' ###
################################################
print("Punkt 3.1 - Operator przynależności 'in'\n")

a = 2
b = [1, 2, 3, 4, 5]

if a in b:
    print("Liczba", a, "znajduje się w zbiorze liczb", b)
else:
    print("Liczba", a, "nie znajduje się w zbiorze liczb", b)

exit()

####################################################
### Punkt 3.2 - Operator przynależności 'not in' ###
####################################################
print("Punkt 3.2 - Operator przynależności 'not in'\n")

a = 2
b = [1, 2, 3, 4, 5]

if a not in b:
    print("Liczba", a, "nie znajduje się w zbiorze liczb", b)
else:
    print("Liczba", a, "znajduje się w zbiorze liczb", b)