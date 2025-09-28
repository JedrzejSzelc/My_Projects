*** Settings ***
### Rozwiązanie zadania dot. testu automatycznego, który:
# 1) ma komentarze w swojej treści,
# 2) automatycznie otwiera przeglądarkę Chrome i maksymalizuje ją,
# 3) otwiera stronę https://robotframework.org/,
# 4) ma funkcjonalność związaną z otwieraniem przeglądarki Chrome oraz wybieraniem właściwej strony www zawartą w jednym, osobnym keywordzie,
# 5) sprawdza czy na stronie wymienionej w punkcie 2. znajdują się następujące wyrażenia: "Get started" oraz "Code is worth a thousand words."
# 6) potwierdza, że na stronie wymienionej w punkcie 2. NIE znajduje się następujące wyrażenie: "Jędrzej jest głupi." - podpowiedź: skorzystaj z keywordów w bibliotece Selenium (https://robotframework.org/SeleniumLibrary/SeleniumLibrary.html)
# 7) automatycznie zamyka przeglądarkę Chrome po zakończeniu testu,
# Następnie:
# a) uruchom ten test w oknie terminala i zapisz logi testu,
# b) przeanalizuj logi testu. Co widzisz w plikach logów lokalnych, gdy Twój test się skończy?
# Uwagi końcowe: jeśli masz wątpliwości, zapytaj Jędrzeja lub popatrz do rozwiązania w osobnym pliku.

Library         SeleniumLibrary

*** Variables ***

*** Keywords ***
Start and Maximise Browser
    [Documentation]     Ten keyword służy uruchomieniu przeglądarki www oraz jej zmaksymalizowaniu
    Open Browser        https://robotframework.org/         chrome       options=add_experimental_option("excludeSwitches", ["enable-logging"])
    Maximize Browser Window

*** Test Cases ***
Exercise-Test-0-2-Solution

    [Documentation]         Dokumentacja testu ćwiczenia nr 0-2 - Ćwiczenie nr 0-2: Podstawy Keywordów
    [Tags]                  tag-testu-cwiczenia-nr-0-2-rozwiazanie
    ...                     tag-wszystkich-testow

    ### Uruchamian przeglądarkę Chrome, maksymalizuję ją i otwieram wybraną stronę www
    Start and Maximise Browser

    ### Sprawdzam zawartość strony
    Page Should Contain         Get started
    Page Should Contain         Code is worth a thousand words.

    ### Zamykam przeglądarkę Chrome
    Close Browser