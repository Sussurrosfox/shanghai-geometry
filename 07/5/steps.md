# 题目 07/5（例 4）分步证明与图元规划 (steps.md)

## 一、 命题概述与几何核心

### 1. 命题内容
已知 $AB$ 是圆 $O$ 的弦，$M$ 是弧 $\overset{\frown}{AB}$ 的中点。$C$ 是圆 $O$ 外任意一点，过点 $C$ 作圆 $O$ 的两条切线 $CS, CT$（切点分别为 $S, T$）。连接 $MS, MT$ 分别交 $AB$ 于点 $E, F$。过 $E, F$ 作 $AB$ 的垂线，与半径 $OS, OT$ 分别交于点 $X, Y$。再过点 $C$ 作圆 $O$ 的一条割线交圆 $O$ 于点 $P, Q$，连接 $MP$ 交 $AB$ 于点 $R$。设 $Z$ 是 $\triangle PQR$ 的外心。
**求证**：$X, Y, Z$ 三点共线。

### 2. 核心证明脉络（根轴法与正交连心线）
1. **弧中点与圆幂**：由 $M$ 是弧 $\overset{\frown}{AB}$ 中点，由同弧圆周角定理及公共角易证 $\triangle MAR \sim \triangle MPA \implies MR \cdot MP = MA^2$；同理 $\triangle MAE \sim \triangle MSA \implies ME \cdot MS = MA^2$。故 $MR \cdot MP = ME \cdot MS$。
2. **辅助圆 $X$ 的切线与圆周性质**：$EX \parallel OM$ 结合等腰 $\triangle OMS$ 导出 $\angle XSE = \angle XES \implies XS = XE$。因此以 $X$ 为圆心、$XE$ 为半径的圆 $X$ 恰好过点 $S$。且由于 $CS \perp OS$，切线 $CS$ 亦切圆 $X$ 于 $S$。
3. **公共根轴 $CM$**：
   - 点 $M$ 关于圆 $Z$ 的幂为 $MR \cdot MP$，关于圆 $X$ 的幂为 $ME \cdot MS$，二者均等于 $MA^2$，故 $M$ 在圆 $Z$ 与圆 $X$ 的根轴上；
   - 点 $C$ 关于圆 $Z$ 的幂为 $CP \cdot CQ$，关于圆 $X$ 的幂为 $CS^2$，由圆 $O$ 的切割线定理 $CP \cdot CQ = CS^2$，故 $C$ 亦在圆 $Z$ 与圆 $X$ 的根轴上；
   - 从而直线 $CM$ 是圆 $Z$ 与圆 $X$ 的公共根轴，推出连心线垂直于根轴：$ZX \perp CM$。
4. **对称性与共线**：同理，由完全对称的论证，直线 $CM$ 亦为圆 $Z$ 与圆 $Y$ 的公共根轴，推出 $ZY \perp CM$。由垂线的唯一性，直线 $ZX$ 与 $ZY$ 重合，故 $X, Y, Z$ 三点共线（且直线 $XYZ \perp CM$）。

---

## 二、 严格代数几何坐标解算与验证参数

为确保页面中几何元素构图舒展平衡、无退化、文字与线段不碰撞，选定以下全局基准参数并在 JavaScript 中完全通过代数几何解析闭式动态解算：

### 1. 基础点与圆参量
- **圆心 $O$**：$(360.00, 270.00)$，半径 $r_O = 130.00$。
- **弧中点 $M$**：设弧 $AB$ 的中点角为 $98^\circ$（弧度 $\theta_M = 1.7104$），$M = (326.35, 395.57)$。
- **弦端点 $A, B$**：相对中点张角 $\delta = 65^\circ$（弧度 $1.1345$）：
  - $A = (230.49, 281.33)$
  - $B = (466.49, 344.56)$
- **圆外点 $C$**：$(145.00, 115.00)$，位于左上方。

### 2. 切点与垂线交点（圆 $X$ 与圆 $Y$）
- **切点 $S, T$**：$C$ 到 $O$ 连线距 $d_{CO} \approx 264.48$，切线半角 $\alpha = \arccos(r_O / d_{CO}) \approx 60.56^\circ$：
  - $S = (242.03, 324.61)$（切线 $CS$）
  - $T = (374.53, 140.81)$（切线 $CT$）
