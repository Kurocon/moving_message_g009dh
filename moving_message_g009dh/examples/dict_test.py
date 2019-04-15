from moving_message_g009dh.ledbar import *

if __name__ == "__main__":
    bar = LEDBar()

    bar.data_from_dict(data={
        'files': [{
            'number': 1,
            'lines': [{
                'fade': 'pacman',
                'speed': 'speed_8',
                'texts': [{
                    'color': 'bright_red',
                    'font': 'extra_wide',
                    'text': 'X',
                }, {
                    'color': 'bright_orange',
                    'font': 'extra_wide',
                    'text': 'T',
                }, {
                    'color': 'bright_yellow',
                    'font': 'extra_wide',
                    'text': 'R',
                }, {
                    'color': 'bright_green',
                    'font': 'extra_wide',
                    'text': 'A',
                }, ]
            }, {
                'fade': 'open_from_center',
                'texts': [{
                    'color': 'bright_layer_mix_rainbow',
                    'font': 'small',
                    'text': 'smol',
                }]
            }]
        }]
    }, clear=True)

    print(" ".join(["0x{:02x}".format(x) for x in bar._data_buffer]))
    bar.send_data()
