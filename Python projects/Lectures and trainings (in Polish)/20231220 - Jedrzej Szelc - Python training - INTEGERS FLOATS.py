#####################################################
##### Date: 2023.12.20                          #####
##### Stream: Python Based Automation           #####
##### Author: jedrzej.szelc@capgemini.com       #####
##### Subject: Typy danych - Integer i Float    #####
#####################################################

print()

###################################################
### Punkt 1 - Wartości liczbowe w języku Python ###
###################################################

########################################################
### Punkt 1.1 - Typ danych 'integer' w języku Python ###
########################################################
print("Punkt 1.1 - Typ danych 'integer' w języku Python\n")

zmienna_integer_1 = 123
zmienna_integer_2 = 456

print("Zmienna typu integer nr 1 ma wartość:", zmienna_integer_1)
print("Zmienna typu integer nr 2 ma wartość:", zmienna_integer_2)

# zmienna_wynik_dodawania_integer = zmienna_integer_1 + zmienna_integer_2
# print("Wynik dodawania dwóch zmiennych typu integer:", zmienna_wynik_dodawania_integer)

# zmienna_wynik_odejmowania_integer = zmienna_integer_1 - zmienna_integer_2
# print("Wynik odejmowania dwóch zmiennych typu integer:", zmienna_wynik_odejmowania_integer)

# integer_number_of_cars = 12
# integer_number_of_people = 340

# integer_on_value = 1
# integer_off_value = 0

exit()

######################################################
### Punkt 1.2 - Typ danych 'float' w języku Python ###
######################################################
print("Punkt 1.2 - Typ danych 'float' w języku Python\n")

zmienna_float_1 = 123.45
zmienna_float_2 = 456.78

print("Zmienna typu float nr 1 ma wartość:", zmienna_float_1)
print("Zmienna typu float nr 2 ma wartość:", zmienna_float_2)

# zmienna_wynik_dodawania_float = zmienna_float_1 + zmienna_float_2
# print("Wynik dodawania dwóch zmiennych typu float:", zmienna_wynik_dodawania_float)

# zmienna_wynik_odejmowania_float = zmienna_float_1 - zmienna_float_2
# print("Wynik odejmowania dwóch zmiennych typu float:", zmienna_wynik_odejmowania_float)

# float_exact_car_speed_in_kmh = 122.35
# float_exact_milk_fat_content_in_grams_per_liter = 35.8

# float_current_interest_rates_percent_value = 5.75
# float_argon_in_atmosphere_percent_value = 0.93

exit()

#########################################################################################
### Punkt 1.3 - Podstawowa arytmetyka przy użyciu typów danych 'integer' oraz 'float' ###
#########################################################################################
print("Punkt 1.3 - Podstawowa arytmetyka przy użyciu typów danych 'integer' oraz 'float'\n")

# '+' - dodawanie
# '-' - odejmowanie
# '*' - mnożenie
# '/' - dzielenie
# '//' - zaokrąglenie 'w dół'
# '**' - funkcja eksponencjalna, czyli 'do potęgi'
# '%' - modulo, czyli reszta z dzielenia
# '()' - nawiasy, czyli kolejność wykonywania działań

print(4 + 3)

# print(((8*2)-2)*10)

exit()

##############################################################################
### Punkt 1.4 - Operatory relacyjne vs. typy danych 'integer' oraz 'float' ###
##############################################################################
print("Punkt 1.4 - Operatory relacyjne vs. typy danych 'integer' oraz 'float'\n")

# '>' - większy
# '>=' - większy równy
# '<' - mniejszy
# '<=' - mniejszy równy
# '==' - równy
# '!=' - nie równy

print(11.2 > 11.2)

exit()

##############################################################
### Punkt 2 - Wybrane funkcje i metody wartości liczbowych ###
##############################################################

##################################################
### Punkt 2.1 - Funkcje 'abs()' oraz 'round()' ###
##################################################
print("Punkt 2.1 - Funkcje 'abs()' oraz 'round()'\n")

float_zmienna_liczbowa = -157.23924

print("Wartość bezwzględna (absolutna), czyli funkcja 'abs()':", abs(float_zmienna_liczbowa))

# print("Zaokrąglenie, czyli funkcja 'round()':", round(float_zmienna_liczbowa, 4))

exit()

#################################################################
### Punkt 2.2 - 'Type Casting', czyli rzutowanie typów danych ###
#################################################################
print("Punkt 2.2 - 'Type Casting', czyli rzutowanie typów danych\n")

zmienna_integer = 123
zmienna_float = 456.78

wynik_dodawania = zmienna_integer + zmienna_float
print("Wynik dodawania zmiennej typu integer i zmiennej typu float:", wynik_dodawania)

