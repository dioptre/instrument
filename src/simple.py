from instrument.grid_instrument import GridInstrument
import threading


def note_callback(messageType, midiNote, velocity):
	print ("Note callback. messageType=", messageType, midiNote, velocity)

def button_callback(x, y, pressed):
	print("Button Callback. x=", x, ", y=", y, ", pressed=", pressed )

instrument = GridInstrument()

# Set settings
instrument.intro_message = 'grid_instrument'
instrument.kid_mode = False
instrument.debugging = True

# set the callback for midi events
instrument.note_callback = note_callback
# set the callback for function buttons
instrument.func_button_callback = button_callback
instrument.start()