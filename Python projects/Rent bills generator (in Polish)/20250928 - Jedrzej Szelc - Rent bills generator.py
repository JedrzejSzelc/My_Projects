#########################################################################################################
##### Ćwiczę klasy - Generator maili 'Bona' #####
#########################################################################################################
print("##############################################################################################")
print("##### Ćwiczę klasy - Generator maili 'Bona' #####")
print("##############################################################################################")

### Otium
# Zmienne dla Otium
string_odmieniona_nazwa_ulicy_Otium = "Jankowskiego"
integer_liczba_lokatorow_Otium = 4
float_calkowity_rachunek_za_elektrycznosc_Otium = 153.53
float_calkowity_rachunek_za_internet_Otium = 55
float_calkowity_rachunek_za_gaz_Otium = 21.75

string_okres_rozliczenia_CO_Otium = "2025.01.01-2025.06.30"
float_calkowity_rachunek_CO_Otium = 0

string_okres_rozliczenia_ZW_CW_Otium = "2025.01.01-2025.06.30"
float_calkowity_rachunek_ZW_CW_Otium = -142.85

### Ferina
# Zmienne dla Ferina
string_odmieniona_nazwa_ulicy_Ferina = "Nowackiego"
integer_liczba_lokatorow_Ferina = 4
float_calkowity_rachunek_za_elektrycznosc_Ferina = 120.37
float_calkowity_rachunek_za_internet_Ferina = 105

string_okres_rozliczenia_ZW_CW_Ferina = "2025.01.01-2025.06.30"
float_calkowity_rachunek_zimna_ciepla_woda_Ferina = 254.67

string_okres_rozliczenia_CO_Ferina = "2025.01.01-2025.06.30"
float_calkowity_rachunek_CO_Ferina = 252.98

########################################################################################################################
########################################################################################################################
########################################################################################################################

### Dane wejściowe (zmienne wejściowe) generatora:
# 1. nazwa mieszkania do tytułu oraz treści
# 2. data wysłania maila - miesiąc i rok
# 3. odmiana nazwy miesiąca do treści maila
# 4. wysokość pełnego rachunku za elektryczność
# 5. wysokość pełnego rachunku za internet
# 6. [OPCJA] wysokość pełnego rachunku za gaz
# 7. [OPCJA] rozliczenia nadpłaty lub niedopłaty ZW i CW
# 8. [OPCJA] rozliczenia nadpłaty lub niedopłaty CO
# 9. Właściwa treść maila do modyfikacji

### Dane wyjściowe generatora:
# a. Treść maila z rozliczeniem podzielonych rachunków za media
# b. [OPCJA] Treść maila z rozliczeniem podzielonych rachunków za media oraz rozliczeniem podzielonej niedopłaty/nadpłaty ZW/CW
# c. [OPCJA] Treść maila z rozliczeniem podzielonych rachunków za media oraz rozliczeniem podzielonej niedopłaty/nadpłaty CO

### Struktura kodu generatora, czyli z czego korzystam:
# - Działam na klasach
# - Automatyczna ocena miesiąca - 2 i 3 to zmienne automatyczne
# - klasa bazowa to ogólna klasa dla danego mieszkania:
#   -- przy użyciu "settera" pobiera zmienne wejściowe: 1
#   -- ma "getter" dla zmiennych: 1
#   -- odpowiada za odmianę miesiąca do treści
# - Otium i Ferina to klasy dziedziczące:
#   -- zmienne wejściowe dla Otium to:
#       --- 4, 5 i 6
#       --- treść wiadomości dla Otium jako osobny parametr wejściowy?
#       --- odpowiada za tytuł dla danej ulicy
#   -- zmienne wejściowe dla Ferina to:
#       --- 4, 5 i 6
#       --- treść wiadomości dla Ferina
#       --- odpowiada za tytuł dla danej ulicy
# - nadpłata lub niedopłata ZW/CW to klasy dziedziczące po Otium i Ferina:
#   -- nadpisanie tekstu tej wiadomości bez nadpłaty/niedopłaty
#   -- flaga "nadpłata/niedopłata"
#   -- pobiera parametr wejściowy: 7
#   -- treść wiadomości dla Otium jako osobny parametr wejściowy?
# - nadpłata lub niedopłata CO to klasy dziedziczące po Otium i Ferina:
#   -- nadpisanie tekstu tej wiadomości bez nadpłaty/niedopłaty
#   -- flaga "nadpłata/niedopłata"
#   -- pobiera parametr wejściowy: 8
#   -- treść wiadomości dla Otium jako osobny parametr wejściowy?
# - korzystam ze zmiennych klasy do przechowywania info - jakich info?
# - obliczenia rachunków wykonuję w metodach statycznych

from datetime import datetime

class klasa_bazowa_mieszkanie():

    slownik_odmienionych_miesiecy_roku = {
        1: "w styczniu",
        2: "w lutym",
        3: "w marcu",
        4: "w kwietniu",
        5: "w maju",
        6: "w czerwcu",
        7: "w lipcu",
        8: "w sierpniu",
        9: "we wrześniu",
        10: "w październiku",
        11: "w listopadzie",
        12: "w grudniu"
    }

    slownik_miesiecy_roku = {
        1: "Styczeń",
        2: "Luty",
        3: "Marzec",
        4: "Kwiecień",
        5: "Maj",
        6: "Czerwiec",
        7: "Lipiec",
        8: "Sierpień",
        9: "Wrzesień",
        10: "Październik",
        11: "Listopad",
        12: "Grudzień"
    }

    @staticmethod
    def metoda_statyczna_numer_aktualnego_miesiaca():
        integer_numer_aktualnego_miesiaca = datetime.now().month
        return integer_numer_aktualnego_miesiaca

    @staticmethod
    def metoda_statyczna_rok_kalendarzowy():
        integer_rok_kalendarzowy = datetime.now().year
        return integer_rok_kalendarzowy

    @staticmethod
    def metoda_statyczna_podzial_rachunku(float_wysokosc_rachunku, integer_liczba_lokatorow):
        float_wysokosc_rachunku = float_wysokosc_rachunku / integer_liczba_lokatorow
        return round(float_wysokosc_rachunku,2)

    def metoda_zwroc_string_nieodmienionego_miesiaca_kalendarzowego(self, integer_numer_aktualnego_miesiaca):
        return self.slownik_miesiecy_roku[integer_numer_aktualnego_miesiaca]

    def metoda_zwroc_string_odmienionego_miesiaca_kalendarzowego(self, integer_numer_aktualnego_miesiaca):
        return self.slownik_odmienionych_miesiecy_roku[integer_numer_aktualnego_miesiaca]

