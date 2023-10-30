# twitch-tts

**Requires PyTorch and Coqui-AI TTS.**

This script will connect to a Twitch channel, listen for any messages, and read aloud the message in the style of "`USERNAME` says `MESSAGE`". Speakers can be controlled by typing "`speaker:[SPEAKER]`" before the chat message.

It's recommended to run all this from a virtual environment. Here are directions for Windows. For other operating systems, you may check out this link: https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/

Windows:
1. Download this entire repo or `git clone` it into an empty directory.
2. Run a command prompt from this folder. Set up a virtual environment: `python -m venv venv`
3. Activate the virtual environment. NOTE: This step is included in main.py and should be altered or removed if your environment path is named something else. `.\venv\Scripts\activate` or `python venv\Scripts\activate`
4. Install packages from requirements: `pip install -r requirements.txt`
5. Run `main.py` from your IDE, or use `python main.py` from a command line.

Please ensure that you have the correct interpreter selected in your IDE. You should use the one that was installed in your virtual environment.

## Config

**To add a speaker**, drop a short WAV for your speaker in `speakers/`, then add an entry to the `speakers` list in `main.py`. Make sure to add "speaker:" before the title of your wav file.

**To change the Twitch channel you're listening to**, switch the `TWITCH_CHANNEL` variable in `dougdoug/TwitchPlays_TTS_READER.py` to your channel. Then reload the script.

This script uses Coqui-TTS models for speech synthesis: https://github.com/coqui-ai/TTS. **To change the model you're using**, edit the TTS line in `main.py` with a valid model. Some English models I have tested are commented. Because of the integration with Coqui, if you have access to their API, this script should automatically detect and use your credentials.

## License

Includes and modifies elements of https://github.com/DougDougGithub/TwitchPlays

Please see the included LICENSE for details on all other files.

## Issues

This repository is uploaded mostly for demonstration purposes and personal use, but pull requests and issues are welcome. Please give me some time to respond.
