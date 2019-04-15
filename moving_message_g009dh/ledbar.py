import struct
from enum import Enum

import serial

# Sign modes
MODE_SIGN_ADDRESS = b'\x00'
MODE_FILE = b'\x01'
MODE_SPECIAL_FILE = b'\x02'
MODE_ALARMING = b'\x04'
MODE_TIME_ALARMING = b'\x05'
MODE_SIGN_ON = b'\x06'
MODE_SIGN_OFF = b'\x07'
MODE_TIME_RESET = b'\x08'
MODE_CUSTOM_GRAPHIC = b'\x09'
MODE_TESTING = b'\x0a'
MODE_SIGNS_LIST = b'\x0b'

MODIFIER_CODE = b'\xef'

MODE_00_SIGN_ADDRESS = b'\xff\xff'
MODE_00_CLEAR_PREVIOUS = b'\x01'
MODE_00_NOT_CLEAR_PREVIOUS = b'\x00'

MODE_01_NEWLINE = b'\xff'
MODE_01_CLOSE_FILE = b'\xff'

MODE_11_END_CODE = b'\xff'

END_CODE = b'\x00'


FADE_MODES = {
    'cyclic': b'\x01',
    'immediate': b'\x02',
    'open_right': b'\x03',
    'open_left': b'\x04',
    'open_from_center': b'\x05',
    'open_to_center': b'\x06',
    'cover_from_center': b'\x07',
    'cover_from_right': b'\x08',
    'cover_from_left': b'\x09',
    'cover_to_center': b'\x0a',
    'scroll_up': b'\x0b',
    'scroll_down': b'\x0c',
    'interlace_center': b'\x0d',
    'interlace_cover': b'\x0e',
    'cover_up': b'\x0f',
    'cover_down': b'\x10',
    'scan_line': b'\x11',
    'explode': b'\x12',
    'pacman': b'\x13',
    'fall_stack': b'\x14',
    'shoot': b'\x15',
    'flash': b'\x16',
    'random': b'\x17',
    'slide_in': b'\x18',
    'auto': b'\x19',
}

SPEEDS = {
    'speed_1': b'\xc0',
    'speed_2': b'\xc1',
    'speed_3': b'\xc2',
    'speed_4': b'\xc3',
    'speed_5': b'\xc4',
    'speed_6': b'\xc5',
    'speed_7': b'\xc6',
    'speed_8': b'\xc7',

    # Alternate names
    'default': b'\xc2',
}

COLORS = {
    'red': b'\xb0',
    'bright_red': b'\xb1',
    'orange': b'\xb2',
    'bright_orange': b'\xb3',
    'yellow': b'\xb4',
    'bright_yellow': b'\xb5',
    'green': b'\xb6',
    'bright_green': b'\xb7',
    'layer_mix_rainbow': b'\xb8',
    'bright_layer_mix_rainbow': b'\xb9',
    'vertical_mix': b'\xba',
    'sawtooth_mix': b'\xbb',
    'green_on_red': b'\xbc',
    'red_on_green': b'\xbd',
    'orange_on_red': b'\xbe',
    'yellow_on_green': b'\xbf',
}

FONTS = {
    'short': b'\xa0',
    'short_wide': b'\xa1',
    'default': b'\xa2',
    'wide': b'\xa3',
    'serif': b'\xa4',
    'extra_wide': b'\xa5',
    'small': b'\xa6',
}


