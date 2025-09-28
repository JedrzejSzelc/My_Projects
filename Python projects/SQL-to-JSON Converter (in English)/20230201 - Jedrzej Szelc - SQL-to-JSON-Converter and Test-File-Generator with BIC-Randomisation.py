###############################################################################################
### Title:          SQL-to-JSON-Converter and Test-File-Generator with BIC-Randomisation    ###
### Version:        20230201                                                                ###
### Creator:        jedrzej.szelc@capgemini.com                                             ###
### Maintainer:     jedrzej.szelc@capgemini.com                                             ###
### Comments:       Requires "cx-Oracle" package in PyCharm.                                ###
###                 See https://cx-oracle.readthedocs.io/en/latest/index.html               ###
###                 and https://pypi.org/project/cx-Oracle/ for further info.               ###
###                 This version randomizes BIC numbers if no BIC numbers are given.        ###
###############################################################################################

##################################################################
### Python Modules - DO NOT MODIFY US UNLESS REALLY NECESSARY! ###
##################################################################

import cx_Oracle
import json
import os
import random
import string
import shutil
from datetime import datetime

##########################################################################
### Variables and Settings - DO NOT MODIFY US UNLESS REALLY NECESSARY! ###
##########################################################################

### Global variables
string_SQL_user = "INT_ALIEN_MIG"
string_SQL_password = "PW_INT_ALIEN_MIG"
strings_SQL_dsn = "10.44.100.187:1521/kaal"

### Connect to SQL Server
SQL_connection = cx_Oracle.connect(user=string_SQL_user, password=string_SQL_password, dsn=strings_SQL_dsn)
SQL_cursor = SQL_connection.cursor()

#####################################################################
### General Functions - DO NOT MODIFY US UNLESS REALLY NECESSARY! ###
#####################################################################

### File Configuration Functions
def Remove_Dir(string_Dir_Name):
   shutil.rmtree(string_Dir_Name)

def Function_Dir_Setup(string_Dir_Name):
   os.makedirs(string_Dir_Name, exist_ok=True)

### SQL Functions
def Function_Select_All_Columns_and_Specific_Number_of_Rows_From_SQL_Table(string_SQL_Table_Name, integer_Number_of_Rows_to_be_extracted):
    string_SQL_Statement = "select * from " + string_SQL_Table_Name + " where rownum <= " + str(integer_Number_of_Rows_to_be_extracted)
    SQL_cursor.execute(string_SQL_Statement)
    list_All_Columns_and_All_Rows = SQL_cursor.fetchall()
    return list_All_Columns_and_All_Rows

def Function_Select_All_Columns_and_All_Rows_From_SQL_Table(string_SQL_Table_Name):
    string_SQL_Statement = "select * from " + string_SQL_Table_Name
    SQL_cursor.execute(string_SQL_Statement)
    list_All_Columns_and_All_Rows = SQL_cursor.fetchall()
    return list_All_Columns_and_All_Rows

def Function_Count_All_Rows_From_SQL_Table(string_SQL_Table_Name):
    string_SQL_Statement = "select count(*) from " + string_SQL_Table_Name
    SQL_cursor.execute(string_SQL_Statement)
    integer_Number_Of_Rows = SQL_cursor.fetchone()
    integer_Number_Of_Rows = integer_Number_Of_Rows[0]
    return integer_Number_Of_Rows

def Function_Randomise_Auxiliary_Dataset_And_Return_Single_Value(list_Randomisation_LookUp_Table):
    return random.choice(list_Randomisation_LookUp_Table)

def Function_Check_And_Replace_SQL_None_Attribute_With_None_String(string_SQL_Attribute):
    if string_SQL_Attribute is None:
        string_SQL_Attribute = "None"
    return string_SQL_Attribute

def Function_Save_JSON_File_For_Given_Data_Name(integer_SQL_Row_Counter_Current, string_Output_JSON_Dir_Current, string_Data_Name, dictionary_JSON_Schema_Current):
    datetime_container = datetime.now()
    string_Date_and_Time = datetime_container.strftime("%Y%m%d_%H%M%S")
    string_JSON_Output_File_Name_Current = string_Date_and_Time + "_JSON_Output_File_" + string_Data_Name + "_" + str(integer_SQL_Row_Counter_Current) + ".json"
    string_JSON_Output_Files_and_Dir_Current = os.path.join(string_Output_JSON_Dir_Current, string_JSON_Output_File_Name_Current)
    with open(string_JSON_Output_Files_and_Dir_Current, 'w') as outfile:
      json.dump(dictionary_JSON_Schema_Current, outfile, ensure_ascii=False, indent=integer_JSON_Indent_Value)

