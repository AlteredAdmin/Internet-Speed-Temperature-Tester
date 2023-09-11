'''
###############################################################################


_______        _______ _______  ______ _______ ______       _______ ______  _______ _____ __   _
|_____| |         |    |______ |_____/ |______ |     \      |_____| |     \ |  |  |   |   | \  |
|     | |_____    |    |______ |    \_ |______ |_____/      |     | |_____/ |  |  | __|__ |  \_|
                                                                                                

Title: Internet Speed & Temperature Tester
Description: This script performs a speed test and retrieves current weather data based on a specified zip code, and writes the results to a CSV file 
with error handling and logging.
More info: https://alteredadmin.github.io/
Name: Altered Admin
Date: March 3 2023
Website: https://alteredadmin.github.io
Twitter: https://twitter.com/Alt3r3dAdm1n

=====================================================
If you found this helpful Please consider:
Buymeacoffee: http://buymeacoffee.com/alteredadmin
BTC: bc1qhkw7kv9dtdk8xwvetreya2evjqtxn06cghyxt7
LTC: ltc1q2mrh9s8sgmh8h5jtra3gqxuhvy04vuagpm3dk9
ETH: 0xef053b0d936746Df00C9CCe0454b7b8afb1497ac
=====================================================

Required modules:
    os
    speedtest
    requests
    csv
    datetime
    logging


Long Description:
    This script performs a speed test and retrieves current weather data based on a specified zip code.
    The script writes the results of the speed test and weather data to a CSV file along with the current date and time.
    The script handles errors in case of failure during the speed test or retrieving the weather data.
    If there is a failure during the speed test, the script will note the failure in the notes column of the CSV file and continue.
    If there is a failure during the retrieval of weather data, the script will note the failure in the notes column of the CSV file and continue.
    The script also logs all events to a log file for debugging and monitoring purposes.


Example:
###############################################################################
'''

import os
import speedtest
import requests
import csv
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(filename='/home/pi/speedtest&temp/speedtest_and_temperature.log', level=logging.INFO,
format='%(asctime)s %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

# Get current date and time
now = datetime.now()

# Format date and time string
formatted_datetime = now.strftime("%m/%d/%Y %H:%M:%S")
logging.info("Current time: " + formatted_datetime)

# Perform speed test
try:
    st = speedtest.Speedtest()
    download_speed = st.download() / 1000000
    upload_speed = st.upload() / 1000000
    logging.info("Download: " + str(download_speed))
    logging.info("Upload: " + str(upload_speed))
except Exception as e:
    download_speed = "Error"
    upload_speed = "Error"
    logging.error("Speed test failed: " + str(e))

# Retrieve current weather data based on zip code
zip_code = "12345" # replace with desired zip code
api_key = "12345YOURAPIKEY54321" # replace with your OpenWeatherMap API key
api_url = f"https://api.openweathermap.org/data/2.5/weather?zip=" + zip_code + ",&appid=" + api_key + "&units=imperial"
logging.info(api_url)

try:
    response = requests.get(api_url)
    logging.info(response)
    weather_data = response.json()
    temperature = weather_data['main']['temp']
    feels_like = weather_data['main']['feels_like']
    temp_max = weather_data['main']['temp_max']
    weathermain = weather_data['weather'][0]['main']
    weatherdescription = weather_data['weather'][0]['description']
    logging.info(temperature)
    logging.info(feels_like)
    logging.info(temp_max)
    logging.info(weathermain)
    logging.info(weatherdescription)
except Exception as e:
    temperature = "Error"
    feels_like = "Error"
    temp_max = "Error"
    weathermain = "Error"
    weatherdescription = "Error"
    logging.error("Failed to retrieve weather data: " + str(e))

# Export data to CSV file
file_exists = os.path.isfile("/home/pi/speedtest&temp/speedtest_and_temperature.csv")
with open("/home/pi/speedtest&temp/speedtest_and_temperature.csv", "a", newline="") as csv_file:
    writer = csv.writer(csv_file)
    if not file_exists:
        writer.writerow(["Date & Time", "Download Speed", "Upload Speed", "Temperature", "Feels Like", "Max Temperature", "Weather Main", "Weather Description", "Notes"])
    notes = ""
    if download_speed == "Error":
        notes += "Speed test failed. "
    if temperature == "Error":
        notes += "Failed to retrieve weather data. "
    writer.writerow([formatted_datetime, download_speed, upload_speed, temperature, feels_like, temp_max, weathermain, weatherdescription, notes])
    logging.info("Data written to CSV file.")


