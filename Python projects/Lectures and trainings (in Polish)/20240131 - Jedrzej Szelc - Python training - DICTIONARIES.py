#################################################
##### Date: 2024.01.31                      #####
##### Stream: Python Based Automation       #####
##### Author: jedrzej.szelc@capgemini.com   #####
##### Subject: Typy danych - Słowniki       #####
#################################################

print()

##########################################
### Punkt 1 - Słowniki w języku Python ###
##########################################

###################################
### Punkt 1.1 - Klucz : Wartość ###
###################################
print("Punkt 1.1 - Klucz : Wartość\n")

slownik = {
    "klucz" : "wartosc klucza"
    }

print(slownik)

# slownik = {
#     "klucz_nr_1" : "wartosc_nr_1", "klucz nr 2" : "wartosc nr 2", "klucz bez podkreslen" : 123,
#     "klucz_z_podkresleniami" : 456,
#     123 : "012 + słowo",
#     1 : 321,
#     2 : "To nie jest lista!"
# }
#
# print(slownik)

# print(slownik["klucz_nr_1"])

# print(slownik["Błędny klucz"])
# print(slownik["klucz_nr 1"])

# klucz_slownika = "klucz_nr_1"
# print("Kluczowi:",klucz_slownika,
#       "\nodpowiada następująca wartość w słowniku:",
#       slownik[klucz_slownika])

exit()

###############################
### Punkt 1.2 - Typy kluczy ###
###############################
print("Punkt 1.2 - Typy kluczy\n")

slownik_kluczy_typu_integers = {
    0 : 0,
    1 : "To jest słownik, nie lista!",
    2 : "To też jest słownik!",
    3 : 4
}

klucz_slownika = 1
print("Kluczowi:",klucz_slownika,
      "\nodpowiada następująca wartość w słowniku:", slownik_kluczy_typu_integers[klucz_slownika])

# slownik_kluczy_typu_string = {
#     "Ania" : 1300,
#     "Piotr" : 1500,
#     "Kasia" : 3500,
#     "Zuza" : 6500
# }
#
# klucz_slownika = "Ania"
# print("Kluczowi:",klucz_slownika,
#       "\nodpowiada następująca wartość w słowniku:", slownik_kluczy_typu_string[klucz_slownika])

# slownik_kluczy_mieszanych = {
#     "Ania" : 1300,
#     1500 : "Piotr",
#     3500 : "Kasia",
#     "Zuza" : 6500
# }
#
# klucz_slownika = 1500
# print("Kluczowi:",klucz_slownika,
#       "\nodpowiada następująca wartość w słowniku:", slownik_kluczy_mieszanych[klucz_slownika])

exit()

##############################################################################
### Punkt 1.3 - Modyfikacja par 'Klucz:Wartość' w już istniejącym słowniku ###
##############################################################################
print("Punkt 1.3 - Modyfikacja par 'Klucz:Wartość' w już istniejącym słowniku\n")

slownik = {
    "Ania" : 1300,
    1500 : "Piotr",
    3500 : "Kasia",
    "Zuza" : 6500
}

slownik["Ania"] = "jest mądra!"
print("Printuję słownik ze zmodyfikowaną parą klucz:wartość:\n", slownik)

# slownik["Nowy klucz"] = "Nowa wartość"
# print("Printuję słownik z dodaną parą klucz:wartość:\n", slownik)

exit()

#############################################
### Punkt 1.4 - Tworzenie nowego słownika ###
#############################################
print("Punkt 1.4 - Tworzenie pustego słownika\n")

pusty_slownik = {}
print("Printuję pusty słownik:", pusty_slownik)

# pusty_slownik["Nowy klucz w pustym słowniku"] = "Nowa wartość w pustym słowniku"
# print("Printuję pusty słownik:", pusty_slownik)

# pusty_slownik = dict()
# print("Printuję pusty słownik:", pusty_slownik)

# nowy_slownik = dict(klucz_imie="Jędrzej", klucz_opis="jest 'gópi'...")
# print("Printuję nowy słownik:", nowy_slownik)

exit()

################################################
### Punkt 1.5 - Słownik z zagnieżdżoną listą ###
################################################
print("Punkt 1.5 - Słownik z zagnieżdżoną listą\n")

slownik_z_zagniezdzona_lista = {
    "klucz" : 123,
    "lista" : [456, 789, "Element listy"]
}

print("Printuję element zagnieżdżonej listy:\n", slownik_z_zagniezdzona_lista["lista"][1])

exit()

######################################################
### Punkt 1.6 - Słownik z zagnieżdżonym słownikiem ###
######################################################
print("Punkt 1.6 - Słownik z zagnieżdżonym słownikiem\n")

slownik_z_zagniezdzonym_slownikiem = {
    "klucz" : 123,
    "slownik" : {789 : "Wartość zagnieżdżonego słownika"}
}

print("Printuję wartość zagnieżdżonego słownika:\n", slownik_z_zagniezdzonym_slownikiem["slownik"][789])

exit()

############################################################
### Punkt 2 - Funkcje i metody słowników w języku Python ###
############################################################

###################################
### Punkt 2.1 - Funkcja 'len()' ###
###################################
print("Punkt 2.1 - Funkcja 'len()'\n")

