# 例 5：两圆相交、对称与四点共圆（分步证明规划）

## 题目回顾
以 $AB$ 为直径的圆 $\omega_1$ 和以 $A$ 为圆心的圆 $\omega_2$ 相交于 $C, D$ 两点，点 $E$ 在圆 $\omega_2$ 上（$E$ 在 $\omega_1$ 外且和点 $C$ 在直线 $AB$ 同侧）。$BE$ 与 $\omega_2$ 交于另一点 $F$。点 $K$ 在 $\omega_1$ 上且满足 $2CK \cdot AC = CE \cdot AB$（点 $K$ 与点 $A$ 在过点 $C$ 的圆 $\omega_1$ 的直径的同一侧），$KF$ 与 $\omega_1$ 交于另一点 $L$。$D$ 关于 $BE$ 的对称点为 $D'$。  
**求证**：$L, F, C, D'$ 四点共圆。

---

## 分步演示规划

### 步骤 0：已知条件与初始构型
- **标题**：已知条件与初始构型
- **数学逻辑**：展示题目给定的几何系统：圆 $\omega_1$（以 $AB$ 为直径）、圆 $\omega_2$（以 $A$ 为圆心，半径 $AC=AD$）、割线 $BEF$、条件点 $K$、割线 $KFL$ 以及关于 $BE$ 对称点 $D'$。
- **画面图元**：
  - 底层基准图元：圆 $\omega_1$、圆 $\omega_2$、直径线段 $AB$、公共弦 $CD$、割线 $BE$、弦 $KF$。
  - 点集：$A, B, C, D, E, F, K, L, D'$，均带白底防遮挡标签。
- **色彩**：基准线条采用柔和灰蓝 `#64748b`、`#94a3b8`。

---

### 步骤 1：相似三角形 $\triangle OCK \sim \triangle ACE$ 与张角相等
- **标题**：① 相似三角形 $\triangle OCK \sim \triangle ACE \implies \angle CLF = \angle CFE$
- **数学逻辑**：
  由题设 $2CK \cdot AC = CE \cdot AB$，代入 $AB = 2 CO = 2 KO$ 及 $AC = AE$，得：
  $$\frac{CK}{CE} = \frac{CO}{AC} = \frac{KO}{AE}$$
  三边成比例推出等腰三角形相似：$\triangle OCK \sim \triangle ACE$。
  因此顶角相等：$\angle COK = \angle CAE$。  
  在 $\omega_1$ 中，圆周角 $\angle CLF = \frac{1}{2}\angle COK$；在 $\omega_2$ 中，圆周角 $\angle CFE = \frac{1}{2}\angle CAE$。  
  由此得出核心角等式：
  $$\angle CLF = \angle CFE$$
- **画面图元**：
  - 新增图元：线段 $OC, OK$、线段 $AC, AE$、线段 $CL, CF$；
  - 动态填充：$\triangle OCK$（淡蓝 `#3b82f61a`）、$\triangle ACE$（淡紫 `#8b5cf61a`）；
  - 角弧标记：$\angle COK$ 与 $\angle CAE$（双弧高亮），圆周角 $\angle CLF$ 与 $\angle CFE$（单弧绿色高亮）。

---

### 步骤 2：切线与割线比值 $\frac{CE}{CF} = \frac{DE}{DF}$
- **标题**：② 切线性质与调和割线比值 $\frac{CE}{CF} = \frac{DE}{DF}$
- **数学逻辑**：
  因为 $AB$ 为 $\omega_1$ 直径，$C, D$ 在圆上，故 $\angle BCA = \angle BDA = 90^\circ$。  
  所以 $BC, BD$ 是圆 $\omega_2$ 的切线！  
  由切线性质与弦切角定理知：$\triangle BFC \sim \triangle BCE$ 且 $\triangle BFD \sim \triangle BDE$。  
  对应边成比例可得：
  $$\frac{CE}{CF} = \sqrt{\frac{BE}{BF}} = \frac{DE}{DF} \quad \text{(式 ③)}$$
- **画面图元**：
  - 新增图元：直角标记 $\angle BCA = 90^\circ$、$\angle BDA = 90^\circ$；
  - 高亮线段：切线段 $BC, BD$、割线段 $BE, BF$，四边形边 $CE, CF, DE, DF$。

---

