#!/usr/bin/env python2
## -*- coding: utf-8 -*-
##
## Triton
##

import sys
import z3

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

ctx = z3.Context()
s   = z3.Solver()

SymVar_0 = z3.BitVec('SymVar_0', 64)
ref_228 = SymVar_0
ref_243 = ref_228 # MOV operation
ref_7088 = ref_243 # MOV operation
ref_9165 = ref_7088 # MOV operation
ref_9171 = ((0x34D870D1 + ref_9165) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_14686 = ref_9171 # MOV operation
ref_21915 = ref_14686 # MOV operation
ref_28628 = ref_243 # MOV operation
ref_29341 = ref_28628 # MOV operation
ref_29353 = ref_21915 # MOV operation
ref_29355 = (ref_29353 | ref_29341) # OR operation
ref_30093 = ref_29355 # MOV operation
ref_30107 = (0xFFFFFFFFD9FCA98B | ref_30093) # OR operation
ref_35621 = ref_30107 # MOV operation
ref_43509 = ref_243 # MOV operation
ref_44222 = ref_43509 # MOV operation
ref_44236 = (0x46BC480 | ref_44222) # OR operation
ref_49750 = ref_44236 # MOV operation
ref_59289 = ref_14686 # MOV operation
ref_59600 = ref_59289 # MOV operation
ref_59614 = ((sx(0x40, 0x38BCA01F) * sx(0x40, ref_59600)) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_59947 = ref_59614 # MOV operation
ref_59961 = (0xF & ref_59947) # AND operation
ref_60699 = ref_59961 # MOV operation
ref_60713 = (0x1 | ref_60699) # OR operation
ref_62216 = ref_60713 # MOV operation
ref_62220 = ((0x40 - ref_62216) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_62228 = ref_62220 # MOV operation
ref_68961 = ref_243 # MOV operation
ref_71038 = ref_68961 # MOV operation
ref_71044 = ((0x1DD9C3C5 + ref_71038) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_71783 = ref_71044 # MOV operation
ref_71795 = ref_62228 # MOV operation
ref_71797 = ref_71783 # MOV operation
ref_71799 = (ref_71795 & 0xFFFFFFFF) # MOV operation
ref_71801 = ((ref_71797 << ((ref_71799 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_71808 = ref_71801 # MOV operation
ref_78541 = ref_243 # MOV operation
ref_80618 = ref_78541 # MOV operation
ref_80624 = ((0x1DD9C3C5 + ref_80618) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_90169 = ref_14686 # MOV operation
ref_90480 = ref_90169 # MOV operation
ref_90494 = ((sx(0x40, 0x38BCA01F) * sx(0x40, ref_90480)) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_90827 = ref_90494 # MOV operation
ref_90841 = (0xF & ref_90827) # AND operation
ref_91579 = ref_90841 # MOV operation
ref_91593 = (0x1 | ref_91579) # OR operation
ref_91937 = ref_80624 # MOV operation
ref_91941 = ref_91593 # MOV operation
ref_91943 = ref_91937 # MOV operation
ref_91945 = (ref_91941 & 0xFFFFFFFF) # MOV operation
ref_91947 = (ref_91943 >> ((ref_91945 & 0xFF) & 0x3F)) # SHR operation
ref_91954 = ref_91947 # MOV operation
ref_92687 = ref_91954 # MOV operation
ref_92699 = ref_71808 # MOV operation
ref_92701 = (ref_92699 | ref_92687) # OR operation
ref_98215 = ref_92701 # MOV operation
ref_108909 = ref_14686 # MOV operation
ref_109220 = ref_108909 # MOV operation
ref_109234 = (0x7 & ref_109220) # AND operation
ref_109972 = ref_109234 # MOV operation
ref_109986 = (0x1 | ref_109972) # OR operation
ref_116065 = ref_49750 # MOV operation
ref_116778 = ref_116065 # MOV operation
ref_116790 = ref_109986 # MOV operation
ref_116792 = ref_116778 # MOV operation
ref_116794 = (ref_116790 & 0xFFFFFFFF) # MOV operation
ref_116796 = ((ref_116792 << ((ref_116794 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_116803 = ref_116796 # MOV operation
ref_117134 = ref_116803 # MOV operation
ref_117148 = (0x3F & ref_117134) # AND operation
ref_117886 = ref_117148 # MOV operation
ref_117900 = ref_117886 # MOV operation
ref_117904 = ((ref_117900 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_117911 = ref_117904 # MOV operation
ref_123985 = ref_98215 # MOV operation
ref_124698 = ref_123985 # MOV operation
ref_124710 = ref_117911 # MOV operation
ref_124712 = (ref_124710 | ref_124698) # OR operation
ref_130226 = ref_124712 # MOV operation
ref_137455 = ref_130226 # MOV operation
ref_137766 = ref_137455 # MOV operation
ref_137780 = ((sx(0x40, 0x2C7C60B7) * sx(0x40, ref_137766)) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_143856 = ref_49750 # MOV operation
ref_144167 = ref_143856 # MOV operation
ref_144179 = ref_137780 # MOV operation
ref_144181 = ((sx(0x40, ref_144179) * sx(0x40, ref_144167)) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_150257 = ref_14686 # MOV operation
ref_156311 = ref_35621 # MOV operation
ref_157233 = ref_150257 # MOV operation
ref_157237 = ref_156311 # MOV operation
ref_157239 = ((ref_157237 + ref_157233) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_157576 = ref_157239 # MOV operation
ref_157588 = ref_144181 # MOV operation
ref_157590 = ((sx(0x40, ref_157588) * sx(0x40, ref_157576)) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_163769 = ref_157590 # MOV operation
ref_164660 = ref_163769 # MOV operation
ref_164662 = ref_164660 # MOV operation


s.add(ref_164662 == int(sys.argv[1]))
collisions = 0
while s.check() == z3.sat and collisions < 10:
    print s.model()
    s.add(SymVar_0 != s.model()[SymVar_0])
    collisions += 1