### 20230915 - Otium - Podstawowy scenariusz
class klasa_dziedziczaca_Otium(klasa_bazowa_mieszkanie):

    def __init__(self, string_odmieniona_nazwa_ulicy):
        self.string_odmieniona_nazwa_ulicy = string_odmieniona_nazwa_ulicy

    def metoda_tytul_maila(self, string_aktualny_niedomieniony_miesiac, integer_aktualny_rok_kalendarzowy):
        string_tytul_maila = "Opłaty za media na ul. {string_nazwa_ulicy} - {string_miesiac} {integer_rok}".format(
            string_nazwa_ulicy=self.string_odmieniona_nazwa_ulicy, string_miesiac=string_aktualny_niedomieniony_miesiac,
            integer_rok=integer_aktualny_rok_kalendarzowy)
        return string_tytul_maila

    def metoda_tresc_wiadomosci_maila(self, string_aktualny_miesiac, integer_aktualny_rok_kalendarzowy,
                                      float_calkowity_rachunek_za_elektrycznosc,
                                      float_calkowity_rachunek_za_internet,
                                      float_calkowity_rachunek_za_gaz,
                                      integer_liczba_lokatorow,
                                      float_rachunek_za_elektrycznosc_na_osobe,
                                      float_rachunek_za_internet_na_osobe,
                                      float_rachunek_za_gaz_na_osobe):

        integer_laczne_oplaty_na_osobe = float_rachunek_za_elektrycznosc_na_osobe + \
                                          float_rachunek_za_internet_na_osobe + float_rachunek_za_gaz_na_osobe
        integer_laczne_oplaty_na_osobe = round(integer_laczne_oplaty_na_osobe, 2)

        ### Odmiana liczby lokatorów
        if integer_liczba_lokatorow <= 4:
            string_osoby_lub_osob = "osoby"
        else:
            string_osoby_lub_osob = "osób"

        ### Obsługa znaków dla rachunku: prąd
        if float_rachunek_za_elektrycznosc_na_osobe < 0:
            float_do_podsumowania_rachunek_prad = -1 * float_rachunek_za_elektrycznosc_na_osobe
            float_do_podsumowania_rachunek_prad = "{:.2f}".format(float_do_podsumowania_rachunek_prad)
            float_do_podsumowania_rachunek_prad = str(float_do_podsumowania_rachunek_prad).replace(".",",")
            string_znak_do_podsumowania_rachunek_prad = "-"
        else:
            float_do_podsumowania_rachunek_prad = float_rachunek_za_elektrycznosc_na_osobe
            float_do_podsumowania_rachunek_prad = "{:.2f}".format(float_do_podsumowania_rachunek_prad)
            float_do_podsumowania_rachunek_prad = str(float_do_podsumowania_rachunek_prad).replace(".", ",")
            string_znak_do_podsumowania_rachunek_prad = ""

        ### Obsługa znaków dla rachunku: internet
        if float_rachunek_za_internet_na_osobe < 0:
            float_do_podsumowania_rachunek_za_internet_na_osobe = -1 * float_rachunek_za_internet_na_osobe
            float_do_podsumowania_rachunek_za_internet_na_osobe = "{:.2f}".format(float_do_podsumowania_rachunek_za_internet_na_osobe)
            float_do_podsumowania_rachunek_za_internet_na_osobe = str(float_do_podsumowania_rachunek_za_internet_na_osobe).replace(".", ",")
            string_znak_podsumowania_internet = "-"
        else:
            float_do_podsumowania_rachunek_za_internet_na_osobe = float_rachunek_za_internet_na_osobe
            float_do_podsumowania_rachunek_za_internet_na_osobe = "{:.2f}".format(
                float_do_podsumowania_rachunek_za_internet_na_osobe)
            float_do_podsumowania_rachunek_za_internet_na_osobe = str(float_do_podsumowania_rachunek_za_internet_na_osobe).replace(".", ",")
            string_znak_podsumowania_internet = "+"

        ### Obsługa znaków dla rachunku: gaz
        if float_rachunek_za_gaz_na_osobe < 0:
            float_do_podsumowania_rachunek_za_gaz_na_osobe = -1 * float_rachunek_za_gaz_na_osobe
            float_do_podsumowania_rachunek_za_gaz_na_osobe = "{:.2f}".format(
                float_do_podsumowania_rachunek_za_gaz_na_osobe)
            float_do_podsumowania_rachunek_za_gaz_na_osobe = str(float_do_podsumowania_rachunek_za_gaz_na_osobe).replace(".", ",")
            string_znak_podsumowania_gaz = "-"
        else:
            float_do_podsumowania_rachunek_za_gaz_na_osobe = float_rachunek_za_gaz_na_osobe
            float_do_podsumowania_rachunek_za_gaz_na_osobe = "{:.2f}".format(
                float_do_podsumowania_rachunek_za_gaz_na_osobe)
            float_do_podsumowania_rachunek_za_gaz_na_osobe = str(float_do_podsumowania_rachunek_za_gaz_na_osobe).replace(".", ",")
            string_znak_podsumowania_gaz = "+"

        ### Nadpłata czy niedopłata
        if integer_laczne_oplaty_na_osobe <= 0:
            string_niedoplata = "Powyższą sumę proszę odliczyć od najbliższej wpłaty czynszu.\n"
        else:
            string_niedoplata = ""

        ### Zamiana kropki na przecinek
        integer_laczne_oplaty_na_osobe = "{:.2f}".format(integer_laczne_oplaty_na_osobe)
        integer_laczne_oplaty_na_osobe = str(integer_laczne_oplaty_na_osobe).replace(".", ",")

        float_calkowity_rachunek_za_elektrycznosc = "{:.2f}".format(float_calkowity_rachunek_za_elektrycznosc)
        float_calkowity_rachunek_za_elektrycznosc = str(float_calkowity_rachunek_za_elektrycznosc).replace(".", ",")
        float_calkowity_rachunek_za_internet = "{:.2f}".format(float_calkowity_rachunek_za_internet)
        float_calkowity_rachunek_za_internet = str(float_calkowity_rachunek_za_internet).replace(".", ",")
        float_calkowity_rachunek_za_gaz = "{:.2f}".format(float_calkowity_rachunek_za_gaz)
        float_calkowity_rachunek_za_gaz = str(float_calkowity_rachunek_za_gaz).replace(".", ",")

        float_rachunek_za_elektrycznosc_na_osobe = "{:.2f}".format(float_rachunek_za_elektrycznosc_na_osobe)
        float_rachunek_za_elektrycznosc_na_osobe = str(float_rachunek_za_elektrycznosc_na_osobe).replace(".", ",")
        float_rachunek_za_internet_na_osobe = "{:.2f}".format(float_rachunek_za_internet_na_osobe)
        float_rachunek_za_internet_na_osobe = str(float_rachunek_za_internet_na_osobe).replace(".", ",")
        float_rachunek_za_gaz_na_osobe = "{:.2f}".format(float_rachunek_za_gaz_na_osobe)
        float_rachunek_za_gaz_na_osobe = str(float_rachunek_za_gaz_na_osobe).replace(".", ",")

        string_tresc_wiadomosci = "Cześć Wszystkim, \n\n" \
                                  "opłaty za media na ul. {string_nazwa_ulicy} wynoszą {string_miesiac} {integer_rok}:\n\n" \
                                  "Tauron (energia elektryczna): {float_calkowita_elektrycznosc}zł / {integer_lokatorzy} {string_osoby_lub_osob} = {float_elektrycznosc_na_osobe}zł na osobę,\n" \
                                  "T-Mobile (internet): {float_calkowity_rachunek_za_internet}zł / {integer_lokatorzy} {string_osoby_lub_osob} = {float_rachunek_za_internet_na_osobe}zł na osobę,\n" \
                                  "PGNiG (gaz): {float_calkowity_rachunek_za_gaz}zł / {integer_lokatorzy} {string_osoby_lub_osob} = {float_rachunek_za_gaz_na_osobe}zł na osobę.\n\n" \
                                  "Tym samym, łączne opłaty za media wynoszą: {string_znak_do_podsumowania_rachunek_prad}{float_do_podsumowania_rachunek_prad}zł {string_znak_podsumowania_internet} {float_do_podsumowania_rachunek_za_internet_na_osobe}zł {string_znak_podsumowania_gaz} {float_do_podsumowania_rachunek_za_gaz_na_osobe}zł = {integer_laczne_oplaty_na_osobe}zł na osobę.\n\n" \
                                  "{string_niedoplata}" \
                                  "Wszystkie rachunki mogę udostępnić do wglądu.\n" \
                                  "Przy przelewie proszę nie zaokrąglać części dziesiętnej ani w dół, ani w górę.\n\n" \
                                  "Pozdrawiam,\n" \
                                  "Jędrzej".format(string_nazwa_ulicy=self.string_odmieniona_nazwa_ulicy,
                                                   string_miesiac=string_aktualny_miesiac,
                                                   integer_rok=integer_aktualny_rok_kalendarzowy,
                                                   float_calkowita_elektrycznosc=float_calkowity_rachunek_za_elektrycznosc,
                                                   integer_lokatorzy=integer_liczba_lokatorow,
                                                   float_elektrycznosc_na_osobe=float_rachunek_za_elektrycznosc_na_osobe,
                                                   float_calkowity_rachunek_za_internet=float_calkowity_rachunek_za_internet,
                                                   float_rachunek_za_internet_na_osobe=float_rachunek_za_internet_na_osobe,
                                                   integer_laczne_oplaty_na_osobe=integer_laczne_oplaty_na_osobe,
                                                   string_osoby_lub_osob=string_osoby_lub_osob,
                                                   float_do_podsumowania_rachunek_prad=float_do_podsumowania_rachunek_prad,
                                                   string_znak_do_podsumowania_rachunek_prad=string_znak_do_podsumowania_rachunek_prad,
                                                   float_do_podsumowania_rachunek_za_internet_na_osobe=float_do_podsumowania_rachunek_za_internet_na_osobe,
                                                   string_znak_podsumowania_internet=string_znak_podsumowania_internet,
                                                   string_niedoplata=string_niedoplata,
                                                   float_calkowity_rachunek_za_gaz=float_calkowity_rachunek_za_gaz,
                                                   float_rachunek_za_gaz_na_osobe=float_rachunek_za_gaz_na_osobe,
                                                   string_znak_podsumowania_gaz=string_znak_podsumowania_gaz,
                                                   float_do_podsumowania_rachunek_za_gaz_na_osobe=float_do_podsumowania_rachunek_za_gaz_na_osobe)

        return string_tresc_wiadomosci

