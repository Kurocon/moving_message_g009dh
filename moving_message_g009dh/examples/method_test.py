from moving_message_g009dh.ledbar import *

if __name__ == "__main__":
    bar = LEDBar()
    bar.mode_00_sign_address()
    bar.mode_11_signs_list([1])
    bar.mode_01_open_file(1)
    bar.mode_01_fade_mode('pacman')
    bar.mode_01_color('bright_layer_mix_rainbow')
    bar.mode_01_font('extra_wide')
    bar.mode_01_text("XTRA")
    bar.mode_01_newline()
    bar.mode_01_fade_mode('interlace_center')
    bar.mode_01_color('bright_layer_mix_rainbow')
    bar.mode_01_font('extra_wide')
    bar.mode_01_text("WIDE")
    bar.mode_01_newline()
    bar.mode_01_close_file()
    bar.data_end_code()

    print(" ".join(["0x{:02x}".format(x) for x in bar._data_buffer]))

    bar.send_data()
