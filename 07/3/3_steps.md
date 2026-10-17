# 3 — 分步证明文字

## 步骤 0：已知条件与几何构型

锐角 $\triangle ABC$ 中，$AB > AC$，$H$ 为垂心，高线 $AD \perp BC$ 于点 $D$。
点 $E, F$ 分别在射线 $AB, AC$ 上且线段 $EF$ 经过点 $D$；
$B, E, C, F$ 四点共圆，圆心记为 $U$；$M$ 为边 $BC$ 的中点。
求证：四边形 $MUDH$ 为平行四边形。

## 步骤 1：① 延长高线 $AD$ 与外接圆交于点 $K$

作 $\triangle ABC$ 的外接圆 $\odot O$。延长高线 $AD$ 与外接圆相交于点 $K$。
由外接圆垂心反射性质，垂心 $H$ 关于边 $BC$ 的对称点必落在外接圆上。
因为对称轴 $BC \perp HK$，所以垂足 $D$ 恰为线段 $HK$ 的中点，即：
$DH = DK = \frac{1}{2}HK$。

## 步骤 2：② 圆幂定理与密克点性质（$AK$ 为直径）

在圆 $\odot O$ 中，由相交弦定理得：$AD \cdot DK = BD \cdot DC$。
在圆 $\odot U$ 中，割线 $EF$ 与 $BC$ 交于点 $D$，得：$ED \cdot DF = BD \cdot DC$。
两式联立导出：$AD \cdot DK = ED \cdot DF$，故 $A, E, K, F$ 四点共圆（圆心记为 $V$）。
点 $K$ 实为完全四边形 $AEBDCF$ 的密克点，由共圆知 $\angle AEK = \angle AFK = 90^\circ$。
因此，$AK$ 为圆 $AEKF$ 的直径，圆心 $V$ 即为线段 $AK$ 的中点。

## 步骤 3：③ 连心线与反平行线导出 $UV \parallel AO$

1. 圆 $\odot U$ 与圆 $\odot V$ 相交于 $E, F$ 两点，公共弦为 $EF$。
两圆连心线垂直平分公共弦，故 $UV \perp EF$。
2. 导角易证：在 $\odot O$ 中 $\angle OAC = 90^\circ - B$；在圆内接四边形 $BECF$ 中外角 $\angle AFE = \angle B$。
在 $\triangle APF$ 中导出 $AO \perp EF$。
3. 两线均垂直于直线 $EF$，故 $UV \parallel AO$。

## 步骤 4：④ 构造平行四边形 $OAVU \implies OU = AV$

因为 $O$ 为外心、$M$ 为 $BC$ 中点，所以中垂线 $OM \perp BC$；
点 $U$ 亦在 $BC$ 中垂线上，故直线 $OU \perp BC$。
而高线 $ADK \perp BC$，即直线 $AV \perp BC$。
因此，$OU \parallel AV$。
结合前一步已证的 $UV \parallel AO$，四边形 $OAVU$ 两组对边分别平行，
因此 四边形 $OAVU$ 为平行四边形，从而对边相等：$OU = AV$。

## 步骤 5：⑤ 线段等长 $MU = DH \implies MUDH$ 为平行四边形

由经典欧拉线性质知 $OM = \frac{1}{2}AH$，且 $V$ 为 $AK$ 中点知 $AV = \frac{1}{2}AK$。
将 $OU = AV$ 代入线段代数式：
$MU = OU - OM = AV - \frac{1}{2}AH = \frac{1}{2}AK - \frac{1}{2}AH = \frac{1}{2}HK = DH$！
因为直线 $MU \perp BC$ 且直线 $DH \perp BC$，故 $MU \parallel DH$；
一组对边平行且相等（对角线 $MD$ 与 $HU$ 互相平分于中点），
因此，四边形 $MUDH$（顶点顺序 $M-H-D-U$）为平行四边形！命题得证。
