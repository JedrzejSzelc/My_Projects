*** Settings ***
Resource        ../../../resources/wspoldzielone_zasoby.robot
Library         ../../../resources/dodatkowe_funkcje_python.py

*** Variables ***

*** Keywords ***

*** Test Cases ***
Training-Test-7

    [Documentation]         Dokumentacja testu szkoleniowego nr 7 - Test nr 7: Python w Robot Framework
    [Tags]                  tag-testu-szkoleniowego-nr-7
    ...                     tag-wszystkich-testow

    ${integer_wynik_dodawania}      Funkcja Dodaj dwie wartosci     ${12}   ${34}
    Log to console          Dodałem dwie wartości przy pomocy keyworda zbudowanego w Pythonie: ${integer_wynik_dodawania}

    ${integer_dlugosc_listy}        Funkcja Podaj Dlugosc Listy     ${global_list_with_strings}
    Log to console          Długość listy określona przy pomocy keyworda zbudowanego w Pythonie: ${integer_dlugosc_listy}