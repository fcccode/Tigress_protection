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
a = (((((0x0) << 64 | ((((0x3F & ((((((((sx(0x40, (0x1247C27B & ((0x17F452 + (0x2918921B | SymVar_0)) & 0xFFFFFFFFFFFFFFFF))) * sx(0x40, SymVar_0)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) - 0x7A3FEB) & 0xFFFFFFFFFFFFFFFF) | ((SymVar_0 >> (((((0x40 - (0x1 | (0xF & (((0x17F452 + (0x2918921B | SymVar_0)) & 0xFFFFFFFFFFFFFFFF) >> (0x4 & 0x3F))))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) & 0xFF) & 0x3F)) | ((SymVar_0 << ((((0x1 | (0xF & (((0x17F452 + (0x2918921B | SymVar_0)) & 0xFFFFFFFFFFFFFFFF) >> (0x4 & 0x3F)))) & 0xFFFFFFFF) & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF))) << (((((0x40 - (0x1 | (0xF & ((((((sx(0x40, (0x1247C27B & ((0x17F452 + (0x2918921B | SymVar_0)) & 0xFFFFFFFFFFFFFFFF))) * sx(0x40, SymVar_0)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) - 0x7A3FEB) & 0xFFFFFFFFFFFFFFFF) | ((SymVar_0 >> (((((0x40 - (0x1 | (0xF & (((0x17F452 + (0x2918921B | SymVar_0)) & 0xFFFFFFFFFFFFFFFF) >> (0x4 & 0x3F))))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) & 0xFF) & 0x3F)) | ((SymVar_0 << ((((0x1 | (0xF & (((0x17F452 + (0x2918921B | SymVar_0)) & 0xFFFFFFFFFFFFFFFF) >> (0x4 & 0x3F)))) & 0xFFFFFFFF) & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF))) >> (0x2 & 0x3F))))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) | ((((((sx(0x40, (0x1247C27B & ((0x17F452 + (0x2918921B | SymVar_0)) & 0xFFFFFFFFFFFFFFFF))) * sx(0x40, SymVar_0)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) - 0x7A3FEB) & 0xFFFFFFFFFFFFFFFF) | ((SymVar_0 >> (((((0x40 - (0x1 | (0xF & (((0x17F452 + (0x2918921B | SymVar_0)) & 0xFFFFFFFFFFFFFFFF) >> (0x4 & 0x3F))))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) & 0xFF) & 0x3F)) | ((SymVar_0 << ((((0x1 | (0xF & (((0x17F452 + (0x2918921B | SymVar_0)) & 0xFFFFFFFFFFFFFFFF) >> (0x4 & 0x3F)))) & 0xFFFFFFFF) & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF))) >> ((((0x1 | (0xF & ((((((sx(0x40, (0x1247C27B & ((0x17F452 + (0x2918921B | SymVar_0)) & 0xFFFFFFFFFFFFFFFF))) * sx(0x40, SymVar_0)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) - 0x7A3FEB) & 0xFFFFFFFFFFFFFFFF) | ((SymVar_0 >> (((((0x40 - (0x1 | (0xF & (((0x17F452 + (0x2918921B | SymVar_0)) & 0xFFFFFFFFFFFFFFFF) >> (0x4 & 0x3F))))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) & 0xFF) & 0x3F)) | ((SymVar_0 << ((((0x1 | (0xF & (((0x17F452 + (0x2918921B | SymVar_0)) & 0xFFFFFFFFFFFFFFFF) >> (0x4 & 0x3F)))) & 0xFFFFFFFF) & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF))) >> (0x2 & 0x3F)))) & 0xFFFFFFFF) & 0xFF) & 0x3F)))) << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) | ((0x17F452 + (0x2918921B | SymVar_0)) & 0xFFFFFFFFFFFFFFFF))) / (((((((((0x0 & 0xFF)) << 8 | (0x0 & 0xFF)) << 8 | (0x0 & 0xFF)) << 8 | (0x0 & 0xFF)) << 8 | (0x0 & 0xFF)) << 8 | (0x0 & 0xFF)) << 8 | (0x0 & 0xFF)) << 8 | (0x7 & 0xFF))) >> (((((0x40 - (0x1 | (0xF & ((((((((sx(0x40, (0x1247C27B & ((0x17F452 + (0x2918921B | SymVar_0)) & 0xFFFFFFFFFFFFFFFF))) * sx(0x40, SymVar_0)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) - 0x7A3FEB) & 0xFFFFFFFFFFFFFFFF) | ((SymVar_0 >> (((((0x40 - (0x1 | (0xF & (((0x17F452 + (0x2918921B | SymVar_0)) & 0xFFFFFFFFFFFFFFFF) >> (0x4 & 0x3F))))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) & 0xFF) & 0x3F)) | ((SymVar_0 << ((((0x1 | (0xF & (((0x17F452 + (0x2918921B | SymVar_0)) & 0xFFFFFFFFFFFFFFFF) >> (0x4 & 0x3F)))) & 0xFFFFFFFF) & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF))) << ((((0x1 | (0x7 & ((((((((sx(0x40, (0x1247C27B & ((0x17F452 + (0x2918921B | SymVar_0)) & 0xFFFFFFFFFFFFFFFF))) * sx(0x40, SymVar_0)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) - 0x7A3FEB) & 0xFFFFFFFFFFFFFFFF) | ((SymVar_0 >> (((((0x40 - (0x1 | (0xF & (((0x17F452 + (0x2918921B | SymVar_0)) & 0xFFFFFFFFFFFFFFFF) >> (0x4 & 0x3F))))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) & 0xFF) & 0x3F)) | ((SymVar_0 << ((((0x1 | (0xF & (((0x17F452 + (0x2918921B | SymVar_0)) & 0xFFFFFFFFFFFFFFFF) >> (0x4 & 0x3F)))) & 0xFFFFFFFF) & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF))) + 0x3E469461) & 0xFFFFFFFFFFFFFFFF) | SymVar_0))) & 0xFFFFFFFF) & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) >> (0x4 & 0x3F))))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) & 0xFF) & 0x3F)) | (((((0x0) << 64 | ((((0x3F & ((((((((sx(0x40, (0x1247C27B & ((0x17F452 + (0x2918921B | SymVar_0)) & 0xFFFFFFFFFFFFFFFF))) * sx(0x40, SymVar_0)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) - 0x7A3FEB) & 0xFFFFFFFFFFFFFFFF) | ((SymVar_0 >> (((((0x40 - (0x1 | (0xF & (((0x17F452 + (0x2918921B | SymVar_0)) & 0xFFFFFFFFFFFFFFFF) >> (0x4 & 0x3F))))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) & 0xFF) & 0x3F)) | ((SymVar_0 << ((((0x1 | (0xF & (((0x17F452 + (0x2918921B | SymVar_0)) & 0xFFFFFFFFFFFFFFFF) >> (0x4 & 0x3F)))) & 0xFFFFFFFF) & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF))) << (((((0x40 - (0x1 | (0xF & ((((((sx(0x40, (0x1247C27B & ((0x17F452 + (0x2918921B | SymVar_0)) & 0xFFFFFFFFFFFFFFFF))) * sx(0x40, SymVar_0)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) - 0x7A3FEB) & 0xFFFFFFFFFFFFFFFF) | ((SymVar_0 >> (((((0x40 - (0x1 | (0xF & (((0x17F452 + (0x2918921B | SymVar_0)) & 0xFFFFFFFFFFFFFFFF) >> (0x4 & 0x3F))))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) & 0xFF) & 0x3F)) | ((SymVar_0 << ((((0x1 | (0xF & (((0x17F452 + (0x2918921B | SymVar_0)) & 0xFFFFFFFFFFFFFFFF) >> (0x4 & 0x3F)))) & 0xFFFFFFFF) & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF))) >> (0x2 & 0x3F))))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) | ((((((sx(0x40, (0x1247C27B & ((0x17F452 + (0x2918921B | SymVar_0)) & 0xFFFFFFFFFFFFFFFF))) * sx(0x40, SymVar_0)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) - 0x7A3FEB) & 0xFFFFFFFFFFFFFFFF) | ((SymVar_0 >> (((((0x40 - (0x1 | (0xF & (((0x17F452 + (0x2918921B | SymVar_0)) & 0xFFFFFFFFFFFFFFFF) >> (0x4 & 0x3F))))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) & 0xFF) & 0x3F)) | ((SymVar_0 << ((((0x1 | (0xF & (((0x17F452 + (0x2918921B | SymVar_0)) & 0xFFFFFFFFFFFFFFFF) >> (0x4 & 0x3F)))) & 0xFFFFFFFF) & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF))) >> ((((0x1 | (0xF & ((((((sx(0x40, (0x1247C27B & ((0x17F452 + (0x2918921B | SymVar_0)) & 0xFFFFFFFFFFFFFFFF))) * sx(0x40, SymVar_0)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) - 0x7A3FEB) & 0xFFFFFFFFFFFFFFFF) | ((SymVar_0 >> (((((0x40 - (0x1 | (0xF & (((0x17F452 + (0x2918921B | SymVar_0)) & 0xFFFFFFFFFFFFFFFF) >> (0x4 & 0x3F))))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) & 0xFF) & 0x3F)) | ((SymVar_0 << ((((0x1 | (0xF & (((0x17F452 + (0x2918921B | SymVar_0)) & 0xFFFFFFFFFFFFFFFF) >> (0x4 & 0x3F)))) & 0xFFFFFFFF) & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF))) >> (0x2 & 0x3F)))) & 0xFFFFFFFF) & 0xFF) & 0x3F)))) << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) | ((0x17F452 + (0x2918921B | SymVar_0)) & 0xFFFFFFFFFFFFFFFF))) / (((((((((0x0 & 0xFF)) << 8 | (0x0 & 0xFF)) << 8 | (0x0 & 0xFF)) << 8 | (0x0 & 0xFF)) << 8 | (0x0 & 0xFF)) << 8 | (0x0 & 0xFF)) << 8 | (0x0 & 0xFF)) << 8 | (0x7 & 0xFF))) << ((((0x1 | (0xF & ((((((((sx(0x40, (0x1247C27B & ((0x17F452 + (0x2918921B | SymVar_0)) & 0xFFFFFFFFFFFFFFFF))) * sx(0x40, SymVar_0)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) - 0x7A3FEB) & 0xFFFFFFFFFFFFFFFF) | ((SymVar_0 >> (((((0x40 - (0x1 | (0xF & (((0x17F452 + (0x2918921B | SymVar_0)) & 0xFFFFFFFFFFFFFFFF) >> (0x4 & 0x3F))))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) & 0xFF) & 0x3F)) | ((SymVar_0 << ((((0x1 | (0xF & (((0x17F452 + (0x2918921B | SymVar_0)) & 0xFFFFFFFFFFFFFFFF) >> (0x4 & 0x3F)))) & 0xFFFFFFFF) & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF))) << ((((0x1 | (0x7 & ((((((((sx(0x40, (0x1247C27B & ((0x17F452 + (0x2918921B | SymVar_0)) & 0xFFFFFFFFFFFFFFFF))) * sx(0x40, SymVar_0)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) - 0x7A3FEB) & 0xFFFFFFFFFFFFFFFF) | ((SymVar_0 >> (((((0x40 - (0x1 | (0xF & (((0x17F452 + (0x2918921B | SymVar_0)) & 0xFFFFFFFFFFFFFFFF) >> (0x4 & 0x3F))))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) & 0xFF) & 0x3F)) | ((SymVar_0 << ((((0x1 | (0xF & (((0x17F452 + (0x2918921B | SymVar_0)) & 0xFFFFFFFFFFFFFFFF) >> (0x4 & 0x3F)))) & 0xFFFFFFFF) & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF))) + 0x3E469461) & 0xFFFFFFFFFFFFFFFF) | SymVar_0))) & 0xFFFFFFFF) & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) >> (0x4 & 0x3F)))) & 0xFFFFFFFF) & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF))
print a & 0xffffffffffffffff
