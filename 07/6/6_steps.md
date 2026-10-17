# 6 — 分步证明文字

## 步骤 0：已知条件与几何命题

在锐角 $\triangle ABC$ 中，点 $X, Y$ 是内部的两个互异动点，满足：
           1. $B, C, X, Y$ 四点共圆（记此圆为 $\omega_2$）；
           2. $\angle AXB - \angle ACB = \angle AYC - \angle ABC$。
           求证：无论动点 $X, Y$ 如何运动，直线 $XY$ 必恒经过一个只与 $\triangle ABC$ 相关的定点。

## 步骤 1：① 构造定点 D 与外接圆 ω₁

设 $\triangle ABC$ 的外接圆为 $\omega_1$。过顶点 $A$ 作 $\omega_1$ 的切线，与边 $BC$ 的延长线交于点 $D$。
           定点确定：由于锐角 $\triangle ABC$ 是固定的，外接圆 $\omega_1$、切线 $AD$ 以及与直线 $BC$ 的交点 $D$ 均唯一确定，与动点 $X, Y$ 无关。
           由切割线定理，切线长满足：$DA^2 = DB \cdot DC$。

## 步骤 2：② 周角拆解转化角差条件

围绕内部动点 $X$，利用平面周角 $360^\circ$ 与三角形内角和性质：
           $\angle AXB = 360^\circ - \angle AXC - \angle CXB$
           $\angle ACB = \angle ACX + \angle BCX$
           在 $\triangle ACX$ 与 $\triangle BCX$ 中利用内角和 $180^\circ$ 相消得：
           $\angle AXB - \angle ACB = \angle CAX + \angle CBX$。
           同理可得：$\angle AYC - \angle ABC = \angle BAY + \angle BCY$。
           代入已知角差相等条件，即得关键对称等式：
           $\angle CAX + \angle CBX = \angle BAY + \angle BCY$。

## 步骤 3：③ 弦切角与圆内接四边形导角

由 $AD$ 切 $\omega_1$ 于 $A$，弦切角 $\angle CAD = \angle ABC$，故外角 $\angle BAD = \angle ABC + \angle BAC$。
           计算角 $\angle YAD$：
           $\angle YAD = \angle BAD - \angle BAY = \angle ABC + \angle BAC - (\angle CAX + \angle CBX - \angle BCY)$
           $= (\angle ABC - \angle CBX) + (\angle BAC - \angle CAX) + \angle BCY = \angle ABX + \angle BAX + \angle BCY$。
           因 $B,C,X,Y$ 共圆，圆内接四边形对角互补：$\angle BCY = 180^\circ - \angle BXY$。
           代入 $\triangle ABX$ 内角和：$\angle YAD = (180^\circ - \angle AXB) + (180^\circ - \angle BXY) = \mathbf{\angle AXY}$！

## 步骤 4：④ 判定 AD 是 ω(AXY) 的切线

在 $\triangle AXY$ 中，射线 $AD$ 与弦 $AY$ 所夹的角满足：
           $\angle YAD = \angle AXY$。
           由弦切角定理的逆定理：直线 $AD$ 必为 $\triangle AXY$ 外接圆 $\omega$ 在点 $A$ 处的切线！
           因此，圆 $\omega$ 与圆 $\omega_1$ 在点 $A$ 处内切，直线 $AD$ 为圆 $\omega$ 与圆 $\omega_1$ 的公共切线（即两圆的根轴）。

## 步骤 5：⑤ 应用三圆根心定理得出结论

考察三个圆及其两两之间的根轴：
           1. $\omega$ 与 $\omega_1$ 在 $A$ 处内切 $\implies$ 公共切线 $AD$ 为其根轴；
           2. $\omega_1$ 与 $\omega_2$ 相交于 $B, C$ $\implies$ 直线 $BC$ 为其根轴；
           3. $\omega$ 与 $\omega_2$ 相交于 $X, Y$ $\implies$ 直线 $XY$ 为其根轴。
           由根心定理（三圆根轴定理）：三圆的两两根轴若不平行，必汇交于同一点（根心）。
           已知根轴 $AD$ 与根轴 $BC$ 显然相交于定点 $D$，故第三条根轴 直线 $XY$ 必经过定点 $D$！命题得证。
