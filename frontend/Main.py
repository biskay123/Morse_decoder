"""
TextWindow GUI Application. Developed by Artem Komarov

This script implements a graphical user interface (GUI) application using Tkinter, a Python GUI toolkit, and PIL (Python Imaging Library) for image processing. The application consists of multiple frames managed by a main window. It allows users to interact with various widgets and perform actions like submitting data and switching frames.

Imports:
    - tkinter (as tk): Used for creating the GUI application.
    - PIL.Image, PIL.ImageTk: Used for image loading and manipulation.
    - Constants: Imports constants used in the application.
    - FirstFrame, SecondFrame: Import custom frame classes for organizing the GUI components.

Classes:
    - TextWindow: Represents the main application window. It initializes the GUI, manages frame switching, and handles user interactions.

Methods:
    - __init__(): Initializes the TextWindow instance, sets up the main window, loads images, and initializes frames.
    - submit_data(): Handles data submission action, retrieves input values, and displays the output.
    - show_second_frame(): Manages frame switching from the first frame to the second frame based on conditions.
    - check_uart_connection(): Checks UART connection status (placeholder method).

Usage:
    The script creates an instance of the TextWindow class, sets up the main Tkinter window, and starts the event loop to handle user interactions.

"""

import tkinter as tk

from PIL import Image, ImageTk

from Constants import Constants
from frames.FirstFrame import FirstFrame
from frames.SecondFrame import SecondFrame


class TextWindow:
    def __init__(self, root):
        self.root = root
        self.root.geometry(Constants.WINDOW_SIZE)

        # Load the image file
        image = Image.open("resources/background.png")
        background_photo = ImageTk.PhotoImage(image)

        self.root.title(Constants.WINDOW_TITLE)
        self.root.resizable(width=False, height=False)

        self.first_frame = FirstFrame(self.root, self.show_second_frame, background_photo)
        self.second_frame = SecondFrame(self.root, self.submit_data, background_photo)
        self.current_frame = self.first_frame

        self.first_frame.pack(expand=True, fill=tk.BOTH)

    def submit_data(self):
        self.second_frame.output.delete("0.0", "end-1c")  # delete the text from previous output

        input1_value = self.second_frame.input.get("1.0", "end-1c")  # String input
        switch_value = self.second_frame.segmented_button_var.get().strip()  # 'Encode' or 'Decode' values

        self.second_frame.output.insert("0.0", switch_value + " " + input1_value)

    def show_second_frame(self):
        if self.check_uart_connection():
            self.first_frame.pack_forget()
            self.second_frame.pack(fill=tk.BOTH)
            self.current_frame = self.second_frame
        else:
            self.first_frame.error_label.pack(side=tk.TOP, pady=(20, 0))

    def check_uart_connection(self):
        # When you click on 'Connect' button, this method is invoked
        return True  # Replace with actual logic


if __name__ == "__main__":
    root = tk.Tk()
    app = TextWindow(root)
    root.mainloop()
