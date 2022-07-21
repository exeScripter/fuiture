# Fuiture 
# Author: @exeScripter
# 2022-2023

# Import the necessary modules
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

# Create a function to download the library
# This function will be called when the user clicks on the button
def download_fuiture():
    # Download the library from the url, save it to a file called "fuiture.css"
    # and create a directory called "fuiture"

    # Create a directory called "fuiture"
    if not os.path.exists("fuiture"):
        os.makedirs("fuiture")

    if os.path.exists("fuiture"):
        # Ask the user if he/she wants to overwrite the library
        overwrite = messagebox.askyesno("Overwrite", "Do you want to overwrite the library?")
        if overwrite:
            # Download the library
            response = requests.get("https://raw.githubusercontent.com/exeScripter/fuiture/master/fuiture.css")
            # Save the library to a file called "fuiture.css"
            with open("fuiture/fuiture.css", "w") as f:
                f.write(response.text)
        else:
            # Display a messagebox to tell the user that the library has not been downloaded
            messagebox.showinfo("Downloaded", "The library has not been downloaded")
    else:
        # Download the library
        response = requests.get("https://raw.githubusercontent.com/exeScripter/fuiture/master/fuiture.css")
        # Save the library to a file called "fuiture.css"
        with open("fuiture/fuiture.css", "w") as f:
            f.write(response.text)
        # Display a messagebox to tell the user that the library has been downloaded
        messagebox.showinfo("Downloaded", "The library has been downloaded")


    # Download the library from the url, save it to a file called "fuiture.css"
    # and create a directory called "fuiture"
    url = "https://raw.githubusercontent.com/exeScripter/fuiture/master/fuiture.css"
    r = requests.get(url)
    with open("fuiture/fuiture.css", "wb") as f:
        f.write(r.content)
        r.version = "2.1.3"
        # Print a message to the user
        messagebox.showinfo("Downloaded", "The library has been downloaded")
        print("--------------------------------------------------------------------------------------------------------------------")
        print("The library has been downloaded successfully")
        print("You can find it in the directory called ''fuiture''")
        print("The downloaded version is: " + r.version + "")

        print("--------------------------------------------------------------------------------------------------------------------")
        print("You can now safely close this window")
        print("--------------------------------------------------------------------------------------------------------------------")
       






# Use the tkinter library to create a window
root = tk.Tk()
root.title("Fuiture Downloader")
root.geometry("350x200")
root.resizable(False, False)

# Create a label for the window
label = tk.Label(root, text="Fuiture Downloader", font=("Helvetica", 20))
label.pack()

# Create a label for the window
label = tk.Label(root, text="Click on the button below to download the latest version", font=("Helvetica", 10))
label.pack()

# Create a button for then download the library
button = tk.Button(root, text="Download", command=download_fuiture)
button.pack()


# Create a label for the window to show the version of the library
label = tk.Label(root, text="Version: 2.1.3", font=("Helvetica", 10))
label.pack()

# Create a label for the window to show the date of the library
label = tk.Label(root, text="2022-07-21", font=("Helvetica", 10))
label.pack()

# Create a label for the window to show the author of the library
label = tk.Label(root, text="Author: @exeScripter", font=("Helvetica", 10))
label.pack()

# Run the mainloop
root.mainloop()

