# OBS Replay Script for Linux
This script lets you automatically save OBS replays on linux by running this script. Optionally, you can use your desktop environment to set up a keybind to run this script at the press of a button.

## Installation instructions
1. Ensure OBS websocket is enabled under Tools -> Websocket Server Settings in OBS. If this option is not present, try installing the flatpak version of OBS.
2. Clone the repo using `git clone https://github.com/Solyphonous/OBSReplay/` or download ZIP by pressing Code -> Download ZIP if you do not have git installed.
3. Install dependencies using `poetry install` while inside the project folder. If you do not have poetry installed:
* [Install pipx](https://pipx.pypa.io/stable/installation/)
* Install poetry using `pipx install poetry`.
4. Create a file called ".env" in the project directory. Fill it with the following information:
```
OBSPASSWORD = "The password available to you in OBS websocket settings."
```
4. Run `poetry run python /path/to/replay.py` to clip a replay.