*** Settings ***
Library         SeleniumLibrary

*** Variables ***

*** Keywords ***

*** Test Cases ***
Test-Konfiguracyjny

    [Documentation]         Dokumentacja testu konfiguracyjnego
    [Tags]                  tag-testu-konfiguracyjnego

    ### Otwórz przeglądarkę, zmaksymalizuj ją, otwórz strone robotframework.org
    Open Browser                https://robotframework.org/         chrome       options=add_experimental_option("excludeSwitches", ["enable-logging"])
    Maximize Browser Window