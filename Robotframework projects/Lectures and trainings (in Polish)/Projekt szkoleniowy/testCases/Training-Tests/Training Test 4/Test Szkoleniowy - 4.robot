*** Settings ***
Resource         ../../../resources/wspoldzielone_zasoby.robot

*** Variables ***
${string_variable_www_address}      https://robotframework.org/

*** Keywords ***
Start and Maximise Browser Using Input Variable
    [Documentation]     Ten keyword służy uruchamieniu przeglądarki www oraz maksymalizowaniu jej okna. Keyword przyjmuje jedną zmienną wejściową.
    [Arguments]         ${string_internal_variable}
    Open Browser        url=${string_internal_variable}         browser=chrome       options=add_experimental_option("excludeSwitches", ["enable-logging"])
    Maximize Browser Window

*** Test Cases ***
Training-Test-4

    [Documentation]         Dokumentacja testu szkoleniowego nr 4 - Test nr 4: XPathy
    [Tags]                  tag-testu-szkoleniowego-nr-4
    ...                     tag-wszystkich-testow

    ### Kroki 1, 2 oraz 3 - Otwórz przeglądarkę, zmaksymalizuj ją, otwórz strone robotframework.org
    Start and Maximise Browser Using Input Variable        ${string_variable_www_address}
    Sleep               2s

    ### Krok 5 - Kliknij przycisk "Docs"
#    Click Button        //button[@data-v-504fa6b0=''][text()='Get started']
#    Click Button        //button[.//text() = 'Get started']
    Click Button        //button[.//text() = 'Docs']
    Sleep               2s

    ### Krok 6 - Kliknij napis "Guides"
    Click Element       //A[@data-v-504fa6b0=''][text()='Guides']
    Sleep               2s

    ### Krok 8 - Sprawdź artykuł dot. Dockera w sekcji "Docs" przy pomocy opcji "Search"
    Click Element                       //SPAN[@class='DocSearch-Button-Placeholder'][text()='Search']
    Wait until Element is Visible       //INPUT[@id='docsearch-input']
    Input Text                          //INPUT[@id='docsearch-input']      Docker
    Sleep                               2s
    Press keys                          //INPUT[@id='docsearch-input']      ENTER
    Sleep                               2s
    Wait Until Page Contains            Check out the official Docker Documentation
    Sleep                               2s

    ### Ostatni Krok - Zamknij przeglądarkę.
    Close Browser