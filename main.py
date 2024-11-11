from mic import listen_for_a_word
import subprocess
import os
import winapps
import webbrowser
from install_go import *


STOP_COMMANDS = ["stop", "exit", "quit", "terminate", "end program", "goodbye"]
OPEN_COMMANDS = ["open", "start", "use"]

BROSWER_COMMANDS = ["google", "browser", "search"]
YOUTUBE_COMMANDS = ["watch"]
while True:

    word = listen_for_a_word()

    if any(command in word.lower() for command in STOP_COMMANDS):
        print("Stop command detected. Exiting...")
        listening = False
        break

    if any(command in word for command in OPEN_COMMANDS):
        program = word.lower().replace('open', '').replace(
            'start', '').replace('use', '').strip()
        print(f"Opening program: {program}")
        open_app(program)

    if any(command in word for command in BROSWER_COMMANDS):
        search = word.lower().replace('google', '').replace(
            'browser', '').replace("search", "").strip()

        if not search:
            search_google("")
        else:
            search_google(search)

    else:
        print("No recognized application command detected.")

    if any(command in word for command in YOUTUBE_COMMANDS):
        vedio = word.lower().replace('watch', '').strip()
        if not vedio:
            webbrowser.open("https://www.youtube.com/")
        else:
            watch_video(vedio)

    else:
        print("No recognized application command detected.")
