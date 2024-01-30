"""
FirstFrame Class. Developed by Artem Komarov

This class represents the first frame of the Molo application, which contains introductory information and a connect button.

Imports:
    - tkinter (as tk): Used for creating the GUI components.
    - customtkinter: Custom module providing additional tkinter components.
    - Constants: Constants module providing styling and configuration settings.

Attributes:
    parent: Parent widget containing the frame.
    show_page2: Callback function to switch to the second frame.
    background_photo: Image used as the background for the frame.

Methods:
    __init__(): Initializes the FirstFrame instance, creates GUI components, and sets their properties.

Widgets:
    - background_label (tk.Label): Label widget displaying the background image.
    - main_text (tk.Label): Label widget displaying the main title text.
    - sub_text (tk.Label): Label widget displaying the subtitle text.
    - connect_button (customtkinter.CTkButton): Custom button widget for connecting.
    - error_label (tk.Label): Label widget displaying error messages.
    - dev_text (tk.Label): Label widget displaying developer information and version.

"""

import tkinter as tk

import customtkinter
from Constants import Constants


class FirstFrame(tk.Frame):
    def __init__(self, parent, show_page2, background_photo):
        super().__init__(parent)

        # Background image
        self.background_label = tk.Label(self, image=background_photo)
        self.background_label.image = background_photo
        self.background_label.place(relwidth=1, relheight=1)

        # Main text
        self.main_text = tk.Label(self, text="Hi, I’m Molo", font=Constants.TITLE_FONT, fg=Constants.BLACK_COLOR,
                                  bg=Constants.BG_COLOR)
        self.main_text.pack(side=tk.TOP, pady=(300, 0))

        # Sub text
        self.sub_text = tk.Label(self, text="The best morse encoder/decoder ever", font=Constants.SUB_TITLE_FONT,
                                 fg=Constants.SUB_TEXT_COLOR, bg=Constants.BG_COLOR)
        self.sub_text.pack(side=tk.TOP, pady=(0, 0))

        # Connect button
        self.connect_button = customtkinter.CTkButton(master=self, text="Connect", command=show_page2,
                                                      corner_radius=5, bg_color=Constants.BG_COLOR,
                                                      fg_color=Constants.BLACK_COLOR, text_color=Constants.WHITE_COLOR,
                                                      font=Constants.MAIN_BUTTON_FONT, border_width=1,
                                                      border_color=Constants.BORDER_COLOR,
                                                      hover_color=Constants.FOCUS_COLOR,
                                                      height=50, width=170)
        self.connect_button.pack(side=tk.TOP, pady=(20, 0))

        # Error label
        self.error_label = tk.Label(self, text="Board is not connected", font=Constants.ERROR_FONT,
                                    fg=Constants.ERROR_COLOR, bd=8, bg=Constants.BLACK_COLOR, relief="solid")
        self.error_label.pack_forget()

        # Dev label
        self.dev_text = tk.Label(self, text="Developed by Granatik \n" + Constants.VERSION,
                                 font=Constants.VERSION_FONT,
                                 fg=Constants.SUB_TEXT_COLOR, bg=Constants.BG_COLOR)
        self.dev_text.pack(side=tk.BOTTOM, pady=(0, 7))
