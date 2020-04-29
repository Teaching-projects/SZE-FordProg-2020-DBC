from lark import Lark

grammar="""
start : ["a" ["b"]  ["b1"]  ["b2"]  ["b3"] ["c"]  ["c1"]  ["c2"]  ["c3"] ["d"]  ["d1"]  ["d2"]  ["d3"] ["e"]  ["e1"]  ["e2"]  ["e3"] ["f"]  ["f1"]  ["f2"]  ["f3"]]
"""

grammar1="""
start : [ "a" b c d e f ]
b: ["b"]  ["b1"]  ["b2"]  ["b3"]
c: ["c"]  ["c1"]  ["c2"]  ["c3"]
d: ["d"] ["d1"]  ["d2"]  ["d3"] 
e:  ["e"]  ["e1"]  ["e2"]  ["e3"]
f:  ["f"]  ["f1"]  ["f2"]  ["f3"]"""


grammar2="""
start : [ "a" _b _c _d _e _f ]
_b: ["b"]  ["b1"]  ["b2"]  ["b3"]
_c: ["c"]  ["c1"]  ["c2"]  ["c3"]
_d: ["d"] ["d1"]  ["d2"]  ["d3"] 
_e:  ["e"]  ["e1"]  ["e2"]  ["e3"]
_f:  ["f"]  ["f1"]  ["f2"]  ["f3"]"""

parser = Lark(grammar2, parser='lalr', lexer='contextual')
