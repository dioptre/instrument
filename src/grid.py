from instrument.grid_instrument import GridInstrument
import rtmidi
import time

def note_callback(messageType, midiNote, velocity):
	if messageType == "note_on":
		midiout.send_message([0x90, midiNote, velocity])
	elif messageType == "note_off":
		midiout.send_message([0x80, midiNote, velocity])

# Create a MIDI output port
midiout = rtmidi.MidiOut()
midiout.open_virtual_port("Grid Instrument (Virtual Port)")

# Set up GridInstrument
instrument = GridInstrument()
instrument.intro_message = 'grid'
instrument.note_callback = note_callback
instrument.launchpad_pro_velocity_multiplier = 2.5
instrument.min_velocity = 100
instrument.max_velocity = 100
instrument.default_velocity = 100

instrument.start()