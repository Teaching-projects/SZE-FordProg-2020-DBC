from lark import Transformer

from pydbc.CAN_data.Signal import Signal
from pydbc.CAN_data.Message import Message


class DBC_Transformer(Transformer):

    _nodes = None


    def nodes(self):
        _nodes = tuple(n.value for n in iter(self))
        return _nodes

    def message(self):
        return Message(
            message_id=self[0].value,
            message_name=self[1].value,
            message_size=self[2].value,
            transmitter=self[3].value,
            signals=self[4:],
        )

    def signal(self):
        if self[1].children:
            mux_indicator = self[1].children[0]
        else:
            mux_indicator = ''
        return Signal(
        name = self[0].value,
        multiplexer_indicator=mux_indicator,
        start_bit = self[2].value,
        signal_size = self[3].value,
        byte_order = self[4].value,
        value_type = self[5].value,
        factor = self[6].value,
        offset = self[7].value,
        minimum = self[8].value,
        maximum = self[9].value,
        unit = self[10],
        )



    def value_description(self):
        value = float(self[0])
        description = str(self[1])
        return (value, description)

    def value_descriptions_for_signal(self):
        message_id = int(self[0])
        signal_name = str(self[1])
        values = self[2:]
        return (message_id, signal_name, values)

    def char_string_ap(self):
        """
        Leave the " characters, make sure the string is not empty
        :return:
        """
        if self[1] == '"':
            return ''
        else:
            return self[1]

    def c_identifier_ap(self):
        """
        Leave the " characters, make sure the string is not empty
        :return:
        """
        if self[1] == '"':
            return ''
        else:
            return self[1]

    pass