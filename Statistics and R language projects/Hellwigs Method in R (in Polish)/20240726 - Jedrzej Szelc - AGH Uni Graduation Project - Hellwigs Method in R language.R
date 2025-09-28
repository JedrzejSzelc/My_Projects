#### Nagłówek ####
# Data:             2024.07.26
# Uczelnia:         Akademia Górniczo-Hutnicza, Kraków
# Studia:           Metody Statystycznej Analizy Danych
# Przedmiot:        Analiza Współzależności Zjawisk - Metoda Hellwiga w R
# Prowadzący:       prof. Łukasz Lach
# Autor/Student:    Jędrzej Szelc

#### Biblioteki i konfiguracja ####

# Biblioteki
library("readxl")
library(dplyr)
library(ggplot2)
library(corrplot)

### Funkcje pomocnicze ####

funkcja_Metoda_Hellwiga <- function( y, x, method="pearson") {
  # Źródło: https://rdrr.io/github/mbojan/mbstats/src/R/hellwig.R
  requireNamespace("utils")
  x <- as.data.frame(x)
  cm <- stats::cor(x, method=method) # correlation matrix among indeps
  cd <- stats::cor(x, y, method=method) # correlations with dependent
  # list of combination vectors
  k <- sapply( seq(2, length(x)), function(i)
    utils::combn(length(x), i, simplify=FALSE) )
  k <- do.call("c", k)
  # function calculating individual capacities
  hfun <- function(v)
  {
    sapply(v, function(i) cd[i]^2 / sum(abs(cm[v,i])) )
  }
  h <- sapply(k, hfun)
  df_Hellwig_Results <- data.frame( Kombinacja = sapply( k, paste, collapse="-"),
                                    Wsp_Hellwiga = sapply(h, sum),
                                    stringsAsFactors=FALSE)
  return(df_Hellwig_Results)
}

#### Wczytywanie danych .csv ####

# Wczytuję dane
string_sciezka_obecnego_katalogu <- getwd()
# string_plik_z_danymi <- "20240730_Dane_Wejsciowe_AWZ_Przeliczanie_X8-X10.xlsx"
string_plik_z_danymi <- "20240811_AWZ_Dane_Roznicowane.xlsx"
df_raw_data <- read_excel(paste0(string_sciezka_obecnego_katalogu,"/",string_plik_z_danymi))

# Zostaw tylko zakres dat od 01.2015 do 12.2022 włącznie
df_dane <- df_raw_data %>%
  filter(Year < 2023)

# Kopia bezpieczeństwa oryginalnych danych - na wszelki wypadek
df_dane_oryginalne <- df_dane

# Nazwy kolumn df_dane
wektor_standardowych_nazw_kolumn <- colnames(df_dane)

# Wstępna EDA
str(df_dane)
summary(df_dane)
head(df_dane)

#### Metoda Hellwiga ####

### Przygotowanie danych do obliczeń Hellwiga

# Wektor Y
wektor_Y <- df_dane$Y_Overdose

# Pomocnicze wektory X
wektor_X1 <- df_dane$X1_SP500
wektor_X2 <- df_dane$X2_GDP_indicators
wektor_X3 <- df_dane$X3_CPI
wektor_X4 <- df_dane$X4_Housing_Case_Shiller
wektor_X5 <- df_dane$X5_Housing_CPI
wektor_X6 <- df_dane$X6_Unemployment
wektor_X7 <- df_dane$X7_Labor_Force
# wektor_X8 <- df_dane$X8_Layoffs_1000
# wektor_X9 <- df_dane$X9_Job_Openings_1000
# wektor_X10 <- df_dane$X10_Personal_Comsumption_1
wektor_X8 <- df_dane$X8_Layoffs
wektor_X9 <- df_dane$X9_Job_Openings
wektor_X10 <- df_dane$X10_Personal_Consumption
wektor_X11 <- df_dane$X11_Consumer_Sentiment
COVID <- df_dane$COVID

# Wybór wektorów do macierzy wektorów X
wektor_wektorow_X_do_macierzy <- c()
wektor_wektorow_X_do_macierzy <- c(wektor_X1,
                                   wektor_X2,
                                   wektor_X3,
                                   wektor_X4,
                                   wektor_X5,
                                   wektor_X6,
                                   wektor_X7,
                                   wektor_X8,
                                   wektor_X9,
                                   wektor_X10,
                                   wektor_X11,
                                   COVID
                                   )

# Automatyczne obliczenia rozmiaru danych
integer_liczba_rekordow_wektora_Y <- length(wektor_Y)
integer_liczba_wektorow_w_macierzy <- length(wektor_wektorow_X_do_macierzy)/integer_liczba_rekordow_wektora_Y

# Macierz wektorów X
macierz_X <- matrix(wektor_wektorow_X_do_macierzy, 
                    nrow = integer_liczba_rekordow_wektora_Y, 
                    ncol = integer_liczba_wektorow_w_macierzy)

### Obliczenia metody Hellwiga
df_Hellwig_Wyniki <- funkcja_Metoda_Hellwiga(wektor_Y, macierz_X)
head(df_Hellwig_Wyniki)

# Znajdź najwyższe wartości wsp. Hellwiga
integer_liczba_najwyzszych_wynikow_do_wyswietlenia <- 10
df_Hellwig_Wyniki %>%
  arrange(desc(Wsp_Hellwiga)) %>%
  head(., integer_liczba_najwyzszych_wynikow_do_wyswietlenia)
print(cat("UWAGA: Numery kombinacji NIE odpowiadają numerom oryginalnych zmiennych X,
       lecz reprezentują jedynie liczby porządkowe kolumn macierzy X.
       Ta macierz X jest parametrem wejściowym funkcji 'funkcja_Metoda_Hellwiga()'.
       Innymi słowy, numery kombinacji należy porównać z wektorami, które przypisane są
       do wektora 'wektor_wektorow_X_do_macierzy' w linijce 86."))