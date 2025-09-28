*** Settings ***
Library         SeleniumLibrary

*** Variables ***

*** Keywords ***

*** Test Cases ***
Training-Test-0a

    [Documentation]         Dokumentacja testu szkoleniowego nr 0a - Test nr 0a: Struktura pliku .robot oraz podstawy składni Robot Framework
    [Tags]                  tag-testu-szkoleniowego-nr-0a
    ...                     tag-wszystkich-testow-0
    ...                     tag-wszystkich-testow

    Log To Console          Printuję do konsoli (terminala) ten oto tekst z testu 0a.
    Log                     Printuję do pliku .log ten oto tekst z testu 0a.