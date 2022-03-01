# PYTHON VIRTUAL ASSISTANT

This virtual assistant is designed with simplicity in mind, which performs basic functionalities that assist users in their daily lives

* __CONTINUING GOAL: OPTIMIZE THE SPEED OF THE BOT__
### List of utilities 
Please refer to file `utilities.txt`

### HIGHLIGHTED UTILITIES 
- __Send email:__ Sending email, including Subject line, to a person in the contact list (Contact list is a hidden .txt file)
- __Play music:__ Playing music from Youtube

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
