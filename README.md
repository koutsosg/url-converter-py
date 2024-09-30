# Documentation for Link Converter Script

## A Short Story Behind the Link Converter

In our bustling office, collaboration is key to our success. We have a dedicated server for all our files, but our team is divided into two worlds: the designers, who work on sleek Macs, and the marketing team, who rely on Windows machines.

This setup often led to confusion and frustration when sharing links to files stored on the server. The designers would send `smb://` links that the marketing team couldn't easily access, while the marketers would share Windows UNC paths that left the designers scratching their heads.

To bridge this gap and enhance our communication, I decided to create the Link Converter. This simple yet effective tool allows our team to convert links seamlessly between `smb://` and Windows UNC paths, making it easier for everyone to access and collaborate on shared files.

## Overview

The Link Converter is a Python script that allows users to convert links between two formats: `smb://` and Windows UNC paths (`\\Server\Share`). It features a simple graphical user interface (GUI) built with Tkinter. Users can paste a link into the application, and it will automatically convert the link to the desired format, opening the path in File Explorer or copying it to the clipboard as necessary.

### Features

- Convert `smb://` links to Windows UNC paths.
- Convert Windows UNC paths to `smb://` links with proper formatting.
- Open valid Windows paths in File Explorer.
- Copy converted `smb://` links to the clipboard for easy use.

## Requirements

- Python 3.6 or higher (can be run in a virtual environment)
- Packages: `pyperclip`, `tkinter`

## Installation Instructions

### Step 1: Install Python

To run this script, you must have Python installed. You can use a portable version of Python to avoid installing it system-wide.
//NEED CORRECTIONS

1. **Download Portable Python**:

   - Go to [Python.org](https://www.python.org/downloads/) and download the latest version of Python (you can find portable versions on sites like [WinPython](https://winpython.github.io/) or [Portable Python](http://portablepython.com/)).

2. **Extract the Files**:
   - Extract the downloaded files to a directory of your choice, e.g., `C:\PortablePython`.

### Step 2: Set Up the Virtual Environment

1. **Open Command Prompt**:

   - Press `Win + R`, type `cmd`, and hit `Enter`.

2. **Navigate to the Script Directory**:

   - Use the `cd` command to navigate to the directory where your `link_converter.py` script is located:
     ```bash
     cd path\to\your\script\directory
     ```

3. **Create a Virtual Environment**:

   - Run the following command to create a virtual environment in a folder called `venv`:
     ```bash
     C:\PortablePython\python.exe -m venv venv
     ```

4. **Activate the Virtual Environment**:
   - After the virtual environment is created, activate it with the following command:
     ```bash
     venv\Scripts\activate
     ```
   - You should see `(venv)` prefixed to your command prompt, indicating that the virtual environment is active.

### Step 3: Install Required Packages

1. **Install Packages Using `pip`**:
   - With the virtual environment active, install the required packages:
     ```bash
     pip install pyperclip
     ```

### Step 4: Run the Script

1. **Run the Link Converter Script**:

   - With the virtual environment still activated, run the script:
     ```bash
     python link_converter.py
     ```

2. **Using the Application**:
   - A GUI window will open where you can paste your links and convert them.

### Step 5: Deactivate the Virtual Environment

- Once you are done using the script, you can deactivate the virtual environment by running:
  ```bash
  deactivate
  ```

### Notes

- The virtual environment isolates the dependencies for this script, allowing it to run without affecting other Python installations on your computer.
- Make sure your network setup is correct to avoid any "Invalid path!" errors when testing links.

## Code Overview

Here is the main portion of the code for your reference:

```python
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
        windows_path = link.replace('smb://', '\\\\').replace('/', '\\').replace('_smb._tcp.local', '')
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
```
