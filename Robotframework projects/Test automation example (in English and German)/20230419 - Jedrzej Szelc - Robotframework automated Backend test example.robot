*** Settings ***
# Date created:     2023.04.19
# Tester/Creator:   jedrzej.szelc@capgemini.com
# Maintainer:       jedrzej.szelc@capgemini.com
Resource            Migration/resource.robot

*** Variables ***
${TXT_TEST_File_Name}                       TEST.2023-04-13T1358
${SQL_Table_Name_TEST_BUCHUNG}              TEST_BUCHUNG
${SQL_Table_Name_INTERIMSTEUERKONTO}        INTERIMSTEUERKONTO
${SQL_Table_Name_TRANSFORM}                 TRANSFORM
${SQL_Table_Name_TRANSFORMERGEBNIS}         TRANSFORMERGEBNIS

*** Keywords ***
Check If F100 Value Exists in List
    [Documentation]         Local Keyword for TEST-TICKET-12345. Checks if F100* value exists in a list given - Migration Project
    [Arguments]             ${SQL_DB_output}
    Remove Values From List     ${SQL_DB_output}        ${None}
    ${SQL_DB_output}            Set Variable            ${SQL_DB_output}[0]
    ${SQL_DB_output}            Set Variable            ${SQL_DB_output}[0:4]
    Should Contain Any          ${SQL_DB_output}        F100

Check If 911602001167 Value Exists in List
    [Documentation]         Local Keyword for TEST-TICKET-12345. Checks if 911602001167* value exists in a list given - Migration Project
    [Arguments]             ${SQL_DB_output}
    Remove Values From List     ${SQL_DB_output}        ${None}
    ${SQL_DB_output}            Set Variable            ${SQL_DB_output}[0]
    ${SQL_DB_output}            Set Variable            ${SQL_DB_output}[0:12]
    Should Contain Any          ${SQL_DB_output}        911602001167

