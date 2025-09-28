*** Settings ***
Library         SeleniumLibrary

*** Variables ***
${string_variable_www_address}          https://robotframework.org/
${string_XPath_Docs_Button}             //button[.//text() = 'Docs']
${string_XPath_Guides_New_Element}      //A[@data-v-504fa6b0=''][text()='Guides']

@{list_strings_of_docs_articles}        Docker          Standard Library        GitLab
@{list_strings_of_docs_content}         Check out the official Docker Documentation         The BuiltIn library is the most important library           GitLab is a development platform

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
Training-Test-6

    [Documentation]         Dokumentacja testu szkoleniowego nr 6 - Test nr 6: Kompletny, finalny test szkoleniowy
    [Tags]                  tag-testu-szkoleniowego-nr-6
    ...                     tag-wszystkich-testow

    ### Kroki 1, 2 oraz 3 - Otwórz przeglądarkę, zmaksymalizuj ją, otwórz strone robotframework.org
    Start and Maximise Browser Using Input Variable        ${string_variable_www_address}

    ### Krok 4 - Potwierdź, że strona zawiera określoną treść
    Page Should Contain         Robot Framework is an open source

    ### Krok 5 - Kliknij przycisk "Docs"
    Click Button                ${string_XPath_Docs_Button}

    ### Krok 6 - Kliknij napis "Guides"
    Click Element               ${string_XPath_Guides_New_Element}

    ### Krok 7 - Potwierdź, że strona zawiera określoną treść
    Wait Until Page Contains         Welcome to
    Wait Until Page Contains         We hope these guides will help you

    ### Kroki 8, 9 i 10 przy pomocy pętli FOR oraz z wykorzystaniem jednego warunku IF
    ${integer_docs_articles_list_length}        Get Length          ${list_strings_of_docs_articles}
    ${integer_docs_content_list_length}         Get Length          ${list_strings_of_docs_content}
    IF      ${integer_docs_articles_list_length} == ${integer_docs_content_list_length}
        FOR    ${integer_counter}    IN RANGE   ${integer_docs_articles_list_length}
                Open Selected Docs Page and Check its Content           ${list_strings_of_docs_articles}[${integer_counter}]          ${list_strings_of_docs_content}[${integer_counter}]
        END
    ELSE
        Log to console      Długość listy "Docs Articles" nie równa się długości listy "Docs Content": ${integer_docs_articles_list_length} != ${integer_docs_content_list_length}
    END

    ### Krok 11 - Zamknij przeglądarkę
    Close Browser