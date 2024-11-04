import platform
import sys
#
import tkinter as tk
from tkinter import *
#
from settings import Settings

settings = Settings(6.0 / 10)


def center_window(window):
    """Center the Tkinter window in the middle of the screen using scale factor."""
    window.update_idletasks()
    # print(f'{window.winfo_width()=}, {window.winfo_height()=}')
    # print(f'{window.winfo_screenwidth()=}, {window.winfo_screenheight()=}')
    width = settings.scaled_width
    height = settings.scaled_height

    screen_width = settings.device_width
    screen_height = settings.device_height
    print(f'{screen_width=}, {screen_height=}')

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window_geometry = f'{width}x{height}+{x}+{y}'
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

    root = tk.Tk()
    title = f'Example using Tkinter {get_tkinter_version()} and python {get_python_version()}'
    root.title(title)
    center_window(root)

    # place a label on the root window
    message = tk.Label(root, text = 'Hello, World!')
    message.pack()

    # display the window until closed by the user
    root.mainloop()


if __name__ == '__main__':
    main()
