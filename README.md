# Moving Message G009DH
This package implements a library to help you interface with the Tri Colour Moving Message Sign with USB (G009DH).

This sign might also be known under the following make/model numbers. It is unknown whether this library will also work with them:
- Bestlink Optoelectronics M500N-7X50R1 / M500N-7X80RG2
- XC-0191, XC-0193 or XC-0198 (as sold by Jaycar and Procon Technology in AU)

# License
[BSD 3-Clause License](LICENSE.md)

# Requirements
- ```pyserial```

# Examples
See the [examples folder](moving_message_g009dh/examples) for some examples on how you can use this library.
The best example to follow is [dict_test.py](moving_message_g009dh/examples/dict_test.py), as it has the most abstractions on top of the bare hardware.
The other two examples [method_test](moving_message_g009dh/examples/method_test.py) and [raw_test](moving_message_g009dh/examples/raw_test.py) are only present to illustrate how the lower levels of the library and the hardware work.

# Documentation
The documentation I could find with regards to this LED sign can be found in the [documentation folder](documentation).

Thanks to [Stichting Borrelbeheer Zilverling](https://sbz.utwente.nl/) for letting me use their sign to build this library.
Also much thanks to [micolous](https://github.com/micolous) for his [ledsign](https://github.com/micolous/ledsign) project, which implements a very similar LED sign.
I used his documentation and implementation as a reference for the basics of this hardware.
