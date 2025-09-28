*** Settings ***
Library         SeleniumLibrary

*** Variables ***
${string_variable_Delay_Time_in_Seconds}        3s
${string_variable_www_address}                  https://robotframework.org/
@{list_with_strings}                            Robot Framework is an open source          widely used in the industry.

*** Keywords ***
Start and Maximise Browser Using Input Variable
    [Documentation]     Ten keyword służy uruchamieniu przeglądarki www oraz maksymalizowaniu jej okna. Keyword przyjmuje jedną zmienną wejściową
    [Arguments]         ${string_internal_variable}
    Open Browser        url=${string_internal_variable}         browser=chrome       options=add_experimental_option("excludeSwitches", ["enable-logging"])
    Maximize Browser Window

Wait Given Number of Seconds
    [Documentation]     To jest keyword opóźniający, który opóźnia program o określony czas
    [Arguments]         ${input_value}
    Sleep               ${input_value}

Page Should Contain Given String
    [Documentation]     Sprawdź czy konkretny, sprecyzowany string znajduje się na stronie
    [Arguments]                 ${string_variable_text_that_should_be_on_webpage}
    Page Should Contain         ${string_variable_text_that_should_be_on_webpage}

Page Should Contain Two Given Strings
    [Documentation]     Sprawdź czy dwa konkretne, sprecyzowane stringi znajdują się na stronie
    [Arguments]                 ${string_variable_text_that_should_be_on_webpage_1}     ${string_variable_text_that_should_be_on_webpage_2}
    Page Should Contain         ${string_variable_text_that_should_be_on_webpage_1}
    Page Should Contain         ${string_variable_text_that_should_be_on_webpage_2}

Page Should Contain One String and Print Info Inside Keyword If String Found
    [Documentation]     Sprawdź czy konkretny, sprecyzowany string znajduje się na stronie. Następnie wypisz informację do konsoli
    [Arguments]                 ${string_variable_text_that_should_be_on_webpage}     ${string_to_be_returned}
    Page Should Contain         ${string_variable_text_that_should_be_on_webpage}
    Log to console              Printuję do konsoli z wnętrza keyworda informcję o tym, że na stronie znaleziono tekst: ${string_variable_text_that_should_be_on_webpage} i dodatkowo dodaję info, że: ${string_to_be_returned}
    Log                         Loguję z wnętrza keyworda informację o tym, że na stronie znaleziono tekst: ${string_variable_text_that_should_be_on_webpage} i dodatkowo dodaję info, że: ${string_to_be_returned}

Page Should Contain One String and Return Info If String Found
    [Documentation]     Sprawdź czy konkretny, sprecyzowany string znajduje się na stronie. Następnie zwróć nowy string jako zmienną wyjściową
    [Arguments]                 ${string_variable_text_that_should_be_on_webpage}     ${string_to_be_returned}
    Page Should Contain         ${string_variable_text_that_should_be_on_webpage}
    RETURN                      Na stronie znaleziono tekst: ${string_variable_text_that_should_be_on_webpage} i dodatkowo dodaję info, że: ${string_to_be_returned}

*** Test Cases ***
Training-Test-3a

    [Documentation]         Dokumentacja testu szkoleniowego nr 3a - Test nr 3a: Praca z lokalnymi keywordami oraz lokalnymi zmiennymi
    [Tags]                  tag-testu-szkoleniowego-nr-3a
    ...                     tag-wszystkich-testow-3
    ...                     tag-wszystkich-testow

    ### Kroki 1, 2 oraz 3 - Otwórz przeglądarkę, zmaksymalizuj ją, otwórz strone robotframework.org
    Start and Maximise Browser Using Input Variable        ${string_variable_www_address}
    Wait Given Number of Seconds                ${string_variable_Delay_Time_in_Seconds}

    ### Krok 4 - Potwierdź, że strona zawiera określoną treść
    Page Should Contain Given String            Robot Framework is an open source
    ${string_variable_text_to_be_checked}       Set Variable            widely used in the industry.
    Wait Until Page Contains                    ${string_variable_text_to_be_checked}
    Page Should Contain Two Given Strings       Robot Framework is an open source        It is supported by the Robot Framework Foundation
    Page Should Contain One String and Print Info Inside Keyword If String Found         Robot Framework is an open source           Jędrzej jest głupi.
    ${string_output_value}                      Page Should Contain One String and Return Info If String Found            Robot Framework is an open source        Jędrzej jest głupi.
    Log to console                              Wartość zwrócona z wnętrza keyworda: ${string_output_value}
    Log                                         Wartość zwrócona z wnętrza keyworda: ${string_output_value}
    Wait Given Number of Seconds                ${string_variable_Delay_Time_in_Seconds}

    ### Modyfikacja kroku 4 - korzystamy z listy lokalnej
    Wait Until Page Contains                    ${list_with_strings}[0]
    Wait Until Page Contains                    ${list_with_strings}[1]
    Wait Given Number of Seconds                ${string_variable_Delay_Time_in_Seconds}

    ### Ostatni Krok - Zamknij przeglądarkę
    Close Browser