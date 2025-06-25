import subprocess
import time
import pyautogui

def prevent_sleep():
    # Launch caffeinate in background to prevent sleep
    return subprocess.Popen(["caffeinate", "-dimsu"])

def keep_teams_active():
    while True:
        pyautogui.press("shift")  # You can also move the mouse slightly
        print("Kept alive at:", time.strftime("%H:%M:%S"))
        time.sleep(240)  # Every 4 minutes

if __name__ == "__main__":
    try:
        caffeinate_proc = prevent_sleep()
        print("Caffeinate running. Preventing sleep.")
        keep_teams_active()
    except KeyboardInterrupt:
        print("Stopping...")
        caffeinate_proc.terminate()
