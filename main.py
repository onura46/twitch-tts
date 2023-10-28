from dougdoug.TwitchPlays_TTS_READER import *
import subprocess
from datetime import datetime
from playsound import playsound
import torch
import TTS
from TTS.api import TTS

current_dir = os.getcwd()
class Talk:
    def generate(text_to_speak, speaker: str = "speaker:kaelin"):
        n = speaker.split("speaker:", 1)[1]

        if speaker in speakers:
            speaker_wav = f"C:/dev/twitch/speakers/{n}.wav"

        timestamp = str(datetime.now().strftime(f'%Y-%m-%d_%H-%M-%S-%f'))
        output_path = f"output/{n}_{timestamp}.wav"

        # Run TTS
        # ❗ Since this model is multi-lingual voice cloning model, we must set the target speaker_wav and language
        # Text to speech to a file
        tts.tts_to_file(text=text_to_speak, speaker_wav=speaker_wav, language="en", file_path=output_path)
        tts_queue.append(output_path)
        
    def speak(user,msg):
        talklist = msg.split(" ", 1)
        if talklist[0] in speakers:
            speech = f"{user} says {talklist[1]}"
            Talk.generate(speech,speaker=talklist[0])
        else:
            speech = f"{user} says {msg}"
            Talk.generate(speech)

    def render():
        # TO-DO: Still goes out of order sometimes; fix
        if tts_queue != []:
            file_path = tts_queue[0]
            playsound(file_path)
            tts_queue.remove(tts_queue[0])

subprocess.run(r"python venv/Scripts/activate")

# Initialize list of speakers. Speaker list must match file name of speaker WAVs, but in the format of "speaker:{wav_file_name}"
speakers = ["speaker:kaelin", "speaker:bernie", "speaker:vader"]

# Initialize a queue for TTS in case multiple messages occur during generation
tts_queue = []

# Get device
device = "cuda" if torch.cuda.is_available() else "cpu"

# Initialize TTS
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v1", progress_bar=True).to(device)