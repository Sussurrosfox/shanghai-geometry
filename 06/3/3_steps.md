# 3 — 分步证明文字

## 步骤 0：题设条件与几何构型

在 △ABC 中，延长边 AB 至 D、延长边 AC 至 E 得到截线 l(DE)。
直线 l 关于 BC 垂直平分线的轴对称直线为 l'，分别交 AB, AC 延长线于 D', E'。
已知条件：BD + CE = DE。
求证目标：BD' + CE' = D'E'。

## 步骤 1：① 截长构造点 R 与内心 O

在 DE 上取点 R，使得 DR = BD。由已知 BD + CE = DE = DR + ER，立得 ER = CE。
设 △RBC 的外心为 O（即 OB = OR = OC）。
在等腰 △DBR 中，D 与 O 均在线段 BR 的垂直平分线上，故直线 OD ⊥ BR 且平分顶角 ∠ADE；
同理在等腰 △CER 中，OE ⊥ CR 且平分顶角 ∠AED。
两条内角平分线交于 O，因此 O 是 △ADE 的内心！

## 步骤 2：② 角度推导与四点共圆

由于 O 为 △RBC 的外心，圆心角 ∠BOC = 2∠BRC。
在平角 R 处：∠BRC = 180° - ∠BRD - ∠CRE。
在等腰 △DBR 与 △CER 中，两底角满足：
2∠BRD = 180° - ∠ADE, 2∠CRE = 180° - ∠AED。
从而 2∠BRC = ∠ADE + ∠AED。
代入三角形内角和得：∠A + ∠BOC = ∠A + ∠ADE + ∠AED = 180°！
对角互补，故 A, B, O, C 四点共圆！
又因 OB = OC，O 恰好落在 BC 的垂直平分线上。

## 步骤 3：③ 轴反射对称与 △AD'E' 的内心

以 BC 的垂直平分线为对称轴作轴反射。
因 OB = OC，O 位于对称轴上，故对称点为其自身！
直线 l 对称至 l'，点 R 对称至 R' ∈ l'，因此 OR' = OR = OB = OC。
由对称性与共圆角关系，∠OR'D' = ∠ORE = 180° - ∠OBD'，故 O, B, D', R' 四点共圆。
结合 OB = OR = OR'，可知直线 OD' 平分 ∠AD'E'，同理 OE' 平分 ∠AE'D'。
即 O 亦为 △AD'E' 的内心！

## 步骤 4：④ 截长构造点 K 与 △OBD' ≅ △OKD'

在 D'E' 上截取点 K，使得 KD' = BD'。
考虑 △OBD' 与 △OKD'：
① D'B = D'K（截长构造）；
② ∠BD'O = ∠KD'O（OD' 为内角平分线）；
③ OD' = OD'（公共边）。
由边角边（SAS）判定：△OBD' ≅ △OKD'！
由此得对应边 OK = OB = OC，且对应角 ∠BOD' = ∠KOD'。

## 步骤 5：⑤ 导角计算与 △OCE' ≅ △OKE'

在 △AD'E' 中，O 为内心，故 ∠D'OE' = 90° + ½∠A。
由 A, B, O, C 共圆，有 ∠BOC = 180° - ∠A。
由此得两翼角之和：∠BOD' + ∠COE' = 360° - ∠BOC - ∠D'OE' = 90° + ½∠A。
结合上一式 ∠BOD' = ∠KOD'，代入得：
∠KOD' + ∠COE' = ∠D'OE' = ∠KOD' + ∠KOE'，两边消去 ∠KOD'，即得：
∠COE' = ∠KOE'！
在 △OCE' 与 △OKE' 中：OC = OK，OE' 为公共边，夹角 ∠COE' = ∠KOE'。
由 SAS 判定：△OCE' ≅ △OKE'！

## 步骤 6：⑥ 对应边相等，原命题得证

由 △OCE' ≅ △OKE' 全等，立得对应边相等：
CE' = KE'。
结合步骤 ④ 截长构造的 BD' = KD'，将两段相加：
D'E' = KD' + KE' = BD' + CE'
即 BD' + CE' = D'E'。
原命题完全得证！
