#####################################################
##### Date: 2024.03.13                          #####
##### Stream: Python Based Automation           #####
##### Author: jedrzej.szelc@capgemini.com       #####
##### Subject: Podstawy Pythona - Pętla 'for'   #####
#####################################################

print()

#############################################
### Punkt 1 - Pętla 'for' w języku Python ###
#############################################

####################################################
### Punkt 1.1 - Podstawowa struktura pętli 'for' ###
####################################################
print("Punkt 1.1 - Podstawowa struktura pętli 'for'\n")

lista_liczb = [1, 2, 3, 4, 5]

for pojedyncza_liczba in lista_liczb:
    print("Printuję liczbę:", pojedyncza_liczba)

# for pojedyncza_liczba in lista_liczb:
#     print("Printuję licznik z dodaną wartością 10:", pojedyncza_liczba+10)

exit()

###################################################
### Punkt 1.2 - Pętla 'for' vs. komenda 'break' ###
###################################################
print("Punkt 1.2 - Pętla 'for' vs. komenda 'break'\n")

lista_liczb = [1, 2, 3, 4, 5]

for pojedyncza_liczba in lista_liczb:
    if pojedyncza_liczba == 3:
        print("Znalazłem liczbę 3 i przerywam pętlę!")
        break
    print("Printuję liczbę:", pojedyncza_liczba)

exit()

#########################################################################
### Punkt 1.3 - Pętla 'for' vs. komenda 'continue' vs. komenda 'pass' ###
#########################################################################
print("Punkt 1.3 - Pętla 'for' vs. komenda 'continue' vs. komenda 'pass'\n")

lista_liczb = [1, 2, 3, 4, 5]

for pojedyncza_liczba in lista_liczb:
    if pojedyncza_liczba == 3:
        continue
        # pass
    print("Printuję liczbę:", pojedyncza_liczba)

# if 3 in lista_liczb:
#     pass
# else:
#     pass

exit()

#################################################################
### Punkt 1.4 - Przykład praktyczny: iterowanie przez stringi ###
#################################################################
print("Punkt 1.4 - Przykłady praktyczne: iterowanie przez stringi\n")

przykladowy_string = "Jędrzej jest 'gópi'."

for pojedyncza_litera in przykladowy_string:
    print("Printuję literę:", pojedyncza_litera)

# lista_litery_ze_stringu = []
# for pojedyncza_litera in przykladowy_string:
#     lista_litery_ze_stringu.append(pojedyncza_litera)
# print("Lista liter ze stringu:", lista_litery_ze_stringu)

exit()

#####################################################
### Punkt 1.5 - Pętla 'for' vs. funkcja 'range()' ###
#####################################################
print("Punkt 1.5 - Pętla 'for' vs. funkcja 'range()'\n")

# Funkcja range() umożliwia tworzenie sekwencji liczb
# wg. następującego schematu : range(start, stop, step)

obiekt_funkcji_range = range(10)
print("Obiektu funkcji range():", obiekt_funkcji_range)

# lista_stworzona_przy_uzyciu_range = list(obiekt_funkcji_range)
# print("Konwersja obiektu funkcji 'range' do listy:", lista_stworzona_przy_uzyciu_range)

# for pojedyncza_liczba in obiekt_funkcji_range:
#     print("Printuję liczbę:", pojedyncza_liczba)

exit()

#############################################################
### Punkt 1.6 - Przykład praktyczny: odwrócony ciąg liczb ###
#############################################################
print("Punkt 1.6 - Przykład praktyczny: odwrócony ciąg liczb\n")

# Funkcja range() umożliwia tworzenie sekwencji liczb
# wg. następującego schematu : range(start, stop, step)

obiekt_funkcji_range = range(10, 0, -1)
print("Obiektu funkcji range():", obiekt_funkcji_range)

for pojedyncza_liczba in obiekt_funkcji_range:
    print("Printuję liczbę:", pojedyncza_liczba)

exit()

###########################################################
### Punkt 1.7 - Przykład praktyczny: odwracanie stringu ###
###########################################################
print("Punkt 1.7 - Przykład praktyczny: odwracanie stringu\n")

przykladowy_string = "Jędrzej jest 'gópi'."

for iterator_liter in range(len(przykladowy_string)-1,-1,-1):
    print("Printuję literę:", przykladowy_string[iterator_liter])

exit()