### 步骤 3：在 $EF$ 上引入分点 $T$ 与相似三角形
- **标题**：③ 在 $EF$ 上引入分点 $T \implies \triangle DFT \sim \triangle DCE$
- **数学逻辑**：
  在割线 $EF$ 上取点 $T$ 使得 $\frac{FT}{FD} = \frac{CE}{CD}$（式 ①）。  
  由圆内接四边形 $CFDE$ 的性质：外角等于内对角，$\angle DFT = \angle DCE$。  
  两边对应成比例且夹角相等推出：
  $$\triangle DFT \sim \triangle DCE \implies \angle FDT = \angle CDE = \angle CFE$$
  同理可证 $\triangle DTE \sim \triangle DFC$，得出：
  $$\frac{ET}{DE} = \frac{CF}{CD} \quad \text{(式 ②)}$$
- **画面图元**：
  - 新增图元：辅助点 $T$、连线 $DT$；
  - 动态填充：$\triangle DFT$（淡橙色）与 $\triangle DCE$（淡紫色）；
  - 角弧标记：$\angle DFT$ 与 $\angle DCE$、$\angle FDT$ 与 $\angle CFE$。

---

### 步骤 4：$T$ 为 $EF$ 中点且点 $T$ 落在圆 $\omega_1$ 上
- **标题**：④ $T$ 为弦 $EF$ 中点 $\implies \angle ATB = 90^\circ \implies T$ 在 $\omega_1$ 上
- **数学逻辑**：
  式 ① 除以式 ② 得：$\frac{FT}{ET} \cdot \frac{DE}{DF} = \frac{CE}{CF}$。  
  结合式 ③ $\frac{CE}{CF} = \frac{DE}{DF}$，相消立即得到：
  $$FT = ET$$
  即点 $T$ 为弦 $EF$ 的中点！  
  由垂径定理知 $AT \perp EF$，即 $\angle ATB = 90^\circ$。  
  因为 $AB$ 是圆 $\omega_1$ 的直径，直角顶点 $T$ 必然落在圆 $\omega_1$ 上！
- **画面图元**：
  - 新增图元：线段 $AT, BT$；
  - 几何标记：$\angle ATB = 90^\circ$ 直角标记、线段 $FT$ 与 $ET$ 上的等长刻度线；
  - 高亮图元：点 $T$ 显式高亮，强调其与圆 $\omega_1$ 的交会。

---

### 步骤 5：对称性与三点共线 $T, C, D'$
- **标题**：⑤ 弧对称性与轴对称点 $D' \implies T, C, D'$ 三点共线
- **数学逻辑**：
  在圆 $\omega_1$ 中，$AB \perp CD$ 故弧 $\overset{\frown}{BC} = \overset{\frown}{BD}$，得圆周角 $\angle CTB = \angle DTB$。  
  由点 $D'$ 为点 $D$ 关于割线 $BE$（即直线 $BT$）的对称点，对称角相等：
  $$\angle D'TB = \angle DTB = \angle CTB$$
  由于 $C$ 与 $D'$ 位于直线 $BE$ 同侧，射线 $TD'$ 与 $TC$ 完全重合，即：
  $$T, C, D' \text{ 三点共线！}$$
- **画面图元**：
  - 新增图元：对称虚线段 $DD'$ 及其垂直标记、轴对称高亮；
  - 贯穿直线：直线 $T-C-D'$（贯通醒目连线）；
  - 角弧标记：对称角 $\angle CTB$ 与 $\angle D'TB$。

---

### 步骤 6：得出最终结论：$L, F, C, D'$ 四点共圆
- **标题**：⑥ 张角对等 $\angle FD'C = \angle CLF \implies L, F, C, D'$ 四点共圆
- **数学逻辑**：
  由于对称三角形 $\triangle FD'T \cong \triangle FDT$，且 $T, C, D'$ 三点共线：
  $$\angle FD'C = \angle FD'T = \angle FDT$$
  由步骤 ③ 知 $\angle FDT = \angle CFE$，由步骤 ① 知 $\angle CFE = \angle CLF$。  
  链式传递得出：
  $$\angle FD'C = \angle CLF \quad (\text{即 } \angle FLC)$$
  对公共底弦 $FC$，点 $D'$ 与点 $L$ 在同侧所张圆周角相等！  
  因此：
  $$L, F, C, D' \text{ 四点共圆！证明完毕。}$$
- **画面图元**：
  - 新增图元：四点共圆辅助圆 $\odot(LFCD')$（醒目彩色虚线圆）；
  - 高亮图元：公共底弦 $FC$、四边形边 $D'F, D'C$ 与 $LF, LC$；
  - 角弧标记：$\angle FD'C$ 与 $\angle FLC$（金色双弧高亮）；
  - 顶点强调：$L, F, C, D'$ 四点高亮圈。
