#import requests
import webbrowser as web

urls = ["https://www.blizzard.com/en-us/download/confirmation?platform=windows&locale=enUS&version=LIVE&id=ow",
                "https://discordapp.com/api/download?platform=win",
                "https://www.mozilla.org/en-US/firefox/download/thanks/",
                "https://steamcdn-a.akamaihd.net/client/installer/SteamSetup.exe",
                "https://atom.io/download/windows_x64"]

def DownloadFiles():
    
    for url in urls:
        print(url)
        web.open(url)

def Main():
    print("downloading...")
    DownloadFiles()

Main()
