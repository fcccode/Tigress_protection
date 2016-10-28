#!/usr/bin/env python2
## -*- coding: utf-8 -*-
##
## Triton
##

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_248 = SymVar_0
ref_263 = ref_248 # MOV operation
ref_2497 = ref_263 # MOV operation
ref_2531 = ref_2497 # MOV operation
ref_2551 = ((ref_2531 << (0x3D & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_2588 = ref_2551 # MOV operation
ref_3875 = ref_263 # MOV operation
ref_4074 = ref_3875 # MOV operation
ref_4132 = ref_4074 # MOV operation
ref_4150 = ref_4132 # MOV operation
ref_4154 = (ref_4150 >> (0x3 & 0x3F)) # SHR operation
ref_4161 = ref_4154 # MOV operation
ref_4187 = ref_4161 # MOV operation
ref_4199 = ref_2588 # MOV operation
ref_4201 = (ref_4187 | ref_4199) # OR operation
ref_4238 = ref_4201 # MOV operation
ref_4606 = ref_4238 # MOV operation
ref_4624 = ref_4606 # MOV operation
ref_4626 = ((ref_4624 - 0x3FEFFF7F) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_4634 = ref_4626 # MOV operation
ref_4660 = ref_4634 # MOV operation
ref_4704 = ref_4660 # MOV operation
ref_4706 = ((ref_4704 >> 56) & 0xFF) # Byte reference - MOV operation
ref_4707 = ((ref_4704 >> 48) & 0xFF) # Byte reference - MOV operation
ref_4708 = ((ref_4704 >> 40) & 0xFF) # Byte reference - MOV operation
ref_4709 = ((ref_4704 >> 32) & 0xFF) # Byte reference - MOV operation
ref_4710 = ((ref_4704 >> 24) & 0xFF) # Byte reference - MOV operation
ref_4711 = ((ref_4704 >> 16) & 0xFF) # Byte reference - MOV operation
ref_4712 = ((ref_4704 >> 8) & 0xFF) # Byte reference - MOV operation
ref_4713 = (ref_4704 & 0xFF) # Byte reference - MOV operation
ref_5446 = ref_4704 # MOV operation
ref_7045 = ref_263 # MOV operation
ref_7079 = ref_7045 # MOV operation
ref_7083 = ref_5446 # MOV operation
ref_7085 = (ref_7079 | ref_7083) # OR operation
ref_7120 = ref_7085 # MOV operation
ref_7516 = ref_7120 # MOV operation
ref_7534 = ref_7516 # MOV operation
ref_7536 = ((ref_7534 - 0x11E59B96) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_7544 = ref_7536 # MOV operation
ref_8228 = ref_7544 # MOV operation
ref_8230 = ((ref_8228 >> 56) & 0xFF) # Byte reference - MOV operation
ref_8231 = ((ref_8228 >> 48) & 0xFF) # Byte reference - MOV operation
ref_8232 = ((ref_8228 >> 40) & 0xFF) # Byte reference - MOV operation
ref_8233 = ((ref_8228 >> 32) & 0xFF) # Byte reference - MOV operation
ref_8234 = ((ref_8228 >> 24) & 0xFF) # Byte reference - MOV operation
ref_8235 = ((ref_8228 >> 16) & 0xFF) # Byte reference - MOV operation
ref_8236 = ((ref_8228 >> 8) & 0xFF) # Byte reference - MOV operation
ref_8237 = (ref_8228 & 0xFF) # Byte reference - MOV operation
ref_9084 = ref_8228 # MOV operation
ref_9176 = ref_9084 # MOV operation
ref_9192 = ((ref_9176 << (0x7 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_10084 = ref_4704 # MOV operation
ref_10288 = ref_10084 # MOV operation
ref_11912 = ref_263 # MOV operation
ref_11946 = ref_11912 # MOV operation
ref_11962 = ref_10288 # MOV operation
ref_11964 = ((sx(0x40, ref_11946) * sx(0x40, ref_11962)) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_11998 = ref_11964 # MOV operation
ref_12032 = ref_11998 # MOV operation
ref_12048 = ref_9192 # MOV operation
ref_12050 = ((sx(0x40, ref_12032) * sx(0x40, ref_12048)) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_12084 = ref_12050 # MOV operation
ref_13095 = ref_12084 # MOV operation
ref_15133 = ref_263 # MOV operation
ref_15167 = ref_15133 # MOV operation
ref_15173 = ((ref_15167 - 0x2000000007A4C37E) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_15209 = ref_15173 # MOV operation
ref_16115 = ref_15209 # MOV operation
ref_19232 = (((((ref_4706 & 0xFF)) << 8 | (ref_4707 & 0xFF)) << 8 | (ref_4708 & 0xFF)) << 8 | (ref_4709 & 0xFF)) # MOV operation
ref_19324 = (ref_19232 & 0xFFFFFFFF) # MOV operation
ref_21486 = (((((ref_4710 & 0xFF)) << 8 | (ref_4711 & 0xFF)) << 8 | (ref_4712 & 0xFF)) << 8 | (ref_4713 & 0xFF)) # MOV operation
ref_23301 = (ref_21486 & 0xFFFFFFFF) # MOV operation
ref_23303 = (((ref_23301 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_23304 = (((ref_23301 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_23305 = (((ref_23301 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_23306 = ((ref_23301 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_25114 = (ref_19324 & 0xFFFFFFFF) # MOV operation
ref_25148 = (ref_25114 & 0xFFFFFFFF) # MOV operation
ref_25150 = (((ref_25148 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_25151 = (((ref_25148 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_25152 = (((ref_25148 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_25153 = ((ref_25148 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_25876 = ref_13095 # MOV operation
ref_27028 = ref_13095 # MOV operation
ref_27060 = ref_27028 # MOV operation
ref_27072 = ref_25876 # MOV operation
ref_27074 = ((ref_27072 + ref_27060) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_27422 = ref_27074 # MOV operation
ref_27490 = ref_27422 # MOV operation
ref_27508 = (ref_27490 & 0x3F) # AND operation
ref_27543 = ref_27508 # MOV operation
ref_27931 = ref_27543 # MOV operation
ref_27947 = ((ref_27931 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_28879 = (((((((((ref_23303 & 0xFF)) << 8 | (ref_23304 & 0xFF)) << 8 | (ref_23305 & 0xFF)) << 8 | (ref_23306 & 0xFF)) << 8 | (ref_25150 & 0xFF)) << 8 | (ref_25151 & 0xFF)) << 8 | (ref_25152 & 0xFF)) << 8 | (ref_25153 & 0xFF)) # MOV operation
ref_28913 = ref_28879 # MOV operation
ref_28929 = ref_27947 # MOV operation
ref_28931 = (ref_28913 | ref_28929) # OR operation
ref_29283 = ref_28931 # MOV operation
ref_30220 = ref_29283 # MOV operation
ref_33861 = (((((ref_8230 & 0xFF)) << 8 | (ref_8231 & 0xFF)) << 8 | (ref_8232 & 0xFF)) << 8 | (ref_8233 & 0xFF)) # MOV operation
ref_33953 = (ref_33861 & 0xFFFFFFFF) # MOV operation
ref_36115 = (((((ref_8234 & 0xFF)) << 8 | (ref_8235 & 0xFF)) << 8 | (ref_8236 & 0xFF)) << 8 | (ref_8237 & 0xFF)) # MOV operation
ref_37930 = (ref_36115 & 0xFFFFFFFF) # MOV operation
ref_37932 = (((ref_37930 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_37933 = (((ref_37930 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_37934 = (((ref_37930 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_37935 = ((ref_37930 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_39743 = (ref_33953 & 0xFFFFFFFF) # MOV operation
ref_39777 = (ref_39743 & 0xFFFFFFFF) # MOV operation
ref_39779 = (((ref_39777 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_39780 = (((ref_39777 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_39781 = (((ref_39777 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_39782 = ((ref_39777 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_40505 = ref_13095 # MOV operation
ref_41657 = ref_16115 # MOV operation
ref_41689 = ref_41657 # MOV operation
ref_41701 = ref_40505 # MOV operation
ref_41703 = ((ref_41701 + ref_41689) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_42051 = ref_41703 # MOV operation
ref_42119 = ref_42051 # MOV operation
ref_42137 = (ref_42119 & 0x3F) # AND operation
ref_42172 = ref_42137 # MOV operation
ref_42560 = ref_42172 # MOV operation
ref_42576 = ((ref_42560 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_43508 = (((((((((ref_37932 & 0xFF)) << 8 | (ref_37933 & 0xFF)) << 8 | (ref_37934 & 0xFF)) << 8 | (ref_37935 & 0xFF)) << 8 | (ref_39779 & 0xFF)) << 8 | (ref_39780 & 0xFF)) << 8 | (ref_39781 & 0xFF)) << 8 | (ref_39782 & 0xFF)) # MOV operation
ref_43542 = ref_43508 # MOV operation
ref_43558 = ref_42576 # MOV operation
ref_43560 = (ref_43542 | ref_43558) # OR operation
ref_43912 = ref_43560 # MOV operation
ref_44849 = ref_43912 # MOV operation
ref_44851 = ((ref_44849 >> 56) & 0xFF) # Byte reference - MOV operation
ref_44852 = ((ref_44849 >> 48) & 0xFF) # Byte reference - MOV operation
ref_44853 = ((ref_44849 >> 40) & 0xFF) # Byte reference - MOV operation
ref_44854 = ((ref_44849 >> 32) & 0xFF) # Byte reference - MOV operation
ref_44855 = ((ref_44849 >> 24) & 0xFF) # Byte reference - MOV operation
ref_44856 = ((ref_44849 >> 16) & 0xFF) # Byte reference - MOV operation
ref_44857 = ((ref_44849 >> 8) & 0xFF) # Byte reference - MOV operation
ref_44858 = (ref_44849 & 0xFF) # Byte reference - MOV operation
ref_48996 = (ref_44853 & 0xFF) # MOVZX operation
ref_49354 = (ref_48996 & 0xFF) # MOVZX operation
ref_52344 = (ref_44857 & 0xFF) # MOVZX operation
ref_52560 = (ref_52344 & 0xFF) # MOVZX operation
ref_52578 = (ref_52560 & 0xFF) # MOVZX operation
ref_52580 = ((ref_52578 & 0xFF) & 0xFF) # Byte reference - MOV operation
ref_54352 = (ref_49354 & 0xFF) # MOVZX operation
ref_54376 = (ref_54352 & 0xFF) # MOVZX operation
ref_54394 = (ref_54376 & 0xFF) # MOVZX operation
ref_54396 = ((ref_54394 & 0xFF) & 0xFF) # Byte reference - MOV operation
ref_56671 = ref_30220 # MOV operation
ref_58129 = (((((((((ref_44851 & 0xFF)) << 8 | (ref_44852 & 0xFF)) << 8 | (ref_52580 & 0xFF)) << 8 | (ref_44854 & 0xFF)) << 8 | (ref_44855 & 0xFF)) << 8 | (ref_44856 & 0xFF)) << 8 | (ref_54396 & 0xFF)) << 8 | (ref_44858 & 0xFF)) # MOV operation
ref_58353 = ref_56671 # MOV operation
ref_58357 = ref_58129 # MOV operation
ref_58359 = ((ref_58357 + ref_58353) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_58569 = ref_58359 # MOV operation
ref_60728 = ref_13095 # MOV operation
ref_60932 = ref_60728 # MOV operation
ref_62126 = ref_16115 # MOV operation
ref_62330 = ref_62126 # MOV operation
ref_62686 = ref_60932 # MOV operation
ref_62702 = ref_62330 # MOV operation
ref_62704 = (ref_62686 & ref_62702) # AND operation
ref_63413 = ref_62704 # MOV operation
ref_63431 = (ref_63413 & 0xF) # AND operation
ref_63641 = ref_63431 # MOV operation
ref_63867 = ref_63641 # MOV operation
ref_63881 = (ref_63867 | 0x1) # OR operation
ref_64112 = ref_63881 # MOV operation
ref_64116 = ((0x40 - ref_64112) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_64124 = ref_64116 # MOV operation
ref_64328 = ref_64124 # MOV operation
ref_64566 = ref_58569 # MOV operation
ref_64574 = ref_64328 # MOV operation
ref_64576 = ref_64566 # MOV operation
ref_64578 = (ref_64574 & 0xFFFFFFFF) # MOV operation
ref_64580 = (ref_64576 >> ((ref_64578 & 0xFF) & 0x3F)) # SHR operation
ref_64587 = ref_64580 # MOV operation
ref_66455 = ref_13095 # MOV operation
ref_66659 = ref_66455 # MOV operation
ref_68244 = ref_16115 # MOV operation
ref_68468 = ref_68244 # MOV operation
ref_68824 = ref_66659 # MOV operation
ref_68840 = ref_68468 # MOV operation
ref_68842 = (ref_68824 & ref_68840) # AND operation
ref_69551 = ref_68842 # MOV operation
ref_69569 = (ref_69551 & 0xF) # AND operation
ref_69779 = ref_69569 # MOV operation
ref_70005 = ref_69779 # MOV operation
ref_70019 = (ref_70005 | 0x1) # OR operation
ref_71916 = (((((((((ref_44851 & 0xFF)) << 8 | (ref_44852 & 0xFF)) << 8 | (ref_52580 & 0xFF)) << 8 | (ref_44854 & 0xFF)) << 8 | (ref_44855 & 0xFF)) << 8 | (ref_44856 & 0xFF)) << 8 | (ref_54396 & 0xFF)) << 8 | (ref_44858 & 0xFF)) # MOV operation
ref_73579 = ref_30220 # MOV operation
ref_73927 = ref_73579 # MOV operation
ref_73939 = ref_71916 # MOV operation
ref_73941 = ((ref_73939 + ref_73927) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_74269 = ref_73941 # MOV operation
ref_74285 = ref_70019 # MOV operation
ref_74287 = (ref_74285 & 0xFFFFFFFF) # MOV operation
ref_74289 = ((ref_74269 << ((ref_74287 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_74519 = ref_74289 # MOV operation
ref_74745 = ref_74519 # MOV operation
ref_74757 = ref_64587 # MOV operation
ref_74759 = (ref_74745 | ref_74757) # OR operation
ref_75000 = ref_74759 # MOV operation
ref_75572 = ref_75000 # MOV operation
ref_75574 = ref_75572 # MOV operation

print ref_75574 & 0xffffffffffffffff
