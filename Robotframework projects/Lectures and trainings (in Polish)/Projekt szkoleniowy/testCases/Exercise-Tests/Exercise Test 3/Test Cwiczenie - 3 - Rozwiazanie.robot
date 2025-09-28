*** Settings ***
### Rozwiązanie zadania dot. testu automatycznego, który:
# 1) ma keyword lokalny, który to keyword przyjmuje dwa parametry wejściowe i zwraca jeden parametr wyjściowy. Ten lokalny lokalny ma służyć dodawaniu dwóch stringów - podpowiedź: skorzystaj z keyworda wbudowanego "Set Variable". Rozwiązanie może wyglądać np. w taki sposób: ${string_output}         Set Variable        Pierwszy string: ${string_input_number_1} został połączony z drugim stringiem: ${string_input_number_2}
# 2) korzysta z zasobów biblioteki "wspoldzielone_zasoby.robot" w katalogu resources, a konkretnie z globalnego keyworda: "Global Keyword that Prints Out Value To Console" oraz z globalnej listy: @{global_list_with_strings}
# 3) przy pomocy Twojego lokalnego keyworda dodaje dwa stringi z listy globalnej ${global_list_with_strings} i przy pomocy "Global Keyword that Prints Out Value To Console" wypisuje do konsoli nowy, połączony string.
# Uwagi końcowe: to nie jest długie lub skomplikowane zadanie. Jeśli masz wątpliwości, zapytaj Jędrzeja lub popatrz do rozwiązania.

Resource         ../../../resources/wspoldzielone_zasoby.robot

*** Variables ***

*** Keywords ***
Add Two Strings Together and Return Them As New String
    [Documentation]     Ten Keyword dodaje dwa stringi i zwraca je jako jeden string
    [Arguments]                 ${string_input_number_1}        ${string_input_number_2}
    ${string_output}            Set Variable        Pierwszy string: ${string_input_number_1} został połączony z drugim stringiem: ${string_input_number_2}
    RETURN                      ${string_output}

*** Test Cases ***
Exercise-Test-3-Solution

    [Documentation]         Dokumentacja testu ćwiczenia nr 3 - Ćwiczenie nr 3: Podstawy Keywordów
    [Tags]                  tag-testu-cwiczenia-nr-3-rozwiazanie
    ...                     tag-wszystkich-testow

    ${string_wyjsciowy}     Add Two Strings Together and Return Them As New String      ${global_list_with_strings}[0]          ${global_list_with_strings}[1]
    Global Keyword that Prints Out Value To Console         ${string_wyjsciowy}