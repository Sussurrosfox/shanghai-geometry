# 3 — 分步证明文字

## 步骤 0：已知条件与图形架构

在 △ABC 中，∠C < ∠A < 90°。
点 D 位于边 AC 上且满足 BD = BA。
△ABC 的内切圆分别切边 AB, AC 于点 K, L；点 J 为 △BCD 的内心。
连结直线 KL 与线段 AJ，求证：直线 KL 经过线段 AJ 的中点。

## 步骤 1：① 作垂线 BS 与 JR，确定 AD 中点 S

过点 B 作 BS ⊥ AC 于点 S，直线 BS 与 KL 交于点 H。
过内心 J 作 JR ⊥ AC 于点 R（R 即为 △BCD 内切圆在边 AC 上的切点）。
在等腰 △BAD 中，因 BA = BD，高 BS 亦为底边中线，故 S 为 AD 的中点，即：
AS = SD = ½ AD

## 步骤 2：② 利用切线长导出 AL = SR 与 SL = DR

由切线长定理，AL = ½(AB + AC - BC)。
在 △BCD 中，切点 R 满足 DR = ½(BD + CD - BC)。
代入 BD = BA 与 CD = AC - AD，相减得：
AL - DR = ½ AD = AS = SD
在直线 AC 上计算：
LR = AD + DR - AL = AD - (AL - DR) = ½ AD = AS。
由此导出：
AL = SR 且 SL = DR

## 步骤 3：③ 由外角与角平分线性质导出 ∠SLH = ∠RDJ

在等腰 △AKL 中（AK = AL），底角 ∠ALK = 90° - ½∠A。
又在等腰 △BAD 中，外角 ∠CDB = 180° - ∠A。
因 J 是 △BCD 的内心，DJ 平分 ∠CDB，故：
∠CDJ = ½∠CDB = 90° - ½∠A
由点 A, S, L 共线知 ∠SLH = ∠ALK；由点 D, R, C 共线知 ∠RDJ = ∠CDJ。
因此得出关键角相等：∠SLH = ∠RDJ。

## 步骤 4：④ △LSH ≌ △DRJ 导出对应边 SH = JR

考察直角三角形 △LSH 与 △DRJ：
1. ∠LSH = ∠DRJ = 90°（垂直于边 AC）；
2. 直角边 SL = DR（由步骤 ②）；
3. 锐角 ∠SLH = ∠RDJ（由步骤 ③）。
根据直角三角形全等判定（ASA），得：
△LSH ≌ △DRJ
从而对应直角边相等：SH = JR。

## 步骤 5：⑤ 判定 HSRJ 为矩形，导出 HJ ∥ AL 且 HJ = AL

因为 HS ⊥ AC 且 JR ⊥ AC，所以 HS ∥ JR。
又 SH = JR（步骤 ④），故四边形 HSRJ 为平行四边形；
再结合 ∠HSR = 90°，知 HSRJ 为矩形！
由矩形性质，对边平行且相等：HJ ∥ SR 且 HJ = SR。
结合步骤 ② 中已证的 SR = AL 及 A, S, R 共线，立即得出：
HJ ∥ AL 且 HJ = AL

## 步骤 6：⑥ 判定 ALJH 为平行四边形，KL 平分 AJ

在四边形 ALJH 中：
因 HJ ∥ AL 且 HJ = AL，一组对边平行且相等，故 ALJH 为平行四边形！
在平行四边形中，对角线互相平分，因此对角线 HL 与 AJ 互相平分。
设其交点为 M，则 M 为线段 AJ 的中点。
又因点 H, L 均在直线 KL 上，直线 HL 即为直线 KL。
由此证明：直线 KL 经过线段 AJ 的中点 M！