### 20230917 - Otium - Scenariusz CO
class klasa_dziedziczaca_Otium_CO(klasa_dziedziczaca_Otium):

    def __init__(self, string_odmieniona_nazwa_ulicy, float_calkowity_rachunek_zimna_ciepla_woda, float_calkowity_rachunek_CO, string_okres_rozliczenia_CO):
        super().__init__(string_odmieniona_nazwa_ulicy)
        self.float_calkowity_rachunek_zimna_ciepla_woda = float_calkowity_rachunek_zimna_ciepla_woda
        self.float_calkowity_rachunek_CO = float_calkowity_rachunek_CO
        self.string_okres_rozliczenia_CO = string_okres_rozliczenia_CO

    def metoda_tytul_maila(self, string_aktualny_niedomieniony_miesiac, integer_aktualny_rok_kalendarzowy):
        string_tytul_maila = "Opłaty za media oraz rozliczenie CO na ul. {string_nazwa_ulicy} - {string_miesiac} {integer_rok}".format(
            string_nazwa_ulicy=self.string_odmieniona_nazwa_ulicy, string_miesiac=string_aktualny_niedomieniony_miesiac,
            integer_rok=integer_aktualny_rok_kalendarzowy)
        return string_tytul_maila

    def metoda_tresc_wiadomosci_maila(self, string_aktualny_miesiac, integer_aktualny_rok_kalendarzowy,
                                      float_calkowity_rachunek_za_elektrycznosc,
                                      float_calkowity_rachunek_za_internet,
                                      float_calkowity_rachunek_za_gaz,
                                      integer_liczba_lokatorow,
                                      float_rachunek_za_elektrycznosc_na_osobe,
                                      float_rachunek_za_internet_na_osobe,
                                      float_rachunek_za_gaz_na_osobe,
                                      float_calkowity_rachunek_CO,
                                      float_rachunek_CO, string_okres_rozliczenia_CO):

        integer_laczne_oplaty_na_osobe = float_rachunek_za_elektrycznosc_na_osobe + \
                                         float_rachunek_za_internet_na_osobe + float_rachunek_za_gaz_na_osobe + float_rachunek_CO
        integer_laczne_oplaty_na_osobe = round(integer_laczne_oplaty_na_osobe,2)

        if integer_liczba_lokatorow <= 4:
            string_osoby_lub_osob = "osoby"
        else:
            string_osoby_lub_osob = "osób"

        ### Obsługa znaków dla rachunku: prąd
        if float_rachunek_za_elektrycznosc_na_osobe < 0:
            float_do_podsumowania_rachunek_prad = -1 * float_rachunek_za_elektrycznosc_na_osobe
            float_do_podsumowania_rachunek_prad = "{:.2f}".format(float_do_podsumowania_rachunek_prad)
            float_do_podsumowania_rachunek_prad = str(float_do_podsumowania_rachunek_prad).replace(".", ",")
            string_znak_do_podsumowania_rachunek_prad = "-"
        else:
            float_do_podsumowania_rachunek_prad = float_rachunek_za_elektrycznosc_na_osobe
            float_do_podsumowania_rachunek_prad = "{:.2f}".format(float_do_podsumowania_rachunek_prad)
            float_do_podsumowania_rachunek_prad = str(float_do_podsumowania_rachunek_prad).replace(".", ",")
            string_znak_do_podsumowania_rachunek_prad = ""

        ### Obsługa znaków dla rachunku: internet
        if float_rachunek_za_internet_na_osobe < 0:
            float_do_podsumowania_rachunek_za_internet_na_osobe = -1 * float_rachunek_za_internet_na_osobe
            float_do_podsumowania_rachunek_za_internet_na_osobe = "{:.2f}".format(
                float_do_podsumowania_rachunek_za_internet_na_osobe)
            float_do_podsumowania_rachunek_za_internet_na_osobe = str(
                float_do_podsumowania_rachunek_za_internet_na_osobe).replace(".", ",")
            string_znak_podsumowania_internet = "-"
        else:
            float_do_podsumowania_rachunek_za_internet_na_osobe = float_rachunek_za_internet_na_osobe
            float_do_podsumowania_rachunek_za_internet_na_osobe = "{:.2f}".format(
                float_do_podsumowania_rachunek_za_internet_na_osobe)
            float_do_podsumowania_rachunek_za_internet_na_osobe = str(
                float_do_podsumowania_rachunek_za_internet_na_osobe).replace(".", ",")
            string_znak_podsumowania_internet = "+"

        ### Obsługa znaków dla rachunku: gaz
        if float_rachunek_za_gaz_na_osobe < 0:
            float_do_podsumowania_rachunek_za_gaz_na_osobe = -1 * float_rachunek_za_gaz_na_osobe
            float_do_podsumowania_rachunek_za_gaz_na_osobe = "{:.2f}".format(
                float_do_podsumowania_rachunek_za_gaz_na_osobe)
            float_do_podsumowania_rachunek_za_gaz_na_osobe = str(
                float_do_podsumowania_rachunek_za_gaz_na_osobe).replace(".", ",")
            string_znak_podsumowania_gaz = "-"
        else:
            float_do_podsumowania_rachunek_za_gaz_na_osobe = float_rachunek_za_gaz_na_osobe
            float_do_podsumowania_rachunek_za_gaz_na_osobe = "{:.2f}".format(
                float_do_podsumowania_rachunek_za_gaz_na_osobe)
            float_do_podsumowania_rachunek_za_gaz_na_osobe = str(
                float_do_podsumowania_rachunek_za_gaz_na_osobe).replace(".", ",")
            string_znak_podsumowania_gaz = "+"

        ### Obsługa znaków dla rachunku: CO
        if float_calkowity_rachunek_CO < 0:
            string_znak_podsumowania_CO = "-"
            float_do_podsumowania_rachunek_CO = -1*float_rachunek_CO
            float_do_podsumowania_rachunek_CO = "{:.2f}".format(
                float_do_podsumowania_rachunek_CO)
            float_do_podsumowania_rachunek_CO = str(float_do_podsumowania_rachunek_CO).replace(".", ",")
        else:
            string_znak_podsumowania_CO = "+"
            float_do_podsumowania_rachunek_CO = float_rachunek_CO
            float_do_podsumowania_rachunek_CO = "{:.2f}".format(
                float_do_podsumowania_rachunek_CO)
            float_do_podsumowania_rachunek_CO = str(float_do_podsumowania_rachunek_CO).replace(".", ",")

        ### Nadpłata czy niedopłata
        if integer_laczne_oplaty_na_osobe <=0:
            string_niedoplata = "Powyższą sumę proszę odliczyć od najbliższej wpłaty czynszu.\n"
        else:
            string_niedoplata = ""

        ### Zamiana kropki na przecinek
        integer_laczne_oplaty_na_osobe = "{:.2f}".format(integer_laczne_oplaty_na_osobe)
        integer_laczne_oplaty_na_osobe = str(integer_laczne_oplaty_na_osobe).replace(".", ",")

        float_calkowity_rachunek_za_elektrycznosc = "{:.2f}".format(float_calkowity_rachunek_za_elektrycznosc)
        float_calkowity_rachunek_za_elektrycznosc = str(float_calkowity_rachunek_za_elektrycznosc).replace(".", ",")
        float_calkowity_rachunek_za_internet = "{:.2f}".format(float_calkowity_rachunek_za_internet)
        float_calkowity_rachunek_za_internet = str(float_calkowity_rachunek_za_internet).replace(".", ",")
        float_calkowity_rachunek_za_gaz = "{:.2f}".format(float_calkowity_rachunek_za_gaz)
        float_calkowity_rachunek_za_gaz = str(float_calkowity_rachunek_za_gaz).replace(".", ",")
        float_calkowity_rachunek_CO = "{:.2f}".format(float_calkowity_rachunek_CO)
        float_calkowity_rachunek_CO = str(float_calkowity_rachunek_CO).replace(".", ",")

        float_rachunek_za_elektrycznosc_na_osobe = "{:.2f}".format(float_rachunek_za_elektrycznosc_na_osobe)
        float_rachunek_za_elektrycznosc_na_osobe = str(float_rachunek_za_elektrycznosc_na_osobe).replace(".", ",")
        float_rachunek_za_internet_na_osobe = "{:.2f}".format(float_rachunek_za_internet_na_osobe)
        float_rachunek_za_internet_na_osobe = str(float_rachunek_za_internet_na_osobe).replace(".", ",")
        float_rachunek_za_gaz_na_osobe = "{:.2f}".format(float_rachunek_za_gaz_na_osobe)
        float_rachunek_za_gaz_na_osobe = str(float_rachunek_za_gaz_na_osobe).replace(".", ",")
        float_rachunek_CO = "{:.2f}".format(float_rachunek_CO)
        float_rachunek_CO = str(float_rachunek_CO).replace(".", ",")

        string_tresc_wiadomosci = "Cześć Wszystkim, \n\n" \
                                  "opłaty za media na ul. {string_nazwa_ulicy} oraz rozliczenie centralnego ogrzewania (CO) za okres {string_okres_rozliczenia_CO} wynoszą {string_miesiac} {integer_rok}:\n\n" \
                                  "Tauron (energia elektryczna): {float_calkowita_elektrycznosc}zł / {integer_lokatorzy} {string_osoby_lub_osob} = {float_elektrycznosc_na_osobe}zł na osobę,\n" \
                                  "T-Mobile (internet): {float_calkowity_rachunek_za_internet}zł / {integer_lokatorzy} {string_osoby_lub_osob} = {float_rachunek_za_internet_na_osobe}zł na osobę,\n" \
                                  "PGNiG (gaz): {float_calkowity_rachunek_za_gaz}zł / {integer_lokatorzy} {string_osoby_lub_osob} = {float_rachunek_za_gaz_na_osobe}zł na osobę,\n" \
                                  "Rozliczenie CO: {float_calkowity_rachunek_CO}zł / {integer_lokatorzy} {string_osoby_lub_osob} = {float_rachunek_CO}zł na osobę.\n\n" \
                                  "Tym samym, łączne opłaty za media wynoszą: {string_znak_do_podsumowania_rachunek_prad}{float_do_podsumowania_rachunek_prad}zł {string_znak_podsumowania_internet} {float_do_podsumowania_rachunek_za_internet_na_osobe}zł {string_znak_podsumowania_gaz} {float_do_podsumowania_rachunek_za_gaz_na_osobe}zł {string_znak_podsumowania_CO} {float_do_podsumowania_rachunek_CO}zł = {integer_laczne_oplaty_na_osobe}zł na osobę.\n\n" \
                                  "{string_niedoplata}" \
                                  "Wszystkie rachunki mogę udostępnić do wglądu.\n" \
                                  "Przy przelewie proszę nie zaokrąglać części dziesiętnej ani w dół, ani w górę.\n\n" \
                                  "Pozdrawiam,\n" \
                                  "Jędrzej".format(string_nazwa_ulicy=self.string_odmieniona_nazwa_ulicy, string_miesiac=string_aktualny_miesiac,
                                                   integer_rok=integer_aktualny_rok_kalendarzowy,
                                                   float_calkowita_elektrycznosc=float_calkowity_rachunek_za_elektrycznosc,
                                                   integer_lokatorzy=integer_liczba_lokatorow,
                                                   float_elektrycznosc_na_osobe=float_rachunek_za_elektrycznosc_na_osobe,
                                                   float_calkowity_rachunek_za_internet=float_calkowity_rachunek_za_internet,
                                                   float_rachunek_za_internet_na_osobe=float_rachunek_za_internet_na_osobe,
                                                   integer_laczne_oplaty_na_osobe=integer_laczne_oplaty_na_osobe,
                                                   string_osoby_lub_osob=string_osoby_lub_osob,
                                                   float_calkowity_rachunek_CO=float_calkowity_rachunek_CO,
                                                   float_rachunek_CO=float_rachunek_CO,
                                                   string_znak_podsumowania_CO=string_znak_podsumowania_CO,
                                                   string_okres_rozliczenia_CO=string_okres_rozliczenia_CO,
                                                   float_do_podsumowania_rachunek_CO=float_do_podsumowania_rachunek_CO,
                                                   float_do_podsumowania_rachunek_prad=float_do_podsumowania_rachunek_prad,
                                                   string_znak_do_podsumowania_rachunek_prad=string_znak_do_podsumowania_rachunek_prad,
                                                   float_do_podsumowania_rachunek_za_internet_na_osobe=float_do_podsumowania_rachunek_za_internet_na_osobe,
                                                   string_znak_podsumowania_internet=string_znak_podsumowania_internet,
                                                   string_niedoplata=string_niedoplata,
                                                   float_calkowity_rachunek_za_gaz=float_calkowity_rachunek_za_gaz,
                                                   float_rachunek_za_gaz_na_osobe=float_rachunek_za_gaz_na_osobe,
                                                   string_znak_podsumowania_gaz=string_znak_podsumowania_gaz,
                                                   float_do_podsumowania_rachunek_za_gaz_na_osobe=float_do_podsumowania_rachunek_za_gaz_na_osobe)

        return string_tresc_wiadomosci

