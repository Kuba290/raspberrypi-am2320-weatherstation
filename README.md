# raspberrypi-am2320-weatherstation

# Contents
- [raspberrypi-am2320-weatherstation](#raspberrypi-am2320-weatherstation)
  - [Raspberry Pi 3B+ \& AM2320 weather station (ENG version)](#raspberry-pi-3b--am2320-weather-station-eng-version)
    - [Connections (AM2320 - Raspberry Pi 3B+)](#connections-am2320---raspberry-pi-3b)
    - [Content of project](#content-of-project)
    - [Weather station](#weather-station)
    - [Weather forecast](#weather-forecast)
  - [Stacja pogodowa Raspberry Pi 3B+ z sensorem AM2320 (PL version)](#stacja-pogodowa-raspberry-pi-3b-z-sensorem-am2320-pl-version)
    - [Połączenia (AM2320 - Raspberry Pi 3B+)](#połączenia-am2320---raspberry-pi-3b)
    - [Zawartość projektu](#zawartość-projektu)
    - [Stacja pogodowa](#stacja-pogodowa)
    - [Prognoza pogody](#prognoza-pogody)
  - [Website layout / Wygląd strony](#website-layout--wygląd-strony)
    - [Weather station / Stacja pogodowa](#weather-station--stacja-pogodowa)
    - [Weather forecast / Prognoza pogody](#weather-forecast--prognoza-pogody)
   

## Raspberry Pi 3B+ &amp; AM2320 weather station (ENG version)

### Connections (AM2320 - Raspberry Pi 3B+)
- VDD - 1 (3.3V)
- SDA - 3 (SDA)
- GND - 9 (GND)
- SCL - 5 (SCL)

### Content of project
- templates: index.html (weather station) & weather.html (weather forecast), both with auto dark mode
- am2320_measure.py (read AM2320 sensor and write data to database every 15 seconds)
- app.py (Flask app with getting data from database and creating endpoints for frontend & backend)
- db_start.py (database creator)
- location.py (coordinates for fetching weather forecast)

### Weather station
- measure time - last measure time from sensor, which is currently visible
- current temperature - in Celsius scale
- Heat Index - calculated above 26 degree C (80F), based on [NOAA formulas](https://en.wikipedia.org/wiki/Heat_index#Formula)
- current humidity
- combined chart with temperature and humidity, with history:
  - last hour
  - last 3 hours
  - last 12 hours
  - last 24 hours
  - all history - API limit (last 10k database rows)

### Weather forecast
Based on API from [Open Meteo](https://open-meteo.com) the following data are fetched for:
- current forecast:
    - temperature
    - humidity
    - precipitation
    - current weather (conversion from weather codes to Polish names weather conditions, based on [WMO CODE TABLE 4677](https://www.nodc.noaa.gov/archive/arc0021/0002199/1.1/data/0-data/HTML/WMO-CODE/WMO4677.HTM)
- daily forecast (7 days):
    - date
    - weather
    - temperature max/min
    - precipitation
    - sunrise & sunset
    - moonrise & moonset
- hourly forecast (next 240h) - with temperature & precipitation combined chart:
    - datetime
    - weather
    - temperature
    - humidity
    - precipitation propability
    - precipitation

## Stacja pogodowa Raspberry Pi 3B+ z sensorem AM2320 (PL version)

### Połączenia (AM2320 - Raspberry Pi 3B+)
- VDD - 1 (3,3V)
- SDA - 3 (SDA)
- GND - 9 (GND)
- SCL - 5 (SCL)

### Zawartość projektu
- templates: index.html (stacja pogodowa) i weather.html (prognoza pogody), obie strony z automatycznym ciemnym motywem
- am2320_measure.py (odczyt sensora AM2320 i zapis danych do bazy co 15 sekund)
- app.py (aplikacja Flask, pobierająca informacje z bazy danych i tworząca endpoint-y dla frontend-u i backend-u)
- db_start.py (kreator bazy danych)
- location.py (koordynaty lokalizacji do pobierania prognozy pogody)

### Stacja pogodowa
- Czas pomiaru - kiedy został odnotowany ostatni pomiar, który jest obecnie widoczny
- Aktualna temperatura
- Heat Index - obliczany powyżej 26 stopni Celsjusza, oparty o [równania Narodowej Służby Oceanicznej i Atmosferycznej NOAA](https://en.wikipedia.org/wiki/Heat_index#Formula)
- Aktualna wilgotność
- wykres z temperaturą (oś Y lewa) i wilgotnością (oś Y prawa), z historią z:
  - ostatniej godziny
  - ostatnich 3 godzin
  - ostatnich 12 godzin
  - ostatnich 24 godzin
  - całej historii - limit API (ustawiony na ostatnie 10 tysięcy rekordów z bazy danych)
 
### Prognoza pogody
Na podstawie dostępnego API z [Open Meteo](https://open-meteo.com) pobierane są następujące wartości:
- dla warunków bieżących:
    - temperatura
    - wilgotność
    - opady
    - bieżąca pogoda (konwersja kodów pogody na polskie nazwy np. "Pochmurno", na podstawie tabeli [WMO CODE TABLE 4677](https://www.nodc.noaa.gov/archive/arc0021/0002199/1.1/data/0-data/HTML/WMO-CODE/WMO4677.HTM)
- dla prognozy dziennej (7 - dniowej):
    - data
    - pogoda
    - temperatura max/min
    - opady
    - wschód i zachód Słońca
    - wschód i zachód Księżyca
- dla prognozy godzinowej (240 godzin w przód) - również przedstawiono na wykresie temperaturę i opady co godzinę:
    - data i godzina
    - pogoda
    - temperatura
    - wilgotność
    - szansa opadów
    - opady
 
## Website layout / Wygląd strony

### Weather station / Stacja pogodowa
<img width="1920" height="1532" alt="obraz" src="https://github.com/user-attachments/assets/f664a651-6b88-4907-9342-7550074fc019" />

### Weather forecast / Prognoza pogody
<img width="1536" height="1575" alt="obraz" src="https://github.com/user-attachments/assets/98384460-a813-487a-9d99-fbeeab6b5396" />


