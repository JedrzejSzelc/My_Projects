*** Settings ***
### Napisz test automatyczny, który:
# 1) automatycznie otwiera przeglądarkę Chrome i maksymalizuje ją (skorzystaj z już dostępnego keyworda - patrz niżej),
# 2) przechodzi od razu do strony: https://docs.robotframework.org/docs
# 3) pomija kroki manualne numer 4,5,6 i 7 (w instrukcji kroków manualnych testu szkoleniowego). Test od razu przechodzi z kroku manualnego nr 3 do kroku nr 8,
# 4) ma lokalny keyword, który zawiera pełną funkcjonalność kroku testowego nr 8, czyli:
#   - wybiera okienko "Search"
#   - przy pomocy okienka “Search” otwiera wybrany artykuł - wartość ta podawana jest jako pierwsza zmienna wejściowa keyworda, np.: ${string_Docs_Page_Keyword}
#   - potwierdza, że na stronie jest określony tekst - string z tekstem jest podawany jako druga zmienna wejściowa keyworda, np.: ${string_Text_To_Be_Found_On_Page}
#   - keyword nie ma zmiennych wyjściowych
# Przy pisaniu lokalnego keyworda wykorzystaj następujące keywordy wbudowane Robot Framework (odnośniki: https://robotframework.org/robotframework/ oraz https://robotframework.org/SeleniumLibrary/SeleniumLibrary.html):
#   - Click element
#   - Wait until element is visible
#	- Input Text
#	- Press keys
#	- Wait until page contains
# Zadania bonusowe:
#   a) znajdź samodzielnie XPath okienka "Search",
#   b) znajdź samodzielnie XPath okienka "Search docs", które otwiera się po kliknięciu "Search",
#   c) przy pomocy nowego keyworda lokalnego zaimplementuj również manualne kroki testowe nr 9 i 10,
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

*** Test Cases ***
Exercise-Test-4

    [Documentation]         Dokumentacja testu ćwiczenia nr 4 - Ćwiczenie nr 4: XPathy - Zadanie
    [Tags]                  tag-testu-cwiczenia-nr-4-zadanie
    ...                     tag-wszystkich-testow

    ### Kroki 1, 2 oraz 3 - Otwórz przeglądarkę, zmaksymalizuj ją, otwórz strone robotframework.org
    Start and Maximise Browser Using Input Variable        ${string_variable_www_address}

    ### Krok 8 - Sprawdź artykuł dot. Dockera w sekcji "Docs" przy pomocy opcji "Search"
    # Tutaj wpisz rozwiązanie

    ### Krok 9 - Sprawdź artykuł dot. Standard Library w sekcji "Docs" przy pomocy opcji "Search"
    # Tutaj wpisz rozwiązanie

    ### Krok 10 - Sprawdź artykuł dot. GitLab w sekcji "Docs" przy pomocy opcji "Search"
    # Tutaj wpisz rozwiązanie

    ### Ostatni Krok - Zamknij przeglądarkę.
    Close Browser