#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_154201 = SymVar_0
ref_154216 = ref_154201 # MOV operation
ref_1139525 = ref_154216 # MOV operation
ref_1139842 = ref_1139525 # MOV operation
ref_1184003 = ref_1139842 # MOV operation
ref_1184311 = ref_1184003 # MOV operation
ref_1184325 = ((0x3F22161B + ref_1184311) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_1184771 = ref_1184325 # MOV operation
ref_1617728 = ref_1184771 # MOV operation
ref_1618045 = ref_1617728 # MOV operation
ref_2367010 = ref_1618045 # MOV operation
ref_2367327 = ref_2367010 # MOV operation
ref_2402587 = ref_2367327 # MOV operation
ref_2411812 = ref_2402587 # MOV operation
ref_2411814 = ((sx(0x40, ref_2411812) * sx(0x40, 0x378AED0A)) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_2412248 = ref_2411814 # MOV operation
ref_2458167 = ref_2412248 # MOV operation
ref_2467392 = ref_2458167 # MOV operation
ref_2467394 = ((sx(0x40, ref_2467392) * sx(0x40, 0xDF2B78B)) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_2467828 = ref_2467394 # MOV operation
ref_2513747 = ref_2467828 # MOV operation
ref_2522968 = ref_2513747 # MOV operation
ref_2522974 = ref_2522968 # MOV operation
ref_2522978 = (ref_2522974 >> (0x1 & 0x3F)) # SHR operation
ref_2522985 = ref_2522978 # MOV operation
ref_2523454 = ref_2522985 # MOV operation
ref_2578274 = ref_2523454 # MOV operation
ref_2578572 = ref_2578274 # MOV operation
ref_2578586 = (0xF & ref_2578572) # AND operation
ref_2579019 = ref_2578586 # MOV operation
ref_2633839 = ref_2579019 # MOV operation
ref_2634147 = ref_2633839 # MOV operation
ref_2634161 = (0x1 | ref_2634147) # OR operation
ref_2634635 = ref_2634161 # MOV operation
ref_2689455 = ref_2634635 # MOV operation
ref_2689807 = ref_2689455 # MOV operation
ref_2689811 = ((0x40 - ref_2689807) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_2689819 = ref_2689811 # MOV operation
ref_2690265 = ref_2689819 # MOV operation
ref_3134945 = ref_154216 # MOV operation
ref_3135262 = ref_3134945 # MOV operation
ref_3170522 = ref_3135262 # MOV operation
ref_3179743 = ref_3170522 # MOV operation
ref_3179749 = ref_3179743 # MOV operation
ref_3179753 = (ref_3179749 >> (0x39 & 0x3F)) # SHR operation
ref_3179760 = ref_3179753 # MOV operation
ref_3180229 = ref_3179760 # MOV operation
ref_3624909 = ref_154216 # MOV operation
ref_3625226 = ref_3624909 # MOV operation
ref_3660486 = ref_3625226 # MOV operation
ref_3669724 = ref_3660486 # MOV operation
ref_3669730 = ref_3669724 # MOV operation
ref_3669734 = ((ref_3669730 << (0x7 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_3669741 = ref_3669734 # MOV operation
ref_3670184 = ref_3669741 # MOV operation
ref_3716103 = ref_3180229 # MOV operation
ref_3725004 = ref_3670184 # MOV operation
ref_3725312 = ref_3725004 # MOV operation
ref_3725324 = ref_3716103 # MOV operation
ref_3725326 = (ref_3725324 | ref_3725312) # OR operation
ref_3725800 = ref_3725326 # MOV operation
ref_3771719 = ref_3725800 # MOV operation
ref_3780620 = ref_2690265 # MOV operation
ref_3780940 = ref_3771719 # MOV operation
ref_3780944 = ref_3780620 # MOV operation
ref_3780946 = ref_3780940 # MOV operation
ref_3780948 = (ref_3780944 & 0xFFFFFFFF) # MOV operation
ref_3780950 = (ref_3780946 >> ((ref_3780948 & 0xFF) & 0x3F)) # SHR operation
ref_3780957 = ref_3780950 # MOV operation
ref_3781426 = ref_3780957 # MOV operation
ref_4477723 = ref_1618045 # MOV operation
ref_4478040 = ref_4477723 # MOV operation
ref_4513300 = ref_4478040 # MOV operation
ref_4522525 = ref_4513300 # MOV operation
ref_4522527 = ((sx(0x40, ref_4522525) * sx(0x40, 0x378AED0A)) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_4522961 = ref_4522527 # MOV operation
ref_4568880 = ref_4522961 # MOV operation
ref_4578105 = ref_4568880 # MOV operation
ref_4578107 = ((sx(0x40, ref_4578105) * sx(0x40, 0xDF2B78B)) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_4578541 = ref_4578107 # MOV operation
ref_4624460 = ref_4578541 # MOV operation
ref_4633681 = ref_4624460 # MOV operation
ref_4633687 = ref_4633681 # MOV operation
ref_4633691 = (ref_4633687 >> (0x1 & 0x3F)) # SHR operation
ref_4633698 = ref_4633691 # MOV operation
ref_4634167 = ref_4633698 # MOV operation
ref_4688987 = ref_4634167 # MOV operation
ref_4689285 = ref_4688987 # MOV operation
ref_4689299 = (0xF & ref_4689285) # AND operation
ref_4689732 = ref_4689299 # MOV operation
ref_4744552 = ref_4689732 # MOV operation
ref_4744860 = ref_4744552 # MOV operation
ref_4744874 = (0x1 | ref_4744860) # OR operation
ref_4745348 = ref_4744874 # MOV operation
ref_5190028 = ref_154216 # MOV operation
ref_5190345 = ref_5190028 # MOV operation
ref_5225605 = ref_5190345 # MOV operation
ref_5234826 = ref_5225605 # MOV operation
ref_5234832 = ref_5234826 # MOV operation
ref_5234836 = (ref_5234832 >> (0x39 & 0x3F)) # SHR operation
ref_5234843 = ref_5234836 # MOV operation
ref_5235312 = ref_5234843 # MOV operation
ref_5679992 = ref_154216 # MOV operation
ref_5680309 = ref_5679992 # MOV operation
ref_5715569 = ref_5680309 # MOV operation
ref_5724807 = ref_5715569 # MOV operation
ref_5724813 = ref_5724807 # MOV operation
ref_5724817 = ((ref_5724813 << (0x7 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_5724824 = ref_5724817 # MOV operation
ref_5725267 = ref_5724824 # MOV operation
ref_5771186 = ref_5235312 # MOV operation
ref_5780087 = ref_5725267 # MOV operation
ref_5780395 = ref_5780087 # MOV operation
ref_5780407 = ref_5771186 # MOV operation
ref_5780409 = (ref_5780407 | ref_5780395) # OR operation
ref_5780883 = ref_5780409 # MOV operation
ref_5826802 = ref_5780883 # MOV operation
ref_5835703 = ref_4745348 # MOV operation
ref_5836040 = ref_5826802 # MOV operation
ref_5836044 = ref_5835703 # MOV operation
ref_5836046 = ref_5836040 # MOV operation
ref_5836048 = (ref_5836044 & 0xFFFFFFFF) # MOV operation
ref_5836050 = ((ref_5836046 << ((ref_5836048 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_5836057 = ref_5836050 # MOV operation
ref_5836500 = ref_5836057 # MOV operation
ref_5882419 = ref_3781426 # MOV operation
ref_5891320 = ref_5836500 # MOV operation
ref_5891628 = ref_5891320 # MOV operation
ref_5891640 = ref_5882419 # MOV operation
ref_5891642 = (ref_5891640 | ref_5891628) # OR operation
ref_5892116 = ref_5891642 # MOV operation
ref_6325073 = ref_5892116 # MOV operation
ref_6325390 = ref_6325073 # MOV operation
ref_6811015 = ref_6325390 # MOV operation
ref_6811332 = ref_6811015 # MOV operation
ref_6855493 = ref_6811332 # MOV operation
ref_6855801 = ref_6855493 # MOV operation
ref_6855815 = ((0xAD6EED + ref_6855801) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_6856261 = ref_6855815 # MOV operation
ref_7248273 = ref_154216 # MOV operation
ref_7248590 = ref_7248273 # MOV operation
ref_7283850 = ref_6856261 # MOV operation
ref_7292751 = ref_7248590 # MOV operation
ref_7293059 = ref_7292751 # MOV operation
ref_7293071 = ref_7283850 # MOV operation
ref_7293073 = ((ref_7293071 + ref_7293059) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_7293519 = ref_7293073 # MOV operation
ref_7726476 = ref_7293519 # MOV operation
ref_7726793 = ref_7726476 # MOV operation
ref_8212418 = ref_6325390 # MOV operation
ref_8212735 = ref_8212418 # MOV operation
ref_8256896 = ref_8212735 # MOV operation
ref_8257204 = ref_8256896 # MOV operation
ref_8257218 = ((0x2B6B05ED + ref_8257204) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_8257664 = ref_8257218 # MOV operation
ref_8690621 = ref_7726793 # MOV operation
ref_8690938 = ref_8690621 # MOV operation
ref_8726198 = ref_8257664 # MOV operation
ref_8735099 = ref_8690938 # MOV operation
ref_8735397 = ref_8735099 # MOV operation
ref_8735409 = ref_8726198 # MOV operation
ref_8735411 = (ref_8735409 & ref_8735397) # AND operation
ref_8735844 = ref_8735411 # MOV operation
ref_9168801 = ref_1618045 # MOV operation
ref_9169118 = ref_9168801 # MOV operation
ref_9550471 = ref_154216 # MOV operation
ref_9550788 = ref_9550471 # MOV operation
ref_9586048 = ref_9169118 # MOV operation
ref_9594949 = ref_9550788 # MOV operation
ref_9595257 = ref_9594949 # MOV operation
ref_9595269 = ref_9586048 # MOV operation
ref_9595271 = (ref_9595269 | ref_9595257) # OR operation
ref_9595745 = ref_9595271 # MOV operation
ref_9641664 = ref_8735844 # MOV operation
ref_9650565 = ref_9595745 # MOV operation
ref_9650873 = ref_9650565 # MOV operation
ref_9650885 = ref_9641664 # MOV operation
ref_9650887 = ((ref_9650885 + ref_9650873) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_9651333 = ref_9650887 # MOV operation
ref_10084290 = ref_9651333 # MOV operation
ref_10084607 = ref_10084290 # MOV operation
ref_10622900 = ref_7726793 # MOV operation
ref_10623217 = ref_10622900 # MOV operation
ref_10667378 = ref_10623217 # MOV operation
ref_10667676 = ref_10667378 # MOV operation
ref_10667690 = (0x3F & ref_10667676) # AND operation
ref_10668123 = ref_10667690 # MOV operation
ref_10714042 = ref_10668123 # MOV operation
ref_10723280 = ref_10714042 # MOV operation
ref_10723286 = ref_10723280 # MOV operation
ref_10723290 = ((ref_10723286 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_10723297 = ref_10723290 # MOV operation
ref_10723740 = ref_10723297 # MOV operation
ref_11156697 = ref_10084607 # MOV operation
ref_11157014 = ref_11156697 # MOV operation
ref_11192274 = ref_10723740 # MOV operation
ref_11201175 = ref_11157014 # MOV operation
ref_11201483 = ref_11201175 # MOV operation
ref_11201495 = ref_11192274 # MOV operation
ref_11201497 = (ref_11201495 | ref_11201483) # OR operation
ref_11201971 = ref_11201497 # MOV operation
ref_11634928 = ref_11201971 # MOV operation
ref_11635245 = ref_11634928 # MOV operation
ref_12278874 = ref_6325390 # MOV operation
ref_12279191 = ref_12278874 # MOV operation
ref_12314451 = ref_12279191 # MOV operation
ref_12323672 = ref_12314451 # MOV operation
ref_12323678 = ref_12323672 # MOV operation
ref_12323682 = (ref_12323678 >> (0x4 & 0x3F)) # SHR operation
ref_12323689 = ref_12323682 # MOV operation
ref_12324158 = ref_12323689 # MOV operation
ref_12378978 = ref_12324158 # MOV operation
ref_12379276 = ref_12378978 # MOV operation
ref_12379290 = (0xF & ref_12379276) # AND operation
ref_12379723 = ref_12379290 # MOV operation
ref_12434543 = ref_12379723 # MOV operation
ref_12434851 = ref_12434543 # MOV operation
ref_12434865 = (0x1 | ref_12434851) # OR operation
ref_12435339 = ref_12434865 # MOV operation
ref_12490159 = ref_12435339 # MOV operation
ref_12490511 = ref_12490159 # MOV operation
ref_12490515 = ((0x40 - ref_12490511) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_12490523 = ref_12490515 # MOV operation
ref_12490969 = ref_12490523 # MOV operation
ref_12923926 = ref_1618045 # MOV operation
ref_12924243 = ref_12923926 # MOV operation
ref_12959503 = ref_12924243 # MOV operation
ref_12968404 = ref_12490969 # MOV operation
ref_12968724 = ref_12959503 # MOV operation
ref_12968728 = ref_12968404 # MOV operation
ref_12968730 = ref_12968724 # MOV operation
ref_12968732 = (ref_12968728 & 0xFFFFFFFF) # MOV operation
ref_12968734 = (ref_12968730 >> ((ref_12968732 & 0xFF) & 0x3F)) # SHR operation
ref_12968741 = ref_12968734 # MOV operation
ref_12969210 = ref_12968741 # MOV operation
ref_13560171 = ref_6325390 # MOV operation
ref_13560488 = ref_13560171 # MOV operation
ref_13595748 = ref_13560488 # MOV operation
ref_13604969 = ref_13595748 # MOV operation
ref_13604975 = ref_13604969 # MOV operation
ref_13604979 = (ref_13604975 >> (0x4 & 0x3F)) # SHR operation
ref_13604986 = ref_13604979 # MOV operation
ref_13605455 = ref_13604986 # MOV operation
ref_13660275 = ref_13605455 # MOV operation
ref_13660573 = ref_13660275 # MOV operation
ref_13660587 = (0xF & ref_13660573) # AND operation
ref_13661020 = ref_13660587 # MOV operation
ref_13715840 = ref_13661020 # MOV operation
ref_13716148 = ref_13715840 # MOV operation
ref_13716162 = (0x1 | ref_13716148) # OR operation
ref_13716636 = ref_13716162 # MOV operation
ref_14149593 = ref_1618045 # MOV operation
ref_14149910 = ref_14149593 # MOV operation
ref_14185170 = ref_14149910 # MOV operation
ref_14194071 = ref_13716636 # MOV operation
ref_14194408 = ref_14185170 # MOV operation
ref_14194412 = ref_14194071 # MOV operation
ref_14194414 = ref_14194408 # MOV operation
ref_14194416 = (ref_14194412 & 0xFFFFFFFF) # MOV operation
ref_14194418 = ((ref_14194414 << ((ref_14194416 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_14194425 = ref_14194418 # MOV operation
ref_14194868 = ref_14194425 # MOV operation
ref_14240787 = ref_12969210 # MOV operation
ref_14249688 = ref_14194868 # MOV operation
ref_14249996 = ref_14249688 # MOV operation
ref_14250008 = ref_14240787 # MOV operation
ref_14250010 = (ref_14250008 | ref_14249996) # OR operation
ref_14250484 = ref_14250010 # MOV operation
ref_14683441 = ref_11635245 # MOV operation
ref_14683758 = ref_14683441 # MOV operation
ref_15106056 = ref_7726793 # MOV operation
ref_15106373 = ref_15106056 # MOV operation
ref_15141633 = ref_14683758 # MOV operation
ref_15150534 = ref_15106373 # MOV operation
ref_15150842 = ref_15150534 # MOV operation
ref_15150854 = ref_15141633 # MOV operation
ref_15150856 = ((ref_15150854 + ref_15150842) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_15151302 = ref_15150856 # MOV operation
ref_15197221 = ref_15151302 # MOV operation
ref_15206122 = ref_14250484 # MOV operation
ref_15206434 = ref_15206122 # MOV operation
ref_15206446 = ref_15197221 # MOV operation
ref_15206448 = ((sx(0x40, ref_15206446) * sx(0x40, ref_15206434)) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_15206882 = ref_15206448 # MOV operation
ref_15598827 = ref_15206882 # MOV operation
ref_15599144 = ref_15598827 # MOV operation
ref_15660405 = ref_15599144 # MOV operation
ref_15660407 = ref_15660405 # MOV operation

print ref_15660407 & 0xffffffffffffffff
