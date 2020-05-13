from dataclasses import dataclass

@dataclass()
class CANDatabase:
    version: list = None
    new_symbols: list = None
    bit_timing: list = None
    nodes: dict = None
    value_tables: list = None
    messages: list = None
    message_transmitters: list = None
    environment_variables: list = None
    environment_variables_data: list = None
    comments: list = None
    attribute_definitions: list = None
    attribute_defaults: list = None
    attribute_values: list = None
    value_descriptions: list = None
    signal_groups: list = None

    def process(self):
        for message in self.messages:
            self.nodes[message.transmitter].messages.append(message)
        print('processing')
