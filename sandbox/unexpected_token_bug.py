from lark import Lark

grammar="""
%import common.CNAME
%import common.INT
%import common.WS
%ignore WS

start : signal* //group
signal : "SG_" signal_name multiplexer_indicator ";" 
?signal_name : c_identifier

//group: "GR_" c_identifier ":" signal_name*

!multiplexer_indicator : | "M" | "m" switch_value

LC_M : "m"

switch_value: value
c_identifier :CNAME
value: INT

"""

parser = Lark(grammar, parser='lalr', lexer='contextual')
print(parser.parse('SG_ motortemp m8 ; SG_ motorrev m8 ;').pretty())
# print(parser.parse('SG_ motortemp m8 ; SG_ motorrev m8 ; GR_ gr1 sa sb').pretty())
# print(parser.parse('SG_ motortemp M ; GR_ gr1 sa sb').pretty())
# print(parser.parse('SG_ motortemp ; GR_ gr1 sa sb').pretty())