###########################################
### Punkt 2 - Zagnieżdżanie pętli 'for' ###
###########################################

############################################
### Punkt 2.1 - Zagnieżdżone pętle 'for' ###
############################################
print("Punkt 2.1 - Zagnieżdżone pętle 'for' \n")

for integer_iterator_zewnetrznej_petli in range(0,3):
    for integer_iterator_wewnetrznej_petli in range(0,3):
        print("Iterator zewnętrznej pętli ma wartość:", integer_iterator_zewnetrznej_petli,
              "a iterator wewnętrznej pętli ma wartość:", integer_iterator_wewnetrznej_petli)
    print("--> Przechodzimy do kolejnej wartości iteratora zewnętrznej pętli.")

exit()

###########################################################
### Punkt 2.2 - Przykład praktyczny: tabliczka mnożenia ###
###########################################################
print("Punkt 2.2 - Przykład praktyczny: tabliczka mnożenia \n")

integer_wartosc_koncowa = 3

for integer_iterator_zewnetrznej_petli in range(0, integer_wartosc_koncowa):
    for integer_iterator_wewnetrznej_petli in range(0, integer_wartosc_koncowa):
        print(integer_iterator_zewnetrznej_petli," x ", integer_iterator_wewnetrznej_petli," = ",
              integer_iterator_zewnetrznej_petli*integer_iterator_wewnetrznej_petli)

exit()

##################################################################
### Punkt 2.3 - Przykład praktyczny: konwersja listy 2D do 1D ###
##################################################################
print("Punkt 2.3 - Przykład praktyczny: konwersja listy 2D do 1D\n")

lista_2D = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Lista dwuwymiarowa:", lista_2D)

lista_1D = []
integer_liczba_rzedow = len(lista_2D)
for integer_iterator_rzedow in range(0,integer_liczba_rzedow):
    lista_dany_rzad = lista_2D[integer_iterator_rzedow]
    integer_liczba_kolumn_w_danym_rzedzie = len(lista_dany_rzad)
    for integer_iterator_danego_elementu in range(0,integer_liczba_kolumn_w_danym_rzedzie):
        lista_1D.append(lista_dany_rzad[integer_iterator_danego_elementu])

print("Lista jednowymiarowa:", lista_1D)

exit()

##################################################################
### Punkt 2.4 - Przykład praktyczny: konwersja listy 1D do 2D ###
##################################################################
print("Punkt 2.4 - Przykład praktyczny: konwersja listy 1D do 2D\n")

lista_1D = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Lista jednowymiarowa:", lista_1D)

integer_wymagana_liczba_kolumn = 3
integer_wymagana_liczba_rzedow = 3

lista_2D = []
for integer_iterator_rzedow in range(0, integer_wymagana_liczba_rzedow):
    lista_dany_rzad = []
    for integer_iterator_kolumn in range(0, integer_wymagana_liczba_kolumn):
        lista_dany_rzad.append(lista_1D.pop(0))
    lista_2D.append(lista_dany_rzad)

print("Lista dwuwymiarowa:", lista_2D)

exit()

################################################
### Punkt 3 - Struktura 'else' w pętli 'for' ###
################################################

######################################################################
### Punkt 3.1 - Struktura 'else' w pętli 'for' jako tzw. 'nobreak' ###
######################################################################
print("Punkt 3.1 - Struktura 'else' w pętli 'for' jako tzw. 'nobreak'\n")

lista_liczb = [1, 2, 3, 4, 5]

for pojedyncza_liczba in lista_liczb:
    print("Printuję liczbę:", pojedyncza_liczba)
    if pojedyncza_liczba == 3:
        print("Przerywamy pętlę!")
        break
else:
    print("Dotarliśmy do końca pętli!")

exit()

########################################################################
### Punkt 3.2 - Przykład praktyczny: szukamy danej wartości w liście ###
########################################################################
print("Punkt 3.2 - Przykład praktyczny: szukamy danej wartości w liście\n")

lista_liczb = [123, 22, 38, 4450, 785]
liczba_do_znalezienia = 38

for pojedyncza_liczba in lista_liczb:
    print("Przeszukuję listę i obecnie analizuję wartość:", pojedyncza_liczba)
    if pojedyncza_liczba == liczba_do_znalezienia:
        print("Ta lista zawiera liczbę:", liczba_do_znalezienia)
        break
else:
    print("Ta lista nie zawiera liczby:", liczba_do_znalezienia)