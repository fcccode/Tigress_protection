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
ref_351 = SymVar_0
ref_366 = ref_351 # MOV operation
ref_19638 = ref_366 # MOV operation
ref_19898 = ref_19638 # MOV operation
ref_19914 = ((0x24D06FB + ref_19898) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_20194 = ref_19914 # MOV operation
ref_20196 = ((ref_20194 >> 56) & 0xFF) # Byte reference - MOV operation
ref_20197 = ((ref_20194 >> 48) & 0xFF) # Byte reference - MOV operation
ref_20198 = ((ref_20194 >> 40) & 0xFF) # Byte reference - MOV operation
ref_20199 = ((ref_20194 >> 32) & 0xFF) # Byte reference - MOV operation
ref_20200 = ((ref_20194 >> 24) & 0xFF) # Byte reference - MOV operation
ref_20201 = ((ref_20194 >> 16) & 0xFF) # Byte reference - MOV operation
ref_20202 = ((ref_20194 >> 8) & 0xFF) # Byte reference - MOV operation
ref_20203 = (ref_20194 & 0xFF) # Byte reference - MOV operation
ref_24735 = ref_20194 # MOV operation
ref_27069 = ref_366 # MOV operation
ref_27355 = ref_27069 # MOV operation
ref_27369 = ref_24735 # MOV operation
ref_27371 = ((ref_27369 + ref_27355) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_27947 = ref_27371 # MOV operation
ref_27955 = (0xB200000000643F31 | ref_27947) # OR operation
ref_28272 = ref_27955 # MOV operation
ref_33030 = ref_366 # MOV operation
ref_33311 = ref_33030 # MOV operation
ref_33327 = ref_33311 # MOV operation
ref_33331 = (ref_33327 >> (0x7 & 0x3F)) # SHR operation
ref_33338 = ref_33331 # MOV operation
ref_33612 = ref_33338 # MOV operation
ref_38189 = ref_33612 # MOV operation
ref_41776 = ref_28272 # MOV operation
ref_42062 = ref_41776 # MOV operation
ref_42078 = ref_42062 # MOV operation
ref_42082 = (ref_42078 >> (0x1 & 0x3F)) # SHR operation
ref_42089 = ref_42082 # MOV operation
ref_42341 = ref_42089 # MOV operation
ref_42357 = (0xF & ref_42341) # AND operation
ref_42984 = ref_42357 # MOV operation
ref_42992 = (0x1 | ref_42984) # OR operation
ref_45394 = ref_20194 # MOV operation
ref_45664 = ref_45394 # MOV operation
ref_45678 = ref_42992 # MOV operation
ref_45680 = ref_45664 # MOV operation
ref_45682 = (ref_45678 & 0xFFFFFFFF) # MOV operation
ref_45684 = (ref_45680 >> ((ref_45682 & 0xFF) & 0x3F)) # SHR operation
ref_45691 = ref_45684 # MOV operation
ref_48091 = ref_20194 # MOV operation
ref_51124 = ref_28272 # MOV operation
ref_51372 = ref_51124 # MOV operation
ref_51388 = ref_51372 # MOV operation
ref_51392 = (ref_51388 >> (0x1 & 0x3F)) # SHR operation
ref_51399 = ref_51392 # MOV operation
ref_51703 = ref_51399 # MOV operation
ref_51719 = (0xF & ref_51703) # AND operation
ref_52290 = ref_51719 # MOV operation
ref_52298 = (0x1 | ref_52290) # OR operation
ref_52930 = ref_52298 # MOV operation
ref_52934 = ((0x40 - ref_52930) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_52942 = ref_52934 # MOV operation
ref_53216 = ref_48091 # MOV operation
ref_53222 = ref_52942 # MOV operation
ref_53224 = ref_53216 # MOV operation
ref_53226 = (ref_53222 & 0xFFFFFFFF) # MOV operation
ref_53228 = ((ref_53224 << ((ref_53226 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_53235 = ref_53228 # MOV operation
ref_53531 = ref_45691 # MOV operation
ref_53537 = ref_53235 # MOV operation
ref_53539 = (ref_53537 | ref_53531) # OR operation
ref_53848 = ref_53539 # MOV operation
ref_53864 = ref_53848 # MOV operation
ref_53868 = (ref_53864 >> (0x2 & 0x3F)) # SHR operation
ref_53875 = ref_53868 # MOV operation
ref_54127 = ref_53875 # MOV operation
ref_54143 = (0x7 & ref_54127) # AND operation
ref_54770 = ref_54143 # MOV operation
ref_54778 = (0x1 | ref_54770) # OR operation
ref_55069 = ref_38189 # MOV operation
ref_55075 = ref_54778 # MOV operation
ref_55077 = ref_55069 # MOV operation
ref_55079 = (ref_55075 & 0xFFFFFFFF) # MOV operation
ref_55081 = ((ref_55077 << ((ref_55079 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_55088 = ref_55081 # MOV operation
ref_57736 = ref_366 # MOV operation
ref_57970 = ref_57736 # MOV operation
ref_57986 = ref_57970 # MOV operation
ref_57990 = (ref_57986 >> (0x5 & 0x3F)) # SHR operation
ref_57997 = ref_57990 # MOV operation
ref_60344 = ref_366 # MOV operation
ref_60917 = ref_60344 # MOV operation
ref_60925 = ref_60917 # MOV operation
ref_60929 = ((ref_60925 << (0x3B & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_60936 = ref_60929 # MOV operation
ref_61232 = ref_57997 # MOV operation
ref_61238 = ref_60936 # MOV operation
ref_61240 = (ref_61238 | ref_61232) # OR operation
ref_61549 = ref_61240 # MOV operation
ref_61563 = ref_55088 # MOV operation
ref_61565 = ref_61549 # MOV operation
ref_61567 = ((ref_61565 - ref_61563) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_61575 = ref_61567 # MOV operation
ref_61835 = ref_61575 # MOV operation
ref_65998 = (ref_20198 & 0xFF) # MOVZX operation
ref_66592 = (ref_65998 & 0xFF) # MOVZX operation
ref_70721 = (ref_20196 & 0xFF) # MOVZX operation
ref_74878 = (ref_70721 & 0xFF) # MOVZX operation
ref_75440 = (ref_66592 & 0xFF) # MOVZX operation
ref_79589 = (ref_75440 & 0xFF) # MOVZX operation
ref_79591 = ((ref_79589 & 0xFF) & 0xFF) # Byte reference - MOV operation
ref_83751 = (ref_20197 & 0xFF) # MOVZX operation
ref_84317 = (ref_83751 & 0xFF) # MOVZX operation
ref_88484 = (ref_74878 & 0xFF) # MOVZX operation
ref_92589 = (ref_88484 & 0xFF) # MOVZX operation
ref_92591 = ((ref_92589 & 0xFF) & 0xFF) # Byte reference - MOV operation
ref_93207 = (ref_84317 & 0xFF) # MOVZX operation
ref_97338 = (ref_93207 & 0xFF) # MOVZX operation
ref_97340 = ((ref_97338 & 0xFF) & 0xFF) # Byte reference - MOV operation
ref_101885 = ref_28272 # MOV operation
ref_104570 = ref_33612 # MOV operation
ref_104856 = ref_104570 # MOV operation
ref_104872 = (0xF & ref_104856) # AND operation
ref_105447 = ref_104872 # MOV operation
ref_105455 = ref_105447 # MOV operation
ref_105459 = ((ref_105455 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_105466 = ref_105459 # MOV operation
ref_105778 = ref_101885 # MOV operation
ref_105784 = ref_105466 # MOV operation
ref_105786 = (ref_105784 | ref_105778) # OR operation
ref_106051 = ref_105786 # MOV operation
ref_110536 = (((((ref_20200 & 0xFF)) << 8 | (ref_20201 & 0xFF)) << 8 | (ref_20202 & 0xFF)) << 8 | (ref_20203 & 0xFF)) # MOV operation
ref_110821 = (ref_110536 & 0xFFFFFFFF) # MOV operation
ref_118825 = (((((ref_79591 & 0xFF)) << 8 | (ref_92591 & 0xFF)) << 8 | (ref_97340 & 0xFF)) << 8 | (ref_20199 & 0xFF)) # MOV operation
ref_119099 = (ref_118825 & 0xFFFFFFFF) # MOV operation
ref_123552 = (ref_110821 & 0xFFFFFFFF) # MOV operation
ref_123830 = (ref_123552 & 0xFFFFFFFF) # MOV operation
ref_128309 = (ref_123830 & 0xFFFFFFFF) # MOV operation
ref_128561 = (ref_128309 & 0xFFFFFFFF) # MOV operation
ref_136603 = (ref_119099 & 0xFFFFFFFF) # MOV operation
ref_136841 = (ref_136603 & 0xFFFFFFFF) # MOV operation
ref_136843 = (((ref_136841 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_136844 = (((ref_136841 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_136845 = (((ref_136841 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_136846 = ((ref_136841 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_141322 = (ref_128561 & 0xFFFFFFFF) # MOV operation
ref_141607 = (ref_141322 & 0xFFFFFFFF) # MOV operation
ref_141609 = (((ref_141607 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_141610 = (((ref_141607 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_141611 = (((ref_141607 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_141612 = ((ref_141607 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_146070 = ref_33612 # MOV operation
ref_149072 = ref_61835 # MOV operation
ref_149353 = ref_149072 # MOV operation
ref_149369 = ref_149353 # MOV operation
ref_149373 = (ref_149369 >> (0x4 & 0x3F)) # SHR operation
ref_149380 = ref_149373 # MOV operation
ref_149646 = ref_149380 # MOV operation
ref_149662 = (0x7 & ref_149646) # AND operation
ref_150285 = ref_149662 # MOV operation
ref_150293 = (0x1 | ref_150285) # OR operation
ref_150558 = ref_146070 # MOV operation
ref_150564 = ref_150293 # MOV operation
ref_150566 = ref_150558 # MOV operation
ref_150568 = (ref_150564 & 0xFFFFFFFF) # MOV operation
ref_150570 = ((ref_150566 << ((ref_150568 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_150577 = ref_150570 # MOV operation
ref_153322 = ref_106051 # MOV operation
ref_153570 = ref_153322 # MOV operation
ref_153586 = (0xF & ref_153570) # AND operation
ref_154209 = ref_153586 # MOV operation
ref_154217 = (0x1 | ref_154209) # OR operation
ref_156606 = (((((((((ref_136843 & 0xFF)) << 8 | (ref_136844 & 0xFF)) << 8 | (ref_136845 & 0xFF)) << 8 | (ref_136846 & 0xFF)) << 8 | (ref_141609 & 0xFF)) << 8 | (ref_141610 & 0xFF)) << 8 | (ref_141611 & 0xFF)) << 8 | (ref_141612 & 0xFF)) # MOV operation
ref_156884 = ref_156606 # MOV operation
ref_156898 = ref_154217 # MOV operation
ref_156900 = ref_156884 # MOV operation
ref_156902 = (ref_156898 & 0xFFFFFFFF) # MOV operation
ref_156904 = (ref_156900 >> ((ref_156902 & 0xFF) & 0x3F)) # SHR operation
ref_156911 = ref_156904 # MOV operation
ref_159342 = (((((((((ref_136843 & 0xFF)) << 8 | (ref_136844 & 0xFF)) << 8 | (ref_136845 & 0xFF)) << 8 | (ref_136846 & 0xFF)) << 8 | (ref_141609 & 0xFF)) << 8 | (ref_141610 & 0xFF)) << 8 | (ref_141611 & 0xFF)) << 8 | (ref_141612 & 0xFF)) # MOV operation
ref_162053 = ref_106051 # MOV operation
ref_162287 = ref_162053 # MOV operation
ref_162303 = (0xF & ref_162287) # AND operation
ref_162930 = ref_162303 # MOV operation
ref_162938 = (0x1 | ref_162930) # OR operation
ref_163519 = ref_162938 # MOV operation
ref_163523 = ((0x40 - ref_163519) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_163531 = ref_163523 # MOV operation
ref_163843 = ref_159342 # MOV operation
ref_163849 = ref_163531 # MOV operation
ref_163851 = ref_163843 # MOV operation
ref_163853 = (ref_163849 & 0xFFFFFFFF) # MOV operation
ref_163855 = ((ref_163851 << ((ref_163853 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_163862 = ref_163855 # MOV operation
ref_164122 = ref_156911 # MOV operation
ref_164128 = ref_163862 # MOV operation
ref_164130 = (ref_164128 | ref_164122) # OR operation
ref_164423 = ref_164130 # MOV operation
ref_164437 = ref_150577 # MOV operation
ref_164439 = ((ref_164437 + ref_164423) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_164749 = ref_164439 # MOV operation
ref_165342 = ref_164749 # MOV operation
ref_165344 = ref_165342 # MOV operation


s.add(ref_165344 == int(sys.argv[1]))
collisions = 0
while s.check() == z3.sat and collisions < 10:
    print s.model()
    s.add(SymVar_0 != s.model()[SymVar_0])
    collisions += 1
