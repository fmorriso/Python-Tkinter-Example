import platform
import sys
#
import tkinter as tk
from tkinter import *
# from ctypes import windll
#

def center_window(window, pct: float):
    """Center the Tkinter window in the middle of the screen using scale factor."""
    window.update_idletasks()

    device_width = window.winfo_screenwidth()
    scaled_width = int(window.winfo_screenwidth() * pct / 100) * 100

    device_height = window.winfo_screenheight()
    scaled_height = int(window.winfo_screenheight() * pct / 100) * 100

    x = (device_width - scaled_width) // 2
    y = (device_height - scaled_height) // 2
    window_geometry = f'{scaled_width}x{scaled_height}+{x}+{y}'
    print(f'{window_geometry=}')
    window.geometry(window_geometry)



def get_python_version() -> str:
    return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'


def get_tkinter_version() -> str:
    return f'{tk.TkVersion}'


def main():
    msg = f'Python version: {get_python_version()} on {platform.system()} {platform.release()}'
    print(msg)

    msg = f'Tkinter version: {get_tkinter_version()}'
    print(msg)

    # windll.shcore.SetProcessDpiAwareness(1)

    root = tk.Tk()
    title = f'Example using Tkinter {get_tkinter_version()} and python {get_python_version()}'
    root.title(title)
    center_window(root, 72./100)
    root.resizable(False, False)

    # place a label on the root window
    message = tk.Label(root, text = 'Hello, World!')
    message.pack()

    # display the window until closed by the user
    root.mainloop()


if __name__ == '__main__':
    main()
