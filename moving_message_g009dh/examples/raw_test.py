import serial

if __name__ == "__main__":
    ser = serial.Serial('/dev/ttyUSB0', 2400)

    data = []
    data.append(b'\x00\xFF\xFF\x00')  # Initialize message
    data.append(b'\x0b\x01\xff')  # Send only to sign 1

    # Fade modes
    # \x01 = cyclic
    # \x02 = immediate
    # \x03 = open_right
    # \x04 = open_left
    # \x05 = open_from_center
    # \x06 = open_to_center
    # \x07 = cover_from_center
    # \x08 = cover_from_right
    # \x09 = cover_from_left
    # \x0a = cover_to_center
    # \x0b = scroll_up
    # \x0c = scroll_down
    # \x0d = interlace_center
    # \x0e = interlace_cover
    # \x0f = cover_up
    # \x10 = cover_down
    # \x11 = scan_line
    # \x12 = explode
    # \x13 = pacman
    # \x14 = fall_stack
    # \x15 = shoot
    # \x16 = flash
    # \x17 = random
    # \x18 = slide_in
    # \x19 = auto

    # Speeds
    # \xef\xc7 = speed 8 (very slow)
    # \xef\xc6 = speed 7
    # \xef\xc5 = speed 6 - unreadable
    # \xef\xc4 = speed 5 - unreadable
    # \xef\xc3 = speed 4 - unreadable
    # \xef\xc2 = speed 3 (Default)
    # \xef\xc1 = speed 2
    # \xef\xc0 = speed 1 (fastest)

    # Colors
    # \xef\xb0 = red
    # \xef\xb1 = brightred
    # \xef\xb2 = orange
    # \xef\xb3 = brightorange
    # \xef\xb4 = yellow
    # \xef\xb5 = brightyellow
    # \xef\xb6 = green
    # \xef\xb7 = brightgreen
    # \xef\xb8 = layermix_rainbow
    # \xef\xb9 = bright_layermix_rainbow
    # \xef\xba = verticalmix
    # \xef\xbb = sawtoothmix
    # \xef\xbc = green_on_red
    # \xef\xbd = red_on_green
    # \xef\xbe = orange_on_red
    # \xef\xbf = yellow_on_green

    # Fonts
    # \xef\xa0 = 5x6 (short) 			<--
    # \xef\xa1 = 5x11 (shortwide)
    # \xef\xa2 = 7x6 (default) 			<--
    # \xef\xa3 = 7x11 (wide)
    # \xef\xa4 = 7x9
    # \xef\xa5 = 7x17 (extrawide)		<--
    # \xef\xa6 = smallfont

    # Switching programs can only be done on the remote using
    # RUN -> (enter program number) -> ENT
    # So not really useful for us, but here are program numbers:
    # \x30\x31 = Program  1
    # \x30\x32 = Program  2
    # \x30\x33 = Program  3
    # ..
    # \x30\x39 = Program  9
    # \x31\x30 = Program 10
    # \x31\x31 = Program 11
    # ..

    data.append(b'\x01\x30\x31')  # Open program 1
    data.append(b'\x01')  # Fade mode for this line
    data.append(b'\xef\xb0')  # Color red
    data.append(b'\xef\xa0')  # Font short
    data.append(b'\x42\x69\x65\x72')  # He
    data.append(b'\xef\xb2')  # Color orange
    data.append(b'\xef\xa1')  # Font shortwide
    data.append(b'\x42\x69\x65\x72')  # ll
    data.append(b'\xef\xb4')  # Color yellow
    data.append(b'\xef\xa2')  # Font default
    data.append(b'\x42\x69\x65\x72')  # oW
    data.append(b'\xef\xb6')  # Color green
    data.append(b'\xef\xa3')  # Font wide
    data.append(b'\x42\x69\x65\x72')  # or
    data.append(b'\xef\xb8')  # Color rainbow
    data.append(b'\xef\xa4')  # Font 7x9
    data.append(b'\x42\x69\x65\x72')  # ld
    data.append(b'\xef\xb1')  # Color red
    data.append(b'\xef\xa5')  # Font 7x9
    data.append(b'\x42\x69\x65\x72')  # BEER!
    data.append(b'\xef\xb1')  # Color red
    data.append(b'\xef\xa6')  # Font 7x9
    data.append(b'\x42\x69\x65\x72')  # smol
    data.append(b'\xef\xb1')  # Color red
    data.append(b'\xef\xa6')  # Font 7x9
    data.append(b'\x42\x69\x65\x72')  # smol
    data.append(b'\xff')  # Close line
    data.append(b'\xff')  # Close file

    data.append(b'\x01\x30\x32')  # Open program 2
    data.append(b'\x02')  # Fade mode for this line
    data.append(b'\xef\xb0')  # Color red
    data.append(b'\xef\xa2')  # Font default
    data.append(b'\x20\x4c\x6f\x72\x65\x6d\x20\x69\x70\x73\x75\x6d\x20\x64\x6f\x6c\x6f\x72\x20\x73\x69\x74\x20\x61\x6d\x65\x74\x2c\x20\x63\x6f\x6e\x73\x65\x63\x74\x65\x74\x75\x72\x20\x61\x64\x69\x70\x69\x73\x63\x69\x6e\x67\x20\x65\x6c\x69\x74\x2e\x20\x50\x72\x61\x65\x73\x65\x6e\x74\x20\x72\x75\x74\x72\x75\x6d\x20\x64\x69\x67\x6e\x69\x73\x73\x69\x6d\x20\x61\x75\x67\x75\x65\x20\x65\x75\x20\x70\x6f\x73\x75\x65\x72\x65\x2e\x20\x45\x74\x69\x61\x6d\x20\x69\x6d\x70\x65\x72\x64\x69\x65\x74\x20\x65\x6c\x65\x6d\x65\x6e\x74\x75\x6d\x20\x6c\x69\x62\x65\x72\x6f\x2c\x20\x6e\x6f\x6e\x20\x76\x69\x76\x65\x72\x72\x61\x20\x65\x6e\x69\x6d\x20\x61\x63\x63\x75\x6d\x73\x61\x6e\x20\x69\x64\x2e\x20\x56\x69\x76\x61\x6d\x75\x73\x20\x73\x61\x67\x69\x74\x74\x69\x73\x20\x6f\x64\x69\x6f\x20\x73\x65\x64\x20\x70\x65\x6c\x6c\x65\x6e\x74\x65\x73\x71\x75\x65\x20\x70\x6c\x61\x63\x65\x72\x61\x74\x2e\x20\x50\x72\x6f\x69\x6e\x20\x65\x6c\x65\x6d\x65\x6e\x74\x75\x6d\x20\x67\x72\x61\x76\x69\x64\x61\x20\x6c\x61\x6f\x72\x65\x65\x74\x2e\x20\x44\x6f\x6e\x65\x63\x20\x6e\x6f\x6e\x20\x70\x68\x61\x72\x65\x74\x72\x61\x20\x6e\x69\x73\x69\x2e\x20\x43\x75\x72\x61\x62\x69\x74\x75\x72\x20\x72\x75\x74\x72\x75\x6d\x20\x74\x69\x6e\x63\x69\x64\x75\x6e\x74\x20\x6c\x69\x67\x75\x6c\x61\x2e\x20\x43\x72\x61\x73\x20\x72\x69\x73\x75\x73\x20\x74\x65\x6c\x6c\x75\x73\x2c\x20\x75\x6c\x74\x72\x69\x63\x69\x65\x73\x20\x6e\x65\x63\x20\x6d\x6f\x6c\x6c\x69\x73\x20\x76\x65\x6c\x2c\x20\x63\x75\x72\x73\x75\x73\x20\x65\x67\x65\x74\x20\x61\x75\x67\x75\x65\x2e\x20\x4d\x61\x75\x72\x69\x73\x20\x69\x70\x73\x75\x6d\x20\x6c\x65\x6f\x2c\x20\x74\x69\x6e\x63\x69\x64\x75\x6e\x74\x20\x65\x67\x65\x74\x20\x76\x69\x76\x65\x72\x72\x61\x20\x65\x75\x2c\x20\x74\x69\x6e\x63\x69\x64\x75\x6e\x74\x20\x61\x74\x20\x73\x61\x70\x69\x65\x6e\x2e\x20\x55\x74\x20\x68\x65\x6e\x64\x72\x65\x72\x69\x74\x20\x61\x74\x20\x70\x75\x72\x75\x73\x20\x73\x65\x64\x20\x63\x6f\x6e\x73\x65\x71\x75\x61\x74\x2e\x20\x55\x74\x20\x65\x67\x65\x74\x20\x64\x75\x69\x20\x61\x6c\x69\x71\x75\x65\x74\x2c\x20\x70\x72\x65\x74\x69\x75\x6d\x20\x65\x78\x20\x61\x63\x2c\x20\x73\x6f\x64\x61\x6c\x65\x73\x20\x6a\x75\x73\x74\x6f\x2e\x20\x4e\x75\x6c\x6c\x61\x6d\x20\x61\x63\x20\x74\x6f\x72\x74\x6f\x72\x20\x6f\x72\x63\x69\x2e\x20\x51\x75\x69\x73\x71\x75\x65\x20\x6c\x69\x67\x75\x6c\x61\x20\x6e\x69\x73\x69\x2c\x20\x73\x75\x73\x63\x69\x70\x69\x74\x20\x76\x69\x74\x61\x65\x20\x64\x69\x61\x6d\x20\x70\x6f\x72\x74\x74\x69\x74\x6f\x72\x2c\x20\x62\x6c\x61\x6e\x64\x69\x74\x20\x74\x65\x6d\x70\x6f\x72\x20\x69\x70\x73\x75\x6d\x2e\x20\x44\x6f\x6e\x65\x63\x20\x76\x69\x74\x61\x65\x20\x72\x69\x73\x75\x73\x20\x73\x61\x70\x69\x65\x6e\x2e\x20\x53\x75\x73\x70\x65\x6e\x64\x69\x73\x73\x65\x20\x73\x61\x67\x69\x74\x74\x69\x73\x20\x65\x67\x65\x74\x20\x74\x6f\x72\x74\x6f\x72\x20\x76\x69\x74\x61\x65\x20\x66\x69\x6e\x69\x62\x75\x73\x2e\x20\x50\x72\x61\x65\x73\x65\x6e\x74\x20\x6e\x6f\x6e\x20\x6c\x65\x6f\x20\x6d\x6f\x6c\x6c\x69\x73\x2c\x20\x72\x75\x74\x72\x75\x6d\x20\x75\x72\x6e\x61\x20\x71\x75\x69\x73\x2c\x20\x74\x69\x6e\x63\x69\x64\x75\x6e\x74\x20\x6d\x61\x73\x73\x61\x2e\x20\x4e\x61\x6d\x20\x6e\x6f\x6e\x20\x6d\x65\x74\x75\x73\x20\x73\x65\x64\x20\x6d\x61\x67\x6e\x61\x20\x68\x65\x6e\x64\x72\x65\x72\x69\x74\x20\x76\x65\x68\x69\x63\x75\x6c\x61\x20\x69\x64\x20\x65\x67\x65\x74\x20\x65\x78\x2e')
    data.append(b'\xff')  # Close line
    data.append(b'\xff')  # Close file

    data.append(b'\x00')  # End code

    msg = b"".join(data)
    print("Writing '{}'".format(msg))
    ser.write(msg)

    """
    0040   00 ff ff 00 0b 00 01 02 03 04 05 06 07 08 09 0a   ................
    0050   0b 0c 0d 0e 0f 10 11 12 13 14 15 16 17 18 19 1a   ................
    0060   1b 1c 1d 1e 1f 20 21 22 23 24 25 26 27 28 29 2a   ..... !"#$%&'()*
    0070   2b 2c 2d 2e 2f 30 31 32 33 34 35 36 37 38 39 3a   +,-./0123456789:
    0080   3b 3c 3d 3e 3f 40 41 42 43 44 45 46 47 48 49 4a   ;<=>?@ABCDEFGHIJ
    0090   4b 4c 4d 4e 4f 50 51 52 53 54 55 56 57 58 59 5a   KLMNOPQRSTUVWXYZ
    00a0   5b 5c 5d 5e 5f 60 61 62 63 64 65 66 67 68 69 6a   [\]^_`abcdefghij
    00b0   6b 6c 6d 6e 6f 70 71 72 73 74 75 76 77 78 79 7a   klmnopqrstuvwxyz
    00c0   7b 7c 7d 7e 7f ff 01 30 31 ef b0 ef a2 48 65 6c   {|}~...01....Hel
    00d0   6c 6f 20 57 6f 72 6c 64 ff ff 00                  lo World...
    
    
    
    0040   00 ff ff 00 0b 01 ff 01 30 31 ef b0 ef a2 48 65   ........01....He
    0050   6c 6c 6f 20 57 6f 72 6c 64 ff ff 00               llo World...
    
    
    
    0040   00 ff ff 00 0b 01 ff 01 30 31 ef b0 ef a2 37 5f   ........01....7_
    0050   36 64 65 66 61 75 6c 74 ef b1 ef a0 ff ef b0 ef   6default........
    0060   a1 35 5f 31 31 73 68 6f 72 74 77 69 64 65 ef b1   .5_11shortwide..
    0070   ef a0 ff ef b0 ef a0 35 5f 36 73 68 6f 72 74 ef   .......5_6short.
    0080   b1 ff ef b0 ef a3 37 5f 31 31 77 69 64 65 ef b1   ......7_11wide..
    0090   ef a0 ff ef b0 ef a4 37 5f 39 ef b1 ef a0 ff ef   .......7_9......
    00a0   b0 ef a5 37 5f 31 37 65 78 74 72 61 77 69 64 65   ...7_17extrawide
    00b0   ef b1 ef a0 ff ef b0 ef a6 73 6d 61 6c 6c 66 6f   .........smallfo
    00c0   6e 74 ff ff 00                                    nt...
    
    
    b0 red
    b1 brightred
    b2 orange
    b3 brightorange
    b4 yellow
    b5 brightyellow
    b6 green
    b7 brightgreen
    b8 layermix_rainbow
    b9 bright_layermix_rainbow
    ba verticalmix
    bb sawtoothmix
    bc green_on_red
    bd red_on_green
    be orange_on_red
    bf yellow_on_green
    
    0040   00 ff ff 00 0b 01 ff 01 30 31 ef b0 ef a2 72 65   ........01....re
    0050   64 ef b1 ef a0 ff ef b0 ef a2 62 72 69 67 68 74   d.........bright
    0060   72 65 64 ef b1 ef a0 ff ef b2 ef a2 6f 72 61 6e   red.........oran
    0070   67 65 ef b1 ef a0 ff ef b3 ef a2 62 72 69 67 68   ge.........brigh
    0080   74 6f 72 61 6e 67 65 ef b1 ef a0 ff ef b4 ef a2   torange.........
    0090   79 65 6c 6c 6f 77 ef b1 ef a0 ff ef b5 ef a2 62   yellow.........b
    00a0   72 69 67 68 74 79 65 6c 6c 6f 77 ef b1 ef a0 ff   rightyellow.....
    00b0   ef b6 ef a2 67 72 65 65 6e ef b1 ef a0 ff ef b7   ....green.......
    00c0   ef a2 62 72 69 67 68 74 67 72 65 65 6e ef b1 ef   ..brightgreen...
    00d0   a0 ff ef b8 ef a2 6c 61 79 65 72 6d 69 78 5f 72   ......layermix_r
    00e0   61 69 6e 62 6f 77 ef b1 ef a0 ff ef b9 ef a2 62   ainbow.........b
    00f0   72 69 67 68 74 5f 6c 61 79 65 72 6d 69 78 5f 72   right_layermix_r
    0100   61 69 6e 62 6f 77 ef b1 ef a0 ff ef ba ef a2 76   ainbow.........v
    0110   65 72 74 69 63 61 6c 6d 69 78 ef b1 ef a0 ff ef   erticalmix......
    0120   bb ef a2 73 61 77 74 6f 6f 74 68 6d 69 78 ef b1   ...sawtoothmix..
    0130   ef a0 ff ef bc ef a2 67 72 65 65 6e 5f 6f 6e 5f   .......green_on_
    0040   72 65 64 ef b1 ef a0 ff ef bd ef a2 72 65 64 5f   red.........red_
    0050   6f 6e 5f 67 72 65 65 6e ef b1 ef a0 ff ef be ef   on_green........
    0060   a2 6f 72 61 6e 67 65 5f 6f 6e 5f 72 65 64 ef b1   .orange_on_red..
    0070   ef a0 ff ef bf ef a2 74 65 6c 6c 6f 77 5f 6f 6e   .......tellow_on
    0080   5f 67 72 65 65 6e ff ff 00                        _green...
    
    
    
    0040   00 ff ff 00 0b 01 ff 01 30 31 01 ef b0 ef a2 63   ........01.....c
    0050   79 63 6c 69 63 ef b1 ef a0 ff 02 ef b0 ef a2 69   yclic..........i
    0060   6d 6d 65 64 69 61 74 65 ef b1 ef a0 ff 03 ef b0   mmediate........
    0070   ef a2 6f 70 65 6e 5f 72 69 67 68 74 ef b1 ef a0   ..open_right....
    0080   ff 04 ef b0 ef a2 6f 70 65 6e 5f 6c 65 66 74 ef   ......open_left.
    0090   b1 ef a0 ff 05 ef b0 ef a2 6f 70 6e 5f 66 5f 63   .........opn_f_c
    00a0   6e 74 72 ef b1 ef a0 ff 06 ef b0 ef a2 6f 70 6e   ntr..........opn
    00b0   5f 74 5f 63 6e 74 72 ef b1 ef a0 ff 07 ef b0 ef   _t_cntr.........
    00c0   a2 63 76 72 5f 66 5f 63 6e 74 72 ef b1 ef a0 ff   .cvr_f_cntr.....
    00d0   08 ef b0 ef a2 63 76 72 5f 66 5f 72 67 68 74 ef   .....cvr_f_rght.
    00e0   b1 ef a0 ff 09 ef b0 ef a2 63 76 72 5f 66 5f 6c   .........cvr_f_l
    00f0   65 66 74 ef b1 ef a0 ff 0a ef b0 ef a2 63 76 72   eft..........cvr
    0100   5f 74 5f 63 6e 74 72 ef b1 ef a0 ff 0b ef b0 ef   _t_cntr.........
    0110   a2 73 63 72 6f 6c 6c 5f 75 70 ef b1 ef a0 ff 0c   .scroll_up......
    0120   ef b0 ef a2 73 63 72 6f 6c 6c 5f 64 6f 77 6e ef   ....scroll_down.
    0130   b1 ef a0 ff 0d ef b0 ef a2 69 6e 74 65 72 6c 5f   .........interl_
    0040   63 6e 74 72 ef b1 ef a0 ff 0e ef b0 ef a2 69 6e   cntr..........in
    0050   74 65 72 6c 5f 63 76 72 ef b1 ef a0 ff 0f ef b0   terl_cvr........
    0060   ef a2 63 6f 76 65 72 5f 75 70 ef b1 ef a0 ff 10   ..cover_up......
    0070   ef b0 ef a2 63 6f 76 65 72 5f 64 6f 77 6e ef b1   ....cover_down..
    0080   ef a0 ff 11 ef b0 ef a2 73 63 61 6e 5f 6c 69 6e   ........scan_lin
    0090   65 ef b1 ef a0 ff 12 ef b0 ef a2 65 78 70         e..........exp
    0040   6c 6f 64 65 ef b1 ef a0 ff 13 ef b0 ef a2 70 61   lode..........pa
    0050   63 6d 61 6e ef b1 ef a0 ff 14 ef b0 ef a2 66 61   cman..........fa
    0060   6c 6c 5f 73 74 61 63 6b ef b1 ef a0 ff 15 ef b0   ll_stack........
    0070   ef a2 73 68 6f 6f 74 ef b1 ef a0 ff 16 ef b0 ef   ..shoot.........
    0080   a2 66 6c 61 73 68 ef b1 ef a0 ff 17 ef b0 ef a2   .flash..........
    0090   72 61 6e 64 6f 6d ef b1 ef a0 ff 18 ef b0 ef a2   random..........
    00a0   73 6c 69 64 65 5f 69 6e ef b1 ef a0 ff 19 ef b0   slide_in........
    00b0   ef a2 61 75 74 6f ff ff 00                        ..auto...
    
    
    
    
    0000   c0 09 72 8b 9a 8e ff ff 53 03 02 15 01 00 2d 00   ..r.....S.....-.
    0010   64 d8 b4 5c 00 00 00 00 63 4d 00 00 8d ff ff ff   d..\....cM......
    0020   00 01 00 00 00 01 00 00 00 00 00 00 00 00 00 00   ................
    0030   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   ................
    0040   00 ff ff 00 0b 01 ff 01 30 31 ef c7 ef b0 ef a2   ........01......
    0050   74 68 69 73 20 69 73 20 61 20 76 65 72 79 20 73   this is a very s
    0060   6c 6f 77 20 6c 69 6e 65 ef b1 ef a0 ff ef c6 ef   low line........
    0070   b0 ef a2 74 68 69 73 20 69 73 20 73 6f 6d 65 20   ...this is some 
    0080   73 70 65 65 64 20 37 ef b1 ef a0 ff ef c5 ef b0   speed 7.........
    0090   ef a2 74 68 69 73 20 69 73 20 73 70 65 65 64 20   ..this is speed 
    00a0   36 20 61 73 64 6c 61 73 64 66 ef b1 ef a0 ff ef   6 asdlasdf......
    00b0   c4 ef b0 ef a2 73 70 65 65 64 20 35 20 6a 66 73   .....speed 5 jfs
    00c0   61 68 64 6b 66 68 6c 61 6b 73 64 66 6c ff ef c3   ahdkfhlaksdfl...
    00d0   ef b0 ef a2 73 70 65 65 64 20 34 20 6a 6b 6c 61   ....speed 4 jkla
    00e0   73 64 66 6b 6a 61 73 3b 64 66 6b 6a ef b1 ef a0   sdfkjas;dfkj....
    00f0   ff ef c2 ef b0 ef a2 73 70 65 65 64 20 33 20 3b   .......speed 3 ;
    0100   6c 6b 73 61 64 6a 66 3b 6c 6b 61 73 6a 64 66 ef   lksadjf;lkasjdf.
    0110   b1 ef a0 ff ef c1 ef b0 ef a2 73 70 65 65 64 20   ..........speed 
    0120   32 20 6b 6a 73 64 6c 66 6b 6a 61 73 64 66 6c 6b   2 kjsdlfkjasdflk
    0130   6a 64 ff ef c0 ef b0 ef a2 73 70 65 65 64 20 31   jd.......speed 1
    """
