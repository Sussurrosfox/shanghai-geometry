# 6 — 分步证明文字

## 步骤 0：题设条件与凸五边形

已知凸五边形 ABCDE 满足三边相等：
           AB = BC = CD
           且对应内角分别相等：
           ∠EAB = ∠BCD，∠EDC = ∠CBA
           求证：过点 E 作 BC 的垂线与对角线 AC, BD 三线共点。

## 步骤 1：作中垂线定点 I 与对角线交点 H

连结对角线 AC 与 BD，相交于点 H。
           因为 BA = BC，点 B 在 AC 的中垂线上；
           同理 CB = CD，点 C 在 BD 的中垂线上。
           设 AC, BD 的中垂线交于点 I，则：
           BI ⊥ AC 且 CI ⊥ BD

## 步骤 2：H 为 △BIC 的垂心 ⟹ IH ⊥ BC

考察 △BIC：
           直线 AC 过顶点 C 且 AC ⊥ BI，故 AC 为边 BI 上的高；
           直线 BD 过顶点 B 且 BD ⊥ CI，故 BD 为边 CI 上的高。
           两高线交点 H 即为 △BIC 的垂心！
           由垂心性质，第三条高线必过点 I 且垂直于底边：
           IH ⊥ BC（垂足为 K）

## 步骤 3：全等三角形 ⟹ AI, DI 为角平分线

连结 IA, ID。由中垂线性质，IA = IC, IB = ID。
           又 AB = BC = CD 且有公共边，由三边对应相等（SSS）：
           △IAB ≅ △ICB ≅ △ICD
           由此可得对应角相等：
           ∠IAB = ∠ICB = ½∠BCD = ½∠EAB ⟹ AI 平分 ∠EAB；
           ∠IDC = ∠IBC = ½∠CBA = ½∠EDC ⟹ DI 平分 ∠EDC。

## 步骤 4：点 I 为内切圆心与 ∠BIE 角度推导

点 I 到五边形各边距离相等，故 圆 I 为凸五边形 ABCDE 的内切圆，IE 平分 ∠AED。
           在四边形 ABIE 中，内角和为 360°：
           
             ∠BIE = 360° - ∠EAB - ½∠ABC - ½∠AED
           
           由五边形内角和 540° 得 ½∠AED = 270° - ∠EAB - ∠ABC，代入化简得：
           
             ∠BIE = 90° + ½∠ABC = 90° + ∠IBC

## 步骤 5：垂线共线 ⟹ 三线共点于 H

在直角 △IBK 中（IK ⊥ BC），∠BIK = 90° - ∠IBC。
           由于 ∠BIE = 90° + ∠IBC，故两角互补：
           
             ∠BIE + ∠BIK = 180° ⟹ 点 E, I, K 三点共线（EI ⊥ BC）
           
           结合 Step 2 已证的 IH ⊥ BC（点 I, H, K 共线），可知点 E, I, H, K 四点共线。
           因此，过点 E 作 BC 的垂线即为直线 EIHK，必然经过对角线交点 H。
           结论：过点 E 作 BC 的垂线与 AC, BD 三线共点于点 H！
