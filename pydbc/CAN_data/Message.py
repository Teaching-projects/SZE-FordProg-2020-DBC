from dataclasses import dataclass

@dataclass()
class Message:
    message_id:int = None
    message_name:str = None
    message_size:int = None
    transmitter: list = None
    signals: list = None