### 20230917 - Otium - Scenariusz ZW i CW
class klasa_dziedziczaca_Otium_ZW_CW(klasa_dziedziczaca_Otium):

    def __init__(self, string_odmieniona_nazwa_ulicy, float_calkowity_rachunek_zimna_ciepla_woda, string_okres_rozliczenia_ZW_CW):
        super().__init__(string_odmieniona_nazwa_ulicy)
        self.float_calkowity_rachunek_zimna_ciepla_woda = float_calkowity_rachunek_zimna_ciepla_woda
        self.string_okres_rozliczenia_ZW_CW = string_okres_rozliczenia_ZW_CW

    def metoda_tytul_maila(self, string_aktualny_niedomieniony_miesiac, integer_aktualny_rok_kalendarzowy):
        string_tytul_maila = "Opłaty za media oraz rozliczenie ZW/CW na ul. {string_nazwa_ulicy} - {string_miesiac} {integer_rok}".format(
            string_nazwa_ulicy=self.string_odmieniona_nazwa_ulicy, string_miesiac=string_aktualny_niedomieniony_miesiac,
            integer_rok=integer_aktualny_rok_kalendarzowy)
        return string_tytul_maila

    def metoda_tresc_wiadomosci_maila(self, string_aktualny_miesiac, integer_aktualny_rok_kalendarzowy,
                                      float_calkowity_rachunek_za_elektrycznosc,
                                      float_calkowity_rachunek_za_internet,
                                      float_calkowity_rachunek_za_gaz,
                                      integer_liczba_lokatorow,
                                      float_rachunek_za_elektrycznosc_na_osobe,
                                      float_rachunek_za_internet_na_osobe,
                                      float_rachunek_za_gaz_na_osobe,
                                      float_calkowity_rachunek_ZW_CW,
                                      float_rachunek_ZW_CW, string_okres_rozliczenia_ZW_CW):

        integer_laczne_oplaty_na_osobe = float_rachunek_za_elektrycznosc_na_osobe + \
                                         float_rachunek_za_internet_na_osobe + float_rachunek_za_gaz_na_osobe + float_rachunek_ZW_CW
        integer_laczne_oplaty_na_osobe = round(integer_laczne_oplaty_na_osobe,2)

        if integer_liczba_lokatorow <= 4:
            string_osoby_lub_osob = "osoby"
        else:
            string_osoby_lub_osob = "osób"

        ### Obsługa znaków dla rachunku: prąd
        if float_rachunek_za_elektrycznosc_na_osobe < 0:
            float_do_podsumowania_rachunek_prad = -1 * float_rachunek_za_elektrycznosc_na_osobe
            float_do_podsumowania_rachunek_prad = "{:.2f}".format(float_do_podsumowania_rachunek_prad)
            float_do_podsumowania_rachunek_prad = str(float_do_podsumowania_rachunek_prad).replace(".", ",")
            string_znak_do_podsumowania_rachunek_prad = "-"
        else:
            float_do_podsumowania_rachunek_prad = float_rachunek_za_elektrycznosc_na_osobe
            float_do_podsumowania_rachunek_prad = "{:.2f}".format(float_do_podsumowania_rachunek_prad)
            float_do_podsumowania_rachunek_prad = str(float_do_podsumowania_rachunek_prad).replace(".", ",")
            string_znak_do_podsumowania_rachunek_prad = ""

        ### Obsługa znaków dla rachunku: internet
        if float_rachunek_za_internet_na_osobe < 0:
            float_do_podsumowania_rachunek_za_internet_na_osobe = -1 * float_rachunek_za_internet_na_osobe
            float_do_podsumowania_rachunek_za_internet_na_osobe = "{:.2f}".format(
                float_do_podsumowania_rachunek_za_internet_na_osobe)
            float_do_podsumowania_rachunek_za_internet_na_osobe = str(
                float_do_podsumowania_rachunek_za_internet_na_osobe).replace(".", ",")
            string_znak_podsumowania_internet = "-"
        else:
            float_do_podsumowania_rachunek_za_internet_na_osobe = float_rachunek_za_internet_na_osobe
            float_do_podsumowania_rachunek_za_internet_na_osobe = "{:.2f}".format(
                float_do_podsumowania_rachunek_za_internet_na_osobe)
            float_do_podsumowania_rachunek_za_internet_na_osobe = str(
                float_do_podsumowania_rachunek_za_internet_na_osobe).replace(".", ",")
            string_znak_podsumowania_internet = "+"

        ### Obsługa znaków dla rachunku: gaz
        if float_rachunek_za_gaz_na_osobe < 0:
            float_do_podsumowania_rachunek_za_gaz_na_osobe = -1 * float_rachunek_za_gaz_na_osobe
            float_do_podsumowania_rachunek_za_gaz_na_osobe = "{:.2f}".format(
                float_do_podsumowania_rachunek_za_gaz_na_osobe)
            float_do_podsumowania_rachunek_za_gaz_na_osobe = str(
                float_do_podsumowania_rachunek_za_gaz_na_osobe).replace(".", ",")
            string_znak_podsumowania_gaz = "-"
        else:
            float_do_podsumowania_rachunek_za_gaz_na_osobe = float_rachunek_za_gaz_na_osobe
            float_do_podsumowania_rachunek_za_gaz_na_osobe = "{:.2f}".format(
                float_do_podsumowania_rachunek_za_gaz_na_osobe)
            float_do_podsumowania_rachunek_za_gaz_na_osobe = str(
                float_do_podsumowania_rachunek_za_gaz_na_osobe).replace(".", ",")
            string_znak_podsumowania_gaz = "+"

        ### Obsługa znaków dla rachunku: ZW i CW
        if float_calkowity_rachunek_ZW_CW < 0:
            string_znak_podsumowania_ZW_CW = "-"
            float_do_podsumowania_rachunek_ZW_CW = -1*float_rachunek_ZW_CW
            float_do_podsumowania_rachunek_ZW_CW = "{:.2f}".format(
                float_do_podsumowania_rachunek_ZW_CW)
            float_do_podsumowania_rachunek_ZW_CW = str(float_do_podsumowania_rachunek_ZW_CW).replace(".", ",")
        else:
            string_znak_podsumowania_ZW_CW = "+"
            float_do_podsumowania_rachunek_ZW_CW = float_rachunek_ZW_CW
            float_do_podsumowania_rachunek_ZW_CW = "{:.2f}".format(
                float_do_podsumowania_rachunek_ZW_CW)
            float_do_podsumowania_rachunek_ZW_CW = str(float_do_podsumowania_rachunek_ZW_CW).replace(".", ",")

        ### Nadpłata czy niedopłata
        if integer_laczne_oplaty_na_osobe <=0:
            string_niedoplata = "Powyższą sumę proszę odliczyć od najbliższej wpłaty czynszu.\n"
        else:
            string_niedoplata = ""

        ### Zamiana kropki na przecinek
        integer_laczne_oplaty_na_osobe = "{:.2f}".format(integer_laczne_oplaty_na_osobe)
        integer_laczne_oplaty_na_osobe = str(integer_laczne_oplaty_na_osobe).replace(".", ",")

        float_calkowity_rachunek_za_elektrycznosc = "{:.2f}".format(float_calkowity_rachunek_za_elektrycznosc)
        float_calkowity_rachunek_za_elektrycznosc = str(float_calkowity_rachunek_za_elektrycznosc).replace(".", ",")
        float_calkowity_rachunek_za_internet = "{:.2f}".format(float_calkowity_rachunek_za_internet)
        float_calkowity_rachunek_za_internet = str(float_calkowity_rachunek_za_internet).replace(".", ",")
        float_calkowity_rachunek_za_gaz = "{:.2f}".format(float_calkowity_rachunek_za_gaz)
        float_calkowity_rachunek_za_gaz = str(float_calkowity_rachunek_za_gaz).replace(".", ",")
        float_calkowity_rachunek_ZW_CW = "{:.2f}".format(float_calkowity_rachunek_ZW_CW)
        float_calkowity_rachunek_ZW_CW = str(float_calkowity_rachunek_ZW_CW).replace(".", ",")

        float_rachunek_za_elektrycznosc_na_osobe = "{:.2f}".format(float_rachunek_za_elektrycznosc_na_osobe)
        float_rachunek_za_elektrycznosc_na_osobe = str(float_rachunek_za_elektrycznosc_na_osobe).replace(".", ",")
        float_rachunek_za_internet_na_osobe = "{:.2f}".format(float_rachunek_za_internet_na_osobe)
        float_rachunek_za_internet_na_osobe = str(float_rachunek_za_internet_na_osobe).replace(".", ",")
        float_rachunek_za_gaz_na_osobe = "{:.2f}".format(float_rachunek_za_gaz_na_osobe)
        float_rachunek_za_gaz_na_osobe = str(float_rachunek_za_gaz_na_osobe).replace(".", ",")
        float_rachunek_ZW_CW = "{:.2f}".format(float_rachunek_ZW_CW)
        float_rachunek_ZW_CW = str(float_rachunek_ZW_CW).replace(".", ",")

        string_tresc_wiadomosci = "Cześć Wszystkim, \n\n" \
                                  "opłaty za media na ul. {string_nazwa_ulicy} oraz rozliczenie zużycia zimnej (ZW) i ciepłej wody (CW) za okres {string_okres_rozliczenia_ZW_CW} wynoszą {string_miesiac} {integer_rok}:\n\n" \
                                  "Tauron (energia elektryczna): {float_calkowita_elektrycznosc}zł / {integer_lokatorzy} {string_osoby_lub_osob} = {float_elektrycznosc_na_osobe}zł na osobę,\n" \
                                  "T-Mobile (internet): {float_calkowity_rachunek_za_internet}zł / {integer_lokatorzy} {string_osoby_lub_osob} = {float_rachunek_za_internet_na_osobe}zł na osobę,\n" \
                                  "PGNiG (gaz): {float_calkowity_rachunek_za_gaz}zł / {integer_lokatorzy} {string_osoby_lub_osob} = {float_rachunek_za_gaz_na_osobe}zł na osobę,\n" \
                                  "Rozliczenie ZW/CW: {float_calkowity_rachunek_ZW_CW}zł / {integer_lokatorzy} {string_osoby_lub_osob} = {float_rachunek_ZW_CW}zł na osobę.\n\n" \
                                  "Tym samym, łączne opłaty za media wynoszą: {string_znak_do_podsumowania_rachunek_prad}{float_do_podsumowania_rachunek_prad}zł {string_znak_podsumowania_internet} {float_do_podsumowania_rachunek_za_internet_na_osobe}zł {string_znak_podsumowania_gaz} {float_do_podsumowania_rachunek_za_gaz_na_osobe}zł {string_znak_podsumowania_ZW_CW} {float_do_podsumowania_rachunek_ZW_CW}zł = {integer_laczne_oplaty_na_osobe}zł na osobę.\n\n" \
                                  "{string_niedoplata}" \
                                  "Wszystkie rachunki mogę udostępnić do wglądu.\n" \
                                  "Przy przelewie proszę nie zaokrąglać części dziesiętnej ani w dół, ani w górę.\n\n" \
                                  "Pozdrawiam,\n" \
                                  "Jędrzej".format(string_nazwa_ulicy=self.string_odmieniona_nazwa_ulicy, string_miesiac=string_aktualny_miesiac,
                                                   integer_rok=integer_aktualny_rok_kalendarzowy,
                                                   float_calkowita_elektrycznosc=float_calkowity_rachunek_za_elektrycznosc,
                                                   integer_lokatorzy=integer_liczba_lokatorow,
                                                   float_elektrycznosc_na_osobe=float_rachunek_za_elektrycznosc_na_osobe,
                                                   float_calkowity_rachunek_za_internet=float_calkowity_rachunek_za_internet,
                                                   float_rachunek_za_internet_na_osobe=float_rachunek_za_internet_na_osobe,
                                                   integer_laczne_oplaty_na_osobe=integer_laczne_oplaty_na_osobe,
                                                   string_osoby_lub_osob=string_osoby_lub_osob,
                                                   float_calkowity_rachunek_ZW_CW=float_calkowity_rachunek_ZW_CW,
                                                   float_rachunek_ZW_CW=float_rachunek_ZW_CW,
                                                   string_znak_podsumowania_ZW_CW=string_znak_podsumowania_ZW_CW,
                                                   string_okres_rozliczenia_ZW_CW=string_okres_rozliczenia_ZW_CW,
                                                   float_do_podsumowania_rachunek_ZW_CW=float_do_podsumowania_rachunek_ZW_CW,
                                                   float_do_podsumowania_rachunek_prad=float_do_podsumowania_rachunek_prad,
                                                   string_znak_do_podsumowania_rachunek_prad=string_znak_do_podsumowania_rachunek_prad,
                                                   float_do_podsumowania_rachunek_za_internet_na_osobe=float_do_podsumowania_rachunek_za_internet_na_osobe,
                                                   string_znak_podsumowania_internet=string_znak_podsumowania_internet,
                                                   string_niedoplata=string_niedoplata,
                                                   float_calkowity_rachunek_za_gaz=float_calkowity_rachunek_za_gaz,
                                                   float_rachunek_za_gaz_na_osobe=float_rachunek_za_gaz_na_osobe,
                                                   string_znak_podsumowania_gaz=string_znak_podsumowania_gaz,
                                                   float_do_podsumowania_rachunek_za_gaz_na_osobe=float_do_podsumowania_rachunek_za_gaz_na_osobe)

        return string_tresc_wiadomosci

