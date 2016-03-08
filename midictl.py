import os, sys, mido

# Settings #
devicename = 'USB O2 MIDI 1'  # Get by running python -c 'import mido; print(mido.get_input_names())'


def process(msg):
    if msg.type == 'control_change':
        # Rogue-Pix3l Volume Control #
        if msg.control == 8:
            percent = int(msg.value) * 100
            percent = percent/127
            os.system('amixer --quiet -c 0 set Capture ' + str(percent) + '%')
            print('Desktop Percent = ' + str(percent))
        # Teamspeak 3 USB Audio Physical Loopback Volume Control #
        if msg.control == 10:
            percent = int(msg.value) * 100
            percent = percent/127
            os.system('amixer --quiet -c 3 set Speaker ' + str(percent) + '%')
            print('TS3 Percent = ' + str(percent))
    # SFX Test #
    elif msg.type == 'note_on':
        if msg.note == 72 and msg.velocity > 0:
            print('Note 72 hit')
        
        


def main():
    dev = mido.open_input(devicename)
    for msg in dev:
        process(msg)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Quitting...')
        quit()
