import os, sys, mido

devicename = 'USB O2 MIDI 1'

def process(msg):
    # Rogue-Pix3l Volume Control #
    if msg.type == 'control_change' and msg.control == 8:
        percent = int(msg.value) * 100
        percent = percent/127
        os.system('amixer --quiet -c 0 set Capture ' + str(percent) + '%')
        print('Desktop Percent = ' + str(percent))
    # Teamspeak 3 USB Audio Physical Loopback Volume Control #
    if msg.type == 'control_change' and msg.control == 10:
        percent = int(msg.value) * 100
        percent = percent/127
        os.system('amixer --quiet -c 3 set Speaker ' + str(percent) + '%')
        print('TS3 Percent = ' + str(percent))

def main():
    dev = mido.open_input(devicename)
    for msg in dev:
        process(msg)

if __name__ == '__main__':
    main()