*** Test Cases ***
TEST-TICKET-12345

    [Documentation]     TEST-TICKET-12345 - Migration - TEST - Transform - Test Type: Postive Path - Tester/Creator: jedrzej.szelc@capgemini.com
    [Setup]             Default Setup Migration
    [Tags]              migration
    ...                 TEST-transform
    ...                 nightly-regression

    ###############################
    ### MIG - Pre-configuration ###
    ###############################

    ### MIG - SSH Connection
    Open SSH Connection With Key For Migration TEST INT01

    ### MIG - SQL processing
    Connect To DB INT_PROJECT_MIG for Migration TEST

    ### MIG - SQL Clean Up for TEST_BUCHUNG TAble
    Execute DB  DELETE FROM ${SQL_Table_Name_TEST_BUCHUNG}

    ### MIG - Delete old folders
    Delete Old Folders From Server For Migration TEST INT01
    Delete Old Folders From Jenkins For Migration TEST INT01

    ### MIG - Prepare folders
    Create New Folders On Server For Migration TEST INT01
    Create New Folders On Jenkins For Migration TEST INT01

    ### MIG - Run Global SQL Clean-Up Batch
    Global SQL CleanUp for Migration

    ##################################################
    ### MIG - Step 1 - Vorbedingung - TEST-Extract ###
    ##################################################

    ### MIG - Upload the input file
    Copy a single TXT Input File from Jenkins to Server For Migration TEST INT01        ${TXT_TEST_File_Name}

    ### MIG - Run Extract Batch and save its .log files
    Run Extract Batch For Migration TEST INT01
    Download All Batch Console Log Files From Server To Jenkins For Migration TEST INT01

    ### MIG - Download and check the log file for TEST-Extract
    Download Selected Log File From Server For Migration TEST INT01         PROJECT-mig-batch-extract--trace.log
    Check If Given File Contains Given Text For Migration TEST INT01        PROJECT-mig-batch-extract--trace.log          [COMPLETED]

    ### MIG - Download the output file
    Download All Output Files From Server To Jenkins For Migration TEST INT01

    ### MIG - Check TEST_BUCHUNG SQL Table
    Compare One-By-One STEUERNR Records in Output TXT File To All SQL Attributes For Migration TEST INT01        ${TXT_TEST_File_Name}

    #####################################
    ### MIG - Step 2 - TEST-Transform ###
    #####################################

    ### MIG - Delete old folders
    Delete Old Folders From Server For Migration TEST INT01
    Delete Old Folders From Jenkins For Migration TEST INT01

    ### MIG - Prepare folders
    Create New Folders On Server For Migration TEST INT01
    Create New Folders On Jenkins For Migration TEST INT01

    ### MIG - Clean up TRANSFORM, TRANSFORMERGEBNIS and INTERIMSTEUERKONTO Tables in INT_PROJECT_MIG Database for Transform
    Execute DB      DELETE FROM ${SQL_Table_Name_TRANSFORM}
    Execute DB      DELETE FROM ${SQL_Table_Name_TRANSFORMERGEBNIS}
    Execute DB      DELETE FROM ${SQL_Table_Name_INTERIMSTEUERKONTO}

    ### MIG - Run Transform Batch and save its .log files
    Run Transform Batch For Migration TEST INT01
    Download All Batch Console Log Files From Server To Jenkins For Migration TEST INT01

    ### MIG - Check TRANSFORM Table in INT_PROJECT_MIG Database for Transform - Positive Path
    ${SQL_Number_of_Rows_in_Transform_to_be_processed_for_Positive_Path}        Set Variable        10

    ${SQL_DB_output}            Extract SQL Given Attribute From Given Table For Migration TEST Transform INT01         ${SQL_Table_Name_TRANSFORM}       STATUS_VERARBEITUNG       ${SQL_Number_of_Rows_in_Transform_to_be_processed_for_Positive_Path}
    Check If List Contains Only Given Word For Migration TEST Transform INT01            ${SQL_DB_output}               BEENDET

    ${SQL_DB_output}            Extract SQL Given Attribute From Given Table For Migration TEST Transform INT01           ${SQL_Table_Name_TRANSFORM}       ANZAHL_DATENSAETZE_TEST       ${SQL_Number_of_Rows_in_Transform_to_be_processed_for_Positive_Path}
    Should Not Be Equal as Integers        ${SQL_DB_output}[0]      0

    ### MIG - Check TRANSFORMERGEBNIS Table in INT_PROJECT_MIG Database for Transform
    ${SQL_Number_of_Rows_in_Transformergebnis_to_be_processed_for_Positive_Path}        Set Variable        10

    ${SQL_DB_output}            Extract SQL Given Attribute From Given Table For Migration TEST Transform INT01           ${SQL_Table_Name_TRANSFORMERGEBNIS}       MIGRIERT        ${SQL_Number_of_Rows_in_Transformergebnis_to_be_processed_for_Positive_Path}
    Should Contain Any          ${SQL_DB_output}        ${1}        Yes

    ${SQL_DB_output}            Extract SQL Given Attribute From Given Table For Migration TEST Transform INT01           ${SQL_Table_Name_TRANSFORMERGEBNIS}       NAME_ALTVERFAHREN       ${SQL_Number_of_Rows_in_Transformergebnis_to_be_processed_for_Positive_Path}
    Should Contain Any          ${SQL_DB_output}        TEST

    Confirm SQL Table Is NOT Empty For Migration         ${SQL_Table_Name_TRANSFORMERGEBNIS}

    ### MIG - Check INTERIMSTEUERKONTO Table in INT_PROJECT_MIG Database for Transform
    ${SQL_Number_of_Rows_in_Interimsteuerkonto_to_be_processed_for_Positive_Path}        Set Variable        10

    ${SQL_DB_output}            Extract SQL Given Attribute From Given Table For Migration TEST Transform INT01           ${SQL_Table_Name_INTERIMSTEUERKONTO}       BUCHUNGSSCHLUESSEL        ${SQL_Number_of_Rows_in_Interimsteuerkonto_to_be_processed_for_Positive_Path}
    Should Contain Any          ${SQL_DB_output}        0046    0053

    ${SQL_DB_output}            Extract SQL Given Attribute From Given Table For Migration TEST Transform INT01           ${SQL_Table_Name_INTERIMSTEUERKONTO}       NEBENSTEUERART       ${SQL_Number_of_Rows_in_Interimsteuerkonto_to_be_processed_for_Positive_Path}
    Should Contain              ${SQL_DB_output}        INFO

    Confirm SQL Table Is NOT Empty For Migration         ${SQL_Table_Name_INTERIMSTEUERKONTO}

    #################################################################################
    ### MIG - Step 3 - Validierung der Attributkonstellationen "Test parameter 1" ###
    #################################################################################

    ### MIG - Check INTERIMSTEUERKONTO Table in INT_PROJECT_MIG Database for Transform
    ${SQL_Number_of_Rows_in_Interimsteuerkonto_to_be_processed_for_Positive_Path}        Set Variable        10

    ${SQL_DB_output}            Extract SQL Given Attribute From Given Table For Migration TEST Transform INT01           ${SQL_Table_Name_INTERIMSTEUERKONTO}       STEUERNUMMER        ${SQL_Number_of_Rows_in_Interimsteuerkonto_to_be_processed_for_Positive_Path}
    Should Contain Any          ${SQL_DB_output}        9116020011670       9116020011671       9116020011672       9116020011673       9116020011674

    ### MIG - Check TRANSFORMERGEBNIS Table in INT_PROJECT_MIG Database for Transform
    ${SQL_Number_of_Rows_in_Transformergebnis_to_be_processed_for_Positive_Path}        Set Variable        1000

    ${SQL_DB_output}            Extract SQL Given Attribute From Given Table For Migration TEST Transform INT01           ${SQL_Table_Name_TRANSFORMERGEBNIS}       SCHLUESSEL_DATENSATZ        ${SQL_Number_of_Rows_in_Transformergebnis_to_be_processed_for_Positive_Path}
    Check If 911602001167 Value Exists in List     ${SQL_DB_output}

    ${SQL_DB_output}            Extract SQL Given Attribute From Given Table For Migration TEST Transform INT01           ${SQL_Table_Name_TRANSFORMERGEBNIS}       FEHLERBESCHREIBUNG        ${SQL_Number_of_Rows_in_Transformergebnis_to_be_processed_for_Positive_Path}
    Should contain              ${SQL_DB_Output}        ${None}

    ################################################################################
    ### MIG - Step 4 - Validierung der Attributtransformation "Test parameter 2" ###
    ################################################################################

    ### MIG - Step 4.1
    ${string_Steuernummer_current_value}        Set Variable        '9116020011670'
    ${string_Buchungstext_current_value}        Set Variable        '0046'

    ${SQL_DB_Output}        Return SQL Column Values With Two SQL Where Selectors for Migration         HAUPTSTEUERART        ${SQL_Table_Name_INTERIMSTEUERKONTO}       STEUERNUMMER      ${string_Steuernummer_current_value}      BUCHUNGSSCHLUESSEL        ${string_Buchungstext_current_value}
    ${SQL_DB_Output}        Unwrap SQL Column Values From List Of Tupples Into List for Migration       ${SQL_DB_Output}
    Should contain any      ${SQL_DB_Output}        000

    ${SQL_DB_Output}        Return SQL Column Values With Two SQL Where Selectors for Migration         NEBENSTEUERART        ${SQL_Table_Name_INTERIMSTEUERKONTO}       STEUERNUMMER      ${string_Steuernummer_current_value}      BUCHUNGSSCHLUESSEL        ${string_Buchungstext_current_value}
    ${SQL_DB_Output}        Unwrap SQL Column Values From List Of Tupples Into List for Migration       ${SQL_DB_Output}
    Should be equal as strings      ${SQL_DB_Output}[0]    0

    ### MIG - Step 4.2
    ${string_Steuernummer_current_value}        Set Variable        '9116020011671'
    ${string_Buchungstext_current_value}        Set Variable        '0046'

    ${SQL_DB_Output}        Return SQL Column Values With Two SQL Where Selectors for Migration         HAUPTSTEUERART        ${SQL_Table_Name_INTERIMSTEUERKONTO}       STEUERNUMMER      ${string_Steuernummer_current_value}      BUCHUNGSSCHLUESSEL        ${string_Buchungstext_current_value}
    ${SQL_DB_Output}        Unwrap SQL Column Values From List Of Tupples Into List for Migration       ${SQL_DB_Output}
    Should contain any      ${SQL_DB_Output}        107

    ${SQL_DB_Output}        Return SQL Column Values With Two SQL Where Selectors for Migration         NEBENSTEUERART        ${SQL_Table_Name_INTERIMSTEUERKONTO}       STEUERNUMMER      ${string_Steuernummer_current_value}      BUCHUNGSSCHLUESSEL        ${string_Buchungstext_current_value}
    ${SQL_DB_Output}        Unwrap SQL Column Values From List Of Tupples Into List for Migration       ${SQL_DB_Output}
    Should be equal as strings      ${SQL_DB_Output}[0]     0

    ### MIG - Step 4.3
    ${string_Steuernummer_current_value}        Set Variable        '9116020011672'
    ${string_Buchungstext_current_value}        Set Variable        '0046'

    ${SQL_DB_Output}        Return SQL Column Values With Two SQL Where Selectors for Migration         HAUPTSTEUERART        ${SQL_Table_Name_INTERIMSTEUERKONTO}       STEUERNUMMER      ${string_Steuernummer_current_value}      BUCHUNGSSCHLUESSEL        ${string_Buchungstext_current_value}
    ${SQL_DB_Output}        Unwrap SQL Column Values From List Of Tupples Into List for Migration       ${SQL_DB_Output}
    Should contain any      ${SQL_DB_Output}        107

    ${SQL_DB_Output}        Return SQL Column Values With Two SQL Where Selectors for Migration         NEBENSTEUERART        ${SQL_Table_Name_INTERIMSTEUERKONTO}       STEUERNUMMER      ${string_Steuernummer_current_value}      BUCHUNGSSCHLUESSEL        ${string_Buchungstext_current_value}
    ${SQL_DB_Output}        Unwrap SQL Column Values From List Of Tupples Into List for Migration       ${SQL_DB_Output}
    Should be equal as strings      ${SQL_DB_Output}[0]    9

    ### MIG - Step 4.4
    ${string_Steuernummer_current_value}        Set Variable        '9116020011673'
    ${string_Buchungstext_current_value}        Set Variable        '0046'

    ${SQL_DB_Output}        Return SQL Column Values With Two SQL Where Selectors for Migration         HAUPTSTEUERART        ${SQL_Table_Name_INTERIMSTEUERKONTO}       STEUERNUMMER      ${string_Steuernummer_current_value}      BUCHUNGSSCHLUESSEL        ${string_Buchungstext_current_value}
    ${SQL_DB_Output}        Unwrap SQL Column Values From List Of Tupples Into List for Migration       ${SQL_DB_Output}
    Should contain any      ${SQL_DB_Output}        108

    ${SQL_DB_Output}        Return SQL Column Values With Two SQL Where Selectors for Migration         NEBENSTEUERART        ${SQL_Table_Name_INTERIMSTEUERKONTO}       STEUERNUMMER      ${string_Steuernummer_current_value}      BUCHUNGSSCHLUESSEL        ${string_Buchungstext_current_value}
    ${SQL_DB_Output}        Unwrap SQL Column Values From List Of Tupples Into List for Migration       ${SQL_DB_Output}
    Should be equal as strings      ${SQL_DB_Output}[0]    0

    ### MIG - Step 4.5
    ${string_Steuernummer_current_value}        Set Variable        '9116020011674'
    ${string_Buchungstext_current_value}        Set Variable        '0046'

    ${SQL_DB_Output}        Return SQL Column Values With Two SQL Where Selectors for Migration         HAUPTSTEUERART        ${SQL_Table_Name_INTERIMSTEUERKONTO}       STEUERNUMMER      ${string_Steuernummer_current_value}      BUCHUNGSSCHLUESSEL        ${string_Buchungstext_current_value}
    ${SQL_DB_Output}        Unwrap SQL Column Values From List Of Tupples Into List for Migration       ${SQL_DB_Output}
    Should contain any      ${SQL_DB_Output}        108

    ${SQL_DB_Output}        Return SQL Column Values With Two SQL Where Selectors for Migration         NEBENSTEUERART        ${SQL_Table_Name_INTERIMSTEUERKONTO}       STEUERNUMMER      ${string_Steuernummer_current_value}      BUCHUNGSSCHLUESSEL        ${string_Buchungstext_current_value}
    ${SQL_DB_Output}        Unwrap SQL Column Values From List Of Tupples Into List for Migration       ${SQL_DB_Output}
    Should be equal as strings      ${SQL_DB_Output}[0]    9

    ################################################################################
    ### MIG - Step 5 - Validierung der Attributtransformation "Test parameter 3" ###
    ################################################################################

    ### MIG - Step 5.1
    ${string_Steuernummer_current_value}        Set Variable        '9116020011670'
    ${string_Buchungstext_current_value}        Set Variable        '0046'

    ${SQL_DB_Output}        Return SQL Column Values With Two SQL Where Selectors for Migration         ZEITRAUM        ${SQL_Table_Name_INTERIMSTEUERKONTO}       STEUERNUMMER      ${string_Steuernummer_current_value}      BUCHUNGSSCHLUESSEL        ${string_Buchungstext_current_value}
    ${SQL_DB_Output}        Unwrap SQL Column Values From List Of Tupples Into List for Migration       ${SQL_DB_Output}
    Should contain          ${SQL_DB_Output}        ${None}

    ${SQL_DB_Output}        Return SQL Column Values With Two SQL Where Selectors for Migration         PERIODENKZ        ${SQL_Table_Name_INTERIMSTEUERKONTO}       STEUERNUMMER      ${string_Steuernummer_current_value}      BUCHUNGSSCHLUESSEL        ${string_Buchungstext_current_value}
    ${SQL_DB_Output}        Unwrap SQL Column Values From List Of Tupples Into List for Migration       ${SQL_DB_Output}
    Should contain          ${SQL_DB_Output}        A

    ### MIG - Step 5.2
    ${string_Steuernummer_current_value}        Set Variable        '9116020011671'
    ${string_Buchungstext_current_value}        Set Variable        '0046'

    ${SQL_DB_Output}        Return SQL Column Values With Two SQL Where Selectors for Migration         ZEITRAUM        ${SQL_Table_Name_INTERIMSTEUERKONTO}       STEUERNUMMER      ${string_Steuernummer_current_value}      BUCHUNGSSCHLUESSEL        ${string_Buchungstext_current_value}
    ${SQL_DB_Output}        Unwrap SQL Column Values From List Of Tupples Into List for Migration       ${SQL_DB_Output}
    Should contain          ${SQL_DB_Output}        20171008

    ${SQL_DB_Output}        Return SQL Column Values With Two SQL Where Selectors for Migration         PERIODENKZ        ${SQL_Table_Name_INTERIMSTEUERKONTO}       STEUERNUMMER      ${string_Steuernummer_current_value}      BUCHUNGSSCHLUESSEL        ${string_Buchungstext_current_value}
    ${SQL_DB_Output}        Unwrap SQL Column Values From List Of Tupples Into List for Migration       ${SQL_DB_Output}
    Should contain          ${SQL_DB_Output}        T

    ### MIG - Step 5.3
    ${string_Steuernummer_current_value}        Set Variable        '9116020011672'
    ${string_Buchungstext_current_value}        Set Variable        '0046'

    ${SQL_DB_Output}        Return SQL Column Values With Two SQL Where Selectors for Migration         ZEITRAUM        ${SQL_Table_Name_INTERIMSTEUERKONTO}       STEUERNUMMER      ${string_Steuernummer_current_value}      BUCHUNGSSCHLUESSEL        ${string_Buchungstext_current_value}
    ${SQL_DB_Output}        Unwrap SQL Column Values From List Of Tupples Into List for Migration       ${SQL_DB_Output}
    Should contain          ${SQL_DB_Output}        20101231

    ${SQL_DB_Output}        Return SQL Column Values With Two SQL Where Selectors for Migration         PERIODENKZ        ${SQL_Table_Name_INTERIMSTEUERKONTO}       STEUERNUMMER      ${string_Steuernummer_current_value}      BUCHUNGSSCHLUESSEL        ${string_Buchungstext_current_value}
    ${SQL_DB_Output}        Unwrap SQL Column Values From List Of Tupples Into List for Migration       ${SQL_DB_Output}
    Should contain          ${SQL_DB_Output}        J

    #######################################################################################################
    ### MIG - Step 6 - Validierung der Attributtransformation "Test parameter 3" und "Test parameter 4" ###
    #######################################################################################################

    ${SQL_DB_Output}        Return SQL Column Values With SQL Where Selector for Migration      ZWANGSGELD      ${SQL_Table_Name_INTERIMSTEUERKONTO}       BUCHUNGSSCHLUESSEL        '0046'
    ${SQL_DB_Output}        Unwrap SQL Column Values From List Of Tupples Into List for Migration       ${SQL_DB_Output}
    Should contain          ${SQL_DB_Output}        ${None}

    ${SQL_DB_Output}        Return SQL Column Values With SQL Where Selector for Migration      FALLSAUMZSCHLG      ${SQL_Table_Name_INTERIMSTEUERKONTO}       BUCHUNGSSCHLUESSEL        '0046'
    ${SQL_DB_Output}        Unwrap SQL Column Values From List Of Tupples Into List for Migration       ${SQL_DB_Output}
    Should contain          ${SQL_DB_Output}        ${None}

    ################################################################################
    ### MIG - Step 7 - Validierung der Attributtransformation "Test parameter 5" ###
    ################################################################################

    ### MIG - Step 7.1
    ${string_Steuernummer_current_value}        Set Variable        '9116020011670'
    ${string_Buchungstext_current_value}        Set Variable        '0046'

    ${SQL_DB_Output}        Return SQL Column Values With Two SQL Where Selectors for Migration         SPERRVERMERK        ${SQL_Table_Name_INTERIMSTEUERKONTO}       STEUERNUMMER      ${string_Steuernummer_current_value}      BUCHUNGSSCHLUESSEL        ${string_Buchungstext_current_value}
    ${SQL_DB_Output}        Unwrap SQL Column Values From List Of Tupples Into List for Migration       ${SQL_DB_Output}
    Should contain          ${SQL_DB_Output}    01

    ### MIG - Step 7.2
    ${string_Steuernummer_current_value}        Set Variable        '9116020011671'
    ${string_Buchungstext_current_value}        Set Variable        '0046'

    ${SQL_DB_Output}        Return SQL Column Values With Two SQL Where Selectors for Migration         SPERRVERMERK        ${SQL_Table_Name_INTERIMSTEUERKONTO}       STEUERNUMMER      ${string_Steuernummer_current_value}      BUCHUNGSSCHLUESSEL        ${string_Buchungstext_current_value}
    ${SQL_DB_Output}        Unwrap SQL Column Values From List Of Tupples Into List for Migration       ${SQL_DB_Output}
    Should contain          ${SQL_DB_Output}    09

    ### MIG - Step 7.3
    ${string_Steuernummer_current_value}        Set Variable        '9116020011672'
    ${string_Buchungstext_current_value}        Set Variable        '0046'

    ${SQL_DB_Output}        Return SQL Column Values With Two SQL Where Selectors for Migration         SPERRVERMERK        ${SQL_Table_Name_INTERIMSTEUERKONTO}       STEUERNUMMER      ${string_Steuernummer_current_value}      BUCHUNGSSCHLUESSEL        ${string_Buchungstext_current_value}
    ${SQL_DB_Output}        Unwrap SQL Column Values From List Of Tupples Into List for Migration       ${SQL_DB_Output}
    Should contain          ${SQL_DB_Output}    13

    ### MIG - Step 7.4
    ${string_Steuernummer_current_value}        Set Variable        '9116020011673'
    ${string_Buchungstext_current_value}        Set Variable        '0046'

    ${SQL_DB_Output}        Return SQL Column Values With Two SQL Where Selectors for Migration         SPERRVERMERK        ${SQL_Table_Name_INTERIMSTEUERKONTO}       STEUERNUMMER      ${string_Steuernummer_current_value}      BUCHUNGSSCHLUESSEL        ${string_Buchungstext_current_value}
    ${SQL_DB_Output}        Unwrap SQL Column Values From List Of Tupples Into List for Migration       ${SQL_DB_Output}
    Should contain          ${SQL_DB_Output}    17

    ################################################################################
    ### MIG - Step 8 - Validierung der Attributtransformation "Test parameter 6" ###
    ################################################################################

    ### MIG - STEUERNUMMER: 9116020011670
    ${string_Steuernummer_current_value}        Set Variable        '9116020011670'
    ${string_Buchungstext_current_value}        Set Variable        '0053'

    ${SQL_DB_Output}        Return SQL Column Values With Two SQL Where Selectors for Migration         BUCHUNGSTEXT        ${SQL_Table_Name_INTERIMSTEUERKONTO}       STEUERNUMMER      ${string_Steuernummer_current_value}      BUCHUNGSSCHLUESSEL        ${string_Buchungstext_current_value}
    ${SQL_DB_Output}        Unwrap SQL Column Values From List Of Tupples Into List for Migration       ${SQL_DB_Output}
    Should contain          ${SQL_DB_Output}        a) Beginn und Ende der Steuerpflicht; Änderung der Zahlungsweise oder des Status einer Steuerart b) Vermerk einer Abmeldung

    ${string_Steuernummer_current_value}        Set Variable        '9116020011670'
    ${string_Buchungstext_current_value}        Set Variable        '0046'

    ${SQL_DB_Output}        Return SQL Column Values With Two SQL Where Selectors for Migration         BUCHUNGSTEXT        ${SQL_Table_Name_INTERIMSTEUERKONTO}       STEUERNUMMER      ${string_Steuernummer_current_value}      BUCHUNGSSCHLUESSEL        ${string_Buchungstext_current_value}
    ${SQL_DB_Output}        Unwrap SQL Column Values From List Of Tupples Into List for Migration       ${SQL_DB_Output}
    Should contain          ${SQL_DB_Output}        (VT-) Sperre setzen oder zurücknehmen, es gibt 3 verschiedene Formate --> KOMPLEX

    ### MIG - STEUERNUMMER: 9116020011671
    ${string_Steuernummer_current_value}        Set Variable        '9116020011671'
    ${string_Buchungstext_current_value}        Set Variable        '0053'

    ${SQL_DB_Output}        Return SQL Column Values With Two SQL Where Selectors for Migration         BUCHUNGSTEXT        ${SQL_Table_Name_INTERIMSTEUERKONTO}       STEUERNUMMER      ${string_Steuernummer_current_value}      BUCHUNGSSCHLUESSEL        ${string_Buchungstext_current_value}
    ${SQL_DB_Output}        Unwrap SQL Column Values From List Of Tupples Into List for Migration       ${SQL_DB_Output}
    Should contain          ${SQL_DB_Output}        a) Beginn und Ende der Steuerpflicht; Änderung der Zahlungsweise oder des Status einer Steuerart b) Vermerk einer Abmeldung

    ${string_Steuernummer_current_value}        Set Variable        '9116020011671'
    ${string_Buchungstext_current_value}        Set Variable        '0046'

    ${SQL_DB_Output}        Return SQL Column Values With Two SQL Where Selectors for Migration         BUCHUNGSTEXT        ${SQL_Table_Name_INTERIMSTEUERKONTO}       STEUERNUMMER      ${string_Steuernummer_current_value}      BUCHUNGSSCHLUESSEL        ${string_Buchungstext_current_value}
    ${SQL_DB_Output}        Unwrap SQL Column Values From List Of Tupples Into List for Migration       ${SQL_DB_Output}
    Should contain          ${SQL_DB_Output}        (VT-) Sperre setzen oder zurücknehmen, es gibt 3 verschiedene Formate --> KOMPLEX

    ### MIG - STEUERNUMMER: 9116020011672
    ${string_Steuernummer_current_value}        Set Variable        '9116020011672'
    ${string_Buchungstext_current_value}        Set Variable        '0053'

    ${SQL_DB_Output}        Return SQL Column Values With Two SQL Where Selectors for Migration         BUCHUNGSTEXT        ${SQL_Table_Name_INTERIMSTEUERKONTO}       STEUERNUMMER      ${string_Steuernummer_current_value}      BUCHUNGSSCHLUESSEL        ${string_Buchungstext_current_value}
    ${SQL_DB_Output}        Unwrap SQL Column Values From List Of Tupples Into List for Migration       ${SQL_DB_Output}
    Should contain          ${SQL_DB_Output}        a) Beginn und Ende der Steuerpflicht; Änderung der Zahlungsweise oder des Status einer Steuerart b) Vermerk einer Abmeldung

    ${string_Steuernummer_current_value}        Set Variable        '9116020011672'
    ${string_Buchungstext_current_value}        Set Variable        '0046'

    ${SQL_DB_Output}        Return SQL Column Values With Two SQL Where Selectors for Migration         BUCHUNGSTEXT        ${SQL_Table_Name_INTERIMSTEUERKONTO}       STEUERNUMMER      ${string_Steuernummer_current_value}      BUCHUNGSSCHLUESSEL        ${string_Buchungstext_current_value}
    ${SQL_DB_Output}        Unwrap SQL Column Values From List Of Tupples Into List for Migration       ${SQL_DB_Output}
    Should contain          ${SQL_DB_Output}        (VT-) Sperre setzen oder zurücknehmen, es gibt 3 verschiedene Formate --> KOMPLEX

    ### MIG - STEUERNUMMER: 9116020011673
    ${string_Steuernummer_current_value}        Set Variable        '9116020011673'
    ${string_Buchungstext_current_value}        Set Variable        '0053'

    ${SQL_DB_Output}        Return SQL Column Values With Two SQL Where Selectors for Migration         BUCHUNGSTEXT        ${SQL_Table_Name_INTERIMSTEUERKONTO}       STEUERNUMMER      ${string_Steuernummer_current_value}      BUCHUNGSSCHLUESSEL        ${string_Buchungstext_current_value}
    ${SQL_DB_Output}        Unwrap SQL Column Values From List Of Tupples Into List for Migration       ${SQL_DB_Output}
    Should contain          ${SQL_DB_Output}        a) Beginn und Ende der Steuerpflicht; Änderung der Zahlungsweise oder des Status einer Steuerart b) Vermerk einer Abmeldung

    ${string_Steuernummer_current_value}        Set Variable        '9116020011673'
    ${string_Buchungstext_current_value}        Set Variable        '0046'

    ${SQL_DB_Output}        Return SQL Column Values With Two SQL Where Selectors for Migration         BUCHUNGSTEXT        ${SQL_Table_Name_INTERIMSTEUERKONTO}       STEUERNUMMER      ${string_Steuernummer_current_value}      BUCHUNGSSCHLUESSEL        ${string_Buchungstext_current_value}
    ${SQL_DB_Output}        Unwrap SQL Column Values From List Of Tupples Into List for Migration       ${SQL_DB_Output}
    Should contain          ${SQL_DB_Output}        (VT-) Sperre setzen oder zurücknehmen, es gibt 3 verschiedene Formate --> KOMPLEX

    ### MIG - STEUERNUMMER: 9116020011674
    ${string_Steuernummer_current_value}        Set Variable        '9116020011674'
    ${string_Buchungstext_current_value}        Set Variable        '0053'

    ${SQL_DB_Output}        Return SQL Column Values With Two SQL Where Selectors for Migration         BUCHUNGSTEXT        ${SQL_Table_Name_INTERIMSTEUERKONTO}       STEUERNUMMER      ${string_Steuernummer_current_value}      BUCHUNGSSCHLUESSEL        ${string_Buchungstext_current_value}
    ${SQL_DB_Output}        Unwrap SQL Column Values From List Of Tupples Into List for Migration       ${SQL_DB_Output}
    Should contain          ${SQL_DB_Output}        a) Beginn und Ende der Steuerpflicht; Änderung der Zahlungsweise oder des Status einer Steuerart b) Vermerk einer Abmeldung

    ${string_Steuernummer_current_value}        Set Variable        '9116020011674'
    ${string_Buchungstext_current_value}        Set Variable        '0046'

    ${SQL_DB_Output}        Return SQL Column Values With Two SQL Where Selectors for Migration         BUCHUNGSTEXT        ${SQL_Table_Name_INTERIMSTEUERKONTO}       STEUERNUMMER      ${string_Steuernummer_current_value}      BUCHUNGSSCHLUESSEL        ${string_Buchungstext_current_value}
    ${SQL_DB_Output}        Unwrap SQL Column Values From List Of Tupples Into List for Migration       ${SQL_DB_Output}
    Should contain          ${SQL_DB_Output}        (VT-) Sperre setzen oder zurücknehmen, es gibt 3 verschiedene Formate --> KOMPLEX

    ################################################################################
    ### MIG - Step 9 - Validierung der Attributtransformation "Test parameter 7" ###
    ################################################################################

    ${string_Steuernummer_current_value}        Set Variable        '9116020011673'
    ${string_Buchungstext_current_value}        Set Variable        '0046'

    ${SQL_DB_Output}        Return SQL Column Values With Two SQL Where Selectors for Migration         MERKZEICHEN0        ${SQL_Table_Name_INTERIMSTEUERKONTO}       STEUERNUMMER      ${string_Steuernummer_current_value}      BUCHUNGSSCHLUESSEL        ${string_Buchungstext_current_value}
    ${SQL_DB_Output}        Unwrap SQL Column Values From List Of Tupples Into List for Migration       ${SQL_DB_Output}
    Should be equal as integers     ${SQL_DB_Output}[0]     2

    ${SQL_DB_Output}        Return SQL Column Values With Two SQL Where Selectors for Migration         MERKZEICHEN1        ${SQL_Table_Name_INTERIMSTEUERKONTO}       STEUERNUMMER      ${string_Steuernummer_current_value}      BUCHUNGSSCHLUESSEL        ${string_Buchungstext_current_value}
    ${SQL_DB_Output}        Unwrap SQL Column Values From List Of Tupples Into List for Migration       ${SQL_DB_Output}
    Should be equal as integers     ${SQL_DB_Output}[0]     0

    ${SQL_DB_Output}        Return SQL Column Values With Two SQL Where Selectors for Migration         MERKZEICHEN2        ${SQL_Table_Name_INTERIMSTEUERKONTO}       STEUERNUMMER      ${string_Steuernummer_current_value}      BUCHUNGSSCHLUESSEL        ${string_Buchungstext_current_value}
    ${SQL_DB_Output}        Unwrap SQL Column Values From List Of Tupples Into List for Migration       ${SQL_DB_Output}
    Should be equal as integers     ${SQL_DB_Output}[0]     1

    ${SQL_DB_Output}        Return SQL Column Values With Two SQL Where Selectors for Migration         MERKZEICHEN3        ${SQL_Table_Name_INTERIMSTEUERKONTO}       STEUERNUMMER      ${string_Steuernummer_current_value}      BUCHUNGSSCHLUESSEL        ${string_Buchungstext_current_value}
    ${SQL_DB_Output}        Unwrap SQL Column Values From List Of Tupples Into List for Migration       ${SQL_DB_Output}
    Should be equal as integers     ${SQL_DB_Output}[0]     0

    ${SQL_DB_Output}        Return SQL Column Values With Two SQL Where Selectors for Migration         MERKZEICHEN4        ${SQL_Table_Name_INTERIMSTEUERKONTO}       STEUERNUMMER      ${string_Steuernummer_current_value}      BUCHUNGSSCHLUESSEL        ${string_Buchungstext_current_value}
    ${SQL_DB_Output}        Unwrap SQL Column Values From List Of Tupples Into List for Migration       ${SQL_DB_Output}
    Should be equal as integers     ${SQL_DB_Output}[0]     0

    ${SQL_DB_Output}        Return SQL Column Values With Two SQL Where Selectors for Migration         MERKZEICHEN5        ${SQL_Table_Name_INTERIMSTEUERKONTO}       STEUERNUMMER      ${string_Steuernummer_current_value}      BUCHUNGSSCHLUESSEL        ${string_Buchungstext_current_value}
    ${SQL_DB_Output}        Unwrap SQL Column Values From List Of Tupples Into List for Migration       ${SQL_DB_Output}
    Should be equal as integers     ${SQL_DB_Output}[0]     0

    ${SQL_DB_Output}        Return SQL Column Values With Two SQL Where Selectors for Migration         MERKZEICHEN6        ${SQL_Table_Name_INTERIMSTEUERKONTO}       STEUERNUMMER      ${string_Steuernummer_current_value}      BUCHUNGSSCHLUESSEL        ${string_Buchungstext_current_value}
    ${SQL_DB_Output}        Unwrap SQL Column Values From List Of Tupples Into List for Migration       ${SQL_DB_Output}
    Should be equal as integers     ${SQL_DB_Output}[0]     0

    ${SQL_DB_Output}        Return SQL Column Values With Two SQL Where Selectors for Migration         MERKZEICHEN7        ${SQL_Table_Name_INTERIMSTEUERKONTO}       STEUERNUMMER      ${string_Steuernummer_current_value}      BUCHUNGSSCHLUESSEL        ${string_Buchungstext_current_value}
    ${SQL_DB_Output}        Unwrap SQL Column Values From List Of Tupples Into List for Migration       ${SQL_DB_Output}
    Should be equal as integers     ${SQL_DB_Output}[0]     0

    ${SQL_DB_Output}        Return SQL Column Values With Two SQL Where Selectors for Migration         MERKZEICHEN8        ${SQL_Table_Name_INTERIMSTEUERKONTO}       STEUERNUMMER      ${string_Steuernummer_current_value}      BUCHUNGSSCHLUESSEL        ${string_Buchungstext_current_value}
    ${SQL_DB_Output}        Unwrap SQL Column Values From List Of Tupples Into List for Migration       ${SQL_DB_Output}
    Should be equal as integers     ${SQL_DB_Output}[0]     0

    ${SQL_DB_Output}        Return SQL Column Values With Two SQL Where Selectors for Migration         MERKZEICHEN9        ${SQL_Table_Name_INTERIMSTEUERKONTO}       STEUERNUMMER      ${string_Steuernummer_current_value}      BUCHUNGSSCHLUESSEL        ${string_Buchungstext_current_value}
    ${SQL_DB_Output}        Unwrap SQL Column Values From List Of Tupples Into List for Migration       ${SQL_DB_Output}
    Should be equal as integers     ${SQL_DB_Output}[0]     0

    ${SQL_DB_Output}        Return SQL Column Values With Two SQL Where Selectors for Migration         MERKZEICHEN10        ${SQL_Table_Name_INTERIMSTEUERKONTO}       STEUERNUMMER      ${string_Steuernummer_current_value}      BUCHUNGSSCHLUESSEL        ${string_Buchungstext_current_value}
    ${SQL_DB_Output}        Unwrap SQL Column Values From List Of Tupples Into List for Migration       ${SQL_DB_Output}
    Should be equal as integers     ${SQL_DB_Output}[0]     0

    #################################################################################
    ### MIG - Step 10 - Validierung der Attributtransformation "Test parameter 8" ###
    #################################################################################

    ### MIG - 10.1
    ${string_Steuernummer_current_value}        Set Variable        '9116020011670'
    ${string_Buchungstext_current_value}        Set Variable        '0046'

    ${SQL_DB_Output}        Return SQL Column Values With Two SQL Where Selectors for Migration         FAELLIGKEIT        ${SQL_Table_Name_INTERIMSTEUERKONTO}       STEUERNUMMER      ${string_Steuernummer_current_value}      BUCHUNGSSCHLUESSEL        ${string_Buchungstext_current_value}
    ${SQL_DB_Output}        Unwrap SQL Column Values From List Of Tupples Into List for Migration       ${SQL_DB_Output}
    Should be equal as integers     ${SQL_DB_Output}[0]     20140101

    ### MIG - 10.2
    ${string_Steuernummer_current_value}        Set Variable        '9116020011671'
    ${string_Buchungstext_current_value}        Set Variable        '0046'

    ${SQL_DB_Output}        Return SQL Column Values With Two SQL Where Selectors for Migration         FAELLIGKEIT        ${SQL_Table_Name_INTERIMSTEUERKONTO}       STEUERNUMMER      ${string_Steuernummer_current_value}      BUCHUNGSSCHLUESSEL        ${string_Buchungstext_current_value}
    ${SQL_DB_Output}        Unwrap SQL Column Values From List Of Tupples Into List for Migration       ${SQL_DB_Output}
    Should contain          ${SQL_DB_Output}[0]     ${None}

    #################################################################################
    ### MIG - Step 11 - Validierung der Attributtransformation "Test parameter 9" ###
    #################################################################################

    ${SQL_DB_Output}        Return SQL Column Values With SQL Where Selector for Migration      BETRAG      ${SQL_Table_Name_INTERIMSTEUERKONTO}       BUCHUNGSSCHLUESSEL        '0046'
    ${SQL_DB_Output}        Unwrap SQL Column Values From List Of Tupples Into List for Migration       ${SQL_DB_Output}
    Should contain          ${SQL_DB_Output}        ${None}

    ##################################################################################
    ### MIG - Step 12 - Validierung der Attributtransformation "Test parameter 10" ###
    ##################################################################################

    ${string_Steuernummer_current_value}        Set Variable        '9116020011670'
    ${string_Buchungstext_current_value}        Set Variable        '0046'

    ${SQL_DB_Output}        Return SQL Column Values With Two SQL Where Selectors for Migration         D_TIMESTAMP        ${SQL_Table_Name_INTERIMSTEUERKONTO}       STEUERNUMMER      ${string_Steuernummer_current_value}      BUCHUNGSSCHLUESSEL        ${string_Buchungstext_current_value}
    ${SQL_DB_Output}        Unwrap SQL Column Values From List Of Tupples Into List for Migration       ${SQL_DB_Output}
    Should be equal as integers     ${SQL_DB_Output}[0]        20210624103232556314

    ######################################################
    ### MIG - Step 13 - Validierung Transform Ergebnis ###
    ######################################################

    ### MIG - Step 13.1
    ${string_Steuernummer_current_value}        Set Variable        '9116020011670'
    ${string_Buchungstext_current_value}        Set Variable        '0046'

    ${SQL_DB_Output}        Return SQL Column Values With Two SQL Where Selectors for Migration         MIGRATIONSKZ        ${SQL_Table_Name_INTERIMSTEUERKONTO}       STEUERNUMMER      ${string_Steuernummer_current_value}      BUCHUNGSSCHLUESSEL        ${string_Buchungstext_current_value}
    ${SQL_DB_Output}        Unwrap SQL Column Values From List Of Tupples Into List for Migration       ${SQL_DB_Output}
    Should be equal as integers     ${SQL_DB_Output}[0]        0

    ### MIG - Step 13.2
    ${string_Steuernummer_current_value}        Set Variable        '9116020011671'
    ${string_Buchungstext_current_value}        Set Variable        '0046'

    ${SQL_DB_Output}        Return SQL Column Values With Two SQL Where Selectors for Migration         MIGRATIONSKZ        ${SQL_Table_Name_INTERIMSTEUERKONTO}       STEUERNUMMER      ${string_Steuernummer_current_value}      BUCHUNGSSCHLUESSEL        ${string_Buchungstext_current_value}
    ${SQL_DB_Output}        Unwrap SQL Column Values From List Of Tupples Into List for Migration       ${SQL_DB_Output}
    Should be equal as integers     ${SQL_DB_Output}[0]        0

    ### MIG - Step 13.3
    ${string_Steuernummer_current_value}        Set Variable        '9116020011672'
    ${string_Buchungstext_current_value}        Set Variable        '0046'

    ${SQL_DB_Output}        Return SQL Column Values With Two SQL Where Selectors for Migration         MIGRATIONSKZ        ${SQL_Table_Name_INTERIMSTEUERKONTO}       STEUERNUMMER      ${string_Steuernummer_current_value}      BUCHUNGSSCHLUESSEL        ${string_Buchungstext_current_value}
    ${SQL_DB_Output}        Unwrap SQL Column Values From List Of Tupples Into List for Migration       ${SQL_DB_Output}
    Should be equal as integers     ${SQL_DB_Output}[0]        0

    ### MIG - Step 13.4
    ${string_Steuernummer_current_value}        Set Variable        '9116020011673'
    ${string_Buchungstext_current_value}        Set Variable        '0046'

    ${SQL_DB_Output}        Return SQL Column Values With Two SQL Where Selectors for Migration         MIGRATIONSKZ        ${SQL_Table_Name_INTERIMSTEUERKONTO}       STEUERNUMMER      ${string_Steuernummer_current_value}      BUCHUNGSSCHLUESSEL        ${string_Buchungstext_current_value}
    ${SQL_DB_Output}        Unwrap SQL Column Values From List Of Tupples Into List for Migration       ${SQL_DB_Output}
    Should be equal as integers     ${SQL_DB_Output}[0]        0

    ### MIG - Step 13.5
    ${string_Steuernummer_current_value}        Set Variable        '9116020011674'
    ${string_Buchungstext_current_value}        Set Variable        '0046'

    ${SQL_DB_Output}        Return SQL Column Values With Two SQL Where Selectors for Migration         MIGRATIONSKZ        ${SQL_Table_Name_INTERIMSTEUERKONTO}       STEUERNUMMER      ${string_Steuernummer_current_value}      BUCHUNGSSCHLUESSEL        ${string_Buchungstext_current_value}
    ${SQL_DB_Output}        Unwrap SQL Column Values From List Of Tupples Into List for Migration       ${SQL_DB_Output}
    Should be equal as integers     ${SQL_DB_Output}[0]        0

    ################################
    ### MIG - Post-configuration ###
    ################################

    ### MIG - Clean up TRANSFORM, TRANSFORMERGEBNIS and INTERIMSTEUERKONTO Tables in INT_PROJECT_MIG Database for Transform
    Execute DB      DELETE FROM ${SQL_Table_Name_TRANSFORM}
    Execute DB      DELETE FROM ${SQL_Table_Name_TRANSFORMERGEBNIS}
    Execute DB      DELETE FROM ${SQL_Table_Name_INTERIMSTEUERKONTO}

    ### MIG - Run Global SQL Clean-Up Batch
    Global SQL CleanUp for Migration

    ### MIG - Clean up old folders for Transform
    Delete Old Folders From Server For Migration TEST INT01
    Delete Old Folders From Jenkins For Migration TEST INT01