*** Settings ***
Library         SeleniumLibrary

*** Variables ***

*** Keywords ***

*** Test Cases ***
Training-Test-0b

    [Documentation]         Dokumentacja testu szkoleniowego nr 0b - Test nr 0b: Struktura pliku .robot oraz podstawy składni Robot Framework
    [Tags]                  tag-testu-szkoleniowego-nr-0b
    ...                     tag-wszystkich-testow-0
    ...                     tag-wszystkich-testow

    Log To Console          Printuję do konsoli (terminala) ten oto tekst z testu 0b.
    Log                     Printuję do pliku .log ten oto tekst z testu 0b.