### 20230917 - Ferina - Podstawowy Scenariusz
class klasa_dziedziczaca_Ferina(klasa_bazowa_mieszkanie):

    def __init__(self, string_odmieniona_nazwa_ulicy):
        self.string_odmieniona_nazwa_ulicy = string_odmieniona_nazwa_ulicy

    def metoda_tytul_maila(self, string_aktualny_niedomieniony_miesiac, integer_aktualny_rok_kalendarzowy):
        string_tytul_maila = "Opłaty za media na ul. {string_nazwa_ulicy} - {string_miesiac} {integer_rok}".format(
            string_nazwa_ulicy=self.string_odmieniona_nazwa_ulicy, string_miesiac=string_aktualny_niedomieniony_miesiac,
            integer_rok=integer_aktualny_rok_kalendarzowy)
        return string_tytul_maila

    def metoda_tresc_wiadomosci_maila(self, string_aktualny_miesiac, integer_aktualny_rok_kalendarzowy,
                                      float_calkowity_rachunek_za_elektrycznosc,
                                      float_calkowity_rachunek_za_internet,
                                      integer_liczba_lokatorow,
                                      float_rachunek_za_elektrycznosc_na_osobe,
                                      float_rachunek_za_internet_na_osobe):

        integer_laczne_oplaty_na_osobe = float_rachunek_za_elektrycznosc_na_osobe + float_rachunek_za_internet_na_osobe
        integer_laczne_oplaty_na_osobe = round(integer_laczne_oplaty_na_osobe, 2)

        if integer_liczba_lokatorow <= 4:
            string_osoby_lub_osob = "osoby"
        else:
            string_osoby_lub_osob = "osób"

        ### Obsługa znaków dla rachunku: prąd
        if float_rachunek_za_elektrycznosc_na_osobe < 0:
            float_do_podsumowania_rachunek_prad = -1 * float_rachunek_za_elektrycznosc_na_osobe
            float_do_podsumowania_rachunek_prad = "{:.2f}".format(float_do_podsumowania_rachunek_prad)
            float_do_podsumowania_rachunek_prad = str(float_do_podsumowania_rachunek_prad).replace(".", ",")
            string_znak_do_podsumowania_rachunek_prad = "-"
        else:
            float_do_podsumowania_rachunek_prad = float_rachunek_za_elektrycznosc_na_osobe
            float_do_podsumowania_rachunek_prad = "{:.2f}".format(float_do_podsumowania_rachunek_prad)
            float_do_podsumowania_rachunek_prad = str(float_do_podsumowania_rachunek_prad).replace(".", ",")
            string_znak_do_podsumowania_rachunek_prad = ""

        ### Obsługa znaków dla rachunku: internet
        if float_rachunek_za_internet_na_osobe < 0:
            float_do_podsumowania_rachunek_za_internet_na_osobe = -1 * float_rachunek_za_internet_na_osobe
            float_do_podsumowania_rachunek_za_internet_na_osobe = "{:.2f}".format(float_do_podsumowania_rachunek_za_internet_na_osobe)
            float_do_podsumowania_rachunek_za_internet_na_osobe = str(float_do_podsumowania_rachunek_za_internet_na_osobe).replace(".", ",")
            string_znak_podsumowania_internet = "-"
        else:
            float_do_podsumowania_rachunek_za_internet_na_osobe = float_rachunek_za_internet_na_osobe
            float_do_podsumowania_rachunek_za_internet_na_osobe = "{:.2f}".format(
                float_do_podsumowania_rachunek_za_internet_na_osobe)
            float_do_podsumowania_rachunek_za_internet_na_osobe = str(float_do_podsumowania_rachunek_za_internet_na_osobe).replace(".", ",")
            string_znak_podsumowania_internet = "+"

        ### Nadpłata czy niedopłata
        if integer_laczne_oplaty_na_osobe <= 0:
            string_niedoplata = "Powyższą sumę proszę odliczyć od najbliższej wpłaty czynszu.\n"
        else:
            string_niedoplata = ""

        ### Zamiana kropki na przecinek
        integer_laczne_oplaty_na_osobe = "{:.2f}".format(
            integer_laczne_oplaty_na_osobe)
        integer_laczne_oplaty_na_osobe = str(integer_laczne_oplaty_na_osobe).replace(".", ",")

        float_calkowity_rachunek_za_elektrycznosc = "{:.2f}".format(
            float_calkowity_rachunek_za_elektrycznosc)
        float_calkowity_rachunek_za_elektrycznosc = str(float_calkowity_rachunek_za_elektrycznosc).replace(".", ",")
        float_calkowity_rachunek_za_internet = "{:.2f}".format(
            float_calkowity_rachunek_za_internet)
        float_calkowity_rachunek_za_internet = str(float_calkowity_rachunek_za_internet).replace(".", ",")

        float_rachunek_za_elektrycznosc_na_osobe = "{:.2f}".format(
            float_rachunek_za_elektrycznosc_na_osobe)
        float_rachunek_za_elektrycznosc_na_osobe = str(float_rachunek_za_elektrycznosc_na_osobe).replace(".", ",")
        float_rachunek_za_internet_na_osobe = "{:.2f}".format(
            float_rachunek_za_internet_na_osobe)
        float_rachunek_za_internet_na_osobe = str(float_rachunek_za_internet_na_osobe).replace(".", ",")

        string_tresc_wiadomosci = "Cześć Wszystkim, \n\n" \
                                  "opłaty za media na ul. {string_nazwa_ulicy} wynoszą {string_miesiac} {integer_rok}:\n\n" \
                                  "Tauron (energia elektryczna): {float_calkowita_elektrycznosc}zł / {integer_lokatorzy} {string_osoby_lub_osob} = {float_elektrycznosc_na_osobe}zł na osobę,\n" \
                                  "Play (internet): {float_calkowity_rachunek_za_internet}zł / {integer_lokatorzy} {string_osoby_lub_osob} = {float_rachunek_za_internet_na_osobe}zł na osobę.\n\n" \
                                  "Tym samym, łączne opłaty za media wynoszą: {string_znak_do_podsumowania_rachunek_prad}{float_do_podsumowania_rachunek_prad}zł {string_znak_podsumowania_internet} {float_do_podsumowania_rachunek_za_internet_na_osobe}zł = {integer_laczne_oplaty_na_osobe}zł na osobę.\n\n" \
                                  "{string_niedoplata}" \
                                  "Wszystkie rachunki mogę udostępnić do wglądu.\n" \
                                  "Przy przelewie proszę nie zaokrąglać części dziesiętnej ani w dół, ani w górę.\n\n" \
                                  "Pozdrawiam,\n" \
                                  "Jędrzej".format(string_nazwa_ulicy=self.string_odmieniona_nazwa_ulicy,
                                                   string_miesiac=string_aktualny_miesiac,
                                                   integer_rok=integer_aktualny_rok_kalendarzowy,
                                                   float_calkowita_elektrycznosc=float_calkowity_rachunek_za_elektrycznosc,
                                                   integer_lokatorzy=integer_liczba_lokatorow,
                                                   float_elektrycznosc_na_osobe=float_rachunek_za_elektrycznosc_na_osobe,
                                                   float_calkowity_rachunek_za_internet=float_calkowity_rachunek_za_internet,
                                                   float_rachunek_za_internet_na_osobe=float_rachunek_za_internet_na_osobe,
                                                   integer_laczne_oplaty_na_osobe=integer_laczne_oplaty_na_osobe,
                                                   string_osoby_lub_osob=string_osoby_lub_osob,
                                                   float_do_podsumowania_rachunek_prad=float_do_podsumowania_rachunek_prad,
                                                   string_znak_do_podsumowania_rachunek_prad=string_znak_do_podsumowania_rachunek_prad,
                                                   float_do_podsumowania_rachunek_za_internet_na_osobe=float_do_podsumowania_rachunek_za_internet_na_osobe,
                                                   string_znak_podsumowania_internet=string_znak_podsumowania_internet,
                                                   string_niedoplata=string_niedoplata)

        return string_tresc_wiadomosci