class LEDBar:

    _data_buffer = b''

    def __init__(self, port='/dev/ttyUSB0'):
        self.serial = serial.Serial(port, 2400)
        self._data_buffer = b''

    def send_data(self):
        """
        Sends the current data buffer to the LED bar.
        """
        self.serial.write(self._data_buffer)
        self._data_buffer = b''

    def mode_00_sign_address(self, clear=True):
        """
        Add a Sign Address data group
        :param clear: Clear all the previous messages.
        :type clear: bool
        """
        # Start the sign address data group
        self._data_buffer += MODE_SIGN_ADDRESS
        # Then 0xFF 0xFF because the manual tells us to
        self._data_buffer += MODE_00_SIGN_ADDRESS
        # Then 1 if clear is set
        self._data_buffer += MODE_00_CLEAR_PREVIOUS if clear else MODE_00_NOT_CLEAR_PREVIOUS

    def mode_01_open_file(self, file_number):
        """
        Open a file data group
        :param file_number: The file number to open. Must be between 1 and 99
        :type file_number: int
        :return: The data
        """
        assert 0 < file_number < 100
        file_str = str("{:02}".format(file_number))

        # Start the file data group
        self._data_buffer += MODE_FILE
        # Add the file number, which are the ASCII codes for both numbers
        self._data_buffer += file_str.encode()

    def mode_01_fade_mode(self, fade_mode):
        """
        Add a fade mode part of a file data group.
        Can only be given once per line, at the start.
        :param fade_mode: The fade mode to use. Must be from enum FadeMode.
        :type fade_mode: FadeMode
        """
        assert fade_mode in FADE_MODES
        self._data_buffer += FADE_MODES[fade_mode]

    def mode_01_speed(self, speed):
        """
        Add a speed part of a file data group.
        Can only be given once per line, at the start.
        :param speed: The speed to use. Must be from enum Speed
        :type speed: Speed
        """
        assert speed in SPEEDS
        self._data_buffer += MODIFIER_CODE + SPEEDS[speed]

    def mode_01_color(self, color):
        """
        Add a color part of a file data group.
        Can be given anywhere in the line, changes the color until the next color mark (or until the end of the line)
        :param color: The color to use. Must be from enum Color
        :type color: Color
        """
        assert color in COLORS
        self._data_buffer += MODIFIER_CODE + COLORS[color]

    def mode_01_font(self, font):
        """
        Add a font part of a file data group.
        Can be given anywhere in the line, changes the font until the next font mark (or until the end of the line)
        :param font: The font to use. Must be from enum Font
        :type font: Font
        """
        assert font in FONTS
        self._data_buffer += MODIFIER_CODE + FONTS[font]

    def mode_01_text(self, text):
        """
        Add a text part to a file data group. Only ascii-characters
        Adds text to the current line. Can be done anywhere in a line.
        :param text: The text to add
        :type text: str
        """
        assert isinstance(text, str)
        assert all(0x00 < ord(x) < 0xFF for x in text)
        self._data_buffer += text.encode()

    def mode_01_newline(self):
        """
        Add a new line to a file data group.
        A file group also needs to end with a new line. (followed by a close file group marker)
        """
        self._data_buffer += MODE_01_NEWLINE

    def mode_01_close_file(self):
        """
        Close off a file data group
        """
        self._data_buffer += MODE_01_CLOSE_FILE

    def mode_11_signs_list(self, signs=None):
        """
        Add a signs list data group.
        :param signs: List of sign numbers that you want to address, or None. If None, all signs will be addressed.
        :type signs: list(int)
        """
        if signs is None:
            signs = list(range(0, 128))

        assert isinstance(signs, list)
        assert all(isinstance(x, int) for x in signs)
        assert all(0 <= x < 128 for x in signs)

        self._data_buffer += MODE_SIGNS_LIST
        for sign in signs:
            self._data_buffer += struct.pack('b', sign)

        self._data_buffer += MODE_11_END_CODE

    def data_end_code(self):
        """
        Adds the data end code. After this no more groups can be added and the data buffer should be sent to the sign.
        """
        self._data_buffer += END_CODE

    @staticmethod
    def check_data(data):
        """
        Check a dictionary of data for validity according to the specification.
        :param data: The data to check
        :return: A tuple of a boolean and a list. The boolean is True if the data is valid.
                  If it is not valid, the list will contain the reason(s) it is not valid.
        """
        errors = []
        if not isinstance(data, dict):
            errors.append("The data parameter must be a dictionary.")
            return False, errors

        if 'bars' in data:
            if not isinstance(data['bars'], list):
                errors.append("The value of the 'bars' key should be a list of integers if it is given.")
            elif not all(isinstance(x, int) for x in data['bars']):
                errors.append("Some of the values in the 'bars' key are not integers.")
            elif not all(0 <= x < 128 for x in data['bars']):
                errors.append("Not all of the values in the 'bars' key are between 0 and 127.")

        if 'files' in data:
            if not isinstance(data['files'], list):
                errors.append("The value of the 'files' key should be a list of dictionaries.")
            else:
                if not all(isinstance(x, dict) for x in data['files']):
                    errors.append("Some of the values in the 'files' key are not dictionaries.")
                else:
                    for i, file in enumerate(data['files']):
                        if 'number' in file:
                            if not isinstance(file['number'], int):
                                errors.append("The value of 'number' in file {} should be an integer.".format(i))
                            elif not 0 < file['number'] < 100:
                                errors.append("The value of 'number' in file {} should be between 1 and 99.".format(i))

                        if 'lines' in file:
                            if not isinstance(file['lines'], list):
                                errors.append("The value of the 'lines' key of file {} "
                                              "should be a list of dictionaries.".format(i))
                            else:
                                if not all(isinstance(x, dict) for x in file['lines']):
                                    errors.append("Some of the values in the 'lines' key of file {} "
                                                  "are not dictionaries.".format(i))
                                else:
                                    for j, line in enumerate(file['lines']):
                                        if 'fade' in line:
                                            if line['fade'] not in FADE_MODES:
                                                errors.append("The key 'fade' in line {} of file {} has an invalid "
                                                              "fade.".format(j, i))
                                        if 'speed' in line:
                                            if line['speed'] not in SPEEDS:
                                                errors.append("The key 'speed' in line {} of file {} has an invalid "
                                                              "speed.".format(j, i))
                                        if 'texts' in line:
                                            if not isinstance(line['texts'], list):
                                                errors.append("The value of the 'text' key of line {} in file {} "
                                                              "should be a list of dictionaries.".format(j, i))
                                            else:
                                                if not all(isinstance(x, dict) for x in line['texts']):
                                                    errors.append("Some of the values in the 'texts' key of line {} in "
                                                                  "file {} are not dictionaries.".format(j, i))
                                                else:
                                                    for k, text in enumerate(line['texts']):
                                                        if 'color' in text:
                                                            if text['color'] not in COLORS:
                                                                errors.append(
                                                                    "The key 'color' in text {} of line {} of file {} "
                                                                    "has an invalid color.".format(k, j, i)
                                                                )
                                                        if 'font' in text:
                                                            if text['font'] not in FONTS:
                                                                errors.append(
                                                                    "The key 'font' in text {} of line {} of file {} "
                                                                    "has an invalid font.".format(k, j, i)
                                                                )
                                                        if 'text' in text:
                                                            if not isinstance(text['text'], str):
                                                                errors.append(
                                                                    "The key 'text' in text {} of line {} of file {} "
                                                                    "should be a string".format(k, j, i)
                                                                )
                                                        else:
                                                            errors.append(
                                                                "Text {} of line {} of file {} is missing the "
                                                                "required key 'texts'".format(k, j, i)
                                                            )

                                        else:
                                            errors.append("Line {} of file {} is missing the "
                                                          "required key 'texts'".format(j, i))

                        else:
                            errors.append("File {} is missing the required key 'lines'".format(i))
        else:
            errors.append("The required key 'files' is missing.")

        return len(errors) == 0, errors

    def data_from_dict(self, data, clear=True):
        """
        Convert a dictionary object formatted according to specification to proper LED-bar commands.
        :param data: The dicitionary to interpret
        :param clear: Clear the old messages off of the bar or not.
        :type data: dict
        """
        valid, reasons = self.check_data(data)
        if valid:
            # Add the Sign Address group
            self.mode_00_sign_address(clear=clear)

            # Add the Signs List group. If bars is set, use that, else give it None
            self.mode_11_signs_list(signs=data['bars'] if 'bars' in data else None)

            # Add the files one by one
            for file_index, file in enumerate(data['files']):
                # Open the file by its number. If number is given, use that, else use its index + 1
                if 'number' in file:
                    self.mode_01_open_file(file_number=file['number'])
                else:
                    self.mode_01_open_file(file_number=file_index + 1)

                # Add the lines
                for line in file['lines']:
                    # Add the fade mode if present
                    if 'fade' in line:
                        self.mode_01_fade_mode(fade_mode=line['fade'])

                    # Add the speed if present
                    if 'speed' in line:
                        self.mode_01_speed(speed=line['speed'])

                    # Add the texts
                    for text in line['texts']:
                        # Add color if present
                        if 'color' in text:
                            self.mode_01_color(color=text['color'])

                        # Add font if present
                        if 'font' in text:
                            self.mode_01_font(font=text['font'])

                        # Add text
                        self.mode_01_text(text=text['text'])

                    # Add newline to close line
                    self.mode_01_newline()

                # Close file
                self.mode_01_close_file()

            # Close the bar
            self.data_end_code()

        else:
            raise ValueError("Invalid input, please check the structure of your input data. Reason(s):\n{}".format(
                    "\n".join(reasons)
            ))
