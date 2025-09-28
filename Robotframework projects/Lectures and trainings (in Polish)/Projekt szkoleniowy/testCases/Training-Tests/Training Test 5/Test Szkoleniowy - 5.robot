*** Settings ***
Resource         ../../../resources/wspoldzielone_zasoby.robot

*** Variables ***
${string_variable_www_address}                  https://docs.robotframework.org/docs

#@{list_docs_strings_for_Docker}                 Docker                  Check out the official Docker Documentation
#@{list_docs_strings_for_Standard_Library}       Standard Library        The BuiltIn library is the most important library
#@{list_docs_strings_for_GitLab}                 GitLab                  GitLab is a development platform

#@{list_strings_of_docs_articles}                Docker          Standard Library        GitLab
#@{list_strings_of_docs_content}                 Check out the official Docker Documentation         The BuiltIn library is the most important library           GitLab is a development platform

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
Training-Test-5

    [Documentation]         Dokumentacja testu szkoleniowego nr 5 - Test nr 5: Listy z pęltą "FOR" oraz warunkiem "IF"
    [Tags]                  tag-testu-szkoleniowego-nr-5
    ...                     tag-wszystkich-testow

    ### Kroki 1, 2 oraz 3 - Otwórz przeglądarkę, zmaksymalizuj ją, otwórz strone robotframework.org
    Start and Maximise Browser Using Input Variable        ${string_variable_www_address}

    ### Krok 8 - Sprawdź artykuł dot. Dockera w sekcji "Docs" przy pomocy opcji "Search"
    Open Selected Docs Page and Check its Content           Docker                  Check out the official Docker Documentation
#    Open Selected Docs Page and Check its Content           ${list_docs_strings_for_Docker}[0]          ${list_docs_strings_for_Docker}[1]

    ### Krok 9 - Sprawdź artykuł dot. Standard Library w sekcji "Docs" przy pomocy opcji "Search"
    Open Selected Docs Page and Check its Content           Standard Library        The BuiltIn library is the most important library
#    Open Selected Docs Page and Check its Content           ${list_docs_strings_for_Standard_Library}[0]        ${list_docs_strings_for_Standard_Library}[1]

    ### Krok 10 - Sprawdź artykuł dot. GitLab w sekcji "Docs" przy pomocy opcji "Search"
    Open Selected Docs Page and Check its Content           GitLab                  GitLab is a development platform
#    Open Selected Docs Page and Check its Content           ${list_docs_strings_for_GitLab}[0]          ${list_docs_strings_for_GitLab}[1]

#    ### Kroki 8, 9 i 10 przy pomocy pętli FOR
#    FOR    ${integer_counter}    IN RANGE   0   3
#            Open Selected Docs Page and Check its Content           ${list_strings_of_docs_articles}[${integer_counter}]          ${list_strings_of_docs_content}[${integer_counter}]
#    END

#    ### Kroki 8, 9 i 10 przy pomocy pętli FOR oraz z wykorzystaniem warunku IF
#    ${string_skip_docs_article}     Set Variable        GitLab
#    FOR    ${integer_counter}    IN RANGE   0   3
#        IF      "${list_strings_of_docs_articles}[${integer_counter}]" != "${string_skip_docs_article}"
#            Open Selected Docs Page and Check its Content           ${list_strings_of_docs_articles}[${integer_counter}]          ${list_strings_of_docs_content}[${integer_counter}]
#        ELSE
#            Log to console      Odrzucam sprawdzanie: ${list_strings_of_docs_articles}[${integer_counter}]
#        END
#    END

#    ### Kroki 8, 9 i 10 przy pomocy pętli FOR oraz z wykorzystaniem dwóch warunków IF
#    ${string_skip_docs_article}     Set Variable        GitLab
#    ${integer_docs_articles_list_length}        Get Length          ${list_strings_of_docs_articles}
#    ${integer_docs_content_list_length}         Get Length          ${list_strings_of_docs_content}
#    ${integer_docs_content_list_length}         Set Variable        2
#    IF      ${integer_docs_articles_list_length} == ${integer_docs_content_list_length}
#        FOR    ${integer_counter}    IN RANGE   ${integer_docs_articles_list_length}
#            IF      "${list_strings_of_docs_articles}[${integer_counter}]" != "${string_skip_docs_article}"
#                Open Selected Docs Page and Check its Content           ${list_strings_of_docs_articles}[${integer_counter}]          ${list_strings_of_docs_content}[${integer_counter}]
#            ELSE
#                Log to console      Odrzucam sprawdzanie: ${list_strings_of_docs_articles}[${integer_counter}]
#            END
#        END
#    ELSE
#        Log to console      Długość listy "Docs Articles" nie równa się długości listy "Docs Content": ${integer_docs_articles_list_length} != ${integer_docs_content_list_length}
#    END

    ### Ostatni Krok - Zamknij przeglądarkę.
    Close Browser