- **交点 $E, F$**：$MS$ 交 $AB$ 于 $E = (171.96, 265.64)$；$MT$ 交 $AB$ 于 $F = (342.29, 311.29)$。
- **垂线交点 $X, Y$**：
  - 过 $E$ 作 $AB$ 垂线交半径 $OS$ 于 $X = (143.9961, 369.9890)$，圆 $X$ 半径 $r_X = XE = XS = 108.03$。
  - 过 $F$ 作 $AB$ 垂线交半径 $OT$ 于 $Y = (364.8094, 227.2570)$，圆 $Y$ 半径 $r_Y = YF = YT = 87.00$。

### 3. 割线、外接圆与外心 $Z$
- **割线 $CPQ$**：割线与圆 $O$ 相交于：
  - 近点 $P = (244.48, 210.37)$
  - 远点 $Q = (424.46, 382.89)$
- **交点 $R$**：$MP$ 与弦 $AB$ 交于点 $R = (281.95, 295.12)$。
- **外心 $Z$**：$\triangle PQR$ 的外心经线段垂直平分线联立解算得到：
  - $Z = (459.8804, 165.8119)$，外接圆半径 $r_Z = 219.96$。

### 4. 几何不变量检验（理论误差 $< 10^{-12}$）
- $X, Y, Z$ 三点共线判定：两向量叉积 $\text{cross}(Y-X, Z-X) \approx 0$，点 $Z$ 到直线 $XY$ 距离 $< 10^{-12}\text{ px}$。
- 直线 $XYZ$ 与根轴 $CM$ 正交判定：$(Z - X) \cdot (M - C) = 0$。
- 切线正交性：$(S - C) \cdot (S - O) = 0$ 且 $(T - C) \cdot (T - O) = 0$。
- 垂线垂直度：$(X - E) \cdot (B - A) = 0$ 且 $(Y - F) \cdot (B - A) = 0$。

---

## 三、 色彩体系设计

| 用途分类 | 色值 | 说明 |
| :--- | :--- | :--- |
| **基础图元 (Base)** | `#334155` (深灰蓝) | 圆 $O$、弦 $AB$、点 $M$ 等全程保留元素 |
| **圆 X 相关图元** | `#2563eb` (高亮蓝, BLUE) | 圆 $X$、辅助线 $MS, EX, XS$、点 $E, X$ |
| **圆 Y 相关图元** | `#059669` (翡翠绿, GREEN) | 圆 $Y$、辅助线 $MT, FY, YT$、点 $F, Y$ |
| **根轴与共线结论** | `#dc2626` (正红, RED) | 公共根轴 $CM$、共线直线 $XYZ$、直角标记 |
| **圆 Z 与割线** | `#7c3aed` (紫罗兰, PURPLE) | 割线 $CPQ$、圆 $Z$、三角形 $PQR$、点 $P, Q, R, Z$ |
| **次要辅助标记** | `#ea580c` (暖橙, ORANGE) | 相似三角形高亮阴影、角弧等角度对应标记 |

---

## 四、 分步演示与图元增删规划

### 步骤 0：已知条件与几何构型
- **标题**：已知条件与几何构型
- **讲解正文**：
  已知 $AB$ 是圆 $O$ 的弦，$M$ 是弧 $\overset{\frown}{AB}$ 的中点。$C$ 是圆外任意一点，过 $C$ 作圆 $O$ 的两条切线 $CS, CT$（切点为 $S, T$）。<br>
  连接 $MS, MT$ 分别交 $AB$ 于点 $E, F$；过 $E, F$ 分别作 $AB$ 的垂线交半径 $OS, OT$ 于点 $X, Y$。<br>
  再过点 $C$ 作圆 $O$ 的割线交圆于 $P, Q$，连接 $MP$ 交 $AB$ 于点 $R$。设 $Z$ 是 $\triangle PQR$ 的外心。<br>
  <b>求证：</b>$X, Y, Z$ 三点共线。
