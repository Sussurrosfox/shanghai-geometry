# 9 — 分步证明文字

## 步骤 0：已知条件与几何构型

在锐角 $\triangle APD$ 的边 $AP$ 和 $PD$ 上各取一点 $B, C$，四边形 $ABCD$ 对角线相交于 $Q$。
           $\triangle APD$ 和 $\triangle BPC$ 的垂心分别为 H₁ 和 H₂。
           已知前提 直线 $H_1H_2$ 经过 $\triangle ABQ$ 与 $\triangle CDQ$ 外接圆的交点 X。
           求证目标 直线 $H_1H_2$ 必经过 $\triangle BQC$ 与 $\triangle AQD$ 外接圆的交点 Y。

## 步骤 1：① 构造直径圆与高线垂足

记 $AC, BD$ 的中点分别为 M, N，以 $AC, BD$ 为直径分别作圆 ω₁, ω₂。
           作高线：$AA_1 \perp PD$ 于 $A_1$，$BB_1 \perp PD$ 于 $B_1$，$CC_1 \perp PA$ 于 $C_1$，$DD_1 \perp PA$ 于 $D_1$。
           由于 $\angle AA_1C = \angle AC_1C = 90^\circ$，故垂足 $A_1, C_1$ 在圆 $\omega_1$ 上；
           同理 $\angle BB_1D = \angle BD_1D = 90^\circ$，故垂足 $B_1, D_1$ 在圆 $\omega_2$ 上。

## 步骤 2：② 垂心圆幂相等 ⇒ H₁H₂ 为根轴

在 $\triangle APD$ 中，$H_1$ 是垂心，$AA_1, DD_1$ 为高，故四点 $A, D, A_1, D_1$ 共圆（以 $AD$ 为直径）。
           由圆幂定理（割线定理）：
           $$H_1A \cdot H_1A_1 = H_1D \cdot H_1D_1$$
           这表明 $H_1$ 对圆 $\omega_1$ 与 $\omega_2$ 的圆幂相等，即点 $H_1$ 在两圆的根轴上。
           同理在 $\triangle BPC$ 中，垂心 $H_2$ 满足 $H_2B \cdot H_2B_1 = H_2C \cdot H_2C_1$，故 $H_2$ 亦在根轴上。
           因此，直线 H₁H₂ 恰好是圆 ω₁ 与圆 ω₂ 的根轴（Radical Axis）！

## 步骤 3：③ 点 X 位于根轴上 ⇒ 圆幂等式

作 $\triangle ABQ$ 和 $\triangle CDQ$ 的外接圆，两圆相交于 $Q$ 与第二交点 X。
           已知条件给定直线 $H_1H_2$ 经过交点 $X$。
           由于 $H_1H_2$ 是圆 $\omega_1$ 与 $\omega_2$ 的根轴，故点 $X$ 对两圆的圆幂严格相等：
           $$\mathrm{Pow}(X, \omega_1) = \mathrm{Pow}(X, \omega_2)$$
           展开即得几何圆幂等式：
           $XM^2 - CM^2 = XN^2 - DN^2$（其中 $CM = \frac{AC}{2}, DN = \frac{BD}{2}$）。

## 步骤 4：④ 螺旋相似 △XAC ~ △XBD ⇒ AC = BD

由外接圆圆周角性质易知：$\angle XBD = \angle XAC$ 且 $\angle XDB = \angle XCA$，故 $\triangle XAC \sim \triangle XBD$。
           $XM, XN$ 分别为对应中线，设相似比为 $k = \frac{AC}{BD} = \frac{CM}{DN} = \frac{XM}{XN}$。
           若圆幂 $XM^2 - CM^2 = 0$，则 $\angle BXD = 90^\circ$，导得 $P, B, X, D$ 四点共圆，从而 $\angle P = 180^\circ - \angle BXD = 90^\circ$，与 $\triangle APD$ 是锐角三角形矛盾！
           因此圆幂非零，由 $XM^2 - CM^2 = k^2(XN^2 - DN^2)$ 代入圆幂等式得：
           $k^2 = 1 \implies k = 1 \implies AC = BD$（对角线严格等长！）。

## 步骤 5：⑤ 对偶相似 △YAC ≅ △YBD ⇒ Y 圆幂相等

同理，作 $\triangle BQC$ 和 $\triangle AQD$ 的外接圆，两圆相交于 $Q$ 与第二交点 Y。
           由完全对称的圆周角关系，同样有 $\triangle YAC \sim \triangle YBD$。
           因为上一步已严格证明相似比 $k = \frac{AC}{BD} = 1$，故 $\triangle YAC \cong \triangle YBD$（全等）！
           对应中线必等长：$YM = YN$，且半弦 $CM = DN$。
           故代入圆幂计算必有：
           $YM^2 - CM^2 = YN^2 - DN^2 \implies \mathrm{Pow}(Y, \omega_1) = \mathrm{Pow}(Y, \omega_2)$。

## 步骤 6：⑥ 最终结论：直线 H₁H₂ 必经过点 Y

点 $Y$ 对圆 $\omega_1$ 与圆 $\omega_2$ 的圆幂完全相等，意味着 点 $Y$ 位于圆 $\omega_1$ 与 $\omega_2$ 的根轴上。
           而步骤 ② 已经证得圆 $\omega_1$ 与 $\omega_2$ 的根轴就是直线 $H_1H_2$！
           因此，点 Y 必定在直线 H₁H₂ 上！
           四点 $X, H_1, Y, H_2$ 严格共线于根轴之上，原命题全部得证！
