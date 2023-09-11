# Speed Test & Weather Logger

This script logs internet speed tests (both download and upload) and current weather information based on a specified ZIP code. The results are saved to a CSV file and also logged.

## Why does thie exist?

I've been experiencing intermittent issues with my home internet lately, which seem to occur randomly throughout the week. However, I've noticed a pattern where it tends to go down between 1:00PM and 3:00PM, and then comes back up around 3:00PM or 4:00PM. Rebooting the router/modem hasn't helped. I've also noticed that during these outages, my speedtest results are terrible. Interestingly, it seems like these issues only happen on very hot days. To keep track of the problem, I've created a log to record my download and upload speeds, as well as the temperature.

## Features
- Fetches download and upload speed using `speedtest`.
- Fetches current weather data from the OpenWeatherMap API.
- Logs results to both a `.log` file and a `.csv` file.

## Description:
This script performs a speed test and retrieves current weather data based on a specified zip code.
The script writes the results of the speed test and weather data to a CSV file along with the current date and time.
The script handles errors in case of failure during the speed test or retrieving the weather data.
If there is a failure during the speed test, the script will note the failure in the notes column of the CSV file and continue.
If there is a failure during the retrieval of weather data, the script will note the failure in the notes column of the CSV file and continue.
The script also logs all events to a log file for debugging and monitoring purposes.

## Dependencies
- `speedtest-cli`: To perform internet speed tests.
- `requests`: To fetch data from the OpenWeatherMap API.
### openweathermap.org
You will need a free account on openweathermap.org and an API key.

## How to Use
1. Clone the repository: `git clone https://github.com/AlteredAdmin/Internet-Speed-Temperature-Tester`
2. Install the required packages: `pip install speedtest-cli requests`
3. Replace the placeholder `zip_code` and `api_key` in the script with your desired ZIP code and your OpenWeatherMap API key respectively.
4. Run the script: `python internet_speed_and_temperature_tester.py`

## Output
The results will be saved in `speedtest_and_temperature.csv` and also logged to `speedtest_and_temperature.log` in the specified directory (`/home/pi/speedtest&temp/` by default).

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
n/a
