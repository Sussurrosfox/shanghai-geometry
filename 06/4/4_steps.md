# 4 — 分步证明文字

## 步骤 0：✦ 已知条件与完全四边形构形

给定凸四边形 $ABCD$。对角线 $AC$ 与 $BD$ 相交于点 $O$；
对边 $AB$ 与 $CD$ 延长线交于 $P$，$AD$ 与 $BC$ 延长线交于 $Q$；
点 $O$ 在直线 $PQ$ 上的投影为 $R$ ($OR \perp PQ$)；
点 $R$ 在四边形四边上的投影分别为 $X, Y, Z, W$。
目标：证明 $X, Y, Z, W$ 四点共圆。

## 步骤 1：① 垂足共圆导出 ∠XWY = ∠XAR - ∠YQR

在四边形 $AWRX$ 中，$\angle AXR = \angle AWR = 90^\circ$，对角互补，故 $A, W, R, X$ 共圆于以 $AR$ 为直径的圆；
同弦圆周角相等：$\angle XWR = \angle XAR$；
在四边形 $QWRY$ 中，$\angle QWR = \angle QYR = 90^\circ$，故 $Q, W, Y, R$ 共圆于以 $QR$ 为直径的圆；
同弦圆周角相等：$\angle YWR = \angle YQR$；

$\angle XWY = \angle XWR - \angle YWR = \angle XAR - \angle YQR$

## 步骤 2：② 对侧同理导角 ∠XZY = ∠YCR - ∠XPR

同理，$\angle PXR = \angle PZR = 90^\circ \implies P, X, R, Z$ 四点共圆于以 $PR$ 为直径的圆；
$\angle CYR = \angle CZR = 90^\circ \implies C, Y, R, Z$ 四点共圆于以 $CR$ 为直径的圆；
同弦圆周角相等得：$\angle XZR = \angle XPR$，$\angle YZR = \angle YCR$；

$\angle XZY = \angle YZR - \angle XZR = \angle YCR - \angle XPR$

## 步骤 3：③ 四点共圆充要条件等价转化

$X, Y, Z, W$ 四点共圆 $\iff \angle XWY = \angle XZY$；
代入前两步角度差式子并移项整理：
$\angle XAR + \angle XPR = \angle YCR + \angle YQR$；
由 $\triangle PAR$ 与 $\triangle QCR$ 的内角与外角关系消去边角：

$\angle XWY = \angle XZY \iff \angle ARQ = \angle CRP$

## 步骤 4：④ 延长 CA 交 PQ 于 E，运用三组梅涅劳斯定理

延长对角线 $CA$ 交直线 $PQ$ 于点 $E$：
对 $\triangle DAC$ 与截线 $PQE$ 用梅涅劳斯定理：$\frac{QA}{DQ} \cdot \frac{PD}{CP} \cdot \frac{EC}{AE} = 1$；
对 $\triangle ACP$ 与截线 $BOD$ 用梅涅劳斯定理：$\frac{AO}{OC} \cdot \frac{CD}{DP} \cdot \frac{PB}{BA} = 1$；
对 $\triangle DAP$ 与截线 $QBC$ 用梅涅劳斯定理：$\frac{DQ}{QA} \cdot \frac{AB}{BP} \cdot \frac{PC}{CD} = 1$。

## 步骤 5：⑤ 三式相乘导出调和点列 (C, A; O, E) = -1

将三组梅涅劳斯定理三式两边分别相乘：
比值中 $\frac{QA}{DQ} \cdot \frac{DQ}{QA} = 1$、$\frac{PD}{CP} \cdot \frac{PC}{CD} \cdot \frac{CD}{DP} = 1$、$\frac{PB}{BA} \cdot \frac{AB}{BP} = 1$ 完全消去！
化简得到核心调和比值：

$\frac{AE}{EC} = \frac{AO}{OC} \iff (C, A; O, E) = -1$

即点列 $C, O, A, E$ 严格构成一条调和点列（$O, E$ 调和分割线段 $CA$）！

## 步骤 6：⑥ 调和线束与直角导出角平分线 ⇒ 命题得证

由点列 $C, O, A, E$ 为调和点列，连线束 $R(C, A; O, E)$ 为调和线束；
已知 $OR \perp PQ$，且 $E$ 落在 $PQ$ 上，故 $\angle ORE = 90^\circ$；
两共轭线互相垂直 $\implies$ $RO$ 平分 $\angle ARC$，即 $\angle ARO = \angle CRO$；
由 $\angle ORQ = \angle ORP = 90^\circ$ 对称相减立得：$\angle ARQ = \angle CRP$；
由步骤 3 逆推得 $\angle XWY = \angle XZY \implies$ **$X, Y, Z, W$ 四点共圆！** [Q.E.D.]
