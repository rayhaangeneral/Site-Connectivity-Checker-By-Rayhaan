import tkinter as tk
import socket

def check_connectivity(url):
    try:
        # Get the host name
        host = socket.gethostbyname(url)
        # Check if the host is reachable
        socket.create_connection((host, 80), 2)
        return True
    except:
        return False

def check_site():
    # Get the website address
    website = entry.get()
    
    # Check the connectivity
    result = check_connectivity(website)
    
    # Display the result
    if result:
        result_label["text"] = "Success: The website is accessible."
        result_label["fg"] = "green"
    else:
        result_label["text"] = "Failure: The website is not accessible."
        result_label["fg"] = "red"
      
def toggle_dark_mode():
    current_bg = root.cget("bg")
    if current_bg == "white":
        root.config(bg="black")
        entry.config(fg="white", bg="black")
        result_label.config(fg="white", bg="black")
        check_button.config(fg="white", bg="black")
        dark_mode_button.config(text="Light mode")
    else:
        root.config(bg="white")
        entry.config(fg="black", bg="white")
        result_label.config(fg="black", bg="white")
        check_button.config(fg="black", bg="white")
        dark_mode_button.config(text="Dark mode")

# Create the main window
root = tk.Tk()
root.geometry("450x200")
root.title("Site Connectivity Checker By Rayhaan")
root.config(bg="white")

# Create a label for the website address
website_label = tk.Label(root, text="Website address:", bg="white", fg="black")
website_label.pack()

# Create an entry widget for the website address
entry = tk.Entry(root, bg="white", fg="black")
entry.pack()

# Create a button to check the site
check_button = tk.Button(root, text="Check site", command=check_site, bg="white", fg="black")
check_button.pack()

# Add the authors' names in the right bottom corner of the window
author_label = tk.Label(root, text="Authors: Rayhaan General", bg="black", fg="white", font=("Arial", 8))
author_label.pack(side="bottom", anchor="se")

# Create a label to display the result
result_label = tk.Label(root, text="", bg="white", fg="black")
result_label.pack()

# Create a button to toggle dark mode
dark_mode_button = tk.Button(root, text="Dark mode", command=toggle_dark_mode, bg="white", fg="black")
dark_mode_button.pack()

# Start the main loop
root.mainloop()
