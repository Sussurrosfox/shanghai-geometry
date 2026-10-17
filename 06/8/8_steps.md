# 8 — 分步证明文字

## 步骤 0：已知条件与几何构形

给定 △ABC 及其内心 I。
      • D 是边 BC 上一点，E 是 BC 延长线上一点，且满足比例：
      BD / DC = BE / EC = λ
      即点对 (D, E) 调和共轭于线段 BC 的两端点。
      • 点 H 在线段 IE 上，且满足 DH ⊥ IE。
      • 求证目标：两角相等 ∠AHE = ∠IDE。
      💡 难点洞察：点 A, H, E 与 I, D, E 位于不同线段且缺乏直接桥梁，需通过阿波罗尼斯圆与外接圆构造辅助点。

## 步骤 1：构造阿氏圆 ω 与外接圆交点 P

以线段 DE 为直径作圆 ω。
      • 记 BD / DC = BE / EC = λ，根据阿波罗尼斯圆性质，圆 ω 正是平面上满足 PB / PC = λ 的所有点 P 的轨迹。
      • 因 DH ⊥ IE（即 ∠DHE = 90°），以直径为弦可知垂足 H 亦落在圆 ω 上。
      • 设 △ABC 的外接圆与圆 ω 交于点 P，则：
      PB / PC = λ = DB / DC
      由角平分线定理逆定理，PD 必为 ∠BPC 的内角平分线！

## 步骤 2：引出弧中点 M 与相似 △MCN ∼ △MAC

设 M 是外接圆上不含 A 的弧 BC 的中点。
      • 因 PD 平分 ∠BPC，延长 PD 必经过外接圆该弧的中点，故 P, D, M 三点共线。
      • 射线 AM 必平分 ∠BAC，因而内心 I 落在 AM 上，设 AM 交 BC 于点 N，即 A, I, N, M 四点共线。
      • 由圆周角定理：∠MCB = ∠A/2 = ∠MAC。
      • 在 △MCN 与 △MAC 中，有公共角 ∠CMA，故：
      △MCN ∼ △MAC ⟹ MN · MA = MC²

## 步骤 3：相似 △MCD ∼ △MPC 与鸡爪定理

考察圆周角与相似关系：
      • 同弧所对圆周角 ∠MPC = ∠MAC = ∠MCB = ∠MCD。
      • 在 △MCD 与 △MPC 中，具有公共角 ∠CMP 与对应角相等，故：
      △MCD ∼ △MPC ⟹ MD · MP = MC²
      • 由著名的内心鸡爪定理（圆心-弧中点-内心性质），弧中点 M 到内心及端点等距：
      MC = MI = MB ⟹ MC² = MI²
      • 综合上述结果，建立核心等积链：
      MN · MA = MD · MP = MI²

## 步骤 4：四点共圆 A, N, D, P 与 △MDI ∼ △MIP

利用步骤 3 的等积链继续推导：
      • 由 MN · MA = MD · MP，根据割线定理逆定理，立即得出 A, N, D, P 四点共圆！
      • 圆内接四边形外角等于内对角：∠PDE = ∠PAN。
      • 另一方面，由 MI² = MD · MP 可得：
      MD / MI = MI / MP
      且夹角 ∠DMI = ∠IMP 是公共角，故：
      △MDI ∼ △MIP ⟹ ∠MID = ∠MPI

## 步骤 5：阿氏圆圆周角传递，导出 A, I, H, P 四点共圆

将视线聚焦到阿波罗尼斯圆 ω 上：
      • 点 P, D, H, E 均在以 DE 为直径的阿氏圆 ω 上。
      • 弦 PE 所对圆周角相等：∠PHE = ∠PDE。
      • 结合步骤 4 的结论 ∠PDE = ∠PAN，由于 A, I, N 共线，故 ∠PAN = ∠PAI，得到：
      ∠PHE = ∠PAI
      • 又因 E, H, I 三点共线，∠PHE = ∠PHI，从而：
      ∠PHI = ∠PAI
      • 这表明点 A, H 对线段 PI 的张角相等，故 A, I, H, P 四点共圆！

## 步骤 6：倒角代换得出结论: ∠AHE = ∠IDE

由四点共圆完成最后的角度闭环：
      • 在共圆 A, I, H, P 中，同弧圆周角相等：∠AHI = ∠API。
      • 拆分角：∠API = ∠APD - ∠IPD。
      • 由共圆 A, N, D, P 知 ∠APD = ∠AND；由相似知 ∠IPD = ∠MID。
      • 在 △IND 中，由三角形外角性质：∠AND = ∠BDI + ∠MID，因此：
      ∠API = ∠AND - ∠MID = ∠BDI
      • 故 ∠AHI = ∠BDI。两边取补角：
      180° - ∠AHI = 180° - ∠BDI ⟹ ∠AHE = ∠IDE
      原命题完全得证！∎
