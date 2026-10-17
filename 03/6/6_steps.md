# 6 — 分步证明文字

## 步骤 0：0️⃣ 构型与四条角平分线

给定凸四边形 ABCD 及其平面内任意点 P。
    连结 PA, PB, PC, PD，分别作 ∠APB, ∠BPC, ∠CPD, ∠DPA 的角平分线，交各边于分点 K, L, M, N。
    由三角形角平分线分对边成比例定理，各边分比恒等于点 P 到相邻两顶点的距离之比：
    
      AKKB = PAPB,   
      BLLC = PBPC,   
      CMMD = PCPD,   
      DNNA = PDPA
    
    内接四边形 KLMN 何时能成为平行四边形？这取决于点 P 的空间位置约束。

## 步骤 1：1️⃣ 充分性构造：取中垂线交点 P

(1) 寻找满足条件的特殊点 P：
    作四边形对角线 AC 与 BD 的垂直平分线（紫色虚线），设它们的交点为 P。
    由垂直平分线的性质，点 P 到对角线两端点的距离严格相等：
    
      PA = PC   且   PB = PD
    
    代入 Step 0 的角平分线比例式中：
    
      AKKB = PAPB = PCPB = CLLB
    
    对应边分线段之比完全一致！

## 步骤 2：2️⃣ 充分性验证：KLMN 必为平行四边形

在 △ABC 中，由 AKKB = CLLB ⟺ BKKA = BLLC，根据平行线分线段成比例定理之逆定理：
    
      KL ∥ AC
    
    同理在 △ADC 中，由 MDCM = PDPC = PBPA = NDAN，得 MN ∥ AC。
    因此两组边均平行于对角线 AC：
    
      KL ∥ MN
    
    完全同理可推得 LM ∥ BD ∥ NK。
    两组对边分别平行，故 KLMN 必为平行四边形！充分性获证。

## 步骤 3：3️⃣ 必要性反证：梅氏定理导出平行

(2) 探求点 P 的全部轨迹（必要性证明）：
    反之，设 KLMN 是平行四边形。将四个角平分线比例式依次连乘，各项首尾相消：
    
      AKKB · BLLC · CMMD · DNNA = PAPB · PBPC · PCPD · PDPA = 1   ①
    
    用反证法证明 KN ∥ BD：
    假设 KN 与 BD 不平行，延长必交于点 Q。对 △ABD 及截线 KNQ，应用梅涅劳斯定理：
    
      DNNA · AKKB · BQQD = 1
    
    结合 ① 式相比消去对应项，立得：BLLC · CMMD · DQQB = 1。

## 步骤 4：4️⃣ 导出 PA=PC 且 PB=PD

在 △BCD 中应用梅涅劳斯定理的逆定理：
    点 Q, M, L 必须三点共线！
    这意味着直线 KN 与直线 LM 将在点 Q 处相交。
    但这与已知条件“KLMN 是平行四边形”（KN ∥ LM，永不相交）产生致命矛盾！
    故反证假设不成立，必有：
    
      KN ∥ BD ∥ LM   且   KL ∥ AC ∥ MN
    
    由 KN ∥ BD 得 PAPB = AKKB = ANND = PAPD ⟹ PB = PD！
    同理由 KL ∥ AC 得 PA = PC！

## 步骤 5：5️⃣ 最终结论：点 P 的唯一轨迹

综上所述，充要条件完全闭环：
    1. 充分性：若 P 为 AC 与 BD 的垂直平分线交点，则 PA=PC, PB=PD，直接导出 KLMN 为平行四边形；
    2. 必要性：若 KLMN 为平行四边形，则必有 PA=PC 且 PB=PD，故点 P 必须同时落在对角线 AC 和 BD 的垂直平分线上。
    对于任意一般凸四边形，两对角线 AC 与 BD 既不重合也不平行，其垂直平分线相交于唯一确定的交点。
    
      核心结论：满足条件的点 P 的轨迹是 AC 与 BD 的垂直平分线的交点（唯一的一个点）。
