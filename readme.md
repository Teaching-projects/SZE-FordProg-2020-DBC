# PyDBC

This package provides a pythonic interface to access and modify data stored in a CAN database
in a DBC format. The specification of the file format is 
[given here](http://read.pudn.com/downloads766/ebook/3041455/DBC_File_Format_Documentation.pdf).

The package gives access to the CAN data in a structured way.

* network (one DBC file describes one network)
    * nodes (nodes are ECUs which are communicating on the bus)
        * messages (the messages are typically uniquely identify the senderby their ID)
            * signals (these are collected into a message)
            
Signals are represented by a `Signal` object and has the following attributes:
```python
    name: str = None
    multiplexer_indicator: str = None
    start_bit: int = None
    signal_size: int = None
    byte_order: str = None
    value_type: str = None
    factor: float = None
    offset: float = None
    minimum: float = None
    maximum: float = None
    unit: str = None
```

The signals are collected into `Message`s with these attributes:
```python
    message_id:int = None
    message_name:str = None
    message_size:int = None
    transmitter: list = None
    signals: list = None
    ```
    
The `Node` is collecting the messages which the given Node can transmit:
```python
    name: str = None
    messages: list = field(default_factory=list)
    ```
An example usage can be to query what are the signal names a given node sends:
```python
>>> for message in database.nodes["IO"].messages:
...     for signal in message.signals:
...         print(signal.name)
...     
IO_DEBUG_test_unsigned
IO_DEBUG_test_enum
IO_DEBUG_test_signed
IO_DEBUG_test_float
```

