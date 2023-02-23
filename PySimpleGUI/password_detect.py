import subprocess


def extract_wifi_passwords():
    profiles_data = subprocess.check_output("netsh wlan show profiles").decode('utf-8').split("\n")
    print(profiles_data)
extract_wifi_passwords()