def Function_String_BIC_Sequence_Generator():
    temp_string = str(''.join(random.choice(string.ascii_uppercase) for _ in range(4)) + ''.join(random.choice(string.ascii_uppercase) for _ in range(2)) + ''.join(random.choice(string.ascii_uppercase) for _ in range(2)) + str(random.randint(100,999)))
    return temp_string

#############################
### Program configuration ###
#############################

### Configuration and settings - you may modify us.
string_SQL_Table_Name_GINSTER_STRADR = "GINSTER_STRADR"
string_SQL_Table_Name_GINSTER_BANKKONTO = "GINSTER_BANKKONTO"
string_JSON_Output_Dir = "Output JSON Files"
integer_JSON_Indent_Value = 2
integer_Number_GINSTER_STRADR_JSON_Files_to_be_generated = 1
integer_Number_GINSTER_BANKDATEN_JSON_Files_to_be_generated = 1

# list_Bundesland_Values = ["THUERINGEN",
#                           "NORDRHEIN_WESTFALEN",
#                           "BADEN_WUERTTEMBERG",
#                           "BAYERN",
#                           "NORDRHEIN_WESTFALEN",
#                           "BADEN_WUERTTEMBERG",
#                           "BERLIN"]

### Extract Data from SQL Tables - you may modify us.
list_SQL_Table_GINSTER_STRADR = Function_Select_All_Columns_and_Specific_Number_of_Rows_From_SQL_Table(string_SQL_Table_Name_GINSTER_STRADR, integer_Number_GINSTER_STRADR_JSON_Files_to_be_generated)
list_SQL_Table_GINSTER_BANKKONTO = Function_Select_All_Columns_and_Specific_Number_of_Rows_From_SQL_Table(string_SQL_Table_Name_GINSTER_BANKKONTO, integer_Number_GINSTER_BANKDATEN_JSON_Files_to_be_generated)

### Set up dirs - DO NOT MODIFY US UNLESS REALLY NECESSARY!
Function_Dir_Setup(string_JSON_Output_Dir)
Remove_Dir(string_JSON_Output_Dir)
Function_Dir_Setup(string_JSON_Output_Dir)

################################################
### File Loop for ANSCHRIFTDATEN starts here ###
################################################

### For loop starts here - Generate multiple JSON files
for integer_SQL_Row_Counter in range(integer_Number_GINSTER_STRADR_JSON_Files_to_be_generated):

    ### JSON input fields from SQL - you may modify us.
    string_SQL_Attribute_Hausnummer_from_STRADR = Function_Check_And_Replace_SQL_None_Attribute_With_None_String(list_SQL_Table_GINSTER_STRADR[integer_SQL_Row_Counter][2])
    string_SQL_Attribute_Staat_from_STRADR = Function_Check_And_Replace_SQL_None_Attribute_With_None_String(list_SQL_Table_GINSTER_STRADR[integer_SQL_Row_Counter][4])
    string_SQL_Attribute_Plz_from_STRADR = Function_Check_And_Replace_SQL_None_Attribute_With_None_String(list_SQL_Table_GINSTER_STRADR[integer_SQL_Row_Counter][6])
    string_SQL_Attribute_Ort_from_STRADR = Function_Check_And_Replace_SQL_None_Attribute_With_None_String(list_SQL_Table_GINSTER_STRADR[integer_SQL_Row_Counter][4])
    string_SQL_Attribute_Strasse_from_STRADR = Function_Check_And_Replace_SQL_None_Attribute_With_None_String(list_SQL_Table_GINSTER_STRADR[integer_SQL_Row_Counter][7])

    ### JSON file schema - you may modify us.
    dictionary_JSON_Schema_for_adresseValidierenKorrektMunchen = {
          "httpRequest": {
            "body": {
              "type": "REGEX",
              "regex": ".*<adresse><Staat>" + string_SQL_Attribute_Staat_from_STRADR + "</Staat><Plz>" + string_SQL_Attribute_Plz_from_STRADR + "</Plz><Ort>" + string_SQL_Attribute_Ort_from_STRADR + "</Ort><Strasse>" + string_SQL_Attribute_Strasse_from_STRADR + "</Strasse><Hausnummer>" + string_SQL_Attribute_Hausnummer_from_STRADR + "</Hausnummer><ErweiterteValidierung>false</ErweiterteValidierung></adresse>.*"
            }
          },
          "httpResponse": {
            "statusCode": 200,
            "headers": {
              "content-type": [
                "text/xml; charset=utf-8"
              ]
            },
            "body": "<soap:Envelope xmlns:soap=\"http://schemas.xmlsoap.org/soap/envelope/\"><soap:Header/><soap:Body><ns3:adresseValidierenResponse xmlns:ns2=\"http://www.zivit.de/stplf/faults/v1.0\" xmlns:ns3=\"http://www.zivit.de/stplf/bd/adressvalidierung/v1.0\"><ValidierteAdresse><ErgebnisCode>1</ErgebnisCode><ErgebnisText>Adresse korrekt</ErgebnisText><KorrigierteAttribute/><UngueltigeAttribute/><AttributKombinationUngueltig>false</AttributKombinationUngueltig><AdressTyp>ZUSTELLADRESSE</AdressTyp><Adresse><Staat>" + string_SQL_Attribute_Staat_from_STRADR + "</Staat><Plz>" + string_SQL_Attribute_Plz_from_STRADR + "</Plz><Ort>" + string_SQL_Attribute_Ort_from_STRADR + "</Ort><Strasse>" + string_SQL_Attribute_Strasse_from_STRADR + "</Strasse><Hausnummer>" + string_SQL_Attribute_Hausnummer_from_STRADR + "</Hausnummer><ErweiterteValidierung>false</ErweiterteValidierung></Adresse></ValidierteAdresse></ns3:adresseValidierenResponse></soap:Body></soap:Envelope>"
          }
        }

    ### Save JSON file for a JSON schema given - you may modify us.
    Function_Save_JSON_File_For_Given_Data_Name(integer_SQL_Row_Counter, string_JSON_Output_Dir, string_SQL_Table_Name_GINSTER_STRADR, dictionary_JSON_Schema_for_adresseValidierenKorrektMunchen)

