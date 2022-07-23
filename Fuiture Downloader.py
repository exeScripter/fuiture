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
import time

# Create a function to download the library
# This function will be called when the user clicks on the button
def download_fuiture():
    print("Fuiture Downloader Logs - " + time.strftime("%d/%m/%Y"))
    print("----------------------------------------------------")
    print("[+] User clicked on the button")
    # Sleep for 1 second
    time.sleep(1)
    print("[+] Creating directory ...")
    time.sleep(1)
    print("[+] Directory Created!")
    # Download the library from the url, save it to a file called "fuiture.css"
    # and create a directory called "fuiture"

    # Create a directory called "fuiture"
    if not os.path.exists("fuiture"):
        # Print the current time in seconds, and the message "Creating directory...""
        # Create the directory
        os.makedirs("fuiture")

    if os.path.exists("fuiture"):
        time.sleep(1)
        print("[=] Directory exists, asking user if he/she wants to overwrite the files ...")
        # Ask the user if he/she wants to overwrite the library
        overwrite = messagebox.askyesno("Overwrite", "Do you want to overwrite the library?")
        if overwrite:
            # Display the options that user choosed
            print("[=] User choosed:", overwrite)
            # Download the library
            response = requests.get("https://raw.githubusercontent.com/exeScripter/fuiture/master/fuiture.css")
            # Save the library to a file called "fuiture.css"
            with open("fuiture/fuiture.css", "w") as f:
                f.write(response.text)
        else:
            print("[-] Error has occured, please try again!")
            time.sleep(1)
            # Display a messagebox to tell the user that the library has not been downloaded
            messagebox.showinfo("Download Info", "The library has not been downloaded")
            # Exit the program
            exit()

    else:
        # Download the library
        response = requests.get("https://raw.githubusercontent.com/exeScripter/fuiture/master/fuiture.css")
        # Save the library to a file called "fuiture.css"
        with open("fuiture/fuiture.css", "w") as j:
            j.write(response.text)
        print("[+] Library downloaded!")
        time.sleep(1)
        # Display a messagebox to tell the user that the library has been downloaded
        messagebox.showinfo("Download Info", "The library has been downloaded")


    # Download the library from the url, save it to a file called "fuiture.css"
    # and create a directory called "fuiture"
    url = "https://raw.githubusercontent.com/exeScripter/fuiture/master/fuiture.css"
    g = requests.get(url)
    with open("fuiture/fuiture.css", "wb") as j:
        # If the fuiture_v2.css file exists, delete it
        if os.path.exists("fuiture/fuiture_v2.css"):
            os.remove("fuiture/fuiture_v2.css")
            
        j.write(g.content)
        g.version = "2.1.5"
        print("[+] Library downloaded!")
        time.sleep(1)
        # Print a message to the user
        messagebox.showinfo("Downloaded", "The library has been downloaded")
        print("--------------------------------------------------------------------------------------------------------------------")
        print("The library has been downloaded successfully")
        print("You can find it in the directory called ''fuiture''")
        print("The downloaded version is: " + g.version + "")

        print("--------------------------------------------------------------------------------------------------------------------")
        print("You can now safely close this window")
        print("--------------------------------------------------------------------------------------------------------------------")

