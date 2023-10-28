# twitch-tts

It's recommended to run all this from a virtual environment. Here are directions for Windows. For other operating systems, you may check out this link: https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/

Windows:
1. Run a command prompt from this folder. Set up a virtual environment: `python -m venv venv`
2. Activate the virtual environment. NOTE: This step is included in main.py and should be altered or removed if your environment path is named something else. `.\venv\Scripts\activate` or `python venv\Scripts\activate`
3. Install packages from requirements: `pip install -r requirements.txt`

Please ensure that you have the correct interpreter selected in your IDE. You should use the one that was installed in your virtual environment.

## Config

To add a speaker, drop a short WAV for your speaker in `speakers/`, then add an entry to the `speakers` list in `main.py`. Make sure to add "speaker:" before the title of your wav file.

To change the Twitch channel you're listening to, switch the `TWITCH_CHANNEL` variable in `dougdoug/TwitchPlays_TTS_READER.py` to your channel.

## License

Includes and modifies elements of https://github.com/DougDougGithub/TwitchPlays