### 20230916 - Ferina - Scenariusz CO
class klasa_dziedziczaca_Ferina_CO(klasa_dziedziczaca_Ferina):

    def __init__(self, string_odmieniona_nazwa_ulicy, float_calkowity_rachunek_zimna_ciepla_woda, float_calkowity_rachunek_CO, string_okres_rozliczenia_CO):
        super().__init__(string_odmieniona_nazwa_ulicy)
        self.float_calkowity_rachunek_zimna_ciepla_woda = float_calkowity_rachunek_zimna_ciepla_woda
        self.float_calkowity_rachunek_CO = float_calkowity_rachunek_CO
        self.string_okres_rozliczenia_CO = string_okres_rozliczenia_CO

    def metoda_tytul_maila(self, string_aktualny_niedomieniony_miesiac, integer_aktualny_rok_kalendarzowy):
        string_tytul_maila = "Opłaty za media oraz rozliczenie CO na ul. {string_nazwa_ulicy} - {string_miesiac} {integer_rok}".format(
            string_nazwa_ulicy=self.string_odmieniona_nazwa_ulicy, string_miesiac=string_aktualny_niedomieniony_miesiac,
            integer_rok=integer_aktualny_rok_kalendarzowy)
        return string_tytul_maila

    def metoda_tresc_wiadomosci_maila(self, string_aktualny_miesiac, integer_aktualny_rok_kalendarzowy,
                                      float_calkowity_rachunek_za_elektrycznosc,
                                      float_calkowity_rachunek_za_internet,
                                      integer_liczba_lokatorow,
                                      float_rachunek_za_elektrycznosc_na_osobe,
                                      float_rachunek_za_internet_na_osobe,
                                      float_calkowity_rachunek_CO,
                                      float_rachunek_CO, string_okres_rozliczenia_CO):

        integer_laczne_oplaty_na_osobe = float_rachunek_za_elektrycznosc_na_osobe + float_rachunek_za_internet_na_osobe + float_rachunek_CO
        integer_laczne_oplaty_na_osobe = round(integer_laczne_oplaty_na_osobe,2)

        if integer_liczba_lokatorow <= 4:
            string_osoby_lub_osob = "osoby"
        else:
            string_osoby_lub_osob = "osób"

        ### Obsługa znaków dla rachunku: prąd
        if float_rachunek_za_elektrycznosc_na_osobe < 0:
            float_do_podsumowania_rachunek_prad = -1 * float_rachunek_za_elektrycznosc_na_osobe
            float_do_podsumowania_rachunek_prad = "{:.2f}".format(float_do_podsumowania_rachunek_prad)
            float_do_podsumowania_rachunek_prad = str(float_do_podsumowania_rachunek_prad).replace(".", ",")
            string_znak_do_podsumowania_rachunek_prad = "-"
        else:
            float_do_podsumowania_rachunek_prad = float_rachunek_za_elektrycznosc_na_osobe
            float_do_podsumowania_rachunek_prad = "{:.2f}".format(float_do_podsumowania_rachunek_prad)
            float_do_podsumowania_rachunek_prad = str(float_do_podsumowania_rachunek_prad).replace(".", ",")
            string_znak_do_podsumowania_rachunek_prad = ""

        ### Obsługa znaków dla rachunku: internet
        if float_rachunek_za_internet_na_osobe < 0:
            float_do_podsumowania_rachunek_za_internet_na_osobe = -1 * float_rachunek_za_internet_na_osobe
            float_do_podsumowania_rachunek_za_internet_na_osobe = "{:.2f}".format(
                float_do_podsumowania_rachunek_za_internet_na_osobe)
            float_do_podsumowania_rachunek_za_internet_na_osobe = str(
                float_do_podsumowania_rachunek_za_internet_na_osobe).replace(".", ",")
            string_znak_podsumowania_internet = "-"
        else:
            float_do_podsumowania_rachunek_za_internet_na_osobe = float_rachunek_za_internet_na_osobe
            float_do_podsumowania_rachunek_za_internet_na_osobe = "{:.2f}".format(
                float_do_podsumowania_rachunek_za_internet_na_osobe)
            float_do_podsumowania_rachunek_za_internet_na_osobe = str(
                float_do_podsumowania_rachunek_za_internet_na_osobe).replace(".", ",")
            string_znak_podsumowania_internet = "+"

        ### Obsługa znaków dla rachunku: CO
        if float_calkowity_rachunek_CO < 0:
            string_znak_podsumowania_CO = "-"
            float_do_podsumowania_rachunek_CO = -1*float_rachunek_CO
            float_do_podsumowania_rachunek_CO = "{:.2f}".format(
                float_do_podsumowania_rachunek_CO)
            float_do_podsumowania_rachunek_CO = str(float_do_podsumowania_rachunek_CO).replace(".", ",")
        else:
            string_znak_podsumowania_CO = "+"
            float_do_podsumowania_rachunek_CO = float_rachunek_CO
            float_do_podsumowania_rachunek_CO = "{:.2f}".format(
                float_do_podsumowania_rachunek_CO)
            float_do_podsumowania_rachunek_CO = str(float_do_podsumowania_rachunek_CO).replace(".", ",")

        ### Nadpłata czy niedopłata
        if integer_laczne_oplaty_na_osobe <=0:
            string_niedoplata = "Powyższą sumę proszę odliczyć od najbliższej wpłaty czynszu.\n"
        else:
            string_niedoplata = ""

        ### Zamiana kropki na przecinek
        integer_laczne_oplaty_na_osobe = "{:.2f}".format(
            integer_laczne_oplaty_na_osobe)
        integer_laczne_oplaty_na_osobe = str(integer_laczne_oplaty_na_osobe).replace(".", ",")

        float_calkowity_rachunek_za_elektrycznosc = "{:.2f}".format(
            float_calkowity_rachunek_za_elektrycznosc)
        float_calkowity_rachunek_za_elektrycznosc = str(float_calkowity_rachunek_za_elektrycznosc).replace(".", ",")
        float_calkowity_rachunek_za_internet = "{:.2f}".format(
            float_calkowity_rachunek_za_internet)
        float_calkowity_rachunek_za_internet = str(float_calkowity_rachunek_za_internet).replace(".", ",")
        float_calkowity_rachunek_CO = "{:.2f}".format(
            float_calkowity_rachunek_CO)
        float_calkowity_rachunek_CO = str(float_calkowity_rachunek_CO).replace(".", ",")

        float_rachunek_za_elektrycznosc_na_osobe = "{:.2f}".format(
            float_rachunek_za_elektrycznosc_na_osobe)
        float_rachunek_za_elektrycznosc_na_osobe = str(float_rachunek_za_elektrycznosc_na_osobe).replace(".", ",")
        float_rachunek_za_internet_na_osobe = "{:.2f}".format(
            float_rachunek_za_internet_na_osobe)
        float_rachunek_za_internet_na_osobe = str(float_rachunek_za_internet_na_osobe).replace(".", ",")
        float_rachunek_CO = "{:.2f}".format(
            float_rachunek_CO)
        float_rachunek_CO = str(float_rachunek_CO).replace(".", ",")

        string_tresc_wiadomosci = "Cześć Wszystkim, \n\n" \
                                  "opłaty za media na ul. {string_nazwa_ulicy} oraz rozliczenie centralnego ogrzewania (CO) za okres {string_okres_rozliczenia_CO} wynoszą {string_miesiac} {integer_rok}:\n\n" \
                                  "Tauron (energia elektryczna): {float_calkowita_elektrycznosc}zł / {integer_lokatorzy} {string_osoby_lub_osob} = {float_elektrycznosc_na_osobe}zł na osobę,\n" \
                                  "Play (internet): {float_calkowity_rachunek_za_internet}zł / {integer_lokatorzy} {string_osoby_lub_osob} = {float_rachunek_za_internet_na_osobe}zł na osobę,\n" \
                                  "Rozliczenie CO: {float_calkowity_rachunek_CO}zł / {integer_lokatorzy} {string_osoby_lub_osob} = {float_rachunek_CO}zł na osobę.\n\n" \
                                  "Tym samym, łączne opłaty za media wynoszą: {string_znak_do_podsumowania_rachunek_prad}{float_do_podsumowania_rachunek_prad}zł {string_znak_podsumowania_internet} {float_do_podsumowania_rachunek_za_internet_na_osobe}zł {string_znak_podsumowania_CO} {float_do_podsumowania_rachunek_CO}zł = {integer_laczne_oplaty_na_osobe}zł na osobę.\n\n" \
                                  "{string_niedoplata}" \
                                  "Wszystkie rachunki mogę udostępnić do wglądu.\n" \
                                  "Przy przelewie proszę nie zaokrąglać części dziesiętnej ani w dół, ani w górę.\n\n" \
                                  "Pozdrawiam,\n" \
                                  "Jędrzej".format(string_nazwa_ulicy=self.string_odmieniona_nazwa_ulicy, string_miesiac=string_aktualny_miesiac,
                                                   integer_rok=integer_aktualny_rok_kalendarzowy,
                                                   float_calkowita_elektrycznosc=float_calkowity_rachunek_za_elektrycznosc,
                                                   integer_lokatorzy=integer_liczba_lokatorow,
                                                   float_elektrycznosc_na_osobe=float_rachunek_za_elektrycznosc_na_osobe,
                                                   float_calkowity_rachunek_za_internet=float_calkowity_rachunek_za_internet,
                                                   float_rachunek_za_internet_na_osobe=float_rachunek_za_internet_na_osobe,
                                                   integer_laczne_oplaty_na_osobe=integer_laczne_oplaty_na_osobe,
                                                   string_osoby_lub_osob=string_osoby_lub_osob,
                                                   float_calkowity_rachunek_CO=float_calkowity_rachunek_CO,
                                                   float_rachunek_CO=float_rachunek_CO,
                                                   string_znak_podsumowania_CO=string_znak_podsumowania_CO,
                                                   string_okres_rozliczenia_CO=string_okres_rozliczenia_CO,
                                                   float_do_podsumowania_rachunek_CO=float_do_podsumowania_rachunek_CO,
                                                   float_do_podsumowania_rachunek_prad=float_do_podsumowania_rachunek_prad,
                                                   string_znak_do_podsumowania_rachunek_prad=string_znak_do_podsumowania_rachunek_prad,
                                                   float_do_podsumowania_rachunek_za_internet_na_osobe=float_do_podsumowania_rachunek_za_internet_na_osobe,
                                                   string_znak_podsumowania_internet=string_znak_podsumowania_internet,
                                                   string_niedoplata=string_niedoplata)

        return string_tresc_wiadomosci

