*** Settings ***
Library         SeleniumLibrary

*** Variables ***

*** Keywords ***

*** Test Cases ***
Training-Test-1a

    [Documentation]         Dokumentacja testu szkoleniowego nr 1a - Test nr 1a: Kompletny, bazowy test szkoleniowy
    [Tags]                  tag-testu-szkoleniowego-nr-1a
    ...                     tag-wszystkich-testow-1
    ...                     tag-wszystkich-testow

    ### Kroki 1, 2 oraz 3 - Otwórz przeglądarkę, zmaksymalizuj ją, otwórz strone robotframework.org
    Open Browser                https://robotframework.org/         chrome       options=add_experimental_option("excludeSwitches", ["enable-logging"])
    Maximize Browser Window

    ### Krok 4 - Potwierdź, że strona zawiera określoną treść
    Page Should Contain         Robot Framework is an open source

    ### Krok 5 - Kliknij przycisk "Docs"
    Click Button                //button[.//text() = 'Docs']

    ### Krok 6 - Kliknij napis "Guides"
    Click Element               //A[@data-v-504fa6b0=''][text()='Guides']

    ### Krok 7 - Potwierdź, że strona zawiera określoną treść
    Wait Until Page Contains         Welcome to
    Wait Until Page Contains         We hope these guides will help you

    ### Krok 8 - Sprawdź artykuł dot. Dockera w sekcji "Docs" przy pomocy opcji "Search"
    Click Element                       //SPAN[@class='DocSearch-Button-Placeholder'][text()='Search']
    Wait until Element is Visible       //INPUT[@id='docsearch-input']
    Input Text                          //INPUT[@id='docsearch-input']      Docker
    Press keys                          //INPUT[@id='docsearch-input']      ENTER
    Wait Until Page Contains            Check out the official Docker Documentation

    ### Krok 9 - Sprawdź artykuł dot. Standard Library w sekcji "Docs" przy pomocy opcji "Search"
    Click Element                       //SPAN[@class='DocSearch-Button-Placeholder'][text()='Search']
    Wait until Element is Visible       //INPUT[@id='docsearch-input']
    Input Text                          //INPUT[@id='docsearch-input']      Standard Library
    Press keys                          //INPUT[@id='docsearch-input']      ENTER
    Wait Until Page Contains            The BuiltIn library is the most important library

    ### Krok 10 - Sprawdź artykuł dot. GitLab w sekcji "Docs" przy pomocy opcji "Search"
    Click Element                       //SPAN[@class='DocSearch-Button-Placeholder'][text()='Search']
    Wait until Element is Visible       //INPUT[@id='docsearch-input']
    Input Text                          //INPUT[@id='docsearch-input']      GitLab
    Press keys                          //INPUT[@id='docsearch-input']      ENTER
    Wait Until Page Contains            GitLab is a development platform

    ### Krok 11 - Zamknij przeglądarkę
    Close Browser