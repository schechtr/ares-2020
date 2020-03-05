# ARES_GROUND TODO

### RESEARCH
* research PySerial
* PyQt/Tkinter for UI (maybe)

### TODO
* build a way to receive a package cleanly
    * be able to split the data at xFF\xFF and end it at \xA4\x55
    * schechter says to look into split
    * be able to identify  and correct for errors like a package isnt long enough or we didn't get the right start and end codes
* be able to identify the correct port (scan for it) (mac and windows)

* data preparation
   * get altitude
   * log a timestamp in localtime (not the millis we are receiving)
   * output data to csv or other easily readable format for prop's pleasure

### Dependencies

* PySerial
* use struct library to unpack the bytes accordingly
