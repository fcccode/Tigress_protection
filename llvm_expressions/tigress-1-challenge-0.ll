; ModuleID = ""
target triple = "unknown-unknown-unknown"
target datalayout = ""

define i64 @"__arybo"(i64 %"SymVar_0") nounwind
{
.3:
  %".4" = sub i64 %"SymVar_0", 244138822
  %".5" = zext i8 57 to i64
  %".6" = and i64 %".5", 63
  %".7" = shl i64 %"SymVar_0", %".6"
  %".8" = zext i8 7 to i64
  %".9" = and i64 %".8", 63
  %".10" = lshr i64 %"SymVar_0", %".9"
  %".11" = or i64 %".7", %".10"
  %".12" = or i64 %".4", %".11"
  %".13" = and i64 63, %".12"
  %".14" = zext i8 4 to i64
  %".15" = and i64 %".14", 63
  %".16" = shl i64 %".13", %".15"
  %".17" = or i64 %".16", %".11"
  %".18" = zext i8 53 to i64
  %".19" = and i64 %".18", 63
  %".20" = shl i64 %"SymVar_0", %".19"
  %".21" = zext i8 11 to i64
  %".22" = and i64 %".21", 63
  %".23" = lshr i64 %"SymVar_0", %".22"
  %".24" = or i64 %".20", %".23"
  %".25" = add i64 %".11", 759888027
  %".26" = and i64 %".25", 492486502
  %".27" = sub i64 %".24", %".26"
  %".28" = and i64 15, %".27"
  %".29" = or i64 %".28", 1
  %".30" = trunc i64 %".29" to i32
  %".31" = zext i32 %".30" to i64
  %".32" = trunc i64 %".31" to i8
  %".33" = zext i8 %".32" to i64
  %".34" = and i64 %".33", 63
  %".35" = lshr i64 %".17", %".34"
  %".36" = and i64 15, %".27"
  %".37" = or i64 1, %".36"
  %".38" = sub i64 64, %".37"
  %".39" = trunc i64 %".38" to i32
  %".40" = zext i32 %".39" to i64
  %".41" = trunc i64 %".40" to i8
  %".42" = zext i8 %".41" to i64
  %".43" = and i64 %".42", 63
  %".44" = shl i64 %".17", %".43"
  %".45" = or i64 %".35", %".44"
  %".46" = zext i8 1 to i64
  %".47" = and i64 %".46", 63
  %".48" = lshr i64 %".17", %".47"
  %".49" = and i64 15, %".48"
  %".50" = or i64 1, %".49"
  %".51" = trunc i64 %".50" to i32
  %".52" = zext i32 %".51" to i64
  %".53" = trunc i64 %".52" to i8
  %".54" = zext i8 %".53" to i64
  %".55" = and i64 %".54", 63
  %".56" = lshr i64 %".27", %".55"
  %".57" = zext i8 1 to i64
  %".58" = and i64 %".57", 63
  %".59" = lshr i64 %".17", %".58"
  %".60" = and i64 15, %".59"
  %".61" = or i64 1, %".60"
  %".62" = sub i64 64, %".61"
  %".63" = trunc i64 %".62" to i32
  %".64" = zext i32 %".63" to i64
  %".65" = trunc i64 %".64" to i8
  %".66" = zext i8 %".65" to i64
  %".67" = and i64 %".66", 63
  %".68" = shl i64 %".27", %".67"
  %".69" = or i64 %".56", %".68"
  %".70" = add i64 541408995, %".11"
  %".71" = sub i64 %"SymVar_0", %".70"
  %".72" = sub i64 %".69", %".71"
  %".73" = or i64 %".72", %".71"
  %".74" = zext i8 1 to i64
  %".75" = and i64 %".74", 63
  %".76" = lshr i64 %".73", %".75"
  %".77" = and i64 7, %".76"
  %".78" = or i64 1, %".77"
  %".79" = trunc i64 %".78" to i32
  %".80" = zext i32 %".79" to i64
  %".81" = trunc i64 %".80" to i8
  %".82" = zext i8 %".81" to i64
  %".83" = and i64 %".82", 63
  %".84" = shl i64 %".45", %".83"
  ret i64 %".84"
}
