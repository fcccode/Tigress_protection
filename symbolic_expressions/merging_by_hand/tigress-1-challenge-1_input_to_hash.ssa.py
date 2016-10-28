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

ref_240 = SymVar_0
ref_255 = ref_240 # MOV operation
ref_2515 = ref_255 # MOV operation
ref_2757 = ref_2515 # MOV operation
ref_2767 = ref_2757 # MOV operation
ref_2771 = (ref_2767 >> (0xD & 0x3F)) # SHR operation
ref_2778 = ref_2771 # MOV operation
ref_3951 = ref_255 # MOV operation
ref_3985 = ref_3951 # MOV operation
ref_4367 = ref_3985 # MOV operation
ref_4381 = ref_4367 # MOV operation
ref_4385 = ((ref_4381 << (0x33 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_4392 = ref_4385 # MOV operation
ref_4418 = ref_2778 # MOV operation
ref_4430 = ref_4392 # MOV operation
ref_4432 = (ref_4418 | ref_4430) # OR operation
ref_4467 = ref_4432 # MOV operation
ref_4826 = ref_4467 # MOV operation
ref_4836 = ((0x2EA4A1C39AF5800 + ref_4826) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_4868 = ref_4836 # MOV operation
ref_4908 = ref_4868 # MOV operation
ref_6771 = ref_255 # MOV operation
ref_6989 = ref_6771 # MOV operation
ref_8211 = ref_4908 # MOV operation
ref_8241 = ref_6989 # MOV operation
ref_8253 = ref_8211 # MOV operation
ref_8255 = ref_8241 # MOV operation
ref_8257 = ((ref_8255 - ref_8253) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_8265 = ref_8257 # MOV operation
ref_8299 = ref_8265 # MOV operation
ref_8331 = ref_8299 # MOV operation
ref_10887 = ref_255 # MOV operation
ref_10913 = ref_10887 # MOV operation
ref_10933 = ((ref_10913 << (0x9 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_12137 = ref_255 # MOV operation
ref_12388 = ref_12137 # MOV operation
ref_12406 = ref_12388 # MOV operation
ref_12410 = (ref_12406 >> (0x37 & 0x3F)) # SHR operation
ref_12417 = ref_12410 # MOV operation
ref_12445 = ref_10933 # MOV operation
ref_12449 = ref_12417 # MOV operation
ref_12451 = (ref_12449 | ref_12445) # OR operation
ref_12482 = ref_12451 # MOV operation
ref_12712 = ref_12482 # MOV operation
ref_14742 = ref_255 # MOV operation
ref_15122 = ref_14742 # MOV operation
ref_15136 = (ref_15122 | 0x3E908497) # OR operation
ref_15181 = ref_15136 # MOV operation
ref_16332 = ref_8331 # MOV operation
ref_16358 = ref_16332 # MOV operation
ref_16372 = ref_16358 # MOV operation
ref_16376 = (ref_16372 >> (0x2 & 0x3F)) # SHR operation
ref_16383 = ref_16376 # MOV operation
ref_16417 = ref_16383 # MOV operation
ref_16799 = ref_16417 # MOV operation
ref_16805 = (0xF & ref_16799) # AND operation
ref_16836 = ref_16805 # MOV operation
ref_16922 = ref_16836 # MOV operation
ref_16928 = (0x1 | ref_16922) # OR operation
ref_18002 = ref_4908 # MOV operation
ref_18332 = ref_18002 # MOV operation
ref_18344 = ref_16928 # MOV operation
ref_18346 = ref_18332 # MOV operation
ref_18348 = (ref_18344 & 0xFFFFFFFF) # MOV operation
ref_18350 = (ref_18346 >> ((ref_18348 & 0xFF) & 0x3F)) # SHR operation
ref_18357 = ref_18350 # MOV operation
ref_18383 = ref_18357 # MOV operation
ref_19651 = ref_4908 # MOV operation
ref_19857 = ref_19651 # MOV operation
ref_20807 = ref_8331 # MOV operation
ref_21031 = ref_20807 # MOV operation
ref_21049 = ref_21031 # MOV operation
ref_21053 = (ref_21049 >> (0x2 & 0x3F)) # SHR operation
ref_21060 = ref_21053 # MOV operation
ref_21130 = ref_21060 # MOV operation
ref_21148 = (0xF & ref_21130) # AND operation
ref_21349 = ref_21148 # MOV operation
ref_21435 = ref_21349 # MOV operation
ref_21441 = (0x1 | ref_21435) # OR operation
ref_21478 = ref_21441 # MOV operation
ref_21482 = ((0x40 - ref_21478) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_21490 = ref_21482 # MOV operation
ref_21698 = ref_19857 # MOV operation
ref_21702 = ref_21490 # MOV operation
ref_21704 = ref_21698 # MOV operation
ref_21706 = (ref_21702 & 0xFFFFFFFF) # MOV operation
ref_21708 = ((ref_21704 << ((ref_21706 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_21715 = ref_21708 # MOV operation
ref_21743 = ref_18383 # MOV operation
ref_21747 = ref_21715 # MOV operation
ref_21749 = (ref_21747 | ref_21743) # OR operation
ref_21780 = ref_21749 # MOV operation
ref_22623 = ref_12712 # MOV operation
ref_23807 = ref_15181 # MOV operation
ref_23825 = ref_23807 # MOV operation
ref_23853 = ref_22623 # MOV operation
ref_23869 = ref_23825 # MOV operation
ref_23871 = ref_23853 # MOV operation
ref_23873 = ((ref_23871 - ref_23869) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_23881 = ref_23873 # MOV operation
ref_23919 = ref_21780 # MOV operation
ref_23931 = ref_23881 # MOV operation
ref_23933 = ((ref_23919 - ref_23931) & 0xFFFFFFFFFFFFFFFF) # CMP operation
ref_23935 = ((((ref_23919 ^ (ref_23931 ^ ref_23933)) ^ ((ref_23919 ^ ref_23933) & (ref_23919 ^ ref_23931))) >> 63) & 0x1) # Carry flag
ref_23941 = ((((ref_23931 >> 8) & 0xFFFFFFFFFFFFFF)) << 8 | (0x1 if ((ref_23935 & 0x1) == 0x1) else 0x0)) # SETB operation
ref_23943 = (ref_23941 & 0xFF) # MOVZX operation
ref_23971 = (ref_23943 & 0xFFFFFFFF) # MOV operation
ref_24323 = (ref_23971 & 0xFFFFFFFF) # MOV operation
ref_24325 = ((ref_24323 & 0xFFFFFFFF) & (ref_24323 & 0xFFFFFFFF)) # TEST operation
ref_24330 = (0x1 if ((ref_24325 & 0xFFFFFFFF) == 0x0) else 0x0) # Zero flag

if ((ref_24330 & 0x1) == 0x1):
    ref_240 = SymVar_0
    ref_255 = ref_240 # MOV operation
    ref_2515 = ref_255 # MOV operation
    ref_2757 = ref_2515 # MOV operation
    ref_2767 = ref_2757 # MOV operation
    ref_2771 = (ref_2767 >> (0xD & 0x3F)) # SHR operation
    ref_2778 = ref_2771 # MOV operation
    ref_3951 = ref_255 # MOV operation
    ref_3985 = ref_3951 # MOV operation
    ref_4367 = ref_3985 # MOV operation
    ref_4381 = ref_4367 # MOV operation
    ref_4385 = ((ref_4381 << (0x33 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_4392 = ref_4385 # MOV operation
    ref_4418 = ref_2778 # MOV operation
    ref_4430 = ref_4392 # MOV operation
    ref_4432 = (ref_4418 | ref_4430) # OR operation
    ref_4467 = ref_4432 # MOV operation
    ref_4826 = ref_4467 # MOV operation
    ref_4836 = ((0x2EA4A1C39AF5800 + ref_4826) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_4868 = ref_4836 # MOV operation
    ref_4908 = ref_4868 # MOV operation
    ref_6771 = ref_255 # MOV operation
    ref_6989 = ref_6771 # MOV operation
    ref_8211 = ref_4908 # MOV operation
    ref_8241 = ref_6989 # MOV operation
    ref_8253 = ref_8211 # MOV operation
    ref_8255 = ref_8241 # MOV operation
    ref_8257 = ((ref_8255 - ref_8253) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_8265 = ref_8257 # MOV operation
    ref_8299 = ref_8265 # MOV operation
    ref_8331 = ref_8299 # MOV operation
    ref_10887 = ref_255 # MOV operation
    ref_10913 = ref_10887 # MOV operation
    ref_10933 = ((ref_10913 << (0x9 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_12137 = ref_255 # MOV operation
    ref_12388 = ref_12137 # MOV operation
    ref_12406 = ref_12388 # MOV operation
    ref_12410 = (ref_12406 >> (0x37 & 0x3F)) # SHR operation
    ref_12417 = ref_12410 # MOV operation
    ref_12445 = ref_10933 # MOV operation
    ref_12449 = ref_12417 # MOV operation
    ref_12451 = (ref_12449 | ref_12445) # OR operation
    ref_12482 = ref_12451 # MOV operation
    ref_12712 = ref_12482 # MOV operation
    ref_14742 = ref_255 # MOV operation
    ref_15122 = ref_14742 # MOV operation
    ref_15136 = (ref_15122 | 0x3E908497) # OR operation
    ref_15181 = ref_15136 # MOV operation
    ref_27355 = ref_8331 # MOV operation
    ref_27399 = ref_27355 # MOV operation
    ref_27417 = ref_27399 # MOV operation
    ref_27421 = (ref_27417 >> (0x4 & 0x3F)) # SHR operation
    ref_27428 = ref_27421 # MOV operation
    ref_27766 = ref_27428 # MOV operation
    ref_27852 = ref_27766 # MOV operation
    ref_27858 = (0xF & ref_27852) # AND operation
    ref_28120 = ref_27858 # MOV operation
    ref_28134 = (ref_28120 | 0x1) # OR operation
    ref_29145 = ref_4908 # MOV operation
    ref_29179 = ref_29145 # MOV operation
    ref_29195 = ref_28134 # MOV operation
    ref_29197 = (ref_29195 & 0xFFFFFFFF) # MOV operation
    ref_29199 = ((ref_29179 << ((ref_29197 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_30423 = ref_4908 # MOV operation
    ref_32323 = ref_8331 # MOV operation
    ref_32349 = ref_32323 # MOV operation
    ref_32363 = ref_32349 # MOV operation
    ref_32367 = (ref_32363 >> (0x4 & 0x3F)) # SHR operation
    ref_32374 = ref_32367 # MOV operation
    ref_32798 = ref_32374 # MOV operation
    ref_32808 = (0xF & ref_32798) # AND operation
    ref_33011 = ref_32808 # MOV operation
    ref_33097 = ref_33011 # MOV operation
    ref_33103 = (0x1 | ref_33097) # OR operation
    ref_33306 = ref_33103 # MOV operation
    ref_33540 = ref_33306 # MOV operation
    ref_33544 = ((0x40 - ref_33540) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_33552 = ref_33544 # MOV operation
    ref_33750 = ref_33552 # MOV operation
    ref_33966 = ref_30423 # MOV operation
    ref_33974 = ref_33750 # MOV operation
    ref_33976 = ref_33966 # MOV operation
    ref_33978 = (ref_33974 & 0xFFFFFFFF) # MOV operation
    ref_33980 = (ref_33976 >> ((ref_33978 & 0xFF) & 0x3F)) # SHR operation
    ref_33987 = ref_33980 # MOV operation
    ref_34193 = ref_29199 # MOV operation
    ref_34197 = ref_33987 # MOV operation
    ref_34199 = (ref_34197 | ref_34193) # OR operation
    ref_35712 = ref_12712 # MOV operation
    ref_35730 = ref_35712 # MOV operation
    ref_37220 = ref_15181 # MOV operation
    ref_37426 = ref_35730 # MOV operation
    ref_37430 = ref_37220 # MOV operation
    ref_37432 = (ref_37430 | ref_37426) # OR operation
    ref_37687 = ref_37432 # MOV operation
    ref_37705 = ref_37687 # MOV operation
    ref_37709 = (ref_37705 >> (0x4 & 0x3F)) # SHR operation
    ref_37716 = ref_37709 # MOV operation
    ref_38120 = ref_37716 # MOV operation
    ref_38130 = (0x7 & ref_38120) # AND operation
    ref_38465 = ref_38130 # MOV operation
    ref_38689 = ref_38465 # MOV operation
    ref_38695 = (0x1 | ref_38689) # OR operation
    ref_38898 = ref_38695 # MOV operation
    ref_39114 = ref_34199 # MOV operation
    ref_39122 = ref_38898 # MOV operation
    ref_39124 = ref_39114 # MOV operation
    ref_39126 = (ref_39122 & 0xFFFFFFFF) # MOV operation
    ref_39128 = (ref_39124 >> ((ref_39126 & 0xFF) & 0x3F)) # SHR operation
    ref_39135 = ref_39128 # MOV operation
    ref_39333 = ref_39135 # MOV operation
    ref_39697 = ref_39333 # MOV operation
    ref_40154 = ref_39697 # MOV operation
    ref_40156 = ref_40154 # MOV operation
    endb = ref_40156

else:
    ref_240 = SymVar_0
    ref_255 = ref_240 # MOV operation
    ref_2515 = ref_255 # MOV operation
    ref_2757 = ref_2515 # MOV operation
    ref_2767 = ref_2757 # MOV operation
    ref_2771 = (ref_2767 >> (0xD & 0x3F)) # SHR operation
    ref_2778 = ref_2771 # MOV operation
    ref_3951 = ref_255 # MOV operation
    ref_3985 = ref_3951 # MOV operation
    ref_4367 = ref_3985 # MOV operation
    ref_4381 = ref_4367 # MOV operation
    ref_4385 = ((ref_4381 << (0x33 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_4392 = ref_4385 # MOV operation
    ref_4418 = ref_2778 # MOV operation
    ref_4430 = ref_4392 # MOV operation
    ref_4432 = (ref_4418 | ref_4430) # OR operation
    ref_4467 = ref_4432 # MOV operation
    ref_4826 = ref_4467 # MOV operation
    ref_4836 = ((0x2EA4A1C39AF5800 + ref_4826) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_4868 = ref_4836 # MOV operation
    ref_4908 = ref_4868 # MOV operation
    ref_6771 = ref_255 # MOV operation
    ref_6989 = ref_6771 # MOV operation
    ref_8211 = ref_4908 # MOV operation
    ref_8241 = ref_6989 # MOV operation
    ref_8253 = ref_8211 # MOV operation
    ref_8255 = ref_8241 # MOV operation
    ref_8257 = ((ref_8255 - ref_8253) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_8265 = ref_8257 # MOV operation
    ref_8299 = ref_8265 # MOV operation
    ref_8331 = ref_8299 # MOV operation
    ref_8333 = ((ref_8331 >> 56) & 0xFF) # Byte reference - MOV operation
    ref_8334 = ((ref_8331 >> 48) & 0xFF) # Byte reference - MOV operation
    ref_8335 = ((ref_8331 >> 40) & 0xFF) # Byte reference - MOV operation
    ref_8336 = ((ref_8331 >> 32) & 0xFF) # Byte reference - MOV operation
    ref_8337 = ((ref_8331 >> 24) & 0xFF) # Byte reference - MOV operation
    ref_8338 = ((ref_8331 >> 16) & 0xFF) # Byte reference - MOV operation
    ref_8339 = ((ref_8331 >> 8) & 0xFF) # Byte reference - MOV operation
    ref_8340 = (ref_8331 & 0xFF) # Byte reference - MOV operation
    ref_10887 = ref_255 # MOV operation
    ref_10913 = ref_10887 # MOV operation
    ref_10933 = ((ref_10913 << (0x9 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_12137 = ref_255 # MOV operation
    ref_12388 = ref_12137 # MOV operation
    ref_12406 = ref_12388 # MOV operation
    ref_12410 = (ref_12406 >> (0x37 & 0x3F)) # SHR operation
    ref_12417 = ref_12410 # MOV operation
    ref_12445 = ref_10933 # MOV operation
    ref_12449 = ref_12417 # MOV operation
    ref_12451 = (ref_12449 | ref_12445) # OR operation
    ref_12482 = ref_12451 # MOV operation
    ref_12712 = ref_12482 # MOV operation
    ref_14742 = ref_255 # MOV operation
    ref_15122 = ref_14742 # MOV operation
    ref_15136 = (ref_15122 | 0x3E908497) # OR operation
    ref_15181 = ref_15136 # MOV operation
    ref_26795 = (((((ref_8333 & 0xFF)) << 8 | (ref_8334 & 0xFF)) << 8 | (ref_8335 & 0xFF)) << 8 | (ref_8336 & 0xFF)) # MOV operation
    ref_26821 = (ref_26795 & 0xFFFFFFFF) # MOV operation
    ref_30657 = (((((ref_8337 & 0xFF)) << 8 | (ref_8338 & 0xFF)) << 8 | (ref_8339 & 0xFF)) << 8 | (ref_8340 & 0xFF)) # MOV operation
    ref_30683 = (ref_30657 & 0xFFFFFFFF) # MOV operation
    ref_30685 = (((ref_30683 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
    ref_30686 = (((ref_30683 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
    ref_30687 = (((ref_30683 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
    ref_30688 = ((ref_30683 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
    ref_32732 = (ref_26821 & 0xFFFFFFFF) # MOV operation
    ref_32928 = (ref_32732 & 0xFFFFFFFF) # MOV operation
    ref_32930 = (((ref_32928 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
    ref_32931 = (((ref_32928 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
    ref_32932 = (((ref_32928 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
    ref_32933 = ((ref_32928 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
    ref_35071 = ref_4908 # MOV operation
    ref_36277 = ref_4908 # MOV operation
    ref_36625 = ref_36277 # MOV operation
    ref_36711 = ref_36625 # MOV operation
    ref_36717 = (0x3F & ref_36711) # AND operation
    ref_36748 = ref_36717 # MOV operation
    ref_37004 = ref_36748 # MOV operation
    ref_37018 = ref_37004 # MOV operation
    ref_37022 = ((ref_37018 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_37029 = ref_37022 # MOV operation
    ref_37055 = ref_35071 # MOV operation
    ref_37067 = ref_37029 # MOV operation
    ref_37069 = (ref_37055 | ref_37067) # OR operation
    ref_37114 = ref_37069 # MOV operation
    ref_39606 = ref_15181 # MOV operation
    ref_39965 = ref_39606 # MOV operation
    ref_41152 = ref_37114 # MOV operation
    ref_41526 = ref_41152 # MOV operation
    ref_41536 = (0x1F & ref_41526) # AND operation
    ref_41567 = ref_41536 # MOV operation
    ref_41587 = ((ref_41567 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_41622 = ref_41587 # MOV operation
    ref_41650 = ref_39965 # MOV operation
    ref_41654 = ref_41622 # MOV operation
    ref_41656 = (ref_41654 | ref_41650) # OR operation
    ref_41687 = ref_41656 # MOV operation
    ref_41912 = ref_41687 # MOV operation
    ref_43460 = ref_37114 # MOV operation
    ref_43494 = ref_43460 # MOV operation
    ref_44584 = ref_37114 # MOV operation
    ref_45335 = ref_12712 # MOV operation
    ref_45361 = ref_45335 # MOV operation
    ref_45579 = ref_44584 # MOV operation
    ref_45587 = ref_45361 # MOV operation
    ref_45589 = ((ref_45587 + ref_45579) & 0xFFFFFFFFFFFFFFFF) # ADD operation
    ref_45621 = ref_45589 # MOV operation
    ref_45707 = ref_45621 # MOV operation
    ref_45713 = (0x1F & ref_45707) # AND operation
    ref_46050 = ref_45713 # MOV operation
    ref_46070 = ((ref_46050 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_46105 = ref_46070 # MOV operation
    ref_46133 = ref_43494 # MOV operation
    ref_46137 = ref_46105 # MOV operation
    ref_46139 = (ref_46137 | ref_46133) # OR operation
    ref_46170 = ref_46139 # MOV operation
    ref_49032 = (((((((((ref_30685 & 0xFF)) << 8 | (ref_30686 & 0xFF)) << 8 | (ref_30687 & 0xFF)) << 8 | (ref_30688 & 0xFF)) << 8 | (ref_32930 & 0xFF)) << 8 | (ref_32931 & 0xFF)) << 8 | (ref_32932 & 0xFF)) << 8 | (ref_32933 & 0xFF)) # MOV operation
    ref_49076 = ref_49032 # MOV operation
    ref_49094 = ref_49076 # MOV operation
    ref_49098 = (ref_49094 >> (0x4 & 0x3F)) # SHR operation
    ref_49105 = ref_49098 # MOV operation
    ref_49443 = ref_49105 # MOV operation
    ref_49529 = ref_49443 # MOV operation
    ref_49535 = (0xF & ref_49529) # AND operation
    ref_49797 = ref_49535 # MOV operation
    ref_49811 = (ref_49797 | 0x1) # OR operation
    ref_50822 = ref_46170 # MOV operation
    ref_50856 = ref_50822 # MOV operation
    ref_50872 = ref_49811 # MOV operation
    ref_50874 = (ref_50872 & 0xFFFFFFFF) # MOV operation
    ref_50876 = ((ref_50856 << ((ref_50874 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
    ref_52100 = ref_46170 # MOV operation
    ref_54000 = (((((((((ref_30685 & 0xFF)) << 8 | (ref_30686 & 0xFF)) << 8 | (ref_30687 & 0xFF)) << 8 | (ref_30688 & 0xFF)) << 8 | (ref_32930 & 0xFF)) << 8 | (ref_32931 & 0xFF)) << 8 | (ref_32932 & 0xFF)) << 8 | (ref_32933 & 0xFF)) # MOV operation
    ref_54026 = ref_54000 # MOV operation
    ref_54040 = ref_54026 # MOV operation
    ref_54044 = (ref_54040 >> (0x4 & 0x3F)) # SHR operation
    ref_54051 = ref_54044 # MOV operation
    ref_54475 = ref_54051 # MOV operation
    ref_54485 = (0xF & ref_54475) # AND operation
    ref_54688 = ref_54485 # MOV operation
    ref_54774 = ref_54688 # MOV operation
    ref_54780 = (0x1 | ref_54774) # OR operation
    ref_54983 = ref_54780 # MOV operation
    ref_55217 = ref_54983 # MOV operation
    ref_55221 = ((0x40 - ref_55217) & 0xFFFFFFFFFFFFFFFF) # SUB operation
    ref_55229 = ref_55221 # MOV operation
    ref_55427 = ref_55229 # MOV operation
    ref_55643 = ref_52100 # MOV operation
    ref_55651 = ref_55427 # MOV operation
    ref_55653 = ref_55643 # MOV operation
    ref_55655 = (ref_55651 & 0xFFFFFFFF) # MOV operation
    ref_55657 = (ref_55653 >> ((ref_55655 & 0xFF) & 0x3F)) # SHR operation
    ref_55664 = ref_55657 # MOV operation
    ref_55870 = ref_50876 # MOV operation
    ref_55874 = ref_55664 # MOV operation
    ref_55876 = (ref_55874 | ref_55870) # OR operation
    ref_57389 = ref_12712 # MOV operation
    ref_57407 = ref_57389 # MOV operation
    ref_58897 = ref_41912 # MOV operation
    ref_59103 = ref_57407 # MOV operation
    ref_59107 = ref_58897 # MOV operation
    ref_59109 = (ref_59107 | ref_59103) # OR operation
    ref_59364 = ref_59109 # MOV operation
    ref_59382 = ref_59364 # MOV operation
    ref_59386 = (ref_59382 >> (0x4 & 0x3F)) # SHR operation
    ref_59393 = ref_59386 # MOV operation
    ref_59797 = ref_59393 # MOV operation
    ref_59807 = (0x7 & ref_59797) # AND operation
    ref_60142 = ref_59807 # MOV operation
    ref_60366 = ref_60142 # MOV operation
    ref_60372 = (0x1 | ref_60366) # OR operation
    ref_60575 = ref_60372 # MOV operation
    ref_60791 = ref_55876 # MOV operation
    ref_60799 = ref_60575 # MOV operation
    ref_60801 = ref_60791 # MOV operation
    ref_60803 = (ref_60799 & 0xFFFFFFFF) # MOV operation
    ref_60805 = (ref_60801 >> ((ref_60803 & 0xFF) & 0x3F)) # SHR operation
    ref_60812 = ref_60805 # MOV operation
    ref_61010 = ref_60812 # MOV operation
    ref_61374 = ref_61010 # MOV operation
    ref_61831 = ref_61374 # MOV operation
    ref_61833 = ref_61831 # MOV operation
    endb = ref_61833

print endb & 0xffffffffffffffff
