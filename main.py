import platform
import sys
#
import tkinter as tk
from tkinter import ttk

from gui_scaling import GuiScaling


#

def center_window(window: tk.Tk, scaling: GuiScaling) -> str:
    window.update_idletasks()
    x = int((scaling.device_width - scaling.scaled_width)) // 2
    y = int((scaling.device_height - scaling.scaled_height)) // 2

    window_geometry = f'{scaling.scaled_width}x{scaling.scaled_height}+{x}+{y}'
    # print(f'{window_geometry=}')
    window.geometry(window_geometry)
    return window_geometry


def scale_and_center_window(window: tk.Tk, pct: float = 0.75, multiple_of: int = 100) -> None:
    """
    Scale and center the Tkinter window in the middle of the screen using the specified percentage of the device screen,
    rounded to the specified multiple of value.
    :param window: The Tkinter window to size and center.
    :param pct: Percentage of the available device width and height to use (between 0 and 1).
    :param multiple_of: The multiple of value that the scaled window should be rounded to.
    """
    window.update_idletasks()

    device_width = window.winfo_screenwidth()
    scaled_width = int(device_width * pct / multiple_of) * multiple_of

    device_height = window.winfo_screenheight()
    scaled_height = int(device_height * pct / multiple_of) * multiple_of

    x = int((device_width - scaled_width)) // 2
    y = int((device_height - scaled_height)) // 2

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

    root = tk.Tk()
    # print(f'{type(root)=}')
    title = f'Example using Tkinter {get_tkinter_version()} and python {get_python_version()}'
    root.title(title)

    scaling = GuiScaling(pct=0.67, square=False, multiple_of = 32)
    print(f'{scaling=}')
    center_window(root, scaling)
    root.resizable(False, False)

    # use a different icon instead of the default
    root.iconbitmap('./assets/pygame.ico')

    # scale font 
    font_size = int(scaling.scaled_width * 0.02)
    label_font = ('Courier New', font_size)
    print(f'{label_font=}')

    # place a label on the root window
    tk.Label(root, text = 'Hello, World!', font=label_font).pack()

    tk.Label(root, text = 'Classic Label', font=label_font).pack()
    ttk.Label(root, text = 'Themed Label', font=label_font).pack()

    root.mainloop()

    # display the window until closed by the user
    root.mainloop()


if __name__ == '__main__':
    main()
