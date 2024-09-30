import os
import tkinter as tk
from tkinter import messagebox
import subprocess
import pyperclip

def convert_link():
    link = input_entry.get().strip()  # Get the input and strip whitespace
    print(f"Input link: {link}")  # Debug: print input link

    if link.startswith('smb://'):
        # Convert smb:// to Windows path and remove _smb._tcp.local
        windows_path = link.replace('smb://', '\\\\').replace('/', '\\').replace('._smb._tcp.local', '')
        print(f"Converted to Windows path: {windows_path}")  # Debug: print converted path
        if os.path.exists(windows_path):
            subprocess.Popen(f'explorer "{windows_path}"')
            messagebox.showinfo("Link Converter", f"Opening: {windows_path}")
        else:
            messagebox.showwarning("Link Converter", "Invalid path!")
    elif link.startswith('\\\\'):
        # Convert Windows path to smb:// and add ._smb._tcp.local if necessary
        smb_path = link.replace('\\\\', 'smb://').replace('\\', '/')
        
        # Add _smb._tcp.local to the server part of the path
        smb_path_parts = smb_path.split('/')
        if len(smb_path_parts) > 0 and not smb_path_parts[2].endswith('._smb._tcp.local'):
            smb_path_parts[2] += '._smb._tcp.local'
        
        smb_path = '/'.join(smb_path_parts)
        
        pyperclip.copy(smb_path)
        messagebox.showinfo("Link Converter", f"Copied to clipboard: {smb_path}")
    else:
        messagebox.showerror("Link Converter", "Invalid link format!")

# Create the Tkinter app window
app = tk.Tk()
app.title('Link Converter')

# Input field
input_label = tk.Label(app, text="Paste your link here:")
input_label.pack(padx=10, pady=10)

input_entry = tk.Entry(app, width=50)
input_entry.pack(padx=10, pady=10)

# Convert button
convert_button = tk.Button(app, text="Convert Link", command=convert_link)
convert_button.pack(padx=10, pady=10)

# Start the Tkinter loop
app.mainloop()
