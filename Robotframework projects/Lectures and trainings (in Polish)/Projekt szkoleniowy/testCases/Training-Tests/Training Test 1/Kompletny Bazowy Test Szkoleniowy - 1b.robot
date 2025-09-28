*** Settings ***
Library         SeleniumLibrary

*** Variables ***

*** Keywords ***

*** Test Cases ***
Training-Test-1b

    [Documentation]         Dokumentacja testu szkoleniowego nr 1b - Test nr 1b: Kompletny, bazowy test szkoleniowy - test celowo spowolniony przy pomocy keywordów "sleep"
    [Tags]                  tag-testu-szkoleniowego-nr-1b
    ...                     tag-wszystkich-testow-1
    ...                     tag-wszystkich-testow

    ### Kroki 1, 2 oraz 3 - Otwórz przeglądarkę, zmaksymalizuj ją, otwórz strone robotframework.org
    Open Browser                https://robotframework.org/         chrome       options=add_experimental_option("excludeSwitches", ["enable-logging"])
    Maximize Browser Window

    ### Krok 4 - Potwierdź, że strona zawiera określoną treść
    Page Should Contain         Robot Framework is an open source
    Sleep                       3s

    ### Krok 5 - Kliknij przycisk "Docs"
    Click Button                //button[.//text() = 'Docs']
    Sleep                       3s

    ### Krok 6 - Kliknij napis "Guides"
    Click Element               //A[@data-v-504fa6b0=''][text()='Guides']

    ### Krok 7 - Potwierdź, że strona zawiera określoną treść
    Wait Until Page Contains        Welcome to
    Wait Until Page Contains        We hope these guides will help you
    Sleep                           3s

    ### Krok 8 - Sprawdź artykuł dot. Dockera w sekcji "Docs" przy pomocy opcji "Search"
    Click Element                       //SPAN[@class='DocSearch-Button-Placeholder'][text()='Search']
    Wait until Element is Visible       //INPUT[@id='docsearch-input']
    Sleep                               1s
    Input Text                          //INPUT[@id='docsearch-input']      Docker
    Sleep                               2s
    Press keys                          //INPUT[@id='docsearch-input']      ENTER
    Wait Until Page Contains            Check out the official Docker Documentation
    Sleep                               3s

    ### Krok 9 - Sprawdź artykuł dot. Standard Library w sekcji "Docs" przy pomocy opcji "Search"
    Click Element                       //SPAN[@class='DocSearch-Button-Placeholder'][text()='Search']
    Wait until Element is Visible       //INPUT[@id='docsearch-input']
    Sleep                               1s
    Input Text                          //INPUT[@id='docsearch-input']      Standard Library
    Sleep                               2s
    Press keys                          //INPUT[@id='docsearch-input']      ENTER
    Wait Until Page Contains            The BuiltIn library is the most important library
    Sleep                               3s

    ### Krok 10 - Sprawdź artykuł dot. GitLab w sekcji "Docs" przy pomocy opcji "Search"
    Click Element                       //SPAN[@class='DocSearch-Button-Placeholder'][text()='Search']
    Wait until Element is Visible       //INPUT[@id='docsearch-input']
    Sleep                               1s
    Input Text                          //INPUT[@id='docsearch-input']      GitLab
    Sleep                               2s
    Press keys                          //INPUT[@id='docsearch-input']      ENTER
    Wait Until Page Contains            GitLab is a development platform
    Sleep                               3s

    ### Krok 11 - Zamknij przeglądarkę
    Close Browser