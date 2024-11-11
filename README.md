# Python Tkinter Example
A simple Python program that roughly follows the Tkinter Tutorial with some
modifications for window scaling using PyAutoGUI.

## Tools Used

| Tool       |  Version |
|:-----------|---------:|
| Python     |   3.13.0 |
| Tkinter    |      8.6 |
| VSCode     |   1.95.2 |
| PyCharm    | 2024.2.4 |

## References

* [Tkinter Tutorial](https://www.pythontutorial.net/tkinter/)
* [PyAutoGUI Documentation](https://pyautogui.readthedocs.io/en/latest/)

## Change History

| Date       | Description                                                                                |
|:-----------|:-------------------------------------------------------------------------------------------|
| 2024-11-04 | Initial creation                                                                           |
| 2024-11-09 | Begin removing PyAutoGUI dependency                                                        |
| 2024-11-11 | Use ctypes.windll.user32 instead of Tkinter to get accurate device screen size information |
