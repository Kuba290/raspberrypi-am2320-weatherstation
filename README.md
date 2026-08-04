# raspberrypi-am2320-weatherstation

## Raspberry Pi 3B+ &amp; AM2320 weather station (ENG version)

### Connections (AM2320 - Raspberry Pi 3B+)
- VDD - 1 (3.3V)
- SDA - 3 (SDA)
- GND - 9 (GND)
- SCL - 5 (SCL)

### Content of project
- templates: index.html (web app)
- am2320_measure.py (read AM2320 sensor and write data to database every 15 seconds)
- app.py (Flask app with getting data from database and creating endpoints for frontend & backend)
- db_start.py (database creator)

### How it looks
<img width="885" height="806" alt="obraz" src="https://github.com/user-attachments/assets/a675c2d3-dc09-4b53-b21a-8c3c7cc2e8c7" />

### Website
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




## Stacja pogodowa Raspberry Pi 3B+ z sensorem AM2320 (PL version)

### Połączenia (AM2320 - Raspberry Pi 3B+)
- VDD - 1 (3,3V)
- SDA - 3 (SDA)
- GND - 9 (GND)
- SCL - 5 (SCL)

### Zawartość projektu
- templates: index.html (plik .html z aplikacją webową)
- am2320_measure.py (odczyt sensora AM2320 i zapis danych do bazy co 15 sekund)
- app.py (aplikacja Flask, pobierająca informacje z bazy danych i tworząca endpoint-y dla frontend-u i backend-u)
- db_start.py (kreator bazy danych)

### Wygląd strony
<img width="885" height="806" alt="obraz" src="https://github.com/user-attachments/assets/a675c2d3-dc09-4b53-b21a-8c3c7cc2e8c7" />

### Strona
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
