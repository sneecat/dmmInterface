Interface primarily for controlling a Siglent SDM3045x and displaying a live reading to the screen. Siglent has an app for this but it's terrible for my purposes (seeing the reading on top of all windows, seeing the reading with my eyes deep in a microscope)

Currently I don't care much for modes other than basic measurements, and some ranges are hard-coded in because I use them the most often and I try not to abuse the relays with auto mode when possible.

TODO:
- GUI: looking at pygame or pyqt for this. tkinter is *okay* but I'm dead set on a transparent, always on top interface. Tkinter does this by "keying" out a particular color of the window, and it re-renders the window for every reading update, which manages to be graphically intense (creates lag in rendering other windows)
- Other instruments: I plan to include some other communication protocols for other instruments I have, as well as custom microcontroller sensors.
- Controls: I haven't quite decided how I want to include this, but I want an external controller to switch modes and perform other functions.
