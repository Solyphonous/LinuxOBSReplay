import obsws_python as obs
import sounddevice as sd
import soundfile as sf
import os

from dotenv import load_dotenv
from pathlib import Path

current_dir = Path(__file__).parent

soundpath = f"{current_dir}/success.wav"

load_dotenv()

data, samplerate = sf.read(soundpath)

cl = obs.ReqClient(host="localhost", port=4455, password=os.getenv("OBSPASSWORD"), timeout=3)
cl.save_replay_buffer()

sd.play(data, samplerate)
sd.wait()