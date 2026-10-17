# 5 — 分步证明文字

## 步骤 0：已知条件与几何构型

在 △ABC 中，AB > AC，外接圆为 Γ。
           AD 为 ∠BAC 的外角平分线，交圆 Γ 于点 D（优弧 BAC 的中点）；
           AM 为 ∠BAC 的内角平分线，交圆 Γ 于点 M（劣弧 BC 的中点）；
           点 D 在 AB 上的射影为点 E（即 DE ⊥ AB）；
           N 为 AM 的中点；M 在 AC 上的射影为点 K（即 MK ⊥ AC）。
           求证：∠NEA = ∠NCK。

## 步骤 1：① 辅助垂线 DT ⟹ △AED ≅ △ATD

过点 D 作 DT ⊥ AC，垂足为 T（T 落在边 CA 的反向延长线上）。
           因为 AD 是 ∠BAC 的外角平分线，平分线上的点到角两边所在直线的距离相等：
           ∠EAD = ∠TAD 且 ∠AED = ∠ATD = 90°，AD 为公共斜边
           由 AAS 全等判定，可得：
           △AED ≅ △ATD ⟹ DE = DT 且 AE = AT。

## 步骤 2：② 圆内接性质与弦长 ⟹ Rt△DEB ≅ Rt△DTC

连接 DB, DC。
           由于 D 是外角平分线与外接圆的交点，D 平分优弧 BAC，故对应弦长 DB = DC。
           在圆内接四边形 ABDC 中，内对角与外角关系得 ∠DCT = ∠DBE。
           在直角三角形 Rt△DEB 与 Rt△DTC 中：
           斜边 DB = DC，直角边 DE = DT
           由斜边直角边（HL）判定定理：
           Rt△DEB ≅ Rt△DTC ⟹ BE = CT。

## 步骤 3：③ 折弦推导 ⟹ AE = CK = ½(AB - AC)

由上一步的 BE = CT，在边 AB 上有：
           AB = AE + BE = AE + CT
           又因为 T 在 CA 的延长线上，且已证 AT = AE，故：
           CT = AC + AT = AC + AE
           代入得：AB = AE + (AC + AE) = AC + 2AE，解得：
           AE = ½(AB - AC)。
           同理，点 M 为劣弧 BC 中点，K 为 M 在 AC 上的垂足，由折弦定理对称性可推得：
           CK = ½(AB - AC) ⟹ AE = CK。

## 步骤 4：④ 斜边中线 ⟹ NK = NA 且 ∠NKC = ∠EAN

在直角三角形 Rt△AKM 中，∠AKM = 90°，点 N 为斜边 AM 的中点。
           由直角三角形斜边中线等于斜边一半的性质，可知：
           NK = NA = NM ⟹ △NAK 为等腰三角形，底角 ∠NKA = ∠NAK。
           由于 A, C, K 共线，故 ∠NKC = ∠NKA = ∠MAC。
           又因为 AM 是 ∠BAC 的内角平分线，故 ∠MAC = ∠BAM = ∠EAN。
           由此得出关键等角关系：
           ∠NKC = ∠EAN。

## 步骤 5：⑤ SAS 全等 △CKN ≅ △EAN ⟹ ∠NEA = ∠NCK

综合前面的几何结论，在 △CKN 与 △EAN 中：
           
           ① CK = AE（由步骤 ③ 证得）
           ② ∠CKN = ∠EAN（由步骤 ④ 证得）
           ③ NK = NA（由步骤 ④ 证得）
           
           由边角边（SAS）全等判定定理，可得：
           △CKN ≅ △EAN。
           因此对应角相等：
           ∠NEA = ∠NCK。
           全题得证！
