#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_679 = SymVar_0
ref_694 = ref_679 # MOV operation
ref_30052 = ref_694 # MOV operation
ref_33571 = ref_30052 # MOV operation
ref_33577 = ref_33571 # MOV operation
ref_33581 = (ref_33577 >> (0x3B & 0x3F)) # SHR operation
ref_33588 = ref_33581 # MOV operation
ref_49010 = ref_694 # MOV operation
ref_50262 = ref_49010 # MOV operation
ref_50278 = ref_50262 # MOV operation
ref_50282 = ((ref_50278 << (0x5 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_50289 = ref_50282 # MOV operation
ref_51654 = ref_50289 # MOV operation
ref_51668 = ref_33588 # MOV operation
ref_51670 = (~(ref_51668) & 0xFFFFFFFFFFFFFFFF) # NOT operation
ref_51672 = (ref_51654 & ref_51670) # AND operation
ref_51691 = ref_33588 # MOV operation
ref_51693 = ((ref_51691 + ref_51672) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_53806 = ref_51693 # MOV operation
ref_53822 = ref_53806 # MOV operation
ref_53824 = ((ref_53822 - 0x153D92600000) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_53836 = ref_51693 # MOV operation
ref_53854 = (0xFFFFEAC26D9FFFFF | ref_53836) # OR operation
ref_53861 = ((ref_53854 + ref_53854) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_53869 = ref_53824 # MOV operation
ref_53871 = ((ref_53869 - ref_53861) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_53879 = ref_53871 # MOV operation
ref_53881 = ((ref_53879 - 0x2) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_55581 = ref_53881 # MOV operation
ref_71166 = ref_694 # MOV operation
ref_71703 = ref_71166 # MOV operation
ref_71729 = (((0x0) << 64 | ref_71703) / (((((((((0x0 & 0xFF)) << 8 | (0x0 & 0xFF)) << 8 | (0x0 & 0xFF)) << 8 | (0x0 & 0xFF)) << 8 | (0x0 & 0xFF)) << 8 | (0x0 & 0xFF)) << 8 | (0x0 & 0xFF)) << 8 | (0x9 & 0xFF))) # DIV operation
ref_75455 = ref_71729 # MOV operation
ref_75461 = ((0x6DE1F60E00 + ref_75455) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_87543 = ref_75461 # MOV operation
ref_87545 = ((ref_87543 >> 56) & 0xFF) # Byte reference - MOV operation
ref_87546 = ((ref_87543 >> 48) & 0xFF) # Byte reference - MOV operation
ref_87547 = ((ref_87543 >> 40) & 0xFF) # Byte reference - MOV operation
ref_87548 = ((ref_87543 >> 32) & 0xFF) # Byte reference - MOV operation
ref_87549 = ((ref_87543 >> 24) & 0xFF) # Byte reference - MOV operation
ref_87550 = ((ref_87543 >> 16) & 0xFF) # Byte reference - MOV operation
ref_87551 = ((ref_87543 >> 8) & 0xFF) # Byte reference - MOV operation
ref_87552 = (ref_87543 & 0xFF) # Byte reference - MOV operation
ref_119757 = ref_694 # MOV operation
ref_121009 = ref_119757 # MOV operation
ref_121025 = ref_121009 # MOV operation
ref_121029 = ((ref_121025 << (0x39 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_121036 = ref_121029 # MOV operation
ref_135412 = ref_694 # MOV operation
ref_138931 = ref_135412 # MOV operation
ref_138937 = ref_138931 # MOV operation
ref_138941 = (ref_138937 >> (0x7 & 0x3F)) # SHR operation
ref_138948 = ref_138941 # MOV operation
ref_140327 = ref_138948 # MOV operation
ref_140341 = ref_121036 # MOV operation
ref_140343 = (~(ref_140341) & 0xFFFFFFFFFFFFFFFF) # NOT operation
ref_140345 = (ref_140327 & ref_140343) # AND operation
ref_140364 = ref_121036 # MOV operation
ref_140366 = ((ref_140364 + ref_140345) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_141950 = ref_140366 # MOV operation
ref_141966 = ref_141950 # MOV operation
ref_141970 = ((ref_141966 << (0x3D & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_141977 = ref_141970 # MOV operation
ref_159335 = ref_694 # MOV operation
ref_160587 = ref_159335 # MOV operation
ref_160603 = ref_160587 # MOV operation
ref_160607 = ((ref_160603 << (0x39 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_160614 = ref_160607 # MOV operation
ref_173040 = ref_694 # MOV operation
ref_176559 = ref_173040 # MOV operation
ref_176565 = ref_176559 # MOV operation
ref_176569 = (ref_176565 >> (0x7 & 0x3F)) # SHR operation
ref_176576 = ref_176569 # MOV operation
ref_177955 = ref_176576 # MOV operation
ref_177969 = ref_160614 # MOV operation
ref_177971 = (~(ref_177969) & 0xFFFFFFFFFFFFFFFF) # NOT operation
ref_177973 = (ref_177955 & ref_177971) # AND operation
ref_177992 = ref_160614 # MOV operation
ref_177994 = ((ref_177992 + ref_177973) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_181845 = ref_177994 # MOV operation
ref_181851 = ref_181845 # MOV operation
ref_181855 = (ref_181851 >> (0x3 & 0x3F)) # SHR operation
ref_181862 = ref_181855 # MOV operation
ref_183241 = ref_181862 # MOV operation
ref_183255 = ref_141977 # MOV operation
ref_183257 = (~(ref_183255) & 0xFFFFFFFFFFFFFFFF) # NOT operation
ref_183259 = (ref_183241 & ref_183257) # AND operation
ref_183278 = ref_141977 # MOV operation
ref_183280 = ((ref_183278 + ref_183259) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_184929 = ref_183280 # MOV operation
ref_198344 = ref_694 # MOV operation
ref_202824 = ref_198344 # MOV operation
ref_202832 = ref_202824 # MOV operation
ref_202834 = (ref_202832 & 0x1D2FE20A) # AND operation
ref_202853 = ref_198344 # MOV operation
ref_202861 = (0x1D2FE20A | ref_202853) # OR operation
ref_202868 = ref_202834 # MOV operation
ref_202870 = ((sx(0x40, ref_202868) * sx(0x40, ref_202861)) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_202886 = ref_198344 # MOV operation
ref_202896 = (ref_202886 & 0xFFFFFFFFE2D01DF5) # AND operation
ref_202915 = ref_198344 # MOV operation
ref_202917 = ref_202915 # MOV operation
ref_202919 = (~(ref_202917) & 0xFFFFFFFFFFFFFFFF) # NOT operation
ref_202927 = (0x1D2FE20A & ref_202919) # AND operation
ref_202934 = ((sx(0x40, ref_202927) * sx(0x40, ref_202896)) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_202938 = ((ref_202934 + ref_202870) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_215191 = ref_202938 # MOV operation
ref_215193 = ((ref_215191 >> 56) & 0xFF) # Byte reference - MOV operation
ref_215194 = ((ref_215191 >> 48) & 0xFF) # Byte reference - MOV operation
ref_215195 = ((ref_215191 >> 40) & 0xFF) # Byte reference - MOV operation
ref_215196 = ((ref_215191 >> 32) & 0xFF) # Byte reference - MOV operation
ref_215197 = ((ref_215191 >> 24) & 0xFF) # Byte reference - MOV operation
ref_215198 = ((ref_215191 >> 16) & 0xFF) # Byte reference - MOV operation
ref_215199 = ((ref_215191 >> 8) & 0xFF) # Byte reference - MOV operation
ref_215200 = (ref_215191 & 0xFF) # Byte reference - MOV operation
ref_238233 = (((((ref_87545 & 0xFF)) << 8 | (ref_87546 & 0xFF)) << 8 | (ref_87547 & 0xFF)) << 8 | (ref_87548 & 0xFF)) # MOV operation
ref_240290 = (ref_238233 & 0xFFFFFFFF) # MOV operation
ref_283483 = (((((ref_87549 & 0xFF)) << 8 | (ref_87550 & 0xFF)) << 8 | (ref_87551 & 0xFF)) << 8 | (ref_87552 & 0xFF)) # MOV operation
ref_284181 = (ref_283483 & 0xFFFFFFFF) # MOV operation
ref_307255 = (ref_240290 & 0xFFFFFFFF) # MOV operation
ref_307953 = (ref_307255 & 0xFFFFFFFF) # MOV operation
ref_329897 = (ref_307953 & 0xFFFFFFFF) # MOV operation
ref_330595 = (ref_329897 & 0xFFFFFFFF) # MOV operation
ref_372650 = (ref_284181 & 0xFFFFFFFF) # MOV operation
ref_373348 = (ref_372650 & 0xFFFFFFFF) # MOV operation
ref_397560 = (ref_330595 & 0xFFFFFFFF) # MOV operation
ref_398258 = (ref_397560 & 0xFFFFFFFF) # MOV operation
ref_435920 = (ref_373348 & 0xFFFFFFFF) # MOV operation
ref_436618 = (ref_435920 & 0xFFFFFFFF) # MOV operation
ref_476509 = (ref_398258 & 0xFFFFFFFF) # MOV operation
ref_477207 = (ref_476509 & 0xFFFFFFFF) # MOV operation
ref_477209 = (((ref_477207 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_477210 = (((ref_477207 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_477211 = (((ref_477207 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_477212 = ((ref_477207 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_498073 = (ref_436618 & 0xFFFFFFFF) # MOV operation
ref_498771 = (ref_498073 & 0xFFFFFFFF) # MOV operation
ref_498773 = (((ref_498771 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_498774 = (((ref_498771 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_498775 = (((ref_498771 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_498776 = ((ref_498771 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_524351 = (((ref_215195 & 0xFF)) << 8 | (ref_215196 & 0xFF)) # MOVZX operation
ref_526417 = (ref_524351 & 0xFFFF) # MOVZX operation
ref_551303 = (((ref_215199 & 0xFF)) << 8 | (ref_215200 & 0xFF)) # MOVZX operation
ref_574993 = (ref_551303 & 0xFFFF) # MOVZX operation
ref_577801 = (ref_526417 & 0xFFFF) # MOVZX operation
ref_601953 = (ref_577801 & 0xFFFF) # MOVZX operation
ref_601955 = (((ref_601953 & 0xFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_601956 = ((ref_601953 & 0xFFFF) & 0xFF) # Byte reference - MOV operation
ref_627523 = (((ref_215197 & 0xFF)) << 8 | (ref_215198 & 0xFF)) # MOVZX operation
ref_629589 = (ref_627523 & 0xFFFF) # MOVZX operation
ref_653337 = (ref_574993 & 0xFFFF) # MOVZX operation
ref_677035 = (ref_653337 & 0xFFFF) # MOVZX operation
ref_677037 = (((ref_677035 & 0xFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_677038 = ((ref_677035 & 0xFFFF) & 0xFF) # Byte reference - MOV operation
ref_679843 = (ref_629589 & 0xFFFF) # MOVZX operation
ref_703987 = (ref_679843 & 0xFFFF) # MOVZX operation
ref_703989 = (((ref_703987 & 0xFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_703990 = ((ref_703987 & 0xFFFF) & 0xFF) # Byte reference - MOV operation
ref_762509 = (((((((((ref_215193 & 0xFF)) << 8 | (ref_215194 & 0xFF)) << 8 | (ref_703989 & 0xFF)) << 8 | (ref_703990 & 0xFF)) << 8 | (ref_677037 & 0xFF)) << 8 | (ref_677038 & 0xFF)) << 8 | (ref_601955 & 0xFF)) << 8 | (ref_601956 & 0xFF)) # MOV operation
ref_764045 = ref_762509 # MOV operation
ref_764047 = ref_764045 # MOV operation
ref_764049 = (~(ref_764047) & 0xFFFFFFFFFFFFFFFF) # NOT operation
ref_764065 = (ref_764049 | 0xF) # OR operation
ref_764076 = ref_762509 # MOV operation
ref_764078 = ((ref_764076 + ref_764065) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_764086 = ((ref_764078 + 0x1) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_765678 = ref_764086 # MOV operation
ref_765694 = ref_765678 # MOV operation
ref_765698 = ((ref_765694 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_765705 = ref_765698 # MOV operation
ref_778077 = (((((((((ref_498773 & 0xFF)) << 8 | (ref_498774 & 0xFF)) << 8 | (ref_498775 & 0xFF)) << 8 | (ref_498776 & 0xFF)) << 8 | (ref_477209 & 0xFF)) << 8 | (ref_477210 & 0xFF)) << 8 | (ref_477211 & 0xFF)) << 8 | (ref_477212 & 0xFF)) # MOV operation
ref_779266 = ref_778077 # MOV operation
ref_779280 = ref_765705 # MOV operation
ref_779282 = (~(ref_779280) & 0xFFFFFFFFFFFFFFFF) # NOT operation
ref_779284 = (ref_779266 & ref_779282) # AND operation
ref_779303 = ref_765705 # MOV operation
ref_779305 = ((ref_779303 + ref_779284) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_791531 = ref_779305 # MOV operation
ref_805631 = ref_55581 # MOV operation
ref_820486 = (((((((((ref_215193 & 0xFF)) << 8 | (ref_215194 & 0xFF)) << 8 | (ref_703989 & 0xFF)) << 8 | (ref_703990 & 0xFF)) << 8 | (ref_677037 & 0xFF)) << 8 | (ref_677038 & 0xFF)) << 8 | (ref_601955 & 0xFF)) << 8 | (ref_601956 & 0xFF)) # MOV operation
ref_821561 = ref_820486 # MOV operation
ref_821575 = ref_805631 # MOV operation
ref_821577 = (~(ref_821575) & 0xFFFFFFFFFFFFFFFF) # NOT operation
ref_821579 = ref_821561 # MOV operation
ref_821581 = (ref_821579 ^ ref_821577) # XOR operation
ref_821592 = ref_820486 # MOV operation
ref_821606 = ref_805631 # MOV operation
ref_821608 = ref_821592 # MOV operation
ref_821610 = (ref_821608 | ref_821606) # OR operation
ref_821621 = ref_820486 # MOV operation
ref_821635 = ref_805631 # MOV operation
ref_821637 = (ref_821635 | ref_821621) # OR operation
ref_821644 = ((ref_821637 + ref_821610) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_821652 = ((ref_821644 + ref_821581) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_821660 = ((ref_821652 + 0x1) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_837378 = ref_821660 # MOV operation
ref_871196 = ref_837378 # MOV operation
ref_883392 = ref_184929 # MOV operation
ref_884467 = ref_883392 # MOV operation
ref_884481 = ref_871196 # MOV operation
ref_884483 = (~(ref_884481) & 0xFFFFFFFFFFFFFFFF) # NOT operation
ref_884485 = ref_884467 # MOV operation
ref_884487 = (ref_884485 ^ ref_884483) # XOR operation
ref_884498 = ref_883392 # MOV operation
ref_884512 = ref_871196 # MOV operation
ref_884514 = ref_884498 # MOV operation
ref_884516 = (ref_884514 | ref_884512) # OR operation
ref_884527 = ref_883392 # MOV operation
ref_884541 = ref_871196 # MOV operation
ref_884543 = (ref_884541 | ref_884527) # OR operation
ref_884550 = ((ref_884543 + ref_884516) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_884558 = ((ref_884550 + ref_884487) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_884566 = ((ref_884558 + 0x1) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_902761 = ref_791531 # MOV operation
ref_904297 = ref_902761 # MOV operation
ref_904299 = ref_904297 # MOV operation
ref_904301 = (~(ref_904299) & 0xFFFFFFFFFFFFFFFF) # NOT operation
ref_904317 = (ref_904301 | 0x7) # OR operation
ref_904328 = ref_902761 # MOV operation
ref_904330 = ((ref_904328 + ref_904317) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_904338 = ((ref_904330 + 0x1) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_905867 = ref_904338 # MOV operation
ref_905885 = (ref_905867 & 0xFFFFFFFFFFFFFFFE) # AND operation
ref_905906 = ((0x1 + ref_905885) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_918434 = ref_55581 # MOV operation
ref_919686 = ref_918434 # MOV operation
ref_919700 = ref_905906 # MOV operation
ref_919702 = ref_919686 # MOV operation
ref_919704 = (ref_919700 & 0xFFFFFFFF) # MOV operation
ref_919706 = ((ref_919702 << ((ref_919704 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_919713 = ref_919706 # MOV operation
ref_921062 = ref_919713 # MOV operation
ref_921074 = ref_884566 # MOV operation
ref_921076 = (~(ref_921074) & 0xFFFFFFFFFFFFFFFF) # NOT operation
ref_921078 = ((ref_921062 + ref_921076) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_921086 = ((ref_921078 + 0x1) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_934605 = ref_921086 # MOV operation
ref_938083 = ref_934605 # MOV operation
ref_938085 = ref_938083 # MOV operation

print ref_938085 & 0xffffffffffffffff
