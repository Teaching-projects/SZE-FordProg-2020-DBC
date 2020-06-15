from lark import Transformer, Tree

from pydbc.CAN_data import Node, Message, Signal, Comment, CANDatabase


class DBC_Transformer(Transformer):

    def dbc_file(self):
        database = CANDatabase(
        version = self[0],
        new_symbols = self[1],
        bit_timing = self[2],
        nodes = self[3],
        value_tables = self[4],
        messages = self[5],
        message_transmitters = self[6],
        environment_variables = self[7],
        environment_variables_data = self[8],
        comments = self[9],
        attribute_definitions = self[10],
        attribute_defaults = self[11],
        attribute_values = self[12],
        value_descriptions = self[13],
        signal_groups = self[14],
        )
        database.process()
        return database

    def new_symbols(self):
        return tuple(n.value for n in iter(self))

    def nodes(self):
        return {n.value : Node(name=n.value) for n in iter(self)}

    def messages(self):
        return self

    def message(self):
        return Message(
            message_id=self[0].value,
            message_name=self[1].value,
            message_size=self[2].value,
            transmitter=self[3].value,
            signals=self[4:],
        )

    def signal(self):
        return Signal(
            name=self[0].value,
            multiplexer_indicator=self[1],
            start_bit=self[2].value,
            signal_size=self[3].value,
            byte_order=self[4].value,
            value_type=self[5].value,
            factor=self[6].value,
            offset=self[7].value,
            minimum=self[8].value,
            maximum=self[9].value,
            unit=self[10],
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

    def multiplexer_indicator(self):
        if self:
            if self[0].type == 'M':
                return 'Multiplexer'
            elif self[0].type == 'SWITCHED':
                return f'Active on value {self[0].value[1:]}'
        else:
            return 'Not multiplexed'

    def comments(self):
        return self

    def comment(self):
        type_ = self[1].value
        data = {}
        if type_ == "BU_":
            data['node_name'] = self[2].value
            data['comment'] = self[3].value
        elif type_ == "BO_":
            data['message_id'] = self[2].value
            data['comment'] = self[3].value
        elif type_ == "SG_":
            data['message_id'] = self[2].value
            data['signal_name'] = self[3].value
            data['comment'] = self[4].value
        elif type_ == "EV_":
            data['envvar_name'] = self[2].value
            data['comment'] = self[3].value
        else:
            type_ = 'DEF_'
            data['comment'] = self[1].value
        return Comment(
            type=type_,
            **data
        )

    def attribute_definitions(self):
        return tuple(self)

    def attribute_values(self):
        pass

    def char_string_ap(self):
        if self:
            return self
        else:
            return ''
