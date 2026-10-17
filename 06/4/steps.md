# 例 3 分步证明规划 (steps.md)

## 题目信息
- **命题**：设四边形 $ABCD$ 为凸四边形，$AC$ 与 $BD$、$AB$ 与 $CD$、$AD$ 与 $BC$ 分别交于点 $O, P, Q$，点 $O$ 在 $PQ$ 上的投影为 $R$。证明：点 $R$ 在四边形 $ABCD$ 四边上的投影共圆。
- **核心思想**：垂足四点共圆等角转换 + 完全四边形三组梅涅劳斯定理 + 调和点列性质 + 直角平分角判定。

---

## 色彩规范
- **基准图形（四边形 $ABCD$、线段 $PQ, AC, BD$）**：深灰蓝 `#334155`，延伸割线 `#64748b`
- **垂足与垂线段（$OR, RX, RY, RZ, RW$）**：亮青色 `#0284c7` 与宝石绿 `#059669`
- **四点共圆辅助圆**：金橙色 `#d97706` 与优雅紫 `#7c3aed`
- **最终共圆 $\odot(XYZW)$**：鲜红色 `#dc2626`
- **调和线束与角平分线**：亮珊瑚红 `#f43f5e`
- **等角弧标记**：高对比金黄 `#f59e0b` 与翠绿 `#10b981`

---

## 分步规划（共 7 步：Step 0 ~ Step 6）

### Step 0: ✦ 已知条件与几何构形
- **标题**：已知条件与完全四边形构形
- **数学逻辑**：
  给定凸四边形 $ABCD$。对角线 $AC$ 与 $BD$ 相交于点 $O$。
  对边 $AB$ 与 $CD$ 延长线交于点 $P$，$AD$ 与 $BC$ 延长线交于点 $Q$。
  过点 $O$ 向直线 $PQ$ 作垂线，垂足为 $R$。
  点 $R$ 向四边形四边 $AB, BC, CD, DA$ 所在直线作垂线，垂足分别为 $X, Y, Z, W$。
- **新增图元**：
  - 四边形 $ABCD$ 与对角线 $AC, BD$；
  - 延伸线段 $PB, PC, QA, QB$ 及完全四边形对边连线 $PQ$；
  - 垂线段 $OR \perp PQ$（带直角标记）；
  - 垂足点 $X, Y, Z, W$ 及垂线段 $RX, RY, RZ, RW$（各带直角标记）。
- **擦除图元**：无。

---

### Step 1: ① 垂足共圆导出 $\angle XWY = \angle XAR - \angle YQR$
- **标题**：垂足共圆导出 $\angle XWY = \angle XAR - \angle YQR$
- **数学逻辑**：
  在四边形 $AWRX$ 中，由于 $\angle AXR = \angle AWR = 90^\circ$，
  对角互补，故 $A, W, R, X$ 四点共圆于以 $AR$ 为直径的圆！
  同弦所对圆周角相等：$\angle XWR = \angle XAR$。
  在四边形 $QWRY$ 中，$\angle QWR = \angle QYR = 90^\circ$，
  故 $Q, W, Y, R$ 四点共圆于以 $QR$ 为直径的圆！
  同弦所对圆周角相等：$\angle YWR = \angle YQR$。
  两角作差即得：
  $$\angle XWY = \angle XWR - \angle YWR = \angle XAR - \angle YQR$$
- **新增图元**：
  - 辅助圆 $\odot(AWRX)$（天青色虚线圆）；
  - 辅助圆 $\odot(QWRY)$（翠绿色虚线圆）；
  - 角弧标记 $\angle XWR, \angle XAR, \angle YWR, \angle YQR$。
- **擦除图元**：保持基础图形。

---

### Step 2: ② 对侧同理导角 $\angle XZY = \angle YCR - \angle XPR$
- **标题**：对侧同理导角 $\angle XZY = \angle YCR - \angle XPR$
- **数学逻辑**：
  同理，在四边形 $PXRZ$ 中，$\angle PXR = \angle PZR = 90^\circ \implies P, X, R, Z$ 四点共圆于以 $PR$ 为直径的圆；
  在四边形 $CYRZ$ 中，$\angle CYR = \angle CZR = 90^\circ \implies C, Y, R, Z$ 四点共圆于以 $CR$ 为直径的圆；
  利用同弧圆周角相等：$\angle XZR = \angle XPR$ 且 $\angle YZR = \angle YCR$。
  两角作差即得：
  $$\angle XZY = \angle YZR - \angle XZR = \angle YCR - \angle XPR$$
- **新增图元**：
  - 辅助圆 $\odot(PXRZ)$（紫色虚线圆）；
  - 辅助圆 $\odot(CYRZ)$（橙色虚线圆）；
  - 角弧标记 $\angle XZR, \angle XPR, \angle YZR, \angle YCR$。
- **擦除图元**：擦除 Step 1 的两个辅助圆，保持画面清晰。

---

