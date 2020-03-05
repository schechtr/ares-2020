# ARES_GROUND TODO

### RESEARCH
* research PySerial
* PyQt/Tkinter for UI (maybe)

### TODO
* build a way to receive a package cleanly
    * be able to split the data at xFF\xFF and end it at \xA4\x55
    * schechter says to look into split
* be able to identify the correct port (scan for it) (mac and windows)

### Dependencies

* PySerial
* use struct library to unpack the bytes accordingly
