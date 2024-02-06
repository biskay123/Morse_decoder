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
from frontend.services.CommandConstants import CommandConstants
from frontend.services.ProtocolHandler import ProtocolHandler
from frontend.services.uart_communication import UARTCommunication


class TextWindow:
    def __init__(self, root, uart_communication):
        self.uart_communication = uart_communication
        self.root = root
        self.root.geometry(Constants.WINDOW_SIZE)

        self.uart_communication = uart_communication
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

        processor = ProtocolHandler()
        command = CommandConstants.PC_TO_STM_REQUEST_MAX_MESSAGE_SIZE

        checkMaxSize = processor.process_command(command, input1_value, self.uart_communication)
        if input1_value.length < checkMaxSize:
            command = CommandConstants.PC_TO_STM_ENCRYPT_REQUEST
            encodedMessage = processor.process_command(command, input1_value, self.uart_communication)
            self.second_frame.output.insert("0.0", switch_value + " " + encodedMessage)
        else:
            self.second_frame.output.insert("0.0", "Error, please try again")

    def show_second_frame(self):
        if self.check_uart_connection():
            self.first_frame.pack_forget()
            self.second_frame.pack(fill=tk.BOTH)
            self.current_frame = self.second_frame
        else:
            self.first_frame.error_label.pack(side=tk.TOP, pady=(20, 0))

    def check_uart_connection(self):
        processor = ProtocolHandler()
        command = CommandConstants.PC_TO_STM_REQUEST_STM_ID
        input_data = 0x00
        result = processor.process_command(command, input_data, self.uart_communication)
        # When you click on 'Connect' button, this method is invoked
        return result


if __name__ == "__main__":
    # Set your COM port and baud rate
    com_port = Constants.COM_PORT
    baud_rate = Constants.BAUD_RATE

    # Create an instance of UARTCommunication
    uart_communication = UARTCommunication(com_port, baud_rate)
    uart_communication.open_port()

    root = tk.Tk()
    app = TextWindow(root, uart_communication)
    root.mainloop()
