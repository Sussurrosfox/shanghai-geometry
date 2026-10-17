# 题目 04/4（例 3）证明分步规划

## 题目概述
设 $O, G$ 分别是 $\triangle ABC$ 的外心和重心，$G, O$ 关于三边 $BC, CA, AB$ 的对称点分别为 $G_1, G_2, G_3$ 和 $O_1, O_2, O_3$。
证明：七个三角形 $\triangle G_2 G_3 A$, $\triangle G_1 G_3 B$, $\triangle G_1 G_2 C$, $\triangle O_2 O_3 A$, $\triangle O_1 O_3 B$, $\triangle O_1 O_2 C$, $\triangle ABC$ 的外接圆共点。

---

## 分步规划表

| 步号 | 标题 | 核心数学逻辑 | 新增图元 | 擦除图元 | 色彩规划 |
|:---:|:---|:---|:---|:---|:---|
| **Step 0** | **已知条件与几何初始构型** | 给定 $\triangle ABC$ 及其外接圆 $\odot(ABC)$，标出外心 $O$、重心 $G$ 及欧拉线 $OH$；给出 $O, G$ 关于三边的轴对称点 $O_1,O_2,O_3$ 与 $G_1,G_2,G_3$。 | $\triangle ABC$ 边、外接圆 $\odot(ABC)$、外心 $O$、重心 $G$、对称点及对称连线虚线 | 无 | $\triangle ABC$ 骨架线（#1e293b），外接圆（#0284c7），对称虚线（#94a3b8） |
| **Step 1** | **边对称全等：$\triangle A O_2 G_2 \cong \triangle A O_3 G_3$** | 轴对称变换保持线段长度与内角。由关于边 $AC, AB$ 对称分别得 $\triangle A O_2 G_2 \cong \triangle AOG \cong \triangle A O_3 G_3$，从而 $A G_2 = A G_3$，$A O_2 = A O_3$，对应角 $\angle A G_2 O_2 = \angle A G_3 O_3$。 | 高亮 $\triangle A O_2 G_2, \triangle A O_3 G_3$ 及基准 $\triangle AOG$；标注对应角弧 $\angle A G_2 O_2, \angle A G_3 O_3$ | 步骤 0 的多余引线 | $\triangle A O_2 G_2$ 蓝色（#2563eb），$\triangle A O_3 G_3$ 紫色（#7c3aed），$\triangle AOG$ 橙色（#ea580c） |
| **Step 2** | **对角互补 ⇒ 圆 $A G_2 G_3$ 与圆 $A O_2 O_3$ 过交点 $X$** | 设反射直线 $O_2 G_2$ 与 $O_3 G_3$ 交于 $X$。由平角性质知 $\angle A G_3 X = 180^\circ - \angle A G_3 O_3 = 180^\circ - \angle A G_2 O_2 = 180^\circ - \angle A G_2 X$。对角互补得 $A, G_2, X, G_3$ 四点共圆；同理 $A, O_2, X, O_3$ 四点共圆。两圆均过交点 $X$。 | 直线 $X O_2, X O_3$；交点 $X$；角弧 $\angle A G_3 X, \angle A G_2 X$；动态绘制圆 $A G_2 G_3$ 与圆 $A O_2 O_3$ | 步骤 1 的全等三角形面填充 | 交点 $X$ 鲜红（#dc2626），圆 $A G_2 G_3$ 绿色（#059669），圆 $A O_2 O_3$ 紫色（#7c3aed） |
| **Step 3** | **垂心对称点落在外接圆与反射欧拉线上** | 垂心 $H$ 关于三边的对称点 $H_1, H_2, H_3$ 落在外接圆 $\odot(ABC)$ 上。因 $H$ 位于欧拉线 $OG$ 上，其对称点 $H_2$ 必在反射线 $X O_2$ 上，$H_3$ 必在反射线 $X O_3$ 上。 | 垂心 $H$、欧拉线 $OH$；对称点 $H_2, H_3$；标示其共线与共圆关系 | 步骤 2 的两辅助圆 | 欧拉线琥珀色（#d97706），垂心及对称点橙红高亮（#ea580c） |
| **Step 4** | **倒角推导：$\angle H_3 X H_2 = \angle H_3 B H_2 \implies X \in \odot(ABC)$** | 欧拉线交 $AB, AC$ 于 $D_3, D_2$。在 $\triangle X D_3 D_2$ 中内角计算：$\angle H_3 X H_2 = 180^\circ - 2\angle BAC$。而外接圆圆周角 $\angle H_3 B H_2 = 180^\circ - 2\angle BAC$。四点 $B, H_3, X, H_2$ 共圆，故 $X$ 落在外接圆 $\odot(ABC)$ 上！ | 点 $D_3, D_2$；高亮 $\triangle X D_3 D_2$；角弧 $\angle H_3 X H_2$ 与 $\angle H_3 B H_2$ | 步骤 3 的次要标记 | 顶角亮红（#dc2626），圆周角宝蓝（#2563eb） |
| **Step 5** | **轮换对称：三条反射欧拉线共点于 $X$** | 同理，$O_1 G_1$ 与 $O_3 G_3$ 交点 $X_2$、$O_1 G_1$ 与 $O_2 G_2$ 交点 $X_3$ 均重合于外接圆上的唯一点 $X$（Collings 定理）。三条反射线 $O_1 G_1, O_2 G_2, O_3 G_3$ 共点于 $X$。 | 绘制第三条反射线 $O_1 G_1$ 并延长至 $X$；标出 $H_1 \in \odot(ABC) \cap O_1 G_1$ | 步骤 4 的倒角弧与 $D_2, D_3$ | 三条反射欧拉线分别红、绿、青（#dc2626, #059669, #0891b2） |
| **Step 6** | **汇聚闭环：七个外接圆全部经过点 $X$** | 轮换对称性推出：圆 $B G_1 G_3$ 与圆 $B O_1 O_3$ 过 $X$，圆 $C G_1 G_2$ 与圆 $C O_1 O_2$ 过 $X$。结合前面已知圆 $A G_2 G_3, A O_2 O_3, \odot(ABC)$ 均过 $X$。七圆相交于点 $X$，全题得证！ | 同时绘制全部 7 个外接圆，线条纤细通透，在 $X$ 处汇交；脉冲光晕高亮交点 $X$ | 单独的辅助线与过程点 | 七圆采用 7 色谱系，高对比度防冲突，交点 $X$ 特效高亮 |
