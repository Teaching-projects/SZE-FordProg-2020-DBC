from pathlib import Path

from lark import Lark

from pydbc.parser.dbc_transformer import DBC_Transformer

import logging
logging.basicConfig(level=logging.DEBUG)

def main():
    print('creating parser...')
    kwargs={
        #"start" : "dbc_file",
        "lexer" : 'contextual',
        "parser" : 'lalr',
        #"transformer" : DBC_Transformer,
        "debug" : True
    }
    parser = Lark(open(r'grammar.lark'), **kwargs)
    print('done')
    print('parsing file...')
    tree = parser.parse(Path(__file__).parent.joinpath(r'../../test_data/example.dbc').open('r').read())
    print('done')
    print(tree.pretty())

if __name__ == '__main__':
    main()