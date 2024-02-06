"""
Constants for Molo Application. Developed by Artem Komarov

These constants define various properties and styles used throughout the Molo application.

Attributes:
    BORDER_COLOR (str): Color code for window border.
    WINDOW_TITLE (str): Title of the main application window.
    WINDOW_SIZE (str): Initial size of the main application window.

    TITLE_FONT (tuple): Font settings for main titles.
    SUB_TITLE_FONT (tuple): Font settings for subtitles.
    ERROR_FONT (tuple): Font settings for error messages.
    MAIN_BUTTON_FONT (tuple): Font settings for main buttons.

    HEADER_FONT (tuple): Font settings for headers.
    VERSION_FONT (tuple): Font settings for version information.

    LABEL_FONT (tuple): Font settings for labels.
    INPUT_FONT (tuple): Font settings for input fields.
    BUTTON_FONT (tuple): Font settings for buttons.

    ERROR_COLOR (str): Color code for error messages.
    BLACK_COLOR (str): Color code for black.
    WHITE_COLOR (str): Color code for white.
    BUTTON_HOVER_TEXT_COLOR (str): Color code for button hover text.
    ACTIVE_BUTTON_COLOR (str): Color code for active buttons.
    DISABLED_BUTTON_COLOR (str): Color code for disabled buttons.
    FOCUS_COLOR (str): Color code for focus.
    SUB_TEXT_COLOR (str): Color code for subtext.
    BG_COLOR (str): Background color.

    TEXT_BOX_WIDTH (int): Width of text boxes.
    TEXT_BOX_HEIGHT (int): Height of text boxes.
    TEXT_BOX_CORNER_RADIUS (int): Corner radius of text boxes.
    TEXT_BOX_BORDER_WIDTH (int): Border width of text boxes.
    TEXT_BOX_BORDER_SPACING (int): Border spacing of text boxes.
    VERSION (str): Version information.

"""


class Constants:
    BORDER_COLOR = "#E7E7E7"
    WINDOW_TITLE = "Molo"
    WINDOW_SIZE = "1100x800"

    TITLE_FONT = ("Inter", 58, "bold")
    SUB_TITLE_FONT = ("Inter", 20, "normal")
    ERROR_FONT = ("Inter", 16, "normal")
    MAIN_BUTTON_FONT = ("Inter", 16, "bold")

    HEADER_FONT = ("Inter", 24, "bold")
    VERSION_FONT = ("Inter", 12, "normal")

    LABEL_FONT = ("Inter", 18, "bold")
    INPUT_FONT = ("Inter", 16, "normal")
    BUTTON_FONT = ("Inter", 14, "bold")

    ERROR_COLOR = "#FF9494"
    BLACK_COLOR = "#1C1C1C"
    WHITE_COLOR = "#FFF"
    BUTTON_HOVER_TEXT_COLOR = "#E3E3E3"
    ACTIVE_BUTTON_COLOR = "#FFFFFF"
    DISABLED_BUTTON_COLOR = "#C0C0C0"
    FOCUS_COLOR = "#323232"
    SUB_TEXT_COLOR = "#979797"
    BG_COLOR = "#EBEAEA"

    COM_PORT = 'COM4'
    BAUD_RATE = 9600

    TEXT_BOX_WIDTH = 550
    TEXT_BOX_HEIGHT = 200
    TEXT_BOX_CORNER_RADIUS = 10
    TEXT_BOX_BORDER_WIDTH = 5
    TEXT_BOX_BORDER_SPACING = 17
    VERSION = "Teraina 1.0"
