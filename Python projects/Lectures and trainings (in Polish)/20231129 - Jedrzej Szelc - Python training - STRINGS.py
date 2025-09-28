#################################################
##### Date: 2023.12.20                      #####
##### Stream: Python Based Automation       #####
##### Author: jedrzej.szelc@capgemini.com   #####
##### Subject: Typy danych - Stringi        #####
#################################################

print()

#########################################
### Punkt 1 - Stringi w języku Python ###
#########################################

##############################################
### Punkt 1.1 - Wstęp do funkcji 'print()' ###
##############################################

print("Witamy na szkoleniach Python!")

# print("Cudzysłów")
# print('Apostrof')
# print("Jędrzej jest 'gópi'...")

# print("'Escape' character: \" ")
# print("'Escape' character: \\")
# print("'Escape' character: \"\"\" ")
# print("Jędrzej jest \"gópi\" - oczywiście tylko w cudzysłowie!")

# print("Teraz złamię \n linię.")
# print("Teraz wstawiam 'tab' \t w linię.")

# print("""To
# jest
# tekst
# w
# wielu
# liniach.
# """)

exit()

######################################
### Punkt 1.2 - Wstęp do zmiennych ###
######################################
print("Punkt 1.2 - Wstęp do zmiennych\n")

zmienna = "To jest zawartość zmiennej."
print(zmienna)

# a = "Takich nazw zmiennych lepiej nie używać."
# print(a)

# zmiennaNazwaCamelCase = "To jest zmienna z nazwą w konwencji 'camelCase'."
# print(zmiennaNazwaCamelCase)

# zmienna_nazwa_snake_case = "To jest zmienna z nazwą w konwencji 'snake_case'."
# print(zmienna_nazwa_snake_case)

exit()

#####################################
### Punkt 1.3 - Łączenie stringów ###
#####################################
print("Punkt 1.3 - Łączenie stringów\n")

string_numer_1 = "Witamy"
string_numer_2 = "na szkoleniach"
string_numer_3 = "Python!"

print(string_numer_1 + string_numer_2 + string_numer_3)

# print(string_numer_1 + " " + string_numer_2 + " " + string_numer_3)

# string_polaczony = string_numer_1 + " " + string_numer_2 + " " + string_numer_3
# print(string_polaczony)

# string_polaczony = string_numer_1 + " " + string_numer_2
# print(string_polaczony + " " + string_numer_3)

# string_data_kalendarzowa = "24.10.2023"
# print("Dziś jest (automatycznie dodana spacja!):", string_data_kalendarzowa)

# string_data_kalendarzowa = "24.10.2023"
# string_polaczony = "Wczoraj był (brak spacji!):" + string_data_kalendarzowa
# print(string_polaczony)

exit()

#########################################
### Punkt 1.4 - Indeksowanie stringów ###
#########################################
print("Punkt 1.4 - Indeksowanie stringów\n")

string_do_indeksowania = "String!"

print(string_do_indeksowania[0])

# print(string_do_indeksowania[7])

# print(string_do_indeksowania[0:3])
# print(string_do_indeksowania[3:])
# print(string_do_indeksowania[:3])
# print(string_do_indeksowania[1:3])

# integer_start_index = 0
# integer_stop_index = 3
# print("Wycinam kawałek stringu:", string_do_indeksowania[integer_start_index:integer_stop_index])
# print("Wycinam kawałek stringu pomiędzy indeksami", integer_start_index, "i", integer_stop_index, ". "
#     "Wycięty fragment to:", string_do_indeksowania[integer_start_index:integer_stop_index])

exit()

######################################
### Punkt 1.5 - Stringi vs. liczby ###
######################################
print("Punkt 1.5 - Stringi vs. liczby\n")

string_zmienna_tekstowa_1 = "123"
string_zmienna_tekstowa_2 = "456"
print(string_zmienna_tekstowa_1 + string_zmienna_tekstowa_2)

# integer_zmienna_liczbowa_1 = 123
# integer_zmienna_liczbowa_2 = 456
# print(integer_zmienna_liczbowa_1 + integer_zmienna_liczbowa_2)

exit()

##############################################
### Punkt 2 - Funkcje i metody w stringach ###
##############################################

############################################################################
### Punkt 2.1 - Funkcje w stringach, czyli 'int()', 'str()' oraz 'len()' ###
############################################################################
print("Punkt 2.1 - Funkcje w stringach, czyli 'int()', 'str()' oraz 'len()' \n")

string_zmienna_tekstowa_1 = "123"
string_zmienna_tekstowa_2 = "456"

# print("'Type Casting', czyli rzutowanie typu tekstowego na liczbowy w Python:",
#       int(string_zmienna_tekstowa_1) + int(string_zmienna_tekstowa_2))

# integer_zmienna_liczbowa_1 = 123
# integer_zmienna_liczbowa_2 = 456
# print("'Type Casting', czyli rzutowanie typu liczbowego na tekstowy w Python:",
#       str(integer_zmienna_liczbowa_1) + str(integer_zmienna_liczbowa_2))

# string_zmienna_tekstowa = "String!"

# print("Długość stringu:", len(string_zmienna_tekstowa))

# integer_dlugosc_stringu = len(string_zmienna_tekstowa)
# print("Ostatnim znakiem tego stringu jest (będzie błąd!):",
#       string_zmienna_tekstowa[integer_dlugosc_stringu])

# integer_dlugosc_stringu = len(string_zmienna_tekstowa)
# print("Ten string ma długość:", integer_dlugosc_stringu ,"znaków, a jego ostatnim znakiem jest:",
#       string_zmienna_tekstowa[integer_dlugosc_stringu-1])

exit()

#####################################################################################################
### Punkt 2.2 - Metody stringów, czyli 'lower()', 'upper()', 'replace()', 'count()' oraz 'find()' ###
#####################################################################################################
print("Punkt 2.2 - Metody stringów, czyli 'lower()', 'upper()', 'replace()', 'count()' oraz 'find()'\n")

string_do_testowania_metod = "Witamy na szkoleniach Python!"

print("Metoda 'upper()':", string_do_testowania_metod.upper())

# print("Metoda 'lower()':", string_do_testowania_metod.lower())

# print("Metoda 'replace()':", string_do_testowania_metod.replace("na szkoleniach Python!", "w piekle!"))

# print("Metoda 'count()':", string_do_testowania_metod.count("o"))

# print("Metoda 'find()':", string_do_testowania_metod.find("m"))