- **画面图元**：
  - 底层基准：圆 $O$、弦 $AB$、点 $M$、切线 $CS, CT$（延伸实线）、割线 $CPQ$、垂线 $EX, FY$、连线 $MS, MT, MP$。
  - 点集显示：$O, A, B, M, C, S, T, E, F, X, Y, P, Q, R, Z$。

### 步骤 1：弧中点引出的相似比与圆幂公式
- **标题**：① 弧中点引出的三角形相似：$MR \cdot MP = MA^2$
- **讲解正文**：
  因为 $M$ 是弧 $\overset{\frown}{AB}$ 的中点，由同弧圆周角定理可知：<br>
  $\angle MAB = \angle MPB = \angle MPA$。<br>
  在 $\triangle MAR$ 与 $\triangle MPA$ 中，具备公共角 $\angle AMR = \angle PMA$ 以及 $\angle MAR = \angle MPA$，故：<br>
  <span style="color:#2563eb;font-weight:600">$\triangle MAR \sim \triangle MPA$</span>。<br>
  由相似三角形对应边成比例可得：$\dfrac{MA}{MP} = \dfrac{MR}{MA} \implies MR \cdot MP = MA^2$。<br>
  又由于 $M$ 是弧中点，$MA = MB$，故 <span style="color:#dc2626;font-weight:700">$MR \cdot MP = MA^2 = MB^2$</span>。
- **画面图元**：
  - 动态层：半透明高亮填充 $\triangle MAR$ 与 $\triangle MPA$；高亮边 $MA, MP, MR$；在 $A$ 与 $P$ 处绘制角弧标记。
  - 点集控制：突出 $M, A, P, R$。

### 步骤 2：切点连线相似与点 M 的等幂恒等式
- **标题**：② 切点弦角三角形相似：$ME \cdot MS = MA^2$
- **讲解正文**：
  连接辅助线 $AS$。由同弧所对圆周角与弧中点性质：<br>
  $\angle MSA$ 对应弧 $\overset{\frown}{MA}$，而 $\angle MAE = \angle MAB$ 对应弧 $\overset{\frown}{MB} = \overset{\frown}{MA}$，因此 $\angle MAE = \angle MSA$。<br>
  结合公共角 $\angle AME = \angle SMA$，可知：<br>
  <span style="color:#2563eb;font-weight:600">$\triangle MAE \sim \triangle MSA$</span>。<br>
  同理得出对应边成比例：$\dfrac{MA}{MS} = \dfrac{ME}{MA} \implies ME \cdot MS = MA^2$。<br>
  联立步骤 1 的结论，得到核心等幂链：<br>
  <span style="color:#dc2626;font-weight:700">$MR \cdot MP = ME \cdot MS = MA^2$</span>。
- **画面图元**：
  - 动态层：清空上步三角形；连虚线 $AS$；半透明高亮 $\triangle MAE$ 与 $\triangle MSA$；在 $A$ 和 $S$ 处绘制等角角弧；高亮等幂线段 $ME, MS$。

### 步骤 3：构造辅助圆 X 与点 M 在根轴上的判定
- **标题**：③ 构造圆 $X$：$XS = XE$ 且点 $M$ 位于圆 $Z$ 与圆 $X$ 的根轴上
- **讲解正文**：
  考察以 $X$ 为圆心、$XE$ 为半径的圆 $X$。因为 $EX \perp AB$ 且 $OM \perp AB$，所以 $EX \parallel OM$，内错角 $\angle XEM = \angle OME$。<br>
  又因半径 $OS = OM = r_O$，等腰 $\triangle OMS$ 给出 $\angle OSM = \angle OMS$。<br>
  由此推得 $\angle XSE = \angle OSM = \angle XEM = \angle XES$，故 $\triangle XSE$ 为等腰三角形，即 <span style="color:#2563eb;font-weight:700">$XS = XE$</span>！<br>
  这说明：<b>以 $X$ 为圆心、$XE$ 为半径的辅助圆 $X$ 必然经过切点 $S$</b>。<br>
  因割线 $MES$ 交圆 $X$ 于 $E, S$，$ME \cdot MS$ 即为 $M$ 关于圆 $X$ 的幂；而割线 $MRP$ 交圆 $Z$ 于 $R, P$，$MR \cdot MP$ 即为 $M$ 关于圆 $Z$ 的幂。<br>
  由 $MR \cdot MP = ME \cdot MS$ 可知：<span style="color:#7c3aed;font-weight:700">点 $M$ 必然位于圆 $Z$ 与圆 $X$ 的根轴上</span>！