### For loop for ANSCHRIFTDATEN ends here

###########################################
### File Loops for BANKDATEN start here ###
###########################################

### For loop starts here - Generate multiple JSON files
for integer_SQL_Row_Counter in range(integer_Number_GINSTER_BANKDATEN_JSON_Files_to_be_generated):

    ### JSON input fields from SQL - you may modify us.
    string_SQL_Attribute_BIC_from_Bankkonto = Function_Check_And_Replace_SQL_None_Attribute_With_None_String(list_SQL_Table_GINSTER_BANKKONTO[integer_SQL_Row_Counter][3])
    string_SQL_Attribute_IBAN_from_Bankkonto = Function_Check_And_Replace_SQL_None_Attribute_With_None_String(list_SQL_Table_GINSTER_BANKKONTO[integer_SQL_Row_Counter][4])

    ### If BIC Number is "None", randomise BIC number
    if string_SQL_Attribute_BIC_from_Bankkonto == "None":
        string_SQL_Attribute_BIC_from_Bankkonto = Function_String_BIC_Sequence_Generator()

    ### JSON file schemas - you may modify us.
    dictionary_JSON_Schema_for_bankverbindungInternationalValidieren_DE_korrekt = {
        "httpRequest": {
            "body": {
                "type": "XML",
                "xml": "<SOAP-ENV:Envelope xmlns:SOAP-ENV=\"http://schemas.xmlsoap.org/soap/envelope/\"><SOAP-ENV:Header><wsse:Security xmlns:wsse=\"http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd\"><wsse:UsernameToken><wsse:Username>Anwender</wsse:Username></wsse:UsernameToken></wsse:Security></SOAP-ENV:Header><SOAP-ENV:Body><ns2:bankverbindungInternationalValidieren xmlns:ns2=\"http://www.zivit.de/stplf/bd/bankdatenvalidierung/v1.0\"><ns2:Bic>" + string_SQL_Attribute_BIC_from_Bankkonto + "</ns2:Bic><ns2:Iban>" + string_SQL_Attribute_IBAN_from_Bankkonto + "</ns2:Iban></ns2:bankverbindungInternationalValidieren></SOAP-ENV:Body></SOAP-ENV:Envelope>"
            }
        },
        "httpResponse": {
            "statusCode": 200,
            "headers": {
                "content-type": ["text/xml; charset=utf-8"]
            },
            "body": "<SOAP-ENV:Envelope xmlns:SOAP-ENV=\"http://schemas.xmlsoap.org/soap/envelope/\"><SOAP-ENV:Header/><SOAP-ENV:Body><ns5:bankverbindungInternationalValidierenResponse xmlns:ns3=\"http://www.zivit.de/stplf/bd/adressvalidierung/v1.0\" xmlns:ns4=\"http://www.zivit.de/stplf/faults/v1.0\" xmlns:ns5=\"http://www.zivit.de/stplf/bd/bankdatenvalidierung/v1.0\"><ns5:Ergebnis><ergebniscode>1</ergebniscode><ergebnistext>Bankverbindung gültig</ergebnistext><iban>" + string_SQL_Attribute_IBAN_from_Bankkonto + "</iban></ns5:Ergebnis></ns5:bankverbindungInternationalValidierenResponse></SOAP-ENV:Body></SOAP-ENV:Envelope>"
        }
    }

    dictionary_JSON_Schema_for_bankverbindungIbanOnlyResponse_false_DEKorrekt = {
        "httpRequest": {
            "body": {
                "type": "XML",
                "xml": "<SOAP-ENV:Envelope xmlns:SOAP-ENV=\"http://schemas.xmlsoap.org/soap/envelope/\"><SOAP-ENV:Header><wsse:Security xmlns:wsse=\"http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd\"><wsse:UsernameToken><wsse:Username>Anwender</wsse:Username></wsse:UsernameToken></wsse:Security></SOAP-ENV:Header><SOAP-ENV:Body><ns2:bankverbindungIbanOnly xmlns:ns2=\"http://www.zivit.de/stplf/bd/bankdatenvalidierung/v1.0\"><ns2:Iban>" + string_SQL_Attribute_IBAN_from_Bankkonto + "</ns2:Iban></ns2:bankverbindungIbanOnly></SOAP-ENV:Body></SOAP-ENV:Envelope>"
            }
        },
        "httpResponse": {
            "statusCode": 200,
            "headers": {
                "content-type": ["text/xml; charset=utf-8"]
            },
            "body": "<SOAP-ENV:Envelope xmlns:SOAP-ENV=\"http://schemas.xmlsoap.org/soap/envelope/\"><SOAP-ENV:Header/><SOAP-ENV:Body><ns5:bankverbindungIbanOnlyResponse xmlns:ns3=\"http://www.zivit.de/stplf/faults/v1.0\" xmlns:ns4=\"http://www.zivit.de/stplf/bd/adressvalidierung/v1.0\" xmlns:ns5=\"http://www.zivit.de/stplf/bd/bankdatenvalidierung/v1.0\"><IbanOnly>false</IbanOnly></ns5:bankverbindungIbanOnlyResponse></SOAP-ENV:Body></SOAP-ENV:Envelope>"
        }
    }

    dictionary_JSON_Schema_for_banknameInternationalErmitteln_DE = {
        "httpRequest": {
            "body": {
                "type": "XML",
                "xml": "<SOAP-ENV:Envelope xmlns:SOAP-ENV=\"http://schemas.xmlsoap.org/soap/envelope/\"><SOAP-ENV:Header><wsse:Security xmlns:wsse=\"http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd\"><wsse:UsernameToken><wsse:Username>Anwender</wsse:Username></wsse:UsernameToken></wsse:Security></SOAP-ENV:Header><SOAP-ENV:Body><ns2:banknameInternationalErmitteln xmlns:ns2=\"http://www.zivit.de/stplf/bd/bankdatenvalidierung/v1.0\" xmlns=\"\"><ns2:Bic>" + string_SQL_Attribute_BIC_from_Bankkonto + "</ns2:Bic><ns2:Iban>" + string_SQL_Attribute_IBAN_from_Bankkonto + "</ns2:Iban></ns2:banknameInternationalErmitteln></SOAP-ENV:Body></SOAP-ENV:Envelope>"
            }
        },
        "httpResponse": {
            "statusCode": 200,
            "headers": {
                "content-type": ["text/xml; charset=utf-8"]
            },
            "body": "<SOAP-ENV:Envelope xmlns:SOAP-ENV=\"http://schemas.xmlsoap.org/soap/envelope/\"><SOAP-ENV:Header/><SOAP-ENV:Body><ns2:banknameInternationalErmittelnResponse xmlns:ns2=\"http://www.zivit.de/stplf/bd/bankdatenvalidierung/v1.0\" xmlns:ns3=\"http://www.zivit.de/stplf/faults/v1.0\"><Bankname>Deutschebank</Bankname></ns2:banknameInternationalErmittelnResponse></SOAP-ENV:Body></SOAP-ENV:Envelope>"
        }
    }

    ### Save JSON file for JSON schemas given - you may modify us.
    Function_Save_JSON_File_For_Given_Data_Name(integer_SQL_Row_Counter, string_JSON_Output_Dir, string_SQL_Table_Name_GINSTER_BANKKONTO + "_International_Validieren", dictionary_JSON_Schema_for_bankverbindungInternationalValidieren_DE_korrekt)
    Function_Save_JSON_File_For_Given_Data_Name(integer_SQL_Row_Counter, string_JSON_Output_Dir, string_SQL_Table_Name_GINSTER_BANKKONTO + "_IBAN_Only", dictionary_JSON_Schema_for_bankverbindungIbanOnlyResponse_false_DEKorrekt)
    Function_Save_JSON_File_For_Given_Data_Name(integer_SQL_Row_Counter, string_JSON_Output_Dir, string_SQL_Table_Name_GINSTER_BANKKONTO + "_International_Ermitteln", dictionary_JSON_Schema_for_banknameInternationalErmitteln_DE)

### For loop for BANKDATEN ends here