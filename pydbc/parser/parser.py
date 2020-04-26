from lark import Lark

from pydbc.parser.dbc_transformer import DBC_Transformer

import logging
logging.basicConfig(level=logging.DEBUG)

def main():
    print('creating parser...')
    parser = Lark(open(r'grammar.lark'), start="dbc_file", lexer='standard',
                  parser='lalr', transformer=DBC_Transformer, debug=True)
    print('done')
    print('parsing file...')
    tree = parser.parse(open(r'../../example.dbc'))
    print('done')
    print(tree.pretty())

if __name__ == '__main__':
    main()