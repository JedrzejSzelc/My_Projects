*** Settings ***
Library         SeleniumLibrary

*** Variables ***
@{global_list_with_strings}            Pierwszy element listy globalnej            Drugi element listy globalnej

*** Keywords ***
Global Keyword that Prints Out Value To Console
    [Documentation]     To jest keyword globaly, który printuje coś do konsoli
    [Arguments]         ${string_input_value}
    Log to console      Printuję z wnętrza keyworda globalnego: ${string_input_value}