### 20230916 - Ferina - Scenariusz ZW i CW
class klasa_dziedziczaca_Ferina_ZW_CW(klasa_dziedziczaca_Ferina):

    def __init__(self, string_odmieniona_nazwa_ulicy, float_calkowity_rachunek_zimna_ciepla_woda, float_rachunek_zimna_ciepla_woda, string_okres_rozliczenia_ZW_CW):
        super().__init__(string_odmieniona_nazwa_ulicy)
        self.float_calkowity_rachunek_zimna_ciepla_woda = float_calkowity_rachunek_zimna_ciepla_woda
        self.float_rachunek_zimna_ciepla_woda = float_rachunek_zimna_ciepla_woda
        self.string_okres_rozliczenia_ZW_CW = string_okres_rozliczenia_ZW_CW

    def metoda_tytul_maila(self, string_aktualny_niedomieniony_miesiac, integer_aktualny_rok_kalendarzowy):
        string_tytul_maila = "Opłaty za media oraz rozliczenie ZW i CW na ul. {string_nazwa_ulicy} - {string_miesiac} {integer_rok}".format(
            string_nazwa_ulicy=self.string_odmieniona_nazwa_ulicy, string_miesiac=string_aktualny_niedomieniony_miesiac,
            integer_rok=integer_aktualny_rok_kalendarzowy)
        return string_tytul_maila

    def metoda_tresc_wiadomosci_maila(self, string_aktualny_miesiac, integer_aktualny_rok_kalendarzowy,
                                      float_calkowity_rachunek_za_elektrycznosc,
                                      float_calkowity_rachunek_za_internet,
                                      integer_liczba_lokatorow,
                                      float_rachunek_za_elektrycznosc_na_osobe,
                                      float_rachunek_za_internet_na_osobe,
                                      float_calkowity_rachunek_zimna_ciepla_woda,
                                      float_rachunek_zimna_ciepla_woda, string_okres_rozliczenia_ZW_CW):

        integer_laczne_oplaty_na_osobe = float_rachunek_za_elektrycznosc_na_osobe + float_rachunek_za_internet_na_osobe + float_rachunek_zimna_ciepla_woda
        integer_laczne_oplaty_na_osobe = round(integer_laczne_oplaty_na_osobe,2)

        if integer_liczba_lokatorow <= 4:
            string_osoby_lub_osob = "osoby"
        else:
            string_osoby_lub_osob = "osób"

        ### Obsługa znaków dla rachunku: prąd
        if float_rachunek_za_elektrycznosc_na_osobe < 0:
            float_do_podsumowania_rachunek_prad = -1 * float_rachunek_za_elektrycznosc_na_osobe
            float_do_podsumowania_rachunek_prad = "{:.2f}".format(float_do_podsumowania_rachunek_prad)
            float_do_podsumowania_rachunek_prad = str(float_do_podsumowania_rachunek_prad).replace(".", ",")
            string_znak_do_podsumowania_rachunek_prad = "-"
        else:
            float_do_podsumowania_rachunek_prad = float_rachunek_za_elektrycznosc_na_osobe
            float_do_podsumowania_rachunek_prad = "{:.2f}".format(float_do_podsumowania_rachunek_prad)
            float_do_podsumowania_rachunek_prad = str(float_do_podsumowania_rachunek_prad).replace(".", ",")
            string_znak_do_podsumowania_rachunek_prad = ""

        ### Obsługa znaków dla rachunku: internet
        if float_rachunek_za_internet_na_osobe < 0:
            float_do_podsumowania_rachunek_za_internet_na_osobe = -1 * float_rachunek_za_internet_na_osobe
            float_do_podsumowania_rachunek_za_internet_na_osobe = "{:.2f}".format(
                float_do_podsumowania_rachunek_za_internet_na_osobe)
            float_do_podsumowania_rachunek_za_internet_na_osobe = str(
                float_do_podsumowania_rachunek_za_internet_na_osobe).replace(".", ",")
            string_znak_podsumowania_internet = "-"
        else:
            float_do_podsumowania_rachunek_za_internet_na_osobe = float_rachunek_za_internet_na_osobe
            float_do_podsumowania_rachunek_za_internet_na_osobe = "{:.2f}".format(
                float_do_podsumowania_rachunek_za_internet_na_osobe)
            float_do_podsumowania_rachunek_za_internet_na_osobe = str(
                float_do_podsumowania_rachunek_za_internet_na_osobe).replace(".", ",")
            string_znak_podsumowania_internet = "+"

        ### Obsługa znaków dla rachunku: ZW i CW
        if float_rachunek_zimna_ciepla_woda < 0:
            string_znak_podsumowania_ZW_CW = "-"
            float_do_podsumowania_rachunek_zimna_ciepla_woda = -1*float_rachunek_zimna_ciepla_woda
            float_do_podsumowania_rachunek_zimna_ciepla_woda = "{:.2f}".format(
                float_do_podsumowania_rachunek_zimna_ciepla_woda)
            float_do_podsumowania_rachunek_zimna_ciepla_woda = str(
                float_do_podsumowania_rachunek_zimna_ciepla_woda).replace(".", ",")
        else:
            string_znak_podsumowania_ZW_CW = "+"
            float_do_podsumowania_rachunek_zimna_ciepla_woda = float_rachunek_zimna_ciepla_woda
            float_do_podsumowania_rachunek_zimna_ciepla_woda = "{:.2f}".format(
                float_do_podsumowania_rachunek_zimna_ciepla_woda)
            float_do_podsumowania_rachunek_zimna_ciepla_woda = str(
                float_do_podsumowania_rachunek_zimna_ciepla_woda).replace(".", ",")

        ### Nadpłata czy niedopłata
        if integer_laczne_oplaty_na_osobe <=0:
            string_niedoplata = "Powyższą sumę proszę odliczyć od najbliższej wpłaty czynszu.\n"
        else:
            string_niedoplata = ""

        ### Zamiana kropki na przecinek
        integer_laczne_oplaty_na_osobe = "{:.2f}".format(
            integer_laczne_oplaty_na_osobe)
        integer_laczne_oplaty_na_osobe = str(integer_laczne_oplaty_na_osobe).replace(".", ",")

        float_calkowity_rachunek_za_elektrycznosc = "{:.2f}".format(
            float_calkowity_rachunek_za_elektrycznosc)
        float_calkowity_rachunek_za_elektrycznosc = str(float_calkowity_rachunek_za_elektrycznosc).replace(".", ",")
        float_calkowity_rachunek_za_internet = "{:.2f}".format(
            float_calkowity_rachunek_za_internet)
        float_calkowity_rachunek_za_internet = str(float_calkowity_rachunek_za_internet).replace(".", ",")
        float_calkowity_rachunek_zimna_ciepla_woda = "{:.2f}".format(
            float_calkowity_rachunek_zimna_ciepla_woda)
        float_calkowity_rachunek_zimna_ciepla_woda = str(float_calkowity_rachunek_zimna_ciepla_woda).replace(".", ",")

        float_rachunek_za_elektrycznosc_na_osobe = "{:.2f}".format(
            float_rachunek_za_elektrycznosc_na_osobe)
        float_rachunek_za_elektrycznosc_na_osobe = str(float_rachunek_za_elektrycznosc_na_osobe).replace(".", ",")
        float_rachunek_za_internet_na_osobe = "{:.2f}".format(
            float_rachunek_za_internet_na_osobe)
        float_rachunek_za_internet_na_osobe = str(float_rachunek_za_internet_na_osobe).replace(".", ",")
        float_rachunek_zimna_ciepla_woda = "{:.2f}".format(
            float_rachunek_zimna_ciepla_woda)
        float_rachunek_zimna_ciepla_woda = str(float_rachunek_zimna_ciepla_woda).replace(".", ",")

        string_tresc_wiadomosci = "Cześć Wszystkim, \n\n" \
                                  "opłaty za media na ul. {string_nazwa_ulicy} oraz rozliczenie zużycia zimnej (ZW) i ciepłej wody (CW) za okres {string_okres_rozliczenia_ZW_CW} wynoszą {string_miesiac} {integer_rok}:\n\n" \
                                  "Tauron (energia elektryczna): {float_calkowita_elektrycznosc}zł / {integer_lokatorzy} {string_osoby_lub_osob} = {float_elektrycznosc_na_osobe}zł na osobę,\n" \
                                  "Play (internet): {float_calkowity_rachunek_za_internet}zł / {integer_lokatorzy} {string_osoby_lub_osob} = {float_rachunek_za_internet_na_osobe}zł na osobę,\n" \
                                  "Rozliczenie ZW/CW: {float_calkowity_rachunek_zimna_ciepla_woda}zł / {integer_lokatorzy} {string_osoby_lub_osob} = {float_rachunek_zimna_ciepla_woda}zł na osobę.\n\n" \
                                  "Tym samym, łączne opłaty za media wynoszą: {string_znak_do_podsumowania_rachunek_prad}{float_do_podsumowania_rachunek_prad}zł {string_znak_podsumowania_internet} {float_do_podsumowania_rachunek_za_internet_na_osobe}zł {string_znak_podsumowania_ZW_CW} {float_do_podsumowania_rachunek_zimna_ciepla_woda}zł = {integer_laczne_oplaty_na_osobe}zł na osobę.\n\n" \
                                  "{string_niedoplata}" \
                                  "Wszystkie rachunki mogę udostępnić do wglądu.\n" \
                                  "Przy przelewie proszę nie zaokrąglać części dziesiętnej ani w dół, ani w górę.\n\n" \
                                  "Pozdrawiam,\n" \
                                  "Jędrzej".format(string_nazwa_ulicy=self.string_odmieniona_nazwa_ulicy, string_miesiac=string_aktualny_miesiac,
                                                   integer_rok=integer_aktualny_rok_kalendarzowy,
                                                   float_calkowita_elektrycznosc=float_calkowity_rachunek_za_elektrycznosc,
                                                   integer_lokatorzy=integer_liczba_lokatorow,
                                                   float_elektrycznosc_na_osobe=float_rachunek_za_elektrycznosc_na_osobe,
                                                   float_calkowity_rachunek_za_internet=float_calkowity_rachunek_za_internet,
                                                   float_rachunek_za_internet_na_osobe=float_rachunek_za_internet_na_osobe,
                                                   integer_laczne_oplaty_na_osobe=integer_laczne_oplaty_na_osobe,
                                                   string_osoby_lub_osob=string_osoby_lub_osob,
                                                   float_calkowity_rachunek_zimna_ciepla_woda=float_calkowity_rachunek_zimna_ciepla_woda,
                                                   float_rachunek_zimna_ciepla_woda=float_rachunek_zimna_ciepla_woda,
                                                   string_znak_podsumowania_ZW_CW=string_znak_podsumowania_ZW_CW,
                                                   string_okres_rozliczenia_ZW_CW=string_okres_rozliczenia_ZW_CW,
                                                   float_do_podsumowania_rachunek_zimna_ciepla_woda=float_do_podsumowania_rachunek_zimna_ciepla_woda,
                                                   float_do_podsumowania_rachunek_prad=float_do_podsumowania_rachunek_prad,
                                                   string_znak_do_podsumowania_rachunek_prad=string_znak_do_podsumowania_rachunek_prad,
                                                   float_do_podsumowania_rachunek_za_internet_na_osobe=float_do_podsumowania_rachunek_za_internet_na_osobe,
                                                   string_znak_podsumowania_internet=string_znak_podsumowania_internet,
                                                   string_niedoplata=string_niedoplata)

        return string_tresc_wiadomosci

### Właściwy program "Generator-Bona"
instancja_klasy_bazowej = klasa_bazowa_mieszkanie()


########################################################################################################################
########################################################################################################################
########################################################################################################################

# Inicjalizacja instancji klasy
instancja_klasy_dziedziczacej_Otium = klasa_dziedziczaca_Otium(string_odmieniona_nazwa_ulicy_Otium)

# Podział rachunków
float_rachunek_za_elektrycznosc_na_osobe_Otium = instancja_klasy_dziedziczacej_Otium.metoda_statyczna_podzial_rachunku(
    float_calkowity_rachunek_za_elektrycznosc_Otium, integer_liczba_lokatorow_Otium)
float_rachunek_za_internet_na_osobe_Otium = instancja_klasy_dziedziczacej_Otium.metoda_statyczna_podzial_rachunku(
    float_calkowity_rachunek_za_internet_Otium, integer_liczba_lokatorow_Otium)
float_rachunek_za_gaz_na_osobe_Otium = instancja_klasy_dziedziczacej_Otium.metoda_statyczna_podzial_rachunku(
    float_calkowity_rachunek_za_gaz_Otium, integer_liczba_lokatorow_Otium)

# Numer i nazwa miesiaca oraz roku
integer_numer_aktualnego_miesiaca = instancja_klasy_dziedziczacej_Otium.metoda_statyczna_numer_aktualnego_miesiaca()
integer_aktualny_rok_kalendarzowy = instancja_klasy_dziedziczacej_Otium.metoda_statyczna_rok_kalendarzowy()
string_aktualny_niedomieniony_miesiac_kalendarzowy = instancja_klasy_dziedziczacej_Otium\
    .metoda_zwroc_string_nieodmienionego_miesiaca_kalendarzowego(integer_numer_aktualnego_miesiaca)
string_aktualny_odmieniony_miesiac_kalendarzowy = instancja_klasy_dziedziczacej_Otium\
    .metoda_zwroc_string_odmienionego_miesiaca_kalendarzowego(integer_numer_aktualnego_miesiaca)

# Generuję tytuł maila dla Otium
string_tytul_maila = instancja_klasy_dziedziczacej_Otium.metoda_tytul_maila(string_aktualny_niedomieniony_miesiac_kalendarzowy,
                                                                            integer_aktualny_rok_kalendarzowy)
print("\n#################")
print("##### Otium #####")
print("#################\n")
print(string_tytul_maila + "\n")

# Generuję treść maila dla Otium
string_tresc_maila = instancja_klasy_dziedziczacej_Otium.metoda_tresc_wiadomosci_maila(string_aktualny_odmieniony_miesiac_kalendarzowy,
                                                                                       integer_aktualny_rok_kalendarzowy,
                                                                                       float_calkowity_rachunek_za_elektrycznosc_Otium,
                                                                                       float_calkowity_rachunek_za_internet_Otium,
                                                                                       float_calkowity_rachunek_za_gaz_Otium,
                                                                                       integer_liczba_lokatorow_Otium,
                                                                                       float_rachunek_za_elektrycznosc_na_osobe_Otium,
                                                                                       float_rachunek_za_internet_na_osobe_Otium,
                                                                                       float_rachunek_za_gaz_na_osobe_Otium)
