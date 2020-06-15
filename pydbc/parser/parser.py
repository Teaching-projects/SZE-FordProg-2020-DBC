from pathlib import Path

from lark import Lark

from pydbc.parser.dbc_transformer import DBC_Transformer

import logging
logging.basicConfig(level=logging.DEBUG)

def main():
    print('creating parser...')
    kwargs={
        "lexer" : 'contextual',
        "parser" : 'lalr',
        "transformer" : DBC_Transformer,
        "debug" : True
    }
    parser = Lark(open(r'grammar.lark'), **kwargs)
    print('done')
    print('parsing file...')
    database = parser.parse(Path(__file__).parent.joinpath(r'../../test_data/example.dbc').open('r').read())
    print(database.nodes["MOTOR"].messages[0].message_name)
    print("\t" + database.nodes["MOTOR"].messages[0].signals[0].name)
    print("\t" + database.nodes["MOTOR"].messages[0].signals[1].name)
    print('done')

if __name__ == '__main__':
    main()