; ModuleID = ""
target triple = "unknown-unknown-unknown"
target datalayout = ""

define i64 @"__arybo"(i64 %"SymVar_0") nounwind
{
.3:
  %".4" = zext i8 59 to i64
  %".5" = and i64 %".4", 63
  %".6" = lshr i64 %"SymVar_0", %".5"
  %".7" = zext i8 5 to i64
  %".8" = and i64 %".7", 63
  %".9" = shl i64 %"SymVar_0", %".8"
  %".10" = xor i64 %".6", -1
  %".11" = and i64 %".9", %".10"
  %".12" = add i64 %".6", %".11"
  %".13" = sub i64 %".12", 23354192953344
  %".14" = or i64 18446720719516598271, %".12"
  %".15" = add i64 %".14", %".14"
  %".16" = sub i64 %".13", %".15"
  %".17" = sub i64 %".16", 2
  %".18" = xor i64 %"SymVar_0", -1
  %".19" = and i64 489677322, %".18"
  %".20" = sext i64 %".19" to i128
  %".21" = and i64 %"SymVar_0", 18446744073219874293
  %".22" = sext i64 %".21" to i128
  %".23" = mul i128 %".20", %".22"
  %".24" = trunc i128 %".23" to i64
  %".25" = and i64 %"SymVar_0", 489677322
  %".26" = sext i64 %".25" to i128
  %".27" = or i64 489677322, %"SymVar_0"
  %".28" = sext i64 %".27" to i128
  %".29" = mul i128 %".26", %".28"
  %".30" = trunc i128 %".29" to i64
  %".31" = add i64 %".24", %".30"
  %".32" = lshr i64 %".31", 32
  %".33" = trunc i64 %".32" to i8
  %".34" = zext i8 %".33" to i16
  %".35" = lshr i64 %".31", 40
  %".36" = trunc i64 %".35" to i8
  %".37" = zext i8 %".36" to i16
  %".38" = shl i16 %".37", 8
  %".39" = or i16 %".34", %".38"
  %".40" = zext i16 %".39" to i32
  %".41" = zext i32 %".40" to i64
  %".42" = trunc i64 %".41" to i16
  %".43" = zext i16 %".42" to i32
  %".44" = zext i32 %".43" to i64
  %".45" = trunc i64 %".44" to i16
  %".46" = zext i16 %".45" to i32
  %".47" = zext i32 %".46" to i64
  %".48" = trunc i64 %".47" to i16
  %".49" = zext i16 %".48" to i32
  %".50" = zext i32 %".49" to i64
  %".51" = trunc i64 %".50" to i16
  %".52" = trunc i16 %".51" to i8
  %".53" = zext i8 %".52" to i64
  %".54" = trunc i64 %".50" to i16
  %".55" = lshr i16 %".54", 8
  %".56" = trunc i16 %".55" to i8
  %".57" = zext i8 %".56" to i64
  %".58" = shl i64 %".57", 8
  %".59" = or i64 %".53", %".58"
  %".60" = trunc i64 %".31" to i8
  %".61" = zext i8 %".60" to i16
  %".62" = lshr i64 %".31", 8
  %".63" = trunc i64 %".62" to i8
  %".64" = zext i8 %".63" to i16
  %".65" = shl i16 %".64", 8
  %".66" = or i16 %".61", %".65"
  %".67" = zext i16 %".66" to i32
  %".68" = zext i32 %".67" to i64
  %".69" = trunc i64 %".68" to i16
  %".70" = zext i16 %".69" to i32
  %".71" = zext i32 %".70" to i64
  %".72" = trunc i64 %".71" to i16
  %".73" = zext i16 %".72" to i32
  %".74" = zext i32 %".73" to i64
  %".75" = trunc i64 %".74" to i16
  %".76" = zext i16 %".75" to i32
  %".77" = zext i32 %".76" to i64
  %".78" = trunc i64 %".77" to i16
  %".79" = trunc i16 %".78" to i8
  %".80" = zext i8 %".79" to i64
  %".81" = shl i64 %".80", 16
  %".82" = or i64 %".59", %".81"
  %".83" = trunc i64 %".77" to i16
  %".84" = lshr i16 %".83", 8
  %".85" = trunc i16 %".84" to i8
  %".86" = zext i8 %".85" to i64
  %".87" = shl i64 %".86", 24
  %".88" = or i64 %".82", %".87"
  %".89" = lshr i64 %".31", 16
  %".90" = trunc i64 %".89" to i8
  %".91" = zext i8 %".90" to i16
  %".92" = lshr i64 %".31", 24
  %".93" = trunc i64 %".92" to i8
  %".94" = zext i8 %".93" to i16
  %".95" = shl i16 %".94", 8
  %".96" = or i16 %".91", %".95"
  %".97" = zext i16 %".96" to i32
  %".98" = zext i32 %".97" to i64
  %".99" = trunc i64 %".98" to i16
  %".100" = zext i16 %".99" to i32
  %".101" = zext i32 %".100" to i64
  %".102" = trunc i64 %".101" to i16
  %".103" = zext i16 %".102" to i32
  %".104" = zext i32 %".103" to i64
  %".105" = trunc i64 %".104" to i16
  %".106" = zext i16 %".105" to i32
  %".107" = zext i32 %".106" to i64
  %".108" = trunc i64 %".107" to i16
  %".109" = trunc i16 %".108" to i8
  %".110" = zext i8 %".109" to i64
  %".111" = shl i64 %".110", 32
  %".112" = or i64 %".88", %".111"
  %".113" = trunc i64 %".107" to i16
  %".114" = lshr i16 %".113", 8
  %".115" = trunc i16 %".114" to i8
  %".116" = zext i8 %".115" to i64
  %".117" = shl i64 %".116", 40
  %".118" = or i64 %".112", %".117"
  %".119" = lshr i64 %".31", 48
  %".120" = trunc i64 %".119" to i8
  %".121" = zext i8 %".120" to i64
  %".122" = shl i64 %".121", 48
  %".123" = or i64 %".118", %".122"
  %".124" = lshr i64 %".31", 56
  %".125" = trunc i64 %".124" to i8
  %".126" = zext i8 %".125" to i64
  %".127" = shl i64 %".126", 56
  %".128" = or i64 %".123", %".127"
  %".129" = xor i64 %".128", -1
  %".130" = or i64 %".129", 15
  %".131" = add i64 %".128", %".130"
  %".132" = add i64 %".131", 1
  %".133" = zext i8 2 to i64
  %".134" = and i64 %".133", 63
  %".135" = shl i64 %".132", %".134"
  %".136" = zext i64 %"SymVar_0" to i128
  %".137" = zext i64 0 to i128
  %".138" = shl i128 %".137", 64
  %".139" = or i128 %".136", %".138"
  %".140" = zext i8 9 to i64
  %".141" = zext i8 0 to i64
  %".142" = shl i64 %".141", 8
  %".143" = or i64 %".140", %".142"
  %".144" = zext i8 0 to i64
  %".145" = shl i64 %".144", 16
  %".146" = or i64 %".143", %".145"
  %".147" = zext i8 0 to i64
  %".148" = shl i64 %".147", 24
  %".149" = or i64 %".146", %".148"
  %".150" = zext i8 0 to i64
  %".151" = shl i64 %".150", 32
  %".152" = or i64 %".149", %".151"
  %".153" = zext i8 0 to i64
  %".154" = shl i64 %".153", 40
  %".155" = or i64 %".152", %".154"
  %".156" = zext i8 0 to i64
  %".157" = shl i64 %".156", 48
  %".158" = or i64 %".155", %".157"
  %".159" = zext i8 0 to i64
  %".160" = shl i64 %".159", 56
  %".161" = or i64 %".158", %".160"
  %".162" = zext i64 %".161" to i128
  %".163" = udiv i128 %".139", %".162"
  %".164" = trunc i128 %".163" to i64
  %".165" = add i64 471942434304, %".164"
  %".166" = lshr i64 %".165", 32
  %".167" = trunc i64 %".166" to i8
  %".168" = zext i8 %".167" to i32
  %".169" = lshr i64 %".165", 40
  %".170" = trunc i64 %".169" to i8
  %".171" = zext i8 %".170" to i32
  %".172" = shl i32 %".171", 8
  %".173" = or i32 %".168", %".172"
  %".174" = lshr i64 %".165", 48
  %".175" = trunc i64 %".174" to i8
  %".176" = zext i8 %".175" to i32
  %".177" = shl i32 %".176", 16
  %".178" = or i32 %".173", %".177"
  %".179" = lshr i64 %".165", 56
  %".180" = trunc i64 %".179" to i8
  %".181" = zext i8 %".180" to i32
  %".182" = shl i32 %".181", 24
  %".183" = or i32 %".178", %".182"
  %".184" = zext i32 %".183" to i64
  %".185" = trunc i64 %".184" to i32
  %".186" = zext i32 %".185" to i64
  %".187" = trunc i64 %".186" to i32
  %".188" = zext i32 %".187" to i64
  %".189" = trunc i64 %".188" to i32
  %".190" = zext i32 %".189" to i64
  %".191" = trunc i64 %".190" to i32
  %".192" = zext i32 %".191" to i64
  %".193" = trunc i64 %".192" to i32
  %".194" = zext i32 %".193" to i64
  %".195" = trunc i64 %".194" to i32
  %".196" = zext i32 %".195" to i64
  %".197" = trunc i64 %".196" to i32
  %".198" = zext i32 %".197" to i64
  %".199" = trunc i64 %".198" to i32
  %".200" = zext i32 %".199" to i64
  %".201" = trunc i64 %".200" to i32
  %".202" = zext i32 %".201" to i64
  %".203" = trunc i64 %".202" to i32
  %".204" = trunc i32 %".203" to i8
  %".205" = zext i8 %".204" to i64
  %".206" = trunc i64 %".202" to i32
  %".207" = lshr i32 %".206", 8
  %".208" = trunc i32 %".207" to i8
  %".209" = zext i8 %".208" to i64
  %".210" = shl i64 %".209", 8
  %".211" = or i64 %".205", %".210"
  %".212" = trunc i64 %".202" to i32
  %".213" = lshr i32 %".212", 16
  %".214" = trunc i32 %".213" to i8
  %".215" = zext i8 %".214" to i64
  %".216" = shl i64 %".215", 16
  %".217" = or i64 %".211", %".216"
  %".218" = trunc i64 %".202" to i32
  %".219" = lshr i32 %".218", 24
  %".220" = trunc i32 %".219" to i8
  %".221" = zext i8 %".220" to i64
  %".222" = shl i64 %".221", 24
  %".223" = or i64 %".217", %".222"
  %".224" = trunc i64 %".165" to i8
  %".225" = zext i8 %".224" to i32
  %".226" = lshr i64 %".165", 8
  %".227" = trunc i64 %".226" to i8
  %".228" = zext i8 %".227" to i32
  %".229" = shl i32 %".228", 8
  %".230" = or i32 %".225", %".229"
  %".231" = lshr i64 %".165", 16
  %".232" = trunc i64 %".231" to i8
  %".233" = zext i8 %".232" to i32
  %".234" = shl i32 %".233", 16
  %".235" = or i32 %".230", %".234"
  %".236" = lshr i64 %".165", 24
  %".237" = trunc i64 %".236" to i8
  %".238" = zext i8 %".237" to i32
  %".239" = shl i32 %".238", 24
  %".240" = or i32 %".235", %".239"
  %".241" = zext i32 %".240" to i64
  %".242" = trunc i64 %".241" to i32
  %".243" = zext i32 %".242" to i64
  %".244" = trunc i64 %".243" to i32
  %".245" = zext i32 %".244" to i64
  %".246" = trunc i64 %".245" to i32
  %".247" = zext i32 %".246" to i64
  %".248" = trunc i64 %".247" to i32
  %".249" = zext i32 %".248" to i64
  %".250" = trunc i64 %".249" to i32
  %".251" = zext i32 %".250" to i64
  %".252" = trunc i64 %".251" to i32
  %".253" = zext i32 %".252" to i64
  %".254" = trunc i64 %".253" to i32
  %".255" = zext i32 %".254" to i64
  %".256" = trunc i64 %".255" to i32
  %".257" = trunc i32 %".256" to i8
  %".258" = zext i8 %".257" to i64
  %".259" = shl i64 %".258", 32
  %".260" = or i64 %".223", %".259"
  %".261" = trunc i64 %".255" to i32
  %".262" = lshr i32 %".261", 8
  %".263" = trunc i32 %".262" to i8
  %".264" = zext i8 %".263" to i64
  %".265" = shl i64 %".264", 40
  %".266" = or i64 %".260", %".265"
  %".267" = trunc i64 %".255" to i32
  %".268" = lshr i32 %".267", 16
  %".269" = trunc i32 %".268" to i8
  %".270" = zext i8 %".269" to i64
  %".271" = shl i64 %".270", 48
  %".272" = or i64 %".266", %".271"
  %".273" = trunc i64 %".255" to i32
  %".274" = lshr i32 %".273", 24
  %".275" = trunc i32 %".274" to i8
  %".276" = zext i8 %".275" to i64
  %".277" = shl i64 %".276", 56
  %".278" = or i64 %".272", %".277"
  %".279" = xor i64 %".135", -1
  %".280" = and i64 %".278", %".279"
  %".281" = add i64 %".135", %".280"
  %".282" = xor i64 %".281", -1
  %".283" = or i64 %".282", 7
  %".284" = add i64 %".281", %".283"
  %".285" = add i64 %".284", 1
  %".286" = and i64 %".285", 18446744073709551614
  %".287" = add i64 1, %".286"
  %".288" = trunc i64 %".287" to i32
  %".289" = zext i32 %".288" to i64
  %".290" = trunc i64 %".289" to i8
  %".291" = zext i8 %".290" to i64
  %".292" = and i64 %".291", 63
  %".293" = shl i64 %".17", %".292"
  %".294" = zext i8 %".52" to i64
  %".295" = zext i8 %".56" to i64
  %".296" = shl i64 %".295", 8
  %".297" = or i64 %".294", %".296"
  %".298" = zext i8 %".79" to i64
  %".299" = shl i64 %".298", 16
  %".300" = or i64 %".297", %".299"
  %".301" = zext i8 %".85" to i64
  %".302" = shl i64 %".301", 24
  %".303" = or i64 %".300", %".302"
  %".304" = zext i8 %".109" to i64
  %".305" = shl i64 %".304", 32
  %".306" = or i64 %".303", %".305"
  %".307" = zext i8 %".115" to i64
  %".308" = shl i64 %".307", 40
  %".309" = or i64 %".306", %".308"
  %".310" = zext i8 %".120" to i64
  %".311" = shl i64 %".310", 48
  %".312" = or i64 %".309", %".311"
  %".313" = zext i8 %".125" to i64
  %".314" = shl i64 %".313", 56
  %".315" = or i64 %".312", %".314"
  %".316" = or i64 %".17", %".315"
  %".317" = or i64 %".315", %".17"
  %".318" = add i64 %".316", %".317"
  %".319" = xor i64 %".17", -1
  %".320" = xor i64 %".315", %".319"
  %".321" = add i64 %".318", %".320"
  %".322" = add i64 %".321", 1
  %".323" = zext i8 57 to i64
  %".324" = and i64 %".323", 63
  %".325" = shl i64 %"SymVar_0", %".324"
  %".326" = zext i8 7 to i64
  %".327" = and i64 %".326", 63
  %".328" = lshr i64 %"SymVar_0", %".327"
  %".329" = xor i64 %".325", -1
  %".330" = and i64 %".328", %".329"
  %".331" = add i64 %".325", %".330"
  %".332" = zext i8 61 to i64
  %".333" = and i64 %".332", 63
  %".334" = shl i64 %".331", %".333"
  %".335" = zext i8 57 to i64
  %".336" = and i64 %".335", 63
  %".337" = shl i64 %"SymVar_0", %".336"
  %".338" = zext i8 7 to i64
  %".339" = and i64 %".338", 63
  %".340" = lshr i64 %"SymVar_0", %".339"
  %".341" = xor i64 %".337", -1
  %".342" = and i64 %".340", %".341"
  %".343" = add i64 %".337", %".342"
  %".344" = zext i8 3 to i64
  %".345" = and i64 %".344", 63
  %".346" = lshr i64 %".343", %".345"
  %".347" = xor i64 %".334", -1
  %".348" = and i64 %".346", %".347"
  %".349" = add i64 %".334", %".348"
  %".350" = or i64 %".322", %".349"
  %".351" = or i64 %".349", %".322"
  %".352" = add i64 %".350", %".351"
  %".353" = xor i64 %".322", -1
  %".354" = xor i64 %".349", %".353"
  %".355" = add i64 %".352", %".354"
  %".356" = add i64 %".355", 1
  %".357" = xor i64 %".356", -1
  %".358" = add i64 %".293", %".357"
  %".359" = add i64 %".358", 1
  ret i64 %".359"
}
