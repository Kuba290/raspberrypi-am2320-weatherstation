# raspberrypi-am2320-weatherstation
Raspberry Pi 3B+ &amp; AM2320 weather station 

## Content of project
- templates: index.html (web app)
- am2320_measure.py (read AM2320 sensor and write data to database every 15 seconds)
- app.py (Flask app with getting data from database and creating endpoints for frontend & backend)
- db_start.py (database creator)

## How it looks
<img width="885" height="806" alt="obraz" src="https://github.com/user-attachments/assets/a675c2d3-dc09-4b53-b21a-8c3c7cc2e8c7" />

### Data (with polish subtitles)
- measure time (czas pomiaru) - last measure time from sensor, which is currently visible
- current temperature (aktualna temperatura) - in Celsius scale
- Heat Index - calculated above 26 degree C (80F), based on [NOAA formulas](https://en.wikipedia.org/wiki/Heat_index#Formula)
- current humidity (aktualna wilgotność)
- combined chart with temperature and humidity, with history (pokaż historię z):
  - last hour (ostatniej godziny)
  - last 3 hours (ostatnich 3 godzin)
  - last 12 hours (ostatnich 12 godzin)
  - last 24 hours (ostatnich 24 godzin)
  - all history (całej historii) - API limit (last 10k database rows)
