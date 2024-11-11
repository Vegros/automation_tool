import subprocess
import platform
import os
from pathlib import Path
import shutil
import sys


def run_go_build(go_project_dir):
    try:
        working_dir = os.getcwd()
        go_project_path = Path(go_project_dir).resolve()
        os.chdir(go_project_path)
        result = subprocess.run(["go", "build", "."],
                                capture_output=True, text=True)

        if result.returncode == 0:
            print("Go build successful!")
            app_folder = os.path.join(os.path.dirname(
                os.path.abspath(__file__)), 'go_executables')

            if sys.platform == "win32":

                for filename in os.listdir(go_project_path):
                    if filename.endswith(".exe"):
                        shutil.copy(filename, app_folder)

            elif sys.platform == "darwin":
                for filename in os.listdir(go_project_path):
                    if not filename.endswith(".sh") or not filename.endswith(".mod") or not filename.endswith(".sum"):
                        shutil.copy(filename, app_folder)
            else:
                print("os not supported yet for file transfer")

        else:
            print(f"Go build failed with error: {result.stderr}")

        os.chdir(working_dir)

    except FileNotFoundError:
        print("Go is not installed. Please install Go to continue.")


def search_google(word):
    processes = []
    for filename in os.listdir("go_executables"):
        if filename.startswith("search"):
            path = os.path.abspath(os.path.join("go_executables", filename))
            arguments = [word]

            process = subprocess.Popen(
                [path] + arguments)
            processes.append(process)

    for process in processes:
        process.wait()
        print(f"Process {process.args} completed.")


def watch_video(video):
    processes = []
    for filename in os.listdir("go_executables"):
        if filename.startswith("watch"):
            path = os.path.abspath(os.path.join("go_executables", filename))
            arguments = [video]

            process = subprocess.Popen(
                [path] + arguments)
            processes.append(process)

    for process in processes:
        process.wait()
        print(f"Process {process.args} completed.")


def open_app(app_name):
    processes = []
    for filename in os.listdir("go_executables"):
        if filename.startswith("start"):
            path = os.path.abspath(os.path.join("go_executables", filename))
            arguments = [app_name]

            process = subprocess.Popen(
                [path] + arguments)
            processes.append(process)

    for process in processes:
        process.wait()
        print(f"Process {process.args} completed.")


paths = ["go_files/open", "go_files/go-web-tool", "go_files/youtube-tool"]


for path in paths:
    run_go_build(path)
