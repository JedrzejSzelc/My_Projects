###################################################################################################
### Title:          XML-Auto-Randomiser                                                         ###
### Version:        20230203                                                                    ###
### Creator:        jedrzej.szelc@capgemini.com                                                 ###
### Maintainer:     jedrzej.szelc@capgemini.com                                                 ###
### Comments:       See the command lines at the bottom of this file.                           ###
###                 Important modules used in this Script:                                      ###
###                 1) Minimal DOM - https://docs.python.org/3/library/xml.dom.minidom.html     ###
###                 2) Faker Package - https://faker.readthedocs.io/en/master/                  ###
###################################################################################################

######################
### Python Modules ###
######################

from xml.dom import minidom
from faker import Faker
import string
import random
import os

#########################
### General Functions ###
#########################

### Processing functions
def Function_Import_Ref_XML_File(string_Dir_Name, string_Input_XML_File_Name):
    string_XML_Reference_Input = os.path.join(string_Dir_Name, string_Input_XML_File_Name)
    return minidom.parse(string_XML_Reference_Input)

def Function_Item_Modification(item_Selector_String, item_Selector_Value, item_Attribute_String, item_Attribute_new_Value, xml_Document_current):
    item_Selector_List = xml_Document_current.getElementsByTagName(item_Selector_String)
    try:
        item_Selector_List[item_Selector_Value].attributes[item_Attribute_String].value = item_Attribute_new_Value
        print(item_Selector_String, "-->", item_Attribute_String)
    except:
        print(item_Selector_String,"-->", item_Attribute_String, " - IS MISSING FROM THE FILE!")

def Function_Save_New_XML_File(string_new_Test_Datei, xml_Document_current):
    with open(string_new_Test_Datei, "w", encoding="utf-8") as xml_file:
        xml_Document_current.writexml(xml_file)

def Function_XML_Attribute_Modify(xml_Document_current, integer_XML_Root_Selection_Value, string_XML_Element_Name, string_XML_Attribute_Name, string_XML_Attribute_new_Value):
    integer_XML_Element_Selection_Value = xml_Document_current.getElementsByTagName(string_XML_Element_Name)
    try:
        integer_XML_Element_Selection_Value[integer_XML_Root_Selection_Value].attributes[string_XML_Attribute_Name].value = string_XML_Attribute_new_Value
        print("[", integer_XML_Root_Selection_Value, "-->", string_XML_Element_Name, "-->", string_XML_Attribute_Name, "] has been randomised.")
    except:
        print("[", integer_XML_Root_Selection_Value, "-->", string_XML_Element_Name, "-->", string_XML_Attribute_Name, "] IS MISSING FROM THE REFERENCE .XML FILE!")

def Function_XML_Randomise_Multiple_Attributes(xml_Current_XML_Document, list_Randomisation_LookUp_Table):
    for integer_Element_Counter in range(len(list_Randomisation_LookUp_Table[:])):
        # Attributes loop
        integer_Number_Of_All_Attributes_To_Be_Randomised_For_Current_Element = Function_Count_XML_Elements_To_Be_Randomised(xml_Current_XML_Document, list_Randomisation_LookUp_Table[integer_Element_Counter][0])
        if integer_Number_Of_All_Attributes_To_Be_Randomised_For_Current_Element > 0:
            for integer_Attribute_Counter in range(integer_Number_Of_All_Attributes_To_Be_Randomised_For_Current_Element):
                string_Element_Name = list_Randomisation_LookUp_Table[integer_Element_Counter][0]
                string_Attribute_Name = list_Randomisation_LookUp_Table[integer_Element_Counter][1]
                string_Randomisation_Type = list_Randomisation_LookUp_Table[integer_Element_Counter][2]
                Function_XML_Randomise_Single_Attribute(xml_Current_XML_Document, integer_Attribute_Counter, string_Element_Name, string_Attribute_Name, string_Randomisation_Type)
        else:
            string_Element_Name = list_Randomisation_LookUp_Table[integer_Element_Counter][0]
            print("[ Element:", string_Element_Name, "] IS MISSING FROM THE REFERENCE .XML FILE!")

def Function_XML_Randomise_Single_Attribute(xml_Document_current, integer_XML_Root_Selection_Value, string_XML_Element_Name, string_XML_Attribute_Name, string_XML_Randomise_Function_Name):

    # Select the randomising function
    if ("fake_user_id" == string_XML_Randomise_Function_Name):
        string_XML_Attribute_new_Value = Function_String_User_ID_Generator()
    elif ("fake_country" == string_XML_Randomise_Function_Name):
        string_XML_Attribute_new_Value = Function_String_Country_Generator()
    elif ("fake_name" == string_XML_Randomise_Function_Name):
        string_XML_Attribute_new_Value = Function_String_First_Name_Generator()
    elif ("fake_surname" == string_XML_Randomise_Function_Name):
        string_XML_Attribute_new_Value = Function_String_Surname_Generator()
    elif ("fake_age" == string_XML_Randomise_Function_Name):
        string_XML_Attribute_new_Value = Function_Integer_Age_Generator()
    elif ("fake_email" == string_XML_Randomise_Function_Name):
        string_XML_Attribute_new_Value = Function_String_EMAIL_Address_Generator()
    elif ("fake_iban" == string_XML_Randomise_Function_Name):
        string_XML_Attribute_new_Value = Function_String_IBAN_Sequence_Generator()
    elif ("fake_company" == string_XML_Randomise_Function_Name):
        string_XML_Attribute_new_Value = Function_String_Company_Name_Generator()
    elif ("fake_colour" == string_XML_Randomise_Function_Name):
        string_XML_Attribute_new_Value = Function_String_Colour_Generator()
    elif ("fake_digits" == string_XML_Randomise_Function_Name):
        string_XML_Attribute_new_Value = Function_Integer_Digits_Generator()
    elif ("fake_www" == string_XML_Randomise_Function_Name):
        string_XML_Attribute_new_Value = Function_String_WWW_Address_Generator()
    elif ("fake_bool_TF" == string_XML_Randomise_Function_Name):
        string_XML_Attribute_new_Value = Function_String_Boolean_True_False_Generator()
    else:
        string_XML_Attribute_new_Value = Function_String_Overwrite_Token()

    # Randomise the given XML Attribute
    Function_XML_Attribute_Modify(xml_Document_current, integer_XML_Root_Selection_Value, string_XML_Element_Name, string_XML_Attribute_Name, string_XML_Attribute_new_Value)