def download_fuiturev2():
    print("Fuiture Downloader Logs - " + time.strftime("%d/%m/%Y"))
    print("----------------------------------------------------")
    print("[+] User clicked on the button")
    # Sleep for 1 second
    time.sleep(1)
    print("[+] Creating directory ...")
    time.sleep(1)
    print("[+] Directory Created!")
    # Download the library from the url, save it to a file called "fuiture.css"
    # and create a directory called "fuiture"

    # Create a directory called "fuiture"
    if not os.path.exists("fuiture"):
        # Print the current time in seconds, and the message "Creating directory...""
        # Create the directory
        os.makedirs("fuiture")

    if os.path.exists("fuiture"):
        time.sleep(1)
        print("[=] Directory exists, asking user if he/she wants to overwrite the files ...")
        # Ask the user if he/she wants to overwrite the library
        overwrite = messagebox.askyesno("Overwrite", "Do you want to overwrite the library?")
        if overwrite:
            # Display the options that user choosed
            print("[=] User choosed:", overwrite)
            # Download the library
            response = requests.get("https://raw.githubusercontent.com/exeScripter/fuiture/main/fuiturev2/fuiture_v2.css")
            # Save the library to a file called "fuiture.css"
            with open("fuiture/fuiture_beta.css", "w") as f:
                f.write(response.text)
            # If the fuiture.css file exists then delete it
            if os.path.exists("fuiture/fuiture.css"):
                os.remove("fuiture/fuiture.css")

        else:
            print("[-] Error has occured, please try again!")
            time.sleep(1)
            # Display a messagebox to tell the user that the library has not been downloaded
            messagebox.showinfo("Download Info", "The library has not been downloaded")
            # Exit the program
            exit()

    else:
        # Download the library
        response = requests.get("https://raw.githubusercontent.com/exeScripter/fuiture/main/fuiturev2/fuiture_v2.css")

    # Download the library from the url, save it to a file called "fuiture.css"
    # and create a directory called "fuiture"
    url = "https://raw.githubusercontent.com/exeScripter/fuiture/main/fuiturev2/fuiture_v2.css"
    r = requests.get(url)
    with open("fuiture/fuiture.css", "wb") as f:
        f.write(r.content)
        r.version = "1.2b"
        print("[+] Library downloaded!")
        time.sleep(1)
        # Print a message to the user
        messagebox.showinfo("Downloaded", "The library has been downloaded")
        print("--------------------------------------------------------------------------------------------------------------------")
        print("The BETA library has been downloaded successfully")
        print("You can find it in the directory called ''fuiture''")
        print("The downloaded version is: " + r.version + "")

        print("--------------------------------------------------------------------------------------------------------------------")
        print("You can now safely close this window")
        print("--------------------------------------------------------------------------------------------------------------------")



# Use the tkinter library to create a window
root = tk.Tk()
root.title("Fuiture Downloader")
root.geometry("450x350")
root.resizable(False, False)

# Create a label to display the message
label = tk.Label(root, text="Fuiture Downloader", font=("Helvetica", 20))
label.pack()

# Create a label for the window
label = tk.Label(root, text="Click on the button below to download the latest version", font=("Helvetica", 10))
label.pack()

# Create a button for then download the library
button = tk.Button(root, text="Download", command=download_fuiture)
button.pack()

# Create a button for then download the library
button = tk.Button(root, text="Download Beta Version", command=download_fuiturev2)
button.pack()

# Create a label for the window to show the version of the library
label = tk.Label(root, text="Version: 2.1.5", font=("Helvetica", 10))
label.pack()

# Create an text box to show the update logs
text = scrolledtext.ScrolledText(root, width=40, height=10)
text.pack()
text.insert(tk.END, "Fuiture Library Update Logs - " + time.strftime("%d/%m/%Y"))
text.insert(tk.END, "\n--------------------------")
text.insert(tk.END, "\n[+] Better data management")
text.insert(tk.END, "\n[+] Improved UI")
text.insert(tk.END, "\n[+] Added a new features")
text.insert(tk.END, "\n[+] Improved the performance")
text.insert(tk.END, "\n")
text.insert(tk.END, "\n[-] Deleted awkwardness")
text.insert(tk.END, "\n[-] Fixed a bug")
text.insert(tk.END, "\n--------------------------")
text.insert(tk.END, "\n[+] Released a Beta Version of Fuiture v2 avaible to download here")



# Create a label for the window to show the date of the library
label = tk.Label(root, text=time.strftime("%d/%m/%Y"), font=("Helvetica", 10))
label.pack()

# Create a label for the window to show the author of the library
label = tk.Label(root, text="Author: @exeScripter", font=("Helvetica", 10))
label.pack()


# Run the mainloop
root.mainloop()


