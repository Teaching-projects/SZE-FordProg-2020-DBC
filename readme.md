# PyDBC

This package provides a pythonic interface to access and modify data stored in a CAN database
in a DBC format. The specification of the file format is 
[given here](http://read.pudn.com/downloads766/ebook/3041455/DBC_File_Format_Documentation.pdf).

The package gives access to the CAN data in a structured way.

* network
    * nodes
        * messages
            * signals
            
The signal object contains all attributes defined for a signal.

Furthermore the valuetables for the signals are also accessible.

The structures can be modified and saved to a file.

