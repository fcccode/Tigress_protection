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
a = ((sx(0x40, ((((((0x3F & ((((0xAD6EED + ((((SymVar_0 >> (0x39 & 0x3F)) | ((SymVar_0 << (0x7 & 0x3F)) & 0xFFFFFFFFFFFFFFFF)) >> (((((0x40 - (0x1 | (0xF & (((sx(0x40, ((sx(0x40, ((0x3F22161B + SymVar_0) & 0xFFFFFFFFFFFFFFFF)) * sx(0x40, 0x378AED0A)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF)) * sx(0x40, 0xDF2B78B)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) >> (0x1 & 0x3F))))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) & 0xFF) & 0x3F)) | ((((SymVar_0 >> (0x39 & 0x3F)) | ((SymVar_0 << (0x7 & 0x3F)) & 0xFFFFFFFFFFFFFFFF)) << ((((0x1 | (0xF & (((sx(0x40, ((sx(0x40, ((0x3F22161B + SymVar_0) & 0xFFFFFFFFFFFFFFFF)) * sx(0x40, 0x378AED0A)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF)) * sx(0x40, 0xDF2B78B)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) >> (0x1 & 0x3F)))) & 0xFFFFFFFF) & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) + SymVar_0) & 0xFFFFFFFFFFFFFFFF)) << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) | (((((0x2B6B05ED + ((((SymVar_0 >> (0x39 & 0x3F)) | ((SymVar_0 << (0x7 & 0x3F)) & 0xFFFFFFFFFFFFFFFF)) >> (((((0x40 - (0x1 | (0xF & (((sx(0x40, ((sx(0x40, ((0x3F22161B + SymVar_0) & 0xFFFFFFFFFFFFFFFF)) * sx(0x40, 0x378AED0A)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF)) * sx(0x40, 0xDF2B78B)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) >> (0x1 & 0x3F))))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) & 0xFF) & 0x3F)) | ((((SymVar_0 >> (0x39 & 0x3F)) | ((SymVar_0 << (0x7 & 0x3F)) & 0xFFFFFFFFFFFFFFFF)) << ((((0x1 | (0xF & (((sx(0x40, ((sx(0x40, ((0x3F22161B + SymVar_0) & 0xFFFFFFFFFFFFFFFF)) * sx(0x40, 0x378AED0A)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF)) * sx(0x40, 0xDF2B78B)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) >> (0x1 & 0x3F)))) & 0xFFFFFFFF) & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) & ((((0xAD6EED + ((((SymVar_0 >> (0x39 & 0x3F)) | ((SymVar_0 << (0x7 & 0x3F)) & 0xFFFFFFFFFFFFFFFF)) >> (((((0x40 - (0x1 | (0xF & (((sx(0x40, ((sx(0x40, ((0x3F22161B + SymVar_0) & 0xFFFFFFFFFFFFFFFF)) * sx(0x40, 0x378AED0A)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF)) * sx(0x40, 0xDF2B78B)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) >> (0x1 & 0x3F))))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) & 0xFF) & 0x3F)) | ((((SymVar_0 >> (0x39 & 0x3F)) | ((SymVar_0 << (0x7 & 0x3F)) & 0xFFFFFFFFFFFFFFFF)) << ((((0x1 | (0xF & (((sx(0x40, ((sx(0x40, ((0x3F22161B + SymVar_0) & 0xFFFFFFFFFFFFFFFF)) * sx(0x40, 0x378AED0A)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF)) * sx(0x40, 0xDF2B78B)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) >> (0x1 & 0x3F)))) & 0xFFFFFFFF) & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) + SymVar_0) & 0xFFFFFFFFFFFFFFFF)) + (((0x3F22161B + SymVar_0) & 0xFFFFFFFFFFFFFFFF) | SymVar_0)) & 0xFFFFFFFFFFFFFFFF)) + ((((0xAD6EED + ((((SymVar_0 >> (0x39 & 0x3F)) | ((SymVar_0 << (0x7 & 0x3F)) & 0xFFFFFFFFFFFFFFFF)) >> (((((0x40 - (0x1 | (0xF & (((sx(0x40, ((sx(0x40, ((0x3F22161B + SymVar_0) & 0xFFFFFFFFFFFFFFFF)) * sx(0x40, 0x378AED0A)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF)) * sx(0x40, 0xDF2B78B)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) >> (0x1 & 0x3F))))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) & 0xFF) & 0x3F)) | ((((SymVar_0 >> (0x39 & 0x3F)) | ((SymVar_0 << (0x7 & 0x3F)) & 0xFFFFFFFFFFFFFFFF)) << ((((0x1 | (0xF & (((sx(0x40, ((sx(0x40, ((0x3F22161B + SymVar_0) & 0xFFFFFFFFFFFFFFFF)) * sx(0x40, 0x378AED0A)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF)) * sx(0x40, 0xDF2B78B)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) >> (0x1 & 0x3F)))) & 0xFFFFFFFF) & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF))) & 0xFFFFFFFFFFFFFFFF) + SymVar_0) & 0xFFFFFFFFFFFFFFFF)) & 0xFFFFFFFFFFFFFFFF)) * sx(0x40, ((((0x3F22161B + SymVar_0) & 0xFFFFFFFFFFFFFFFF) >> (((((0x40 - (0x1 | (0xF & (((((SymVar_0 >> (0x39 & 0x3F)) | ((SymVar_0 << (0x7 & 0x3F)) & 0xFFFFFFFFFFFFFFFF)) >> (((((0x40 - (0x1 | (0xF & (((sx(0x40, ((sx(0x40, ((0x3F22161B + SymVar_0) & 0xFFFFFFFFFFFFFFFF)) * sx(0x40, 0x378AED0A)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF)) * sx(0x40, 0xDF2B78B)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) >> (0x1 & 0x3F))))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) & 0xFF) & 0x3F)) | ((((SymVar_0 >> (0x39 & 0x3F)) | ((SymVar_0 << (0x7 & 0x3F)) & 0xFFFFFFFFFFFFFFFF)) << ((((0x1 | (0xF & (((sx(0x40, ((sx(0x40, ((0x3F22161B + SymVar_0) & 0xFFFFFFFFFFFFFFFF)) * sx(0x40, 0x378AED0A)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF)) * sx(0x40, 0xDF2B78B)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) >> (0x1 & 0x3F)))) & 0xFFFFFFFF) & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF)) >> (0x4 & 0x3F))))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) & 0xFF) & 0x3F)) | ((((0x3F22161B + SymVar_0) & 0xFFFFFFFFFFFFFFFF) << ((((0x1 | (0xF & (((((SymVar_0 >> (0x39 & 0x3F)) | ((SymVar_0 << (0x7 & 0x3F)) & 0xFFFFFFFFFFFFFFFF)) >> (((((0x40 - (0x1 | (0xF & (((sx(0x40, ((sx(0x40, ((0x3F22161B + SymVar_0) & 0xFFFFFFFFFFFFFFFF)) * sx(0x40, 0x378AED0A)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF)) * sx(0x40, 0xDF2B78B)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) >> (0x1 & 0x3F))))) & 0xFFFFFFFFFFFFFFFF) & 0xFFFFFFFF) & 0xFF) & 0x3F)) | ((((SymVar_0 >> (0x39 & 0x3F)) | ((SymVar_0 << (0x7 & 0x3F)) & 0xFFFFFFFFFFFFFFFF)) << ((((0x1 | (0xF & (((sx(0x40, ((sx(0x40, ((0x3F22161B + SymVar_0) & 0xFFFFFFFFFFFFFFFF)) * sx(0x40, 0x378AED0A)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF)) * sx(0x40, 0xDF2B78B)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) >> (0x1 & 0x3F)))) & 0xFFFFFFFF) & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF)) >> (0x4 & 0x3F)))) & 0xFFFFFFFF) & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF)))) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF)
print a & 0xffffffffffffffff
