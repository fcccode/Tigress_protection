#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys
import z3

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

ctx = z3.Context()
s   = z3.Solver()

SymVar_0 = z3.BitVec('SymVar_0', 64)
ref_244 = SymVar_0
ref_259 = ref_244 # MOV operation
ref_1442 = ref_259 # MOV operation
ref_1788 = ref_1442 # MOV operation
ref_1880 = ref_1788 # MOV operation
ref_1894 = (0x1F02C962 | ref_1880) # OR operation
ref_1931 = ref_1894 # MOV operation
ref_2328 = ref_1931 # MOV operation
ref_2342 = (0x1F8797B2 & ref_2328) # AND operation
ref_3073 = ref_2342 # MOV operation
ref_4664 = ref_259 # MOV operation
ref_4694 = ref_4664 # MOV operation
ref_5653 = ref_3073 # MOV operation
ref_5681 = ref_4694 # MOV operation
ref_5697 = ref_5653 # MOV operation
ref_5699 = (ref_5697 & ref_5681) # AND operation
ref_6904 = ref_5699 # MOV operation
ref_7992 = ref_259 # MOV operation
ref_8384 = ref_7992 # MOV operation
ref_8398 = ((sx(0x40, 0x66AF1DF) * sx(0x40, ref_8384)) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_9278 = ref_6904 # MOV operation
ref_9310 = ref_9278 # MOV operation
ref_9536 = ref_9310 # MOV operation
ref_9556 = (ref_9536 >> (0x7 & 0x3F)) # SHR operation
ref_9591 = ref_9556 # MOV operation
ref_10415 = ref_6904 # MOV operation
ref_10839 = ref_10415 # MOV operation
ref_10853 = ref_10839 # MOV operation
ref_10857 = ((ref_10853 << (0x39 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_10864 = ref_10857 # MOV operation
ref_10890 = ref_9591 # MOV operation
ref_10902 = ref_10864 # MOV operation
ref_10904 = (ref_10890 | ref_10902) # OR operation
ref_10939 = ref_10904 # MOV operation
ref_11151 = ref_8398 # MOV operation
ref_11155 = ref_10939 # MOV operation
ref_11157 = ((ref_11151 + ref_11155) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_11195 = ref_11157 # MOV operation
ref_12075 = ref_11195 # MOV operation
ref_24901 = ref_12075 # MOV operation
ref_26347 = ref_12075 # MOV operation
ref_26585 = ref_24901 # MOV operation
ref_26593 = ref_26347 # MOV operation
ref_26595 = ((ref_26585 + ref_26593) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_26633 = ref_26595 # MOV operation
ref_28091 = ref_12075 # MOV operation
ref_28121 = ref_28091 # MOV operation
ref_29387 = ref_6904 # MOV operation
ref_29419 = ref_29387 # MOV operation
ref_29817 = ref_29419 # MOV operation
ref_29831 = (0x7 & ref_29817) # AND operation
ref_29862 = ref_29831 # MOV operation
ref_29892 = ref_29862 # MOV operation
ref_29910 = ref_29892 # MOV operation
ref_29914 = ((ref_29910 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_29921 = ref_29914 # MOV operation
ref_30135 = ref_28121 # MOV operation
ref_30139 = ref_29921 # MOV operation
ref_30141 = (ref_30135 | ref_30139) # OR operation
ref_30178 = ref_30141 # MOV operation
ref_31388 = ref_30178 # MOV operation
ref_31390 = ((ref_31388 >> 56) & 0xFF) # Byte reference - MOV operation
ref_31391 = ((ref_31388 >> 48) & 0xFF) # Byte reference - MOV operation
ref_31392 = ((ref_31388 >> 40) & 0xFF) # Byte reference - MOV operation
ref_31393 = ((ref_31388 >> 32) & 0xFF) # Byte reference - MOV operation
ref_31394 = ((ref_31388 >> 24) & 0xFF) # Byte reference - MOV operation
ref_31395 = ((ref_31388 >> 16) & 0xFF) # Byte reference - MOV operation
ref_31396 = ((ref_31388 >> 8) & 0xFF) # Byte reference - MOV operation
ref_31397 = (ref_31388 & 0xFF) # Byte reference - MOV operation
ref_33681 = (ref_31390 & 0xFF) # MOVZX operation
ref_33691 = (ref_33681 & 0xFF) # MOVZX operation
ref_33723 = (ref_33691 & 0xFF) # MOVZX operation
ref_38532 = (ref_31397 & 0xFF) # MOVZX operation
ref_38556 = (ref_38532 & 0xFF) # MOVZX operation
ref_38558 = ((ref_38556 & 0xFF) & 0xFF) # Byte reference - MOV operation
ref_41134 = (ref_33723 & 0xFF) # MOVZX operation
ref_41343 = (ref_41134 & 0xFF) # MOVZX operation
ref_41345 = ((ref_41343 & 0xFF) & 0xFF) # Byte reference - MOV operation
ref_42159 = ref_3073 # MOV operation
ref_42517 = ref_42159 # MOV operation
ref_43849 = (((((((((ref_38558 & 0xFF)) << 8 | (ref_31391 & 0xFF)) << 8 | (ref_31392 & 0xFF)) << 8 | (ref_31393 & 0xFF)) << 8 | (ref_31394 & 0xFF)) << 8 | (ref_31395 & 0xFF)) << 8 | (ref_31396 & 0xFF)) << 8 | (ref_41345 & 0xFF)) # MOV operation
ref_43881 = ref_43849 # MOV operation
ref_45097 = ref_6904 # MOV operation
ref_45127 = ref_45097 # MOV operation
ref_45153 = ref_43881 # MOV operation
ref_45157 = ref_45127 # MOV operation
ref_45159 = (ref_45157 & ref_45153) # AND operation
ref_45562 = ref_45159 # MOV operation
ref_45576 = (0x1F & ref_45562) # AND operation
ref_45607 = ref_45576 # MOV operation
ref_45637 = ref_45607 # MOV operation
ref_45655 = ref_45637 # MOV operation
ref_45659 = ((ref_45655 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_45666 = ref_45659 # MOV operation
ref_45864 = ref_45666 # MOV operation
ref_45892 = ref_42517 # MOV operation
ref_45908 = ref_45864 # MOV operation
ref_45910 = (ref_45908 | ref_45892) # OR operation
ref_46860 = ref_45910 # MOV operation
ref_51124 = ref_26633 # MOV operation
ref_52570 = ref_26633 # MOV operation
ref_52808 = ref_51124 # MOV operation
ref_52816 = ref_52570 # MOV operation
ref_52818 = ((ref_52808 + ref_52816) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_52856 = ref_52818 # MOV operation
ref_54314 = ref_52856 # MOV operation
ref_54344 = ref_54314 # MOV operation
ref_55610 = (((((((((ref_38558 & 0xFF)) << 8 | (ref_31391 & 0xFF)) << 8 | (ref_31392 & 0xFF)) << 8 | (ref_31393 & 0xFF)) << 8 | (ref_31394 & 0xFF)) << 8 | (ref_31395 & 0xFF)) << 8 | (ref_31396 & 0xFF)) << 8 | (ref_41345 & 0xFF)) # MOV operation
ref_55642 = ref_55610 # MOV operation
ref_56040 = ref_55642 # MOV operation
ref_56054 = (0x7 & ref_56040) # AND operation
ref_56085 = ref_56054 # MOV operation
ref_56115 = ref_56085 # MOV operation
ref_56133 = ref_56115 # MOV operation
ref_56137 = ((ref_56133 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_56144 = ref_56137 # MOV operation
ref_56358 = ref_54344 # MOV operation
ref_56362 = ref_56144 # MOV operation
ref_56364 = (ref_56358 | ref_56362) # OR operation
ref_56401 = ref_56364 # MOV operation
ref_57611 = ref_56401 # MOV operation
ref_57613 = ((ref_57611 >> 56) & 0xFF) # Byte reference - MOV operation
ref_57614 = ((ref_57611 >> 48) & 0xFF) # Byte reference - MOV operation
ref_57615 = ((ref_57611 >> 40) & 0xFF) # Byte reference - MOV operation
ref_57616 = ((ref_57611 >> 32) & 0xFF) # Byte reference - MOV operation
ref_57617 = ((ref_57611 >> 24) & 0xFF) # Byte reference - MOV operation
ref_57618 = ((ref_57611 >> 16) & 0xFF) # Byte reference - MOV operation
ref_57619 = ((ref_57611 >> 8) & 0xFF) # Byte reference - MOV operation
ref_57620 = (ref_57611 & 0xFF) # Byte reference - MOV operation
ref_59904 = (ref_57613 & 0xFF) # MOVZX operation
ref_59914 = (ref_59904 & 0xFF) # MOVZX operation
ref_59946 = (ref_59914 & 0xFF) # MOVZX operation
ref_64755 = (ref_57620 & 0xFF) # MOVZX operation
ref_64779 = (ref_64755 & 0xFF) # MOVZX operation
ref_64781 = ((ref_64779 & 0xFF) & 0xFF) # Byte reference - MOV operation
ref_67357 = (ref_59946 & 0xFF) # MOVZX operation
ref_67566 = (ref_67357 & 0xFF) # MOVZX operation
ref_67568 = ((ref_67566 & 0xFF) & 0xFF) # Byte reference - MOV operation
ref_68382 = ref_46860 # MOV operation
ref_68740 = ref_68382 # MOV operation
ref_70072 = (((((((((ref_64781 & 0xFF)) << 8 | (ref_57614 & 0xFF)) << 8 | (ref_57615 & 0xFF)) << 8 | (ref_57616 & 0xFF)) << 8 | (ref_57617 & 0xFF)) << 8 | (ref_57618 & 0xFF)) << 8 | (ref_57619 & 0xFF)) << 8 | (ref_67568 & 0xFF)) # MOV operation
ref_70104 = ref_70072 # MOV operation
ref_71320 = (((((((((ref_38558 & 0xFF)) << 8 | (ref_31391 & 0xFF)) << 8 | (ref_31392 & 0xFF)) << 8 | (ref_31393 & 0xFF)) << 8 | (ref_31394 & 0xFF)) << 8 | (ref_31395 & 0xFF)) << 8 | (ref_31396 & 0xFF)) << 8 | (ref_41345 & 0xFF)) # MOV operation
ref_71350 = ref_71320 # MOV operation
ref_71376 = ref_70104 # MOV operation
ref_71380 = ref_71350 # MOV operation
ref_71382 = (ref_71380 & ref_71376) # AND operation
ref_71785 = ref_71382 # MOV operation
ref_71799 = (0x1F & ref_71785) # AND operation
ref_71830 = ref_71799 # MOV operation
ref_71860 = ref_71830 # MOV operation
ref_71878 = ref_71860 # MOV operation
ref_71882 = ((ref_71878 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_71889 = ref_71882 # MOV operation
ref_72087 = ref_71889 # MOV operation
ref_72115 = ref_68740 # MOV operation
ref_72131 = ref_72087 # MOV operation
ref_72133 = (ref_72131 | ref_72115) # OR operation
ref_73083 = ref_72133 # MOV operation
ref_76398 = (((((((((ref_38558 & 0xFF)) << 8 | (ref_31391 & 0xFF)) << 8 | (ref_31392 & 0xFF)) << 8 | (ref_31393 & 0xFF)) << 8 | (ref_31394 & 0xFF)) << 8 | (ref_31395 & 0xFF)) << 8 | (ref_31396 & 0xFF)) << 8 | (ref_41345 & 0xFF)) # MOV operation
ref_76428 = ref_76398 # MOV operation
ref_77504 = (((((((((ref_64781 & 0xFF)) << 8 | (ref_57614 & 0xFF)) << 8 | (ref_57615 & 0xFF)) << 8 | (ref_57616 & 0xFF)) << 8 | (ref_57617 & 0xFF)) << 8 | (ref_57618 & 0xFF)) << 8 | (ref_57619 & 0xFF)) << 8 | (ref_67568 & 0xFF)) # MOV operation
ref_77532 = ref_76428 # MOV operation
ref_77548 = ref_77504 # MOV operation
ref_77550 = (ref_77548 | ref_77532) # OR operation
ref_77822 = ref_77550 # MOV operation
ref_77836 = (0xF & ref_77822) # AND operation
ref_78267 = ref_77836 # MOV operation
ref_78273 = (ref_78267 | 0x1) # OR operation
ref_79278 = ref_6904 # MOV operation
ref_79308 = ref_79278 # MOV operation
ref_79512 = ref_79308 # MOV operation
ref_79532 = (ref_79512 >> (0x1 & 0x3F)) # SHR operation
ref_79567 = ref_79532 # MOV operation
ref_79611 = ref_79567 # MOV operation
ref_79629 = (0xF & ref_79611) # AND operation
ref_79864 = ref_79629 # MOV operation
ref_79874 = (0x1 | ref_79864) # OR operation
ref_80085 = ref_79874 # MOV operation
ref_81857 = ref_73083 # MOV operation
ref_81889 = ref_81857 # MOV operation
ref_81923 = ref_81889 # MOV operation
ref_81939 = ref_80085 # MOV operation
ref_81941 = (ref_81939 & 0xFFFFFFFF) # MOV operation
ref_81943 = (ref_81923 >> ((ref_81941 & 0xFF) & 0x3F)) # SHR operation
ref_82277 = ref_81943 # MOV operation
ref_83724 = ref_6904 # MOV operation
ref_83754 = ref_83724 # MOV operation
ref_83960 = ref_83754 # MOV operation
ref_83980 = (ref_83960 >> (0x1 & 0x3F)) # SHR operation
ref_84015 = ref_83980 # MOV operation
ref_84059 = ref_84015 # MOV operation
ref_84077 = (0xF & ref_84059) # AND operation
ref_84611 = ref_84077 # MOV operation
ref_84621 = (0x1 | ref_84611) # OR operation
ref_84832 = ref_84621 # MOV operation
ref_85076 = ref_84832 # MOV operation
ref_85078 = ((0x40 - ref_85076) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_86993 = ref_73083 # MOV operation
ref_87023 = ref_86993 # MOV operation
ref_87039 = ref_85078 # MOV operation
ref_87041 = ref_87023 # MOV operation
ref_87043 = (ref_87039 & 0xFFFFFFFF) # MOV operation
ref_87045 = ((ref_87041 << ((ref_87043 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_87052 = ref_87045 # MOV operation
ref_87248 = ref_87052 # MOV operation
ref_87276 = ref_82277 # MOV operation
ref_87292 = ref_87248 # MOV operation
ref_87294 = (ref_87292 | ref_87276) # OR operation
ref_87525 = ref_87294 # MOV operation
ref_87749 = ref_87525 # MOV operation
ref_87765 = ref_78273 # MOV operation
ref_87767 = ref_87749 # MOV operation
ref_87769 = (ref_87765 & 0xFFFFFFFF) # MOV operation
ref_87771 = ((ref_87767 << ((ref_87769 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_87778 = ref_87771 # MOV operation
ref_89833 = (((((((((ref_38558 & 0xFF)) << 8 | (ref_31391 & 0xFF)) << 8 | (ref_31392 & 0xFF)) << 8 | (ref_31393 & 0xFF)) << 8 | (ref_31394 & 0xFF)) << 8 | (ref_31395 & 0xFF)) << 8 | (ref_31396 & 0xFF)) << 8 | (ref_41345 & 0xFF)) # MOV operation
ref_89863 = ref_89833 # MOV operation
ref_91417 = (((((((((ref_64781 & 0xFF)) << 8 | (ref_57614 & 0xFF)) << 8 | (ref_57615 & 0xFF)) << 8 | (ref_57616 & 0xFF)) << 8 | (ref_57617 & 0xFF)) << 8 | (ref_57618 & 0xFF)) << 8 | (ref_57619 & 0xFF)) << 8 | (ref_67568 & 0xFF)) # MOV operation
ref_91647 = ref_91417 # MOV operation
ref_91873 = ref_89863 # MOV operation
ref_91877 = ref_91647 # MOV operation
ref_91879 = (ref_91873 | ref_91877) # OR operation
ref_92248 = ref_91879 # MOV operation
ref_92498 = ref_92248 # MOV operation
ref_92508 = (0xF & ref_92498) # AND operation
ref_93250 = ref_92508 # MOV operation
ref_93256 = (ref_93250 | 0x1) # OR operation
ref_93293 = ref_93256 # MOV operation
ref_93517 = ref_93293 # MOV operation
ref_93521 = ((0x40 - ref_93517) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_93529 = ref_93521 # MOV operation
ref_93735 = ref_93529 # MOV operation
ref_95666 = ref_6904 # MOV operation
ref_95696 = ref_95666 # MOV operation
ref_96026 = ref_95696 # MOV operation
ref_96046 = (ref_96026 >> (0x1 & 0x3F)) # SHR operation
ref_96415 = ref_96046 # MOV operation
ref_96665 = ref_96415 # MOV operation
ref_96675 = (0xF & ref_96665) # AND operation
ref_97277 = ref_96675 # MOV operation
ref_97283 = (ref_97277 | 0x1) # OR operation
ref_98272 = ref_73083 # MOV operation
ref_98304 = ref_98272 # MOV operation
ref_98528 = ref_98304 # MOV operation
ref_98544 = ref_97283 # MOV operation
ref_98546 = (ref_98544 & 0xFFFFFFFF) # MOV operation
ref_98548 = (ref_98528 >> ((ref_98546 & 0xFF) & 0x3F)) # SHR operation
ref_98583 = ref_98548 # MOV operation
ref_100204 = ref_73083 # MOV operation
ref_102838 = ref_6904 # MOV operation
ref_102870 = ref_102838 # MOV operation
ref_102904 = ref_102870 # MOV operation
ref_102924 = (ref_102904 >> (0x1 & 0x3F)) # SHR operation
ref_103140 = ref_102924 # MOV operation
ref_103230 = ref_103140 # MOV operation
ref_103244 = (0xF & ref_103230) # AND operation
ref_103798 = ref_103244 # MOV operation
ref_103808 = (0x1 | ref_103798) # OR operation
ref_104019 = ref_103808 # MOV operation
ref_104263 = ref_104019 # MOV operation
ref_104265 = ((0x40 - ref_104263) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_104501 = ref_104265 # MOV operation
ref_104853 = ref_100204 # MOV operation
ref_104857 = ref_104501 # MOV operation
ref_104859 = ref_104853 # MOV operation
ref_104861 = (ref_104857 & 0xFFFFFFFF) # MOV operation
ref_104863 = ((ref_104859 << ((ref_104861 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_104870 = ref_104863 # MOV operation
ref_105067 = ref_104870 # MOV operation
ref_105095 = ref_98583 # MOV operation
ref_105111 = ref_105067 # MOV operation
ref_105113 = (ref_105111 | ref_105095) # OR operation
ref_105344 = ref_105113 # MOV operation
ref_105566 = ref_105344 # MOV operation
ref_105582 = ref_93735 # MOV operation
ref_105584 = ref_105566 # MOV operation
ref_105586 = (ref_105582 & 0xFFFFFFFF) # MOV operation
ref_105588 = (ref_105584 >> ((ref_105586 & 0xFF) & 0x3F)) # SHR operation
ref_105595 = ref_105588 # MOV operation
ref_105811 = ref_105595 # MOV operation
ref_105839 = ref_87778 # MOV operation
ref_105855 = ref_105811 # MOV operation
ref_105857 = (ref_105855 | ref_105839) # OR operation
ref_107363 = ref_105857 # MOV operation
ref_107917 = ref_107363 # MOV operation
ref_107919 = ref_107917 # MOV operation


s.add(ref_107919 == int(sys.argv[1]))
collisions = 0
while s.check() == z3.sat and collisions < 10:
    print s.model()
    s.add(SymVar_0 != s.model()[SymVar_0])
    collisions += 1
