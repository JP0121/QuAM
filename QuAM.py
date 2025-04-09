import os
import subprocess
import tkinter as tk
from tkinter import messagebox

def open_win_dir_stat():
    try:
        # Specify the path to WinDirStat.exe
        win_dir_stat_path = r"C:\Program Files (x86)\WinDirStat\WinDirStat.exe"

        # Check if the file exists
        if os.path.exists(win_dir_stat_path):
            subprocess.run(win_dir_stat_path, shell=True)
        else:
            # Prompt user to download WinDirStat
            response = messagebox.askquestion("WinDirStat Not Found", "WinDirStat is not installed. Do you want to download it?")
            if response == 'yes':
                # Open the download link in the default web browser
                download_link = "https://drive.google.com/file/d/1em_wn2WJzqjaTdMjH8L50Ipk0XfgnB7A/view?usp=sharing"
                subprocess.run(['start', 'cmd', '/c', 'start', '', download_link], shell=True)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def open_disk_management():
    try:
        subprocess.run("diskmgmt.msc", shell=True)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def open_apps_folder():
    try:
        subprocess.run("explorer shell:AppsFolder", shell=True)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def open_ctt():
    try:
        powershell_command = 'irm "https://christitus.com/win" | iex'
        subprocess.run(['powershell', '-Command', powershell_command], shell=True)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")




# Create the main window
window = tk.Tk()
window.title("QuAM - Quick Access Menu")

# Set the initial size of the window
window.geometry("400x200")

# Configure window style and color with a dark blue to purple gradient
window.configure(bg='#141439')

# Create custom font for buttons
button_font = ("Arial", 12, "bold")

# Create buttons to open WinDirStat, Disk Management, and Apps Folder
button_win_dir_stat = tk.Button(window, text="Open WinDirStat", command=open_win_dir_stat, bg='#4E4CB8', fg='white', font=button_font, bd=2)
button_disk_management = tk.Button(window, text="Open Disk Management", command=open_disk_management, bg='#3E3C8C', fg='white', font=button_font, bd=2)
button_apps_folder = tk.Button(window, text="Open Apps Folder", command=open_apps_folder, bg='#2D2B5B', fg='white', font=button_font, bd=2)
button_ctt = tk.Button(window, text="Open Chris Titus Windows Tool", command=open_ctt, bg='#2D2B5B', fg='white', font=button_font, bd=2)


# Pack buttons
button_win_dir_stat.pack(pady=10)
button_disk_management.pack(pady=10)
button_apps_folder.pack(pady=10)
button_ctt.pack(pady=10)


# Run the main loop
window.mainloop()
