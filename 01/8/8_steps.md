# 8 — 分步证明文字

## 步骤 0：已知条件与几何构形

在 $\bigtriangleup ABC$ 中，已知：
    • $L$ 是底边 $BC$ 的中点，即 $BL = CL$；
    • $E, F$ 分别是 $L$ 在边 $AC, AB$ 上的垂足射影（$LE \bot AC, LF \bot AB$）；
    • 圆 $ABE$ 与圆 $ACF$ 交于顶点 $A$ 与另一点 $P$。
    求证目标：公共弦割线 $AP \bot BC$

## 步骤 1：① 作直径 $AM, AN$，将垂直转化为平行

分别作圆 $ABE$ 的直径 $AM$ 与圆 $ACF$ 的直径 $AN$：
    • 由直径所对圆周角为直角：$\angle APM = 90^\circ$ 且 $\angle APN = 90^\circ$；
    • 两角之和 $\angle APM + \angle APN = 180^\circ$，故 $P, M, N$ 三点共线，且 $AP \bot MN$；
    目标转化：要证 $AP \bot BC$，只需证明 $MN \parallel BC$

## 步骤 2：② 利用直径与射影垂直，发现三点共线

分析点 $M, N$ 的几何位置：
    • 在圆 $ABE$ 中，直径所对圆周角 $\angle AEM = 90^\circ$；又已知 $LE \bot AC$（$\angle AEL = 90^\circ$）；
    • 过点 $E$ 垂直于 $AC$ 的直线唯一，因此 $E, L, M$ 三点共线（$M$ 落在直线 $LE$ 延长线上）；
    • 同理，$\angle AFN = \angle AFL = 90^\circ$，因此 $F, L, N$ 三点共线（$N$ 落在直线 $LF$ 延长线上）。

## 步骤 3：③ 连结 $BM, CN$，完成角度导引

连结辅助线段 $BM$ 与 $CN$：
    • 因 $AM$ 为直径，$\angle ABM = 90^\circ$，故 $\angle LBM = 90^\circ - \angle B$；
    • 在直角 $\triangle BFL$ 中，$\angle FLB = 90^\circ - \angle B$；由对顶角知 $\angle CLN = \angle FLB$；
    第一组等角：$\angle LBM = \angle CLN = 90^\circ - \angle B$
    • 同理，在圆 $ACF$ 中，$\angle ACN = 90^\circ$，由余角与对顶角变换：
    第二组等角：$\angle BLM = \angle LCN = 90^\circ - \angle C$

## 步骤 4：④ 判定 $\triangle BLM \cong \triangle CLN$，对应高相等

观察由中点 $L$ 对称展开的两个三角形 $\triangle BLM$ 与 $\triangle CLN$：
    • $\angle BLM = \angle LCN$（Step 3 已证）；
    • $BL = CL$（$L$ 是 $BC$ 中点）；
    • $\angle LBM = \angle CLN$（Step 3 已证）；
    由角边角（ASA）公理，知 $\triangle BLM \cong \triangle CLN$！
    全等三角形对应高相等：$h_M = h_N$（点 $M, N$ 到底边 $BC$ 距离相等）

## 步骤 5：⑤ 推得 $MN \parallel BC$，得出最终结论

• 由于点 $M, N$ 到直线 $BC$ 的距离相等且位于 $BC$ 同侧，因此：
    $MN \parallel BC$
    • 结合 Step 1 中已证的垂直关系 $AP \bot MN$：
    • 一条直线垂直于两条平行线之一，必垂直于另一条：
    $MN \parallel BC \quad \text{且} \quad AP \bot MN \implies AP \bot BC$
    至此，原命题全部证毕！
