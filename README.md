# Internet Speed & Temperature Tester

 Python script that scrapes pastebin.com for newly posted paste.

## Description:
This script performs a speed test and retrieves current weather data based on a specified zip code.
The script writes the results of the speed test and weather data to a CSV file along with the current date and time.
The script handles errors in case of failure during the speed test or retrieving the weather data.
If there is a failure during the speed test, the script will note the failure in the notes column of the CSV file and continue.
If there is a failure during the retrieval of weather data, the script will note the failure in the notes column of the CSV file and continue.
The script also logs all events to a log file for debugging and monitoring purposes.

## Why does thie exist?

I've been experiencing intermittent issues with my home internet lately, which seem to occur randomly throughout the week. However, I've noticed a pattern where it tends to go down between 1:00PM and 3:00PM, and then comes back up around 3:00PM or 4:00PM. Rebooting the router/modem hasn't helped. I've also noticed that during these outages, my speedtest results are terrible. Interestingly, it seems like these issues only happen on very hot days. To keep track of the problem, I've created a log to record my download and upload speeds, as well as the temperature.

## openweathermap.org

You will need a free account on openweathermap.org and an API key. 