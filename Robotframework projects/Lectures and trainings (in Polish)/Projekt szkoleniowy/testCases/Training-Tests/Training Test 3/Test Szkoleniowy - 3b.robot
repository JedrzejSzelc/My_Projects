*** Settings ***
Resource         ../../../resources/wspoldzielone_zasoby.robot

*** Variables ***
${list_with_strings}       Pierwszy string z listy lokalnej        Drugi string z listy lokalnej

*** Keywords ***
Log to console two values given as single list
    [Documentation]     Wyprintuj do konsoli dwie wartosci z pojedynczej listy wejsciowej
    [Arguments]         ${list_input_variable}
    Log to console      ${list_input_variable}[0]
    Log to console      ${list_input_variable}[1]

*** Test Cases ***
Training-Test-3b

    [Documentation]         Dokumentacja testu szkoleniowego nr 3b - Test nr 3b: Praca z globalnymi keywordami oraz globalnymi zmiennymi
    [Tags]                  tag-testu-szkoleniowego-nr-3b
    ...                     tag-wszystkich-testow-3
    ...                     tag-wszystkich-testow

    ### Lista jako pojedynczy parametr wejściowy Keyworda
    Log to console two values given as single list          ${list_with_strings}

    ### Współdzielone zasoby z biblioteki "wspoldzielone_zasoby.robot" w katalogu "Resources"
    Global Keyword that Prints Out Value To Console         To jest test 3b
    Global Keyword that Prints Out Value To Console         ${global_list_with_strings}[0]
    Global Keyword that Prints Out Value To Console         ${global_list_with_strings}[1]