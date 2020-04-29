from lark import Lark

grammar="""
%import common.CNAME
%import common.INT
%import common.WS
%ignore WS

start :  "BO_" signal*
signal : "SG_" signal_name multiplexer_indicator ":" value "|" value c_identifier (","c_identifier)*
?signal_name : c_identifier

!multiplexer_indicator : | "M" | "m" switch_value

LC_M : "m"

switch_value: value
c_identifier :CNAME
value: INT

"""

parser = Lark(grammar, parser='lalr', lexer='contextual')
print(parser.parse('BO_ SG_ motortemp m8 : 1|2 D SG_ motortemp m8 : 1|2 D,d').pretty())
print(parser.parse('BO_ SG_ motortemp M :1|2 D').pretty())
print(parser.parse('BO_ SG_ motortemp : 1|2 D').pretty())