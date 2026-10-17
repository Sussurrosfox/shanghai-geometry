# 2 — 分步证明文字

## 步骤 0：圆内接六边形 ABCDEF 构型

已知六边形 ABCDEF 内接于圆 ⊙O。

           帕斯卡定理（Pascal's Theorem）是射影几何与欧几里得几何中最著名的经典定理之一：

           圆内接六边形的三对对边所在直线的交点必在同一直线上。

           我们首先建立六边形的基础构型，观察六个顶点在圆周上的几何分布。

## 步骤 1：对边延长相交得交点 P, Q, R

分别延长六边形的三对对边，得到三对交点：

           • 直线 AB 与 DE 交于点 P；

           • 直线 CD 与 FA 交于点 R；

           • 直线 BC 与 EF 交于点 Q。

           本证明的核心目标：证明这三个交点 P, Q, R 三点共线。

## 步骤 2：聚焦 △ADR 与圆周角等量代换

将视点转换至由边交织而成的关键三角形 △ADR，利用同弧圆周角相等与平角补角性质建立角量对应：

           • 弦 DB 所对圆周角：∠DCB = ∠DAB

           • 弦 BF 所对圆周角：∠BCF = ∠BAF

           • 点 R 处平角补角关系（互补角正弦值相等）：

           &nbsp;&nbsp;∠FRP = 180° − ∠ARP ⟹ sin∠FRP = sin∠ARP

           &nbsp;&nbsp;∠PRC = 180° − ∠PRD ⟹ sin∠PRC = sin∠PRD

           • 弦 CE 所对圆周角：∠CFE = ∠RDE

           • 弦 EA 所对圆周角：∠EFR = ∠EDA

## 步骤 3：角元塞瓦定理应用于 △ADR 与点 P

在 △ADR 中，从三个顶点引向点 P 的三条射线：

           • 射线 PA 即直线 AB；

           • 射线 PD 即直线 DE；

           • 射线 PR 连结顶点 R 与点 P。

           因直线 PA, PD, PR 显然共点于 P，由第一角元形式的塞瓦定理（Trigonometric Ceva's Theorem）：
           
             sin ∠DABsin ∠BAF · 
             sin ∠ARPsin ∠PRD · 
             sin ∠RDEsin ∠EDA = 1

## 步骤 4：正弦等比代换转移至 △RCF

利用 Step 2 中的同弧圆周角相等与补角正弦不变性进行等比代换：
           
             sin ∠DCBsin ∠BCF = sin ∠DABsin ∠BAF ，
             sin ∠FRPsin ∠PRC = sin ∠ARPsin ∠PRD ，
             sin ∠CFEsin ∠EFR = sin ∠RDEsin ∠EDA
           
           代入 Step 3 的等式，立即导出对 △RCF 的正弦比乘积关系：
           
             sin ∠DCBsin ∠BCF · 
             sin ∠FRPsin ∠PRC · 
             sin ∠CFEsin ∠EFR = 1

## 步骤 5：角元塞瓦逆定理导出三点共线

在 △RCF 中，三条射线 CB, FE, RP 分割顶角的正弦比乘积恒等于 1。

           根据第一角元形式的塞瓦定理逆定理：

           三条直线 BC, FE, RP 必共点！

           又由已知条件，直线 BC 与 FE 本就交于点 Q，因此直线 RP 必须通过点 Q，即：

           点 Q 落在直线 RP 上。

           
             ∴ P, Q, R 三点共线！（帕斯卡线）
           
           证毕。

