from dataclasses import dataclass


@dataclass
class Signal:
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


if __name__ == '__main__':
    a = Signal(name='ezaneve', signal_size=5, factor=7.4, byte_order='?')
    print(a.name)
    print(a)
