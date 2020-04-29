from lark import Lark

grammar="""
start : ["a" ["b"]  ["b1"]  ["b2"]  ["b3"] ["c"]  ["c1"]  ["c2"]  ["c3"] ["d"]  ["d1"]  ["d2"]  ["d3"] ["e"]  ["e1"]  ["e2"]  ["e3"] ["f"]  ["f1"]  ["f2"]  ["f3"]]
"""

parser = Lark(grammar, parser='lalr', lexer='contextual')
