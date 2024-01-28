"""
SecondFrame Class. Developed by Artem Komarov

This class represents the second frame of the Molo application, which contains input and output textboxes, a segmented button, and a submit button.

Imports:
    - tkinter (as tk): Used for creating the GUI components.
    - customtkinter: Custom module providing additional tkinter components.
    - Constants: Constants module providing styling and configuration settings.

Attributes:
    parent: Parent widget containing the frame.
    submit_data: Callback function for submitting data.
    background_photo: Image used as the background for the frame.

Methods:
    __init__(): Initializes the SecondFrame instance, creates GUI components, and sets their properties.

Widgets:
    - background_label (tk.Label): Label widget displaying the background image.
    - logo_label (tk.Label): Label widget displaying the application logo/header.
    - input_label (tk.Label): Label widget displaying the input label.
    - input (customtkinter.CTkTextbox): Custom textbox widget for input.
    - output_label (tk.Label): Label widget displaying the output label.
    - output (customtkinter.CTkTextbox): Custom textbox widget for output.
    - segmented_button (customtkinter.CTkSegmentedButton): Custom segmented button widget for encoding/decoding.
    - submit_button (customtkinter.CTkButton): Custom button widget for submitting data.
    - button_frame (tk.Frame): Frame to hold the segmented button and submit button.
    - dev_text (tk.Label): Label widget displaying developer information and version.

"""

import tkinter as tk

import customtkinter
from Constants import Constants


class SecondFrame(tk.Frame):
    def __init__(self, parent, submit_data, background_photo):
        super().__init__(parent)

        # Background image
        self.background_label = tk.Label(self, image=background_photo)
        self.background_label.image = background_photo
        self.background_label.place(relwidth=1, relheight=1)

        # Header
        logo_label = tk.Label(self, text="Molo", font=Constants.HEADER_FONT, fg=Constants.BLACK_COLOR,
                              bg=Constants.BG_COLOR)
        logo_label.pack(side=tk.TOP, pady=(20, 0))

        input_label = tk.Label(self, text="Input", font=Constants.LABEL_FONT, fg=Constants.BLACK_COLOR,
                               bg=Constants.BG_COLOR)
        input_label.pack(side=tk.TOP, pady=(80, 0))

        # Input
        self.input = customtkinter.CTkTextbox(master=self, width=Constants.TEXT_BOX_WIDTH,
                                              height=Constants.TEXT_BOX_HEIGHT,
                                              corner_radius=Constants.TEXT_BOX_CORNER_RADIUS,
                                              font=Constants.INPUT_FONT, bg_color=Constants.BG_COLOR,
                                              fg_color=Constants.WHITE_COLOR, text_color=Constants.BLACK_COLOR,
                                              border_width=Constants.TEXT_BOX_BORDER_WIDTH,
                                              border_color=Constants.BORDER_COLOR,
                                              border_spacing=Constants.TEXT_BOX_BORDER_SPACING)
        self.input.pack(side=tk.TOP, pady=(0, 0))

        output_label = tk.Label(self, text="Output", font=Constants.LABEL_FONT, fg=Constants.BLACK_COLOR,
                                bg=Constants.BG_COLOR)

        output_label.pack(side=tk.TOP, pady=(10, 0))
        self.output = customtkinter.CTkTextbox(master=self, width=Constants.TEXT_BOX_WIDTH,
                                               height=Constants.TEXT_BOX_HEIGHT,
                                               corner_radius=Constants.TEXT_BOX_CORNER_RADIUS,
                                               font=Constants.INPUT_FONT, bg_color=Constants.BG_COLOR,
                                               fg_color=Constants.WHITE_COLOR, text_color=Constants.BLACK_COLOR,
                                               border_width=Constants.TEXT_BOX_BORDER_WIDTH,
                                               border_color=Constants.BORDER_COLOR,
                                               border_spacing=Constants.TEXT_BOX_BORDER_SPACING)
        # self.output.insert("0.0", "")  # insert at line 0 character 0
        # self.output.configure(state="disabled")  # configure textbox to be read-only
        self.output.pack(side=tk.TOP, pady=(0, 0))

        # Create a frame to hold the buttons
        button_frame = tk.Frame(self)

        # Unfortunately, we cannot configure width of the values in buttons, in order to have a margin between,
        # we need to implement hard-coded spaces, these spaces are removed in submit_data() method,
        self.segmented_button_var = customtkinter.StringVar(value="     Encode     ")
        self.segmented_button = customtkinter.CTkSegmentedButton(master=button_frame,
                                                                 values=["     Encode     ", "     Decode     "],
                                                                 variable=self.segmented_button_var,
                                                                 font=Constants.BUTTON_FONT,
                                                                 corner_radius=4,
                                                                 border_width=1, width=0, height=40,
                                                                 selected_color="#DBEEFF",
                                                                 selected_hover_color="#E8F4FF",
                                                                 unselected_color=Constants.WHITE_COLOR,
                                                                 unselected_hover_color="#E8F4FF",
                                                                 text_color_disabled="red",
                                                                 fg_color=Constants.BLACK_COLOR,
                                                                 text_color=Constants.BLACK_COLOR)

        self.segmented_button.pack(side=tk.LEFT, pady=(0, 0))

        submit_button = customtkinter.CTkButton(master=button_frame, text="Submit", command=submit_data,
                                                corner_radius=5, bg_color=Constants.BG_COLOR,
                                                fg_color=Constants.BLACK_COLOR, text_color=Constants.WHITE_COLOR,
                                                font=Constants.BUTTON_FONT, border_width=1,
                                                border_color=Constants.BORDER_COLOR,
                                                hover_color=Constants.FOCUS_COLOR,
                                                height=40, width=130)
        submit_button.pack(side=tk.RIGHT, padx=(15, 0))

        # Pack the button frame with anchor set to center
        button_frame.pack(anchor='w', padx=(280, 0))
        button_frame.pack(anchor='w', pady=(15, 0))
        button_frame.configure(bg=Constants.BG_COLOR)

        # Dev label
        dev_text = tk.Label(self, text=Constants.VERSION, font=Constants.VERSION_FONT,
                            fg=Constants.SUB_TEXT_COLOR, bg=Constants.BG_COLOR)
        dev_text.pack(side=tk.BOTTOM, pady=(120, 7))
