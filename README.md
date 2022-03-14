# PYTHON VIRTUAL ASSISTANT

This virtual assistant is designed with simplicity in mind, which performs basic functionalities that assist users in their daily lives

* __CONTINUING GOAL: OPTIMIZE THE SPEED OF THE BOT__
### List of utilities 
Please refer to file `utilities.txt`

### HIGHLIGHTED UTILITIES 
- __Send email:__ Sending email, including Subject line, to a person in the contact list
- __Add email contact:__ Add a new email contact to the contact list
- __Play music:__ Playing music from Youtube
- __Get weather__: Get current weather data for a location (if specified) or the user's location (based on user's public IP address)
- __Wiki search__: Give a short summary of a person or a thing

#### :star: UPGRADES :star:
- User can now add new email contact when sending an email if the recipient is not in the contact list
- All manual inputs from client have now been transformed to text-to-speech inputs

### Setup
- Clone this repo
- Create a virtual environment: `python3 -m venv <path_to_virtual_env>` (i.e `python3 -m venv myenv/.`)
- Download the required packages: `pip install -r requirements.txt` <br/>
__Make sure to have `SpeechRecognition`, `PyAudio` and `pyttsx3` installed for the skeleton to function__<br/>
__Any packages not listed in `requirements.txt` are python built-in packages__

#### To get Weather Data
- Create an account at [openweathermap.org](https://openweathermap.org)
- Create an API key and replace `configs["WEATHER_API_KEY"]` with your own

### Important Notes
- Some of the imports are explicitly imported to suppress warnings and errors. These do not affect the flow of the virtual assistant as some imports are device-dependant.
