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
ref_9864 = ref_243 # MOV operation
ref_11227 = ref_9864 # MOV operation
ref_11233 = ref_11227 # MOV operation
ref_11237 = (ref_11233 >> (0x3F & 0x3F)) # SHR operation
ref_11244 = ref_11237 # MOV operation
ref_16669 = ref_243 # MOV operation
ref_17801 = ref_16669 # MOV operation
ref_17807 = ref_17801 # MOV operation
ref_17811 = ((ref_17807 << (0x1 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_17818 = ref_17811 # MOV operation
ref_18380 = ref_17818 # MOV operation
ref_18392 = ref_11244 # MOV operation
ref_18394 = (ref_18392 | ref_18380) # OR operation
ref_20013 = ref_18394 # MOV operation
ref_20019 = ((0x100E532E000 + ref_20013) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_20595 = ref_20019 # MOV operation
ref_30917 = ref_243 # MOV operation
ref_36356 = ref_20595 # MOV operation
ref_37719 = ref_36356 # MOV operation
ref_37725 = ref_37719 # MOV operation
ref_37729 = (ref_37725 >> (0x4 & 0x3F)) # SHR operation
ref_37736 = ref_37729 # MOV operation
ref_38888 = ref_37736 # MOV operation
ref_38894 = (0x7 & ref_38888) # AND operation
ref_39461 = ref_38894 # MOV operation
ref_39475 = (0x1 | ref_39461) # OR operation
ref_40050 = ref_30917 # MOV operation
ref_40054 = ref_39475 # MOV operation
ref_40056 = ref_40050 # MOV operation
ref_40058 = (ref_40054 & 0xFFFFFFFF) # MOV operation
ref_40060 = (ref_40056 >> ((ref_40058 & 0xFF) & 0x3F)) # SHR operation
ref_40067 = ref_40060 # MOV operation
ref_40629 = ref_40067 # MOV operation
ref_40643 = (0x3CE3ECE5 | ref_40629) # OR operation
ref_41218 = ref_40643 # MOV operation
ref_50727 = ref_243 # MOV operation
ref_51859 = ref_50727 # MOV operation
ref_51865 = ref_51859 # MOV operation
ref_51869 = ((ref_51865 << (0x3F & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_51876 = ref_51869 # MOV operation
ref_57301 = ref_243 # MOV operation
ref_58664 = ref_57301 # MOV operation
ref_58670 = ref_58664 # MOV operation
ref_58674 = (ref_58670 >> (0x1 & 0x3F)) # SHR operation
ref_58681 = ref_58674 # MOV operation
ref_59243 = ref_58681 # MOV operation
ref_59255 = ref_51876 # MOV operation
ref_59257 = (ref_59255 | ref_59243) # OR operation
ref_59832 = ref_59257 # MOV operation
ref_69341 = ref_243 # MOV operation
ref_70935 = ref_69341 # MOV operation
ref_70941 = ((0xB6AFCA8 + ref_70935) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_71517 = ref_70941 # MOV operation
ref_80247 = ref_59832 # MOV operation
ref_84873 = ref_59832 # MOV operation
ref_85646 = ref_84873 # MOV operation
ref_85658 = ref_80247 # MOV operation
ref_85660 = ((sx(0x40, ref_85658) * sx(0x40, ref_85646)) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_86232 = ref_85660 # MOV operation
ref_94962 = ref_59832 # MOV operation
ref_99588 = ref_59832 # MOV operation
ref_100369 = ref_94962 # MOV operation
ref_100373 = ref_99588 # MOV operation
ref_100375 = ((ref_100373 + ref_100369) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_100951 = ref_100375 # MOV operation
ref_110469 = ref_86232 # MOV operation
ref_115095 = ref_41218 # MOV operation
ref_115816 = ref_110469 # MOV operation
ref_115820 = ref_115095 # MOV operation
ref_115822 = ref_115816 # MOV operation
ref_115824 = ((ref_115822 - ref_115820) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_115832 = ref_115824 # MOV operation
ref_122104 = ref_100951 # MOV operation
ref_127543 = ref_71517 # MOV operation
ref_128675 = ref_127543 # MOV operation
ref_128681 = ref_128675 # MOV operation
ref_128685 = ((ref_128681 << (0x3D & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_128692 = ref_128685 # MOV operation
ref_133338 = ref_71517 # MOV operation
ref_134701 = ref_133338 # MOV operation
ref_134707 = ref_134701 # MOV operation
ref_134711 = (ref_134707 >> (0x3 & 0x3F)) # SHR operation
ref_134718 = ref_134711 # MOV operation
ref_135280 = ref_134718 # MOV operation
ref_135292 = ref_128692 # MOV operation
ref_135294 = (ref_135292 | ref_135280) # OR operation
ref_136682 = ref_135294 # MOV operation
ref_136688 = ref_136682 # MOV operation
ref_136692 = (ref_136688 >> (0x1 & 0x3F)) # SHR operation
ref_136699 = ref_136692 # MOV operation
ref_137851 = ref_136699 # MOV operation
ref_137857 = (0x7 & ref_137851) # AND operation
ref_138424 = ref_137857 # MOV operation
ref_138438 = (0x1 | ref_138424) # OR operation
ref_138782 = ref_122104 # MOV operation
ref_138786 = ref_138438 # MOV operation
ref_138788 = ref_138782 # MOV operation
ref_138790 = (ref_138786 & 0xFFFFFFFF) # MOV operation
ref_138792 = ((ref_138788 << ((ref_138790 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_138799 = ref_138792 # MOV operation
ref_140182 = ref_138799 # MOV operation
ref_140188 = ref_140182 # MOV operation
ref_140192 = (ref_140188 >> (0x1 & 0x3F)) # SHR operation
ref_140199 = ref_140192 # MOV operation
ref_141351 = ref_140199 # MOV operation
ref_141357 = (0xF & ref_141351) # AND operation
ref_141924 = ref_141357 # MOV operation
ref_141938 = (0x1 | ref_141924) # OR operation
ref_142688 = ref_141938 # MOV operation
ref_142692 = ((0x40 - ref_142688) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_142700 = ref_142692 # MOV operation
ref_143270 = ref_115832 # MOV operation
ref_143274 = ref_142700 # MOV operation
ref_143276 = ref_143270 # MOV operation
ref_143278 = (ref_143274 & 0xFFFFFFFF) # MOV operation
ref_143280 = (ref_143276 >> ((ref_143278 & 0xFF) & 0x3F)) # SHR operation
ref_143287 = ref_143280 # MOV operation
ref_147933 = ref_86232 # MOV operation
ref_152559 = ref_41218 # MOV operation
ref_153280 = ref_147933 # MOV operation
ref_153284 = ref_152559 # MOV operation
ref_153286 = ref_153280 # MOV operation
ref_153288 = ((ref_153286 - ref_153284) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_153296 = ref_153288 # MOV operation
ref_158755 = ref_100951 # MOV operation
ref_164194 = ref_71517 # MOV operation
ref_165326 = ref_164194 # MOV operation
ref_165332 = ref_165326 # MOV operation
ref_165336 = ((ref_165332 << (0x3D & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_165343 = ref_165336 # MOV operation
ref_169989 = ref_71517 # MOV operation
ref_171352 = ref_169989 # MOV operation
ref_171358 = ref_171352 # MOV operation
ref_171362 = (ref_171358 >> (0x3 & 0x3F)) # SHR operation
ref_171369 = ref_171362 # MOV operation
ref_171931 = ref_171369 # MOV operation
ref_171943 = ref_165343 # MOV operation
ref_171945 = (ref_171943 | ref_171931) # OR operation
ref_173333 = ref_171945 # MOV operation
ref_173339 = ref_173333 # MOV operation
ref_173343 = (ref_173339 >> (0x1 & 0x3F)) # SHR operation
ref_173350 = ref_173343 # MOV operation
ref_174502 = ref_173350 # MOV operation
ref_174508 = (0x7 & ref_174502) # AND operation
ref_175075 = ref_174508 # MOV operation
ref_175089 = (0x1 | ref_175075) # OR operation
ref_175433 = ref_158755 # MOV operation
ref_175437 = ref_175089 # MOV operation
ref_175439 = ref_175433 # MOV operation
ref_175441 = (ref_175437 & 0xFFFFFFFF) # MOV operation
ref_175443 = ((ref_175439 << ((ref_175441 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_175450 = ref_175443 # MOV operation
ref_176833 = ref_175450 # MOV operation
ref_176839 = ref_176833 # MOV operation
ref_176843 = (ref_176839 >> (0x1 & 0x3F)) # SHR operation
ref_176850 = ref_176843 # MOV operation
ref_178002 = ref_176850 # MOV operation
ref_178008 = (0xF & ref_178002) # AND operation
ref_178575 = ref_178008 # MOV operation
ref_178589 = (0x1 | ref_178575) # OR operation
ref_178933 = ref_153296 # MOV operation
ref_178937 = ref_178589 # MOV operation
ref_178939 = ref_178933 # MOV operation
ref_178941 = (ref_178937 & 0xFFFFFFFF) # MOV operation
ref_178943 = ((ref_178939 << ((ref_178941 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_178950 = ref_178943 # MOV operation
ref_179512 = ref_178950 # MOV operation
ref_179524 = ref_143287 # MOV operation
ref_179526 = (ref_179524 | ref_179512) # OR operation
ref_180101 = ref_179526 # MOV operation
ref_181022 = ref_180101 # MOV operation
ref_181024 = ref_181022 # MOV operation


s.add(ref_181024 == int(sys.argv[1]))
collisions = 0
while s.check() == z3.sat and collisions < 10:
    print s.model()
    s.add(SymVar_0 != s.model()[SymVar_0])
    collisions += 1