def Function_Count_XML_Elements_To_Be_Randomised(xml_Document_current, string_XML_Element_Name):
    # print("There are [", len(xml_Document_current.getElementsByTagName(string_XML_Element_Name)), "x", string_XML_Element_Name, "] elements in the reference XML file.")
    return len(xml_Document_current.getElementsByTagName(string_XML_Element_Name))

def Function_Dir_Setup(string_Dir_Name):
    os.makedirs(string_Dir_Name, exist_ok=True)

def Function_Save_Randomised_XML_File(xml_Current_XML_Document, string_Dir_Name, string_original_Test_Datei):
    string_Randomised_XML_Test_File = str("Randomised-" + string_original_Test_Datei + ".xml")
    string_Randomised_XML_Test_File = os.path.join(string_Dir_Name, string_Randomised_XML_Test_File)
    Function_Save_New_XML_File(string_Randomised_XML_Test_File, xml_Current_XML_Document)

### Randomisation functions
def Function_String_User_ID_Generator():
    return str(''.join(random.choice(string.ascii_uppercase) for _ in range(2))) + str(faker_instance.random_number(digits=3, fix_len=True))

def Function_String_Country_Generator():
    return faker_instance.country()

def Function_String_First_Name_Generator():
    return faker_instance.first_name()

def Function_String_Surname_Generator():
    return faker_instance.last_name()

def Function_Integer_Age_Generator():
    return str(faker_instance.random_int(18, 95))

def Function_String_EMAIL_Address_Generator():
    return faker_instance.ascii_company_email()

def Function_String_IBAN_Sequence_Generator():
    return faker_instance.iban()

def Function_String_Company_Name_Generator():
    return faker_instance.company()

def Function_String_Colour_Generator():
    return faker_instance.color_name()

def Function_Integer_Digits_Generator():
    return str(faker_instance.random_int(1400, 2900))

def Function_String_WWW_Address_Generator():
    return faker_instance.url()

def Function_String_Boolean_True_False_Generator():
    return str(faker_instance.boolean())

def Function_String_Overwrite_Token():
    return str("XXXXXXXXXX")

######################################
### The proper program starts here ###
######################################

### Start Faker
faker_instance = Faker()

### Command and execution code - File and directories names
string_Reference_Input_XML_Test_File = "Ref-XML-Datei-To-Be-Randomised.xml"
string_Reference_Dir_Name = "Reference XML File"
string_Randomised_Dir_Name = "Randomised XML File"

### Dir and xml configuration - Do NOT change this part of code!
Function_Dir_Setup(string_Reference_Dir_Name)
Function_Dir_Setup(string_Randomised_Dir_Name)

### Parse reference .xml - Do NOT change this part of code!
xml_Current_XML_Document = Function_Import_Ref_XML_File(string_Reference_Dir_Name, string_Reference_Input_XML_Test_File)

### Command and execution code - Randomise data in .xml. Build the randomisation for a given .xml file here with the "Function_XML_Attribute_Randomise" function!
# Randomisation LookUp Table
list_Randomisation_LookUp_Table = [
    # [Element, Attribute, Randomisation_Type]

    # Single Record
    ["Single_Record", "User_Id", "fake_user_id"],
    ["Single_Record", "User_Country", "fake_country"],

    # User Info
    ["User_Info", "User_Name", "fake_name"],
    ["User_Info", "User_Surname", "fake_surname"],
    ["User_Info", "User_Age", "fake_age"],
    ["User_Info", "User_Email", "fake_email"],
    ["User_Info", "User_IBAN", "fake_iban"],

    # Car Info
    ["Car_Info", "Car_Manufacturer", "fake_company"],
    ["Car_Info", "Car_Colour", "fake_colour"],
    ["Car_Info", "Car_Engine_Capacity", "fake_digits"],
    ["Car_Info", "Car_Manufacturer_Webpage", "fake_www"],
    ["Car_Info", "Car_Rented", "fake_bool_TF"],

    # Safety Feature Demo
    ["Car_Info", "Car_Engine_Capacity", "incorrect_randomisation_token"],
    ["Car_Info", "Car_Safety_Rating", "fake_company"],
    ["Car_Specs", "Car_Engine_Capacity", "fake_company"],
]

# Randomise multiple elements using the look-up table above
Function_XML_Randomise_Multiple_Attributes(xml_Current_XML_Document, list_Randomisation_LookUp_Table)

### Save randomised XML File - Do NOT change this part of code!
Function_Save_Randomised_XML_File(xml_Current_XML_Document, string_Randomised_Dir_Name, string_Reference_Input_XML_Test_File)