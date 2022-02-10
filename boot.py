import machine
import gc
import wifista
import senko


def main():
    """Main function. Runs after board boot, before main.py
    Connects to Wi-Fi and checks for latest OTA version.
    """

    gc.collect()
    gc.enable()

    wifista.connect()


    GITHUB_URL = "https://github.com/smartcomputerlab/OTA/"
    OTA = senko.Senko(url=GITHUB_URL, files=["boot.py", "main.py"])

    if OTA.update():
        print("Updated to the latest version! Rebooting...")
        machine.reset()


if __name__ == "__main__":
    main()