print(string_tresc_maila)

### 20230917 - Otium - CO
print("\n######################")
print("##### Otium - CO #####")
print("######################\n")

float_rachunek_CO_Otium = instancja_klasy_dziedziczacej_Otium.metoda_statyczna_podzial_rachunku(
    float_calkowity_rachunek_CO_Otium, integer_liczba_lokatorow_Otium)

instacja_klasa_dziedziczaca_Otium_CO = klasa_dziedziczaca_Otium_CO(string_odmieniona_nazwa_ulicy_Otium,
                                                                           float_calkowity_rachunek_CO_Otium,
                                                                           float_rachunek_CO_Otium,
                                                                           string_okres_rozliczenia_CO_Otium)

string_tytul_maila = instacja_klasa_dziedziczaca_Otium_CO.metoda_tytul_maila(string_aktualny_niedomieniony_miesiac_kalendarzowy,
                                                                            integer_aktualny_rok_kalendarzowy)
print(string_tytul_maila + "\n")

string_tresc_maila = instacja_klasa_dziedziczaca_Otium_CO.metoda_tresc_wiadomosci_maila(string_aktualny_odmieniony_miesiac_kalendarzowy,
                                                                                       integer_aktualny_rok_kalendarzowy,
                                                                                       float_calkowity_rachunek_za_elektrycznosc_Otium,
                                                                                       float_calkowity_rachunek_za_internet_Otium,
                                                                                       float_calkowity_rachunek_za_gaz_Otium,
                                                                                       integer_liczba_lokatorow_Otium,
                                                                                       float_rachunek_za_elektrycznosc_na_osobe_Otium,
                                                                                       float_rachunek_za_internet_na_osobe_Otium,
                                                                                       float_rachunek_za_gaz_na_osobe_Otium,
                                                                                       float_calkowity_rachunek_CO_Otium,
                                                                                       float_rachunek_CO_Otium,
                                                                                       string_okres_rozliczenia_CO_Otium)
print(string_tresc_maila)

### 20230917 - Otium - ZW i CW
print("\n###########################")
print("##### Otium - ZW i CW #####")
print("###########################\n")

float_rachunek_ZW_CW_Otium = instancja_klasy_dziedziczacej_Otium.metoda_statyczna_podzial_rachunku(
    float_calkowity_rachunek_ZW_CW_Otium, integer_liczba_lokatorow_Otium)

instacja_klasa_dziedziczaca_Otium_ZW_CW = klasa_dziedziczaca_Otium_ZW_CW(string_odmieniona_nazwa_ulicy_Otium,
                                                                           float_calkowity_rachunek_ZW_CW_Otium,
                                                                           string_okres_rozliczenia_ZW_CW_Otium)

string_tytul_maila = instacja_klasa_dziedziczaca_Otium_ZW_CW.metoda_tytul_maila(string_aktualny_niedomieniony_miesiac_kalendarzowy,
                                                                            integer_aktualny_rok_kalendarzowy)
print(string_tytul_maila + "\n")

string_tresc_maila = instacja_klasa_dziedziczaca_Otium_ZW_CW.metoda_tresc_wiadomosci_maila(string_aktualny_odmieniony_miesiac_kalendarzowy,
                                                                                       integer_aktualny_rok_kalendarzowy,
                                                                                       float_calkowity_rachunek_za_elektrycznosc_Otium,
                                                                                       float_calkowity_rachunek_za_internet_Otium,
                                                                                       float_calkowity_rachunek_za_gaz_Otium,
                                                                                       integer_liczba_lokatorow_Otium,
                                                                                       float_rachunek_za_elektrycznosc_na_osobe_Otium,
                                                                                       float_rachunek_za_internet_na_osobe_Otium,
                                                                                       float_rachunek_za_gaz_na_osobe_Otium,
                                                                                       float_calkowity_rachunek_ZW_CW_Otium,
                                                                                       float_rachunek_ZW_CW_Otium,
                                                                                       string_okres_rozliczenia_ZW_CW_Otium)
print(string_tresc_maila)

########################################################################################################################
########################################################################################################################
########################################################################################################################

# Inicjalizacja instancji klasy
instancja_klasy_dziedziczacej_Ferina = klasa_dziedziczaca_Ferina(string_odmieniona_nazwa_ulicy_Ferina)

# Podział rachunków
float_rachunek_za_elektrycznosc_na_osobe_Ferina = \
    instancja_klasy_dziedziczacej_Ferina.metoda_statyczna_podzial_rachunku(
    float_calkowity_rachunek_za_elektrycznosc_Ferina, integer_liczba_lokatorow_Ferina)
float_rachunek_za_internet_na_osobe_Ferina = instancja_klasy_dziedziczacej_Ferina.metoda_statyczna_podzial_rachunku(
    float_calkowity_rachunek_za_internet_Ferina, integer_liczba_lokatorow_Ferina)

# Numer i nazwa miesiaca oraz roku
integer_numer_aktualnego_miesiaca = instancja_klasy_dziedziczacej_Ferina.metoda_statyczna_numer_aktualnego_miesiaca()
integer_aktualny_rok_kalendarzowy = instancja_klasy_dziedziczacej_Ferina.metoda_statyczna_rok_kalendarzowy()
string_aktualny_niedomieniony_miesiac_kalendarzowy = instancja_klasy_dziedziczacej_Ferina\
    .metoda_zwroc_string_nieodmienionego_miesiaca_kalendarzowego(integer_numer_aktualnego_miesiaca)
string_aktualny_odmieniony_miesiac_kalendarzowy = instancja_klasy_dziedziczacej_Ferina\
    .metoda_zwroc_string_odmienionego_miesiaca_kalendarzowego(integer_numer_aktualnego_miesiaca)

# Generuję tytuł maila dla Ferina
string_tytul_maila = instancja_klasy_dziedziczacej_Ferina.metoda_tytul_maila(string_aktualny_niedomieniony_miesiac_kalendarzowy,
                                                                            integer_aktualny_rok_kalendarzowy)

print("\n##################")
print("##### Ferina #####")
print("##################\n")
print(string_tytul_maila + "\n")

# Generuję treść maila dla Ferina
string_tresc_maila = instancja_klasy_dziedziczacej_Ferina.metoda_tresc_wiadomosci_maila(string_aktualny_odmieniony_miesiac_kalendarzowy,
                                                                                       integer_aktualny_rok_kalendarzowy,
                                                                                       float_calkowity_rachunek_za_elektrycznosc_Ferina,
                                                                                       float_calkowity_rachunek_za_internet_Ferina,
                                                                                       integer_liczba_lokatorow_Ferina,
                                                                                       float_rachunek_za_elektrycznosc_na_osobe_Ferina,
                                                                                       float_rachunek_za_internet_na_osobe_Ferina)
print(string_tresc_maila)

### Ferina - ZW i CW
print("\n############################")
print("##### Ferina - ZW i CW #####")
print("############################\n")


float_rachunek_zimna_ciepla_woda_Ferina = instancja_klasy_dziedziczacej_Ferina.metoda_statyczna_podzial_rachunku(
    float_calkowity_rachunek_zimna_ciepla_woda_Ferina, integer_liczba_lokatorow_Ferina)

instacja_klasa_dziedziczaca_Ferina_ZW_CW = klasa_dziedziczaca_Ferina_ZW_CW(string_odmieniona_nazwa_ulicy_Ferina,
                                                                           float_calkowity_rachunek_zimna_ciepla_woda_Ferina,
                                                                           float_rachunek_zimna_ciepla_woda_Ferina,
                                                                           string_okres_rozliczenia_ZW_CW_Ferina)

string_tytul_maila = instacja_klasa_dziedziczaca_Ferina_ZW_CW.metoda_tytul_maila(string_aktualny_niedomieniony_miesiac_kalendarzowy,
                                                                            integer_aktualny_rok_kalendarzowy)
print(string_tytul_maila + "\n")

string_tresc_maila = instacja_klasa_dziedziczaca_Ferina_ZW_CW.metoda_tresc_wiadomosci_maila(string_aktualny_odmieniony_miesiac_kalendarzowy,
                                                                                       integer_aktualny_rok_kalendarzowy,
                                                                                       float_calkowity_rachunek_za_elektrycznosc_Ferina,
                                                                                       float_calkowity_rachunek_za_internet_Ferina,
                                                                                       integer_liczba_lokatorow_Ferina,
                                                                                       float_rachunek_za_elektrycznosc_na_osobe_Ferina,
                                                                                       float_rachunek_za_internet_na_osobe_Ferina,
                                                                                       float_calkowity_rachunek_zimna_ciepla_woda_Ferina,
                                                                                       float_rachunek_zimna_ciepla_woda_Ferina,
                                                                                       string_okres_rozliczenia_ZW_CW_Ferina)
print(string_tresc_maila)

### Ferina - CO
print("\n#######################")
print("##### Ferina - CO #####")
print("#######################\n")

float_rachunek_CO_Ferina = instancja_klasy_dziedziczacej_Ferina.metoda_statyczna_podzial_rachunku(
    float_calkowity_rachunek_CO_Ferina, integer_liczba_lokatorow_Ferina)

instacja_klasa_dziedziczaca_Ferina_CO = klasa_dziedziczaca_Ferina_CO(string_odmieniona_nazwa_ulicy_Ferina,
                                                                           float_calkowity_rachunek_CO_Ferina,
                                                                           float_rachunek_CO_Ferina,
                                                                           string_okres_rozliczenia_CO_Ferina)

string_tytul_maila = instacja_klasa_dziedziczaca_Ferina_CO.metoda_tytul_maila(string_aktualny_niedomieniony_miesiac_kalendarzowy,
                                                                            integer_aktualny_rok_kalendarzowy)
print(string_tytul_maila + "\n")

string_tresc_maila = instacja_klasa_dziedziczaca_Ferina_CO.metoda_tresc_wiadomosci_maila(string_aktualny_odmieniony_miesiac_kalendarzowy,
                                                                                       integer_aktualny_rok_kalendarzowy,
                                                                                       float_calkowity_rachunek_za_elektrycznosc_Ferina,
                                                                                       float_calkowity_rachunek_za_internet_Ferina,
                                                                                       integer_liczba_lokatorow_Ferina,
                                                                                       float_rachunek_za_elektrycznosc_na_osobe_Ferina,
                                                                                       float_rachunek_za_internet_na_osobe_Ferina,
                                                                                       float_calkowity_rachunek_CO_Ferina,
                                                                                       float_rachunek_CO_Ferina,
                                                                                       string_okres_rozliczenia_CO_Ferina)
print(string_tresc_maila)
print()
