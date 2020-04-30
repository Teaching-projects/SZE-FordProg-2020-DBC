import lark

grammar="""
%import common.CNAME
%import common.INT
%import common.WS
%ignore WS

start : signal* group
signal : "SG_" signal_name multiplexer_indicator ";"
signal_name : CNAME
multiplexer_indicator : M?

M.10: "M" | "m" INT

group: "GR_" CNAME ":" signal_name*

"""
parser = lark.Lark(grammar, parser='lalr')
print(parser.parse('SG_ motortemp m8 ; SG_ motorrev m8 ; GR_ m8 : m8 eae mea2').pretty())
print(parser.parse('SG_ motortemp M ; SG_ motorrev m8 ; GR_ m8 : m8').pretty())
print(parser.parse('SG_ motortemp  ; SG_ motorrev  ; GR_ m8 : m8').pretty())