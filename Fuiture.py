# 
#   Fuiture Downloader
#   Made by @bedwarsmurf
#   2020-2022
#


import requests
import time
import os
import datetime
import webbrowser
# ASCII
import pyfiglet

# Print the text in ASCII
print(pyfiglet.figlet_format("Fuiture Lib", font="slant"))

# Print the welcome message
print("------------------------------------------------------")
print("Welcome to Fuiture Downloader!")
print("Made by: @bedwarsmurf")
print("github.com/exeScripter/fuiture")
print("------------------------------------------------------")

# set the url for the checker
url = 'https://raw.githubusercontent.com/exeScripter/fuiture/main/fuiture.css'

# if the fuiture.css file does not exist, print a message about
# the fuiture.css file not existing and download it from github

if not os.path.exists("fuiture.css"):
    print("fuiture.css file not found!")
    print("------------------------------------------------------")
    print("Downloading fuiture.css...")
    time.sleep(1.5)
    print("------------------------------------------------------")
    print("Fetching fuiture.css...")
    time.sleep(1.5)
    print("Trying to obtain connection with the server")
    time.sleep(1.5)
    print("------------------------------------------------------")
    r = requests.get(url)
    with open("fuiture.css", "wb") as f:
        f.write(r.content)
        print("------------------------------------------------------")
        print("Download complete!")
        print("------------------------------------------------------")
        # open the downloaded file in the VSC code editor
        webbrowser.open("fuiture.css")
        print('Opening fuiture.css in your code editor...')
        time.sleep(1.5)
        print("------------------------------------------------------")

# if the fuiture.css file does exist, print a message about
# the fuiture.css file existing and download it from github
else:
    print("fuiture.css file found!")
    print("------------------------------------------------------")
    print("Downloading fuiture.css...")
    time.sleep(1.5)
    print("------------------------------------------------------")
    print("Fetching fuiture.css...")
    time.sleep(1.5)
    print("Trying to obtain connection with the server")
    time.sleep(1.5)
    print("Connection achieved! Downloading fuiture.css...")
    time.sleep(1.5)
    print("------------------------------------------------------")
    r = requests.get(url)
    with open("fuiture.css", "wb") as f:
        f.write(r.content)
        print("------------------------------------------------------")
        print("Download complete!")
        print("------------------------------------------------------")
        # open the downloaded file in the VSC code editor
        webbrowser.open("fuiture.css")
        print('Opening fuiture.css in your code editor...')
        time.sleep(1.5)
        print("------------------------------------------------------")