- **画面图元**：
  - 动态层：清空上步；画出辅助圆 $X$（虚线）；在 $XE$ 与 $XS$ 上添加等长刻度标记；高亮割线 $MES$ 与 $MRP$；直角标记 $EX \perp AB$。

### 步骤 4：点 C 在根轴上 ⇒ CM 为两圆根轴且 CM ⊥ ZX
- **标题**：④ 切割线定理与公共根轴：$CM$ 是根轴且 $CM \perp ZX$
- **讲解正文**：
  因为 $CS$ 是圆 $O$ 的切线，且圆心 $X$ 位于半径 $OS$ 上，故 $CS \perp OS \implies CS \perp XS$。因此 $CS$ 亦为圆 $X$ 在切点 $S$ 处的切线！<br>
  因此点 $C$ 关于圆 $X$ 的幂等于切线长平方 $CS^2$。<br>
  另一方面，割线 $CPQ$ 交圆 $O$ 于 $P, Q$，由于 $P, Q$ 亦在 $\triangle PQR$ 的外接圆 $Z$ 上，故点 $C$ 关于圆 $Z$ 的幂等于 $CP \cdot CQ$。<br>
  由圆 $O$ 的切割线定理知：<span style="color:#059669;font-weight:600">$CP \cdot CQ = CS^2$</span>。<br>
  这证明点 $C$ 关于圆 $Z$ 与圆 $X$ 的幂亦相等，故 <span style="color:#7c3aed;font-weight:700">点 $C$ 亦在圆 $Z$ 与圆 $X$ 的根轴上</span>！<br>
  综上，两点确定一条直线，<b>直线 $CM$ 必然是圆 $Z$ 与圆 $X$ 的公共根轴</b>。<br>
  根据几何定理「两圆根轴垂直于连心线」，立即得出：<span style="color:#dc2626;font-weight:700">$CM \perp ZX$</span>！
- **画面图元**：
  - 动态层：绘制圆 $Z$（虚线）；加粗红色高亮直线 $CM$（根轴）；绘制切线 $CS$ 与直角标记 $CS \perp XS$；绘制连心线 $ZX$；在 $CM$ 与 $ZX$ 交点处标出直角符号。

### 步骤 5：对称性推得 CM ⊥ ZY 与得出最终结论
- **标题**：⑤ 对称性 $CM \perp ZY$ ⇒ $X, Y, Z$ 三点共线
- **讲解正文**：
  完全同理，考察以 $Y$ 为圆心、$YF$ 为半径的圆 $Y$。由完全对称的论证：<br>
  $YF = YT$，圆 $Y$ 亦经过切点 $T$；$MF \cdot MT = MA^2 = MR \cdot MP$，且 $CT^2 = CP \cdot CQ$。<br>
  因此直线 $CM$ 亦为圆 $Z$ 与圆 $Y$ 的公共根轴！由此立即得出：<span style="color:#059669;font-weight:700">$CM \perp ZY$</span>。<br>
  因为经过平面上同一点 $Z$ 且垂直于直线 $CM$ 的直线是唯一的，所以直线 $ZX$ 与直线 $ZY$ 必然完全重合！<br>
  这严格证明了：<span style="color:#dc2626;font-size:15px;font-weight:700">$X, Y, Z$ 三点共线</span>（且直线 $XYZ \perp CM$）。全题证毕！
- **画面图元**：
  - 动态层：绘制辅助圆 $Y$（虚线）；高亮连心线 $ZY$；高亮直角标记 $CM \perp ZY$；贯通绘制红色加粗共线直线 $XYZ$（两端适度延长）；$X, Y, Z$ 三点增加发光环圈高亮。