# wynik_odejmowania = zmienna_integer - zmienna_float
# print("Wynik odejmowania zmiennej typu integer i zmiennej typu float:", wynik_odejmowania)

# print("'Type Casting' typu float na typ integer:", int(zmienna_float))

# print("'Type Casting' typu integer na typ float:", float(zmienna_integer))

# wynik_dodania_dwoch_stringow = str(zmienna_integer) + str(zmienna_float)
# print("Informacja bonusowa: Wynik dodania dwóch stringów\n"
#       "po przeprowadzeniu 'Type Casting' z typów integer oraz float\n"
#       "na typ string:", wynik_dodania_dwoch_stringow)

exit()

##################################################################
### Punkt 2.3 - Metoda 'isnumeric()' oraz funkcja 'isinstance' ###
##################################################################
print("Punkt 2.3 - Metoda 'isnumeric()' oraz funkcja 'isinstance'\n")

zmienna_string_numeryczny = "123"
zmienna_string_tekstowy = "123x"
zmienna_integer = 123
zmienna_float = 456.78

print(zmienna_string_numeryczny.isnumeric())

# print(isinstance(zmienna_string_numeryczny, str))

exit()

################################################################
### Bonus - Dwuliczbowy kalkulator z wykorzystaniem stringów ###
################################################################
### Opis:
### Piszemy dwuliczbowy kalkulator, który jako parametry wejściowe przyjmuje dwie liczby
### a jako wartości wyjściowe zwraca sformatowane i opisane wyniki wybranej, podstawowej arytmetyki (patrz punkt 1.3)
### oraz porównuje dane wejściowe (dwie liczby) przy użyciu operatorów relacyjnych (patrz punkt 1.4).
### Warunki dodatkowe:
### - korzystamy ze stringów,
### - stosujemy komentarze i konwencję "snake_case" nazw zmiennych,
### - wyniki operacji arytmetycznych powinny być z dokładnością do dwóch miejsc po przecinku,
### - sprawdź czy zmienne wejściowe są typu "integer" lub "float".

### Dane wejściowe:
zmienna_wejsciowa_1 = 123.45
zmienna_wejsciowa_2 = 67.89

### Dane wyjściowe - podstawowa arytmetyka:
print("Wyniki podstawowych obliczeń arytmetycznych:")

wynik_dodawnia = round(zmienna_wejsciowa_1 + zmienna_wejsciowa_2, 2)
wynik_odejmowania = round(zmienna_wejsciowa_1 - zmienna_wejsciowa_2, 2)
wynik_mnozenia = round(zmienna_wejsciowa_1 * zmienna_wejsciowa_2, 2)
wynik_dzielenia = round(zmienna_wejsciowa_1 / zmienna_wejsciowa_2, 2)

print(zmienna_wejsciowa_1,"+",zmienna_wejsciowa_2,"=", wynik_dodawnia)
print(zmienna_wejsciowa_1,"-",zmienna_wejsciowa_2,"=", wynik_odejmowania)
print(zmienna_wejsciowa_1,"*",zmienna_wejsciowa_2,"=", wynik_mnozenia)
print(zmienna_wejsciowa_1,"/",zmienna_wejsciowa_2,"=", wynik_dzielenia)

### Dane wyjściowe - podstawowe porównanie:
print("Wyniki podstawowego porównania:")

print(zmienna_wejsciowa_1,">",zmienna_wejsciowa_2,"=", zmienna_wejsciowa_1 > zmienna_wejsciowa_2)
print(zmienna_wejsciowa_1,">=",zmienna_wejsciowa_2,"=", zmienna_wejsciowa_1 >= zmienna_wejsciowa_2)
print(zmienna_wejsciowa_1,"<",zmienna_wejsciowa_2,"=", zmienna_wejsciowa_1 < zmienna_wejsciowa_2)
print(zmienna_wejsciowa_1,"<=",zmienna_wejsciowa_2,"=", zmienna_wejsciowa_1 <= zmienna_wejsciowa_2)

### Dane wyjściowe - sprawdzam czy wartości wejściowe są typu "integer" lub "float":
print("Sprawdzam czy zmienne wejściowe są typu 'integer' lub 'float':")

print("Czy zmienna wejściowa nr 1 to integer? Odpowiedź:", isinstance(zmienna_wejsciowa_1, int))
print("Czy zmienna wejściowa nr 1 to float? Odpowiedź:", isinstance(zmienna_wejsciowa_1, float))
print("Czy zmienna wejściowa nr 2 to integer? Odpowiedź:", isinstance(zmienna_wejsciowa_2, int))
print("Czy zmienna wejściowa nr 2 to float? Odpowiedź:", isinstance(zmienna_wejsciowa_2, float))