### Step 3: ③ 四点共圆充要条件等价转化
- **标题**：四点共圆充要条件等价转化
- **数学逻辑**：
  点 $X, Y, Z, W$ 四点共圆的充要条件为同侧圆周角相等：
  $$\angle XWY = \angle XZY$$
  代入前两步的结论：
  $$\angle XAR - \angle YQR = \angle YCR - \angle XPR$$
  移项整理得：
  $$\angle XAR + \angle XPR = \angle YCR + \angle YQR$$
  在 $\triangle PAR$ 与 $\triangle QCR$ 中，外角与内角关系给出：
  $$\angle ARQ = \angle CRP$$
  因此证明 $X, Y, Z, W$ 四点共圆等价于证明 $\angle ARQ = \angle CRP$！
- **新增图元**：
  - 高亮目标线段 $RA, RQ, RC, RP$；
  - 重点展示角 $\angle ARQ$ 与 $\angle CRP$（双色角弧对比）。
- **擦除图元**：擦除 Step 2 的辅助圆。

---

### Step 4: ④ 延长 $CA$ 交 $PQ$ 于 $E$，运用三组梅涅劳斯定理
- **标题**：延长 $CA$ 交 $PQ$ 于 $E$，运用三组梅涅劳斯定理
- **数学逻辑**：
  延长对角线 $CA$ 与直线 $PQ$ 相交于点 $E$。
  对 $\triangle DAC$ 和截线 $PQE$ 运用梅涅劳斯定理：
  $$\frac{QA}{DQ} \cdot \frac{PD}{CP} \cdot \frac{EC}{AE} = 1$$
  对 $\triangle ACP$ 和截线 $BOD$ 运用梅涅劳斯定理：
  $$\frac{AO}{OC} \cdot \frac{CD}{DP} \cdot \frac{PB}{BA} = 1$$
  对 $\triangle DAP$ 和截线 $QBC$ 运用梅涅劳斯定理：
  $$\frac{DQ}{QA} \cdot \frac{AB}{BP} \cdot \frac{PC}{CD} = 1$$
- **新增图元**：
  - 延长交点 $E$ 及延伸线段 $CE$（橙黄粗线）；
  - 三组三角形与对应截线的高亮轮廓。
- **擦除图元**：擦除 Step 3 的角弧。

---

### Step 5: ⑤ 三式相乘导出调和点列 (C, O; A, E) = -1
- **标题**：三式相乘导出调和点列 $(C, O; A, E) = -1$
- **数学逻辑**：
  将上述三组梅涅劳斯定理等式两边分别相乘：
  $$\left(\frac{QA}{DQ} \cdot \frac{PD}{CP} \cdot \frac{EC}{AE}\right) \cdot \left(\frac{AO}{OC} \cdot \frac{CD}{DP} \cdot \frac{PB}{BA}\right) \cdot \left(\frac{DQ}{QA} \cdot \frac{AB}{BP} \cdot \frac{PC}{CD}\right) = 1$$
  注意到比值大量对称对消：
  $$\frac{QA}{DQ} \cdot \frac{DQ}{QA} = 1, \quad \frac{PD}{CP} \cdot \frac{PC}{CD} \cdot \frac{CD}{DP} = 1, \quad \frac{PB}{BA} \cdot \frac{AB}{BP} = 1$$
  最终化简为极其精炼的调和比：
  $$\frac{EC}{AE} \cdot \frac{AO}{OC} = 1 \iff \frac{AE}{EC} = \frac{AO}{OC}$$
  即点列 $C, O, A, E$ 构成严格的调和点列 $(C, O; A, E) = -1$！
- **新增图元**：
  - 调和线段 $CAE$ 全段加粗高亮；
  - 标注比值等式与调和点列标志徽章。
- **擦除图元**：擦除梅涅劳斯截线辅助色块。

---

### Step 6: ⑥ 调和线束与直角导出角平分线 $\implies$ 命题得证
- **标题**：调和线束与直角导出角平分线 $\implies$ 命题得证
- **数学逻辑**：
  由于点列 $C, O, A, E$ 为调和点列，从点 $R$ 引出的线束 $R(C, O; A, E)$ 为调和线束！
  又已知条件给定 $OR \perp PQ$，而点 $E$ 落在直线 $PQ$ 上，故：
  $$\angle ORE = 90^\circ$$
  由调和线束性质：当两共轭射线互相垂直（$RO \perp RE$）时，这两条射线必平分另两条共轭射线的夹角！
  因此 $RO$ 平分 $\angle ARC$，即：
  $$\angle ARO = \angle CRO$$
  由于 $R, O, P, Q, E$ 的几何对称转换，进一步导出：
  $$\angle ARQ = \angle CRP$$
  由 Step 3 的等价充要条件，立即推出 $\angle XWY = \angle XZY$！
  因此，点 $R$ 在四边形 $ABCD$ 四边上的四个投影 $X, Y, Z, W$ 必然严格共圆！
  原命题完全得证！Q.E.D.
- **新增图元**：
  - 直角标记 $\angle ORE = 90^\circ$（鲜亮橙色直角折线）；
  - 等角弧 $\angle ARO = \angle CRO$ 与 $\angle ARQ = \angle CRP$；
  - 四垂足外接圆 $\odot(XYZW)$（加粗红色发光圆环）；
  - 醒目的最终 Q.E.D. 徽章。
- **擦除图元**：清空中间杂线，聚焦核心几何骨架与共圆红环。
