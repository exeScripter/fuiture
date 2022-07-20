# Make an application that has a button which downloads a file from the url
# and opens it in the code editor.

# import the necessary modules
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import *
from tkinter import scrolledtext
import os
import requests
import time
import webbrowser


# define the download_fuiture_css function
def download_fuiture_css():
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
    # the fuiture.css file existing and check if it is up to date
    else:
        # print a message about the fuiture.css file existing
        print("fuiture.css file found!")
        print("------------------------------------------------------")
        print("Checking if fuiture.css is up to date...")
        time.sleep(1.5)
        print("------------------------------------------------------")
        # set the url for the checker
        url = 'https://raw.githubusercontent.com/exeScripter/fuiture/main/fuiture.css'
        # Check if the fuiture.css file is up to date
        r = requests.get(url)
        with open("fuiture.css", "wb") as f:
            f.write(r.content)
            print("------------------------------------------------------")
            print("Up to date!")
            print("------------------------------------------------------")
            # open the downloaded file in the VSC code editor
            webbrowser.open("fuiture.css")
            print('Opening fuiture.css in your code editor...')
            time.sleep(1.5)
            print("------------------------------------------------------")

# create a window
root = tk.Tk()
root.title("Fuiture Downloader")
root.geometry("500x200")
root.resizable(False, False)

# create a label
label = ttk.Label(root, text="Welcome to Fuiture Downloader!")
label.pack()

# create a label
label = ttk.Label(root, text="Made by: @exeScripter")
label.pack()

# create a label
label = ttk.Label(root, text="github.com/exeScripter/fuiture")
label.pack()

# create a label
label = ttk.Label(root, text="")
label.pack()


# create a label
label = ttk.Label(root, text="This application will download the current version of the fuiture.css library from github.")
label.pack()

# create a button and style it
button = ttk.Button(root, text="Download fuiture.css", command=download_fuiture_css)
button.pack()





# code to run the application
root.mainloop()




