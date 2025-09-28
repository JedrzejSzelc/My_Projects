*** Settings ***
Library         SeleniumLibrary

*** Variables ***

*** Keywords ***
Start and Maximise Browser
    [Documentation]     Ten keyword służy uruchamieniu przeglądarki www oraz maksymalizowaniu jej okna
    Open Browser        https://robotframework.org/         chrome       options=add_experimental_option("excludeSwitches", ["enable-logging"])
    Maximize Browser Window

Page Should Contain Robot Framework is an open source
    [Documentation]             Sprawdź czy konkretny, sprecyzowany string: "Robot Framework is an open source" znajduje się na stronie
    Page Should Contain         Robot Framework is an open source

Wait 3 Seconds
    [Documentation]     To jest keyword opóźniający, który opóźnia program o dokładnie trzy sekundy
    Sleep       3s

*** Test Cases ***
Training-Test-2

    [Documentation]         Dokumentacja testu szkoleniowego nr 2 - Test nr 2: Podstawy Keywordów
    [Tags]                  tag-testu-szkoleniowego-nr-2
    ...                     tag-wszystkich-testow

    ### Kroki 1, 2 oraz 3 - Otwórz przeglądarkę, zmaksymalizuj ją, otwórz strone robotframework.org
    Start and Maximise Browser

    ### Krok 4 - Potwierdź, że strona zawiera określoną treść.
    Page Should Contain         Robot Framework is an open source
    Sleep                       3s

    ### Ostatni Krok - Zamknij przeglądarkę.
    Close Browser