slownik = {
    "Ania" : 1300,
    1500 : "Piotr",
    3500 : "Kasia",
    "Zuza" : 6500
}

print("Printuję liczbę kluczy słownika:", len(slownik))

exit()

##############################################################
### Punkt 2.2 - Metody 'keys()', 'values()' oraz 'items()' ###
##############################################################
print("Punkt 2.2 - Metody 'keys()', 'values()' oraz 'items()'\n")

slownik = {
    "Ania" : 1300,
    1500 : "Piotr",
    3500 : "Kasia",
    "Zuza" : 6500
}

print("Printuję klucze słownika w formie 'dictionary view object':\n", slownik.keys())

# print("Printuję wartości słownika w formie 'dictionary view object':\n", slownik.values())

# print("Printuję wszystkie elementy słownika w formie 'dictionary view object':\n", slownik.items())

# klucze_slownika = list(slownik.keys())
# print("Printuję klucze słownika w formie listy:\n", klucze_slownika)

exit()

#####################################
### Punkt 2.3 - Metoda 'update()' ###
#####################################
print("Punkt 2.3 - Metoda 'update()'\n")

slownik = {
    "Ania" : 1300,
    1500 : "Piotr",
    3500 : "Kasia",
    "Zuza" : 6500
}

slownik["Ania"] = "jest mądra!"
print("Printuję słownik ze zmodyfikowaną parą klucz:wartość:\n", slownik)

# slownik.update({"Ania":"jest jeszcze mądrzejsza..."})
# print("Printuję słownik z parą klucz:wartość zmodyfikowaną metodą 'update()':\n", slownik)

# slownik.update(
#     {"Ania":"jest jeszcze mądrzejsza...",
#      "Zuza":"jest debeściakiem!"}
# )
# print("Printuję słownik z parą klucz:wartość zmodyfikowaną metodą 'update()':\n", slownik)

exit()

###############################################
### Punkt 2.4 - Metoda 'get()' oraz 'pop()' ###
###############################################
print("Punkt 2.4 - Metoda 'get()' oraz 'pop()'\n")

slownik = {
    "Ania" : 1300,
    1500 : "Piotr",
    3500 : "Kasia",
    "Zuza" : 6500
}

pobrana_wartosc = slownik.get("Ania")
print("Printuję wartość pobraną ze słownika metodą 'get()':", pobrana_wartosc,
      "\noraz cały słownik po użyciu metody 'get()':\n", slownik)

# wyjeta_wartosc = slownik.pop("Ania")
# print("Printuję wartość wyjętą ze słownika metodą 'pop()':", wyjeta_wartosc,
#       "\noraz cały słownik po użyciu metody 'pop()':\n", slownik)

exit()

#######################################################
### Punkt 2.5 - Komenda 'del' oraz metoda 'clear()' ###
#######################################################
print("Punkt 2.5 - Komenda 'del' oraz metoda 'clear()'\n")

slownik = {
    "Ania" : 1300,
    1500 : "Piotr",
    3500 : "Kasia",
    "Zuza" : 6500
}

del slownik[3500]
print("Printuję cały słownik po użyciu komendy del:\n", slownik)

# slownik.clear()
# print("Printuję cały słownik po użyciu metody 'clear()':\n", slownik)

exit()

######################################################
### Bonus nr 1 - Biblioteka i kalkulator Dłużników ###
######################################################
### Opis:
### Piszemy kalkulator Dłużników oparty o bibliotekę danych.
### W bibliotece:
### - kluczem każdego Dłużnika jest NIP (Numer Identyfikacji Podatkowej),
### - dane każdego Dłużnika przechowywane są w formie zagnieżdżonej listy.
### Kalkulator ma za zadanie:
### - obliczyć bilans zadłużenia danego Dłużnika,
### - obliczyć proporcję zadłużenia do oszczędności danego Dłużnika.

### Biblioteka danych:
slownik_biblioteka_dluznikow = {
    8918223666 : ["Jędrzej", "Szelc", -1623.78, 1231.92],
    8288113724 : ["Jan", "Nowak", -123.45, 1478]
}

### Selektor danych:
integer_NIP = 8918223666

### Konfiguracja - Rozpakowanie danych:
string_imie = slownik_biblioteka_dluznikow[integer_NIP][0]
string_nazwisko = slownik_biblioteka_dluznikow[integer_NIP][1]
float_dlug = slownik_biblioteka_dluznikow[integer_NIP][2]
float_oszczednosci = slownik_biblioteka_dluznikow[integer_NIP][3]
float_bilans = round(float_dlug + float_oszczednosci, 2)
float_proporcja_zadluzenia = round(-100*float_dlug/float_oszczednosci,2)

### Odczyt danych:
print("Dłużnik o numerze NIP:", integer_NIP,
      "\nimię:", string_imie,
      "\nnazwisko:", string_nazwisko,
      "\nma długi w wysokości:", float_dlug,
      "\noraz oszczędności w wysokości:", float_oszczednosci,
      "\nco daje łączny bilans w wysokości:", float_bilans,
      "\ni proporcję zadłużenia do oszczędności:",float_proporcja_zadluzenia, "%")

exit()

#####################################
### Bonus nr 2 - Słownik vs. JSON ###
#####################################

fruit_dictionary = {
    "fruit": "Apple",
    "size": "Large",
    "color": "Red"
}