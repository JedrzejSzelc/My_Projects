*** Settings ***
### Rozwiązanie zadania dot. testu automatycznego, który:
# 1) automatycznie otwiera przeglądarkę Chrome i maksymalizuje ją (skorzystaj z już dostępnego keyworda - patrz niżej),
# 2) przechodzi od razu do strony: https://docs.robotframework.org/docs
# 3) pomija kroki manualne numer 4,5,6 i 7 (w instrukcji kroków manualnych testu szkoleniowego). Test od razu przechodzi z kroku manualnego nr 3 do kroku nr 8,
# 4) wykonuje kroki testowe nr 8, 9 i 10 korzystając z już dostępnego keyworda lokalnego "Start and Maximise Browser Using Input Variable" - patrz niżej,
# 5) ma zdefiniowane dwie listy lokalne, których wartości stanowić będą dane wejściowe dla ww. keyworda lokalnego - np.: "@{list_strings_of_docs_articles}" oraz "@{list_strings_of_docs_content}",
# 6) wykonuje kroki testowe nr 8, 9 i 10 powtarzając przy pomocy pętli "FOR" oraz dwóch list lokalnych keyword "Start and Maximise Browser Using Input Variable",
# Zadania bonusowe:
#   a) przy pisaniu pętli "FOR" wykorzystaj keyword wbudowany "Get Length", aby znaleźć długość danej listy,
#   b) przenieś listy lokalne do współdzielonych zasobów - innymi słowy, zrób ze zmiennych lokalnych, zmienne globalne,
#   c) implementując pętle "FOR", wykorzystaj warunek "IF" do odrzucenia jednej z wartości wewnątrz wybranej listy.
# Uwagi końcowe: Cześć testu jest już zaimplementowana poniżej.

Resource         ../../../resources/wspoldzielone_zasoby.robot

*** Variables ***
${string_variable_www_address}      https://docs.robotframework.org/docs

*** Keywords ***
Start and Maximise Browser Using Input Variable
    [Documentation]     Ten keyword służy uruchamieniu przeglądarki www oraz maksymalizowaniu jej okna. Keyword przyjmuje jedną zmienną wejściową.
    [Arguments]         ${string_internal_variable}
    Open Browser        url=${string_internal_variable}         browser=chrome       options=add_experimental_option("excludeSwitches", ["enable-logging"])
    Maximize Browser Window

Open Selected Docs Page and Check its Content
    [Documentation]     Ten keyword otwiera wybraną stronę w 'Docs' i potwierdza, że na tej stronie znajduje się dany tekst
    [Arguments]         ${string_Docs_Page_Keyword}     ${string_Text_To_Be_Found_On_Page}
    Click Element                       //SPAN[@class='DocSearch-Button-Placeholder'][text()='Search']
    Wait until Element is Visible       //INPUT[@id='docsearch-input']
    Input Text                          //INPUT[@id='docsearch-input']      ${string_Docs_Page_Keyword}
    Press keys                          //INPUT[@id='docsearch-input']      ENTER
    Wait Until Page Contains            ${string_Text_To_Be_Found_On_Page}

*** Test Cases ***
Exercise-Test-5

    [Documentation]         Dokumentacja testu ćwiczenia nr 5 - Ćwiczenie nr 5: Listy z pęltą "FOR" oraz warunkiem "IF" - Zadanie
    [Tags]                  tag-testu-cwiczenia-nr-5-zadanie
    ...                     tag-wszystkich-testow

    ### Kroki 1, 2 oraz 3 - Otwórz przeglądarkę, zmaksymalizuj ją, otwórz strone robotframework.org
    Start and Maximise Browser Using Input Variable        ${string_variable_www_address}

    ### Kroki 8, 9 i 10 przy pomocy pętli FOR oraz z wykorzystaniem dwóch warunków IF
    # Tutaj wpisz rozwiązanie

    ### Ostatni Krok - Zamknij przeglądarkę.
    Close Browser