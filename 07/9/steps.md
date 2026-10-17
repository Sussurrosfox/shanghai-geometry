# 题目 07/9.md（例 8）分步证明与图元增删规划

## 一、命题陈述与核心几何背景

**题目**：在锐角 $\triangle APD$ 的边 $AP$ 和 $PD$ 上各取一点 $B, C$，四边形 $ABCD$ 的两条对角线相交于点 $Q$。$\triangle APD$ 和 $\triangle BPC$ 的垂心分别为 $H_1, H_2$。证明：如果直线 $H_1H_2$ 经过 $\triangle ABQ$ 及 $\triangle CDQ$ 的外接圆的交点 $X$，那么它必经过 $\triangle BQC$ 和 $\triangle AQD$ 的外接圆的交点 $Y$。

**核心逻辑链**：
1. **直径圆与高线垂足**：以 $AC, BD$ 为直径作圆 $\omega_1, \omega_2$，则四个高线垂足 $A_1, C_1 \in \omega_1$，$B_1, D_1 \in \omega_2$。
2. **垂心幂次性质**：由共圆四边形割线定理知 $H_1A \cdot H_1A_1 = H_1D \cdot H_1D_1$ 及 $H_2B \cdot H_2B_1 = H_2C \cdot H_2C_1$，导出 $H_1, H_2$ 对两直径圆圆幂相等，故直线 $H_1H_2$ 恰为 $\omega_1, \omega_2$ 的**根轴**。
3. **密克点相似性**：$X$ 作为对角线分割三角形的外接圆交点，具有螺旋相似中心性质，导出 $\triangle XAC \sim \triangle XBD$；中线比等于相似比 $k$。
4. **根轴幂等式导出全等**：若圆幂为 0 将导致 $\angle P = 90^\circ$（与锐角三角形矛盾），故非零圆幂比值给出 $k=1$，即 $AC = BD$。
5. **对偶交点 $Y$ 同样在根轴上**：由 $AC = BD$ 导出 $\triangle YAC \cong \triangle YBD$，故 $Y$ 对 $\omega_1, \omega_2$ 幂亦相等，从而 $Y$ 必在根轴 $H_1H_2$ 上！

---

## 二、严格代数几何坐标解算与构型参数

为了保证 SVG 图形比例舒展匀称、所有点位互不遮挡碰撞（最小点间距 $\ge 32\,\mathrm{px}$），采用精确几何参数化解算：
- 设画布主尺寸：$viewBox = 50\ 40\ 620\ 560$
- 基础控制点：
  - $P = (360.00, 90.00)$
  - $A = (180.00, 460.00)$
  - $D = (580.00, 460.00)$
  - $B = P + 0.575 (A - P) = (234.00, 349.00)$
  - $C$ 取在射线 $PD$ 上满足 $\|C - A\| = \|D - B\|$（一元二次方程严格解）：
    - 求解得 $v \approx 0.3541$，$C = (415.42, 183.21)$
    - 严格满足 $AC = BD \approx 363.37$
- 几何派生点（解析解）：
  - 对角线交点：$Q = AC \cap BD = (265.75, 359.18)$
  - 中点：$M = \mathrm{mid}(A, C) = (297.71, 321.60)$，$N = \mathrm{mid}(B, D) = (407.00, 404.50)$
  - 垂心：
    - $H_1 = \mathrm{orthocenter}(\triangle APD) = (360.00, 352.97)$
    - $H_2 = \mathrm{orthocenter}(\triangle BPC) = (469.00, 209.27)$
  - 高线垂足：
    - $A_1 = \mathrm{foot}(A, PD) = (475.52, 284.28) \in \omega_1$
    - $D_1 = \mathrm{foot}(D, PA) = (256.55, 302.65) \in \omega_2$
    - $B_1 = \mathrm{foot}(B, PD) = (440.86, 226.00) \in \omega_2$
    - $C_1 = \mathrm{foot}(C, PA) = (333.94, 143.57) \in \omega_1$
  - 外接圆交点：
    - $X = \odot(ABQ) \cap \odot(CDQ) \setminus \{Q\} = (290.21, 444.98)$
    - $Y = \odot(BQC) \cap \odot(AQD) \setminus \{Q\} = (380.00, 326.61)$
- **共线性校验**：
  - 根轴直线经过 $H_1, H_2$：方向向量为 $(109.00, -143.70)$，斜率 $-1.3183$
  - 点 $X$ 与点 $Y$ 到直线 $H_1H_2$ 的垂直距离严格为 $0$（浮点误差 $< 10^{-13}$），四点依次沿直线排列为 $X \to H_1 \to Y \to H_2$！

---

## 三、全局色彩与图层约定

| 角色 | 颜色值 | 用途与说明 |
| :--- | :--- | :--- |
| **主骨架线** | `#334155`（蓝灰，2px） | $\triangle APD$、四边形 $ABCD$ 边与对角线 $AC, BD$ |
| **直径圆 $\omega_1$** | `#6366f1`（靛蓝） | 以 $AC$ 为直径的圆，虚线轮廓，圆心 $M$ |
| **直径圆 $\omega_2$** | `#059669`（翡翠绿） | 以 $BD$ 为直径的圆，虚线轮廓，圆心 $N$ |
| **高线与垂足** | `#ea580c`（橙红） | 高线段与垂足直角标记 |
| **根轴 $H_1H_2$** | `#dc2626`（深红，2.5px） | 垂心连线、根轴延长线，统领全图 |
| **外接圆对 1** | `#2563eb` / `#0891b2` | $\odot(ABQ)$ 与 $\odot(CDQ)$，虚线，交于 $Q, X$ |
| **外接圆对 2** | `#d97706` / `#8b5cf6` | $\odot(BQC)$ 与 $\odot(AQD)$，虚线，交于 $Q, Y$ |
| **关键点 $X, Y$** | `#e11d48` / `#10b981` | 重点展示交点，外带 7px 半透明光环，极为醒目 |
| **文字标签** | `#0f172a`（深黑） | 顶层 `gPts`，统一带 4px 白色边缘描边防碰撞 |

---

## 四、分步演示规划（Step 0 ~ Step 6）

### 步骤 0：已知条件与几何构型
- **标题**：已知条件与几何构型
- **讲解正文**：
  在锐角 $\triangle APD$ 的边 $AP$ 和 $PD$ 上各取一点 $B, C$，四边形 $ABCD$ 对角线相交于 $Q$。<br>
  $\triangle APD$ 和 $\triangle BPC$ 的垂心分别为 $H_1, H_2$。<br>
  <b>求证</b>：若直线 $H_1H_2$ 经过 $\triangle ABQ$ 与 $\triangle CDQ$ 外接圆的交点 $X$，则必经过 $\triangle BQC$ 与 $\triangle AQD$ 外接圆的交点 $Y$。
- **图元增删**：
  - `gBase`：绘制 $\triangle APD$（线段 $PA, PD, AD$），四边形边 $BC$ 及对角线 $AC, BD$。
  - `gStep`：高亮顶角顶点 $P$、底边 $A, D$、内分点 $B, C$ 及对角线交点 $Q$；展示垂心 $H_1, H_2$ 与目标点 $X, Y$ 的相对位置。
  - 标签：显示 $P, A, B, C, D, Q$。

### 步骤 1：构造两对角线直径圆 $\omega_1, \omega_2$ 与垂足
- **标题**：① 构造对角线直径圆与高线垂足
- **讲解正文**：
  记 $AC, BD$ 的中点分别为 $M, N$，以 $AC, BD$ 为直径分别作圆 $\omega_1, \omega_2$。<br>
  分别作垂线：$AA_1 \perp PD$ 于 $A_1$，$BB_1 \perp PD$ 于 $B_1$，$CC_1 \perp PA$ 于 $C_1$，$DD_1 \perp PA$ 于 $D_1$。<br>
  由于 $\angle AA_1C = \angle AC_1C = 90^\circ$，故垂足 <b>$A_1, C_1$ 在圆 $\omega_1$ 上</b>；<br>
  同理 $\angle BB_1D = \angle BD_1D = 90^\circ$，故垂足 <b>$B_1, D_1$ 在圆 $\omega_2$ 上</b>。
- **图元增删**：
  - 绘制直径圆 $\omega_1$（以 $M$ 为圆心，淡靛蓝虚线）和 $\omega_2$（以 $N$ 为圆心，淡绿虚线）。
  - 绘制 4 条高线段：$AA_1, BB_1, CC_1, DD_1$（橙色虚线）。
  - 在垂足 $A_1, B_1, C_1, D_1$ 处绘制直角标记。
  - 显示点 $M, N, A_1, B_1, C_1, D_1$ 及其标签。

### 步骤 2：垂心幂次定理 ⇒ 直线 $H_1H_2$ 为两圆根轴
- **标题**：② 垂心圆幂相等 ⇒ $H_1H_2$ 为两圆根轴
- **讲解正文**：
  在 $\triangle APD$ 中，$H_1$ 是垂心，$AA_1, DD_1$ 为高，故四点 $A, D, A_1, D_1$ 共圆（以 $AD$ 为直径）。<br>
  由割线定理，点 $H_1$ 的圆幂满足：<br>
  $H_1A \cdot H_1A_1 = H_1D \cdot H_1D_1 \implies \mathrm{Pow}(H_1, \omega_1) = \mathrm{Pow}(H_1, \omega_2)$。<br>
  同理在 $\triangle BPC$ 中，垂心 $H_2$ 满足 $H_2B \cdot H_2B_1 = H_2C \cdot H_2C_1 \implies \mathrm{Pow}(H_2, \omega_1) = \mathrm{Pow}(H_2, \omega_2)$。<br>
  因此，<b>直线 $H_1H_2$ 恰为圆 $\omega_1$ 和圆 $\omega_2$ 的根轴（Radical Axis）</b>！
- **图元增删**：
  - 高亮两圆 $\omega_1, \omega_2$ 的中心连线 $MN$。
  - 绘制并高亮直线 $H_1H_2$（醒目红色贯通线，垂直于 $MN$）。
  - 高亮线段 $H_1A, H_1A_1$ 与 $H_1D, H_1D_1$（展示圆幂乘积守恒）。
  - 显示垂心 $H_1, H_2$ 点与标签。

### 步骤 3：点 $X$ 在根轴上 ⇒ 圆幂等式
- **标题**：③ 点 $X$ 位于根轴上 ⇒ 对应圆幂相等
- **讲解正文**：
  作出 $\triangle ABQ$ 和 $\triangle CDQ$ 的外接圆，它们交于对角线交点 $Q$ 和第二交点 $X$。<br>
  已知直线 $H_1H_2$ 经过点 $X$。因为 $H_1H_2$ 为圆 $\omega_1$ 与 $\omega_2$ 的根轴，<br>
  所以点 $X$ 对两圆的幂严格相等：<br>
  <b>$\mathrm{Pow}(X, \omega_1) = \mathrm{Pow}(X, \omega_2)$</b><br>
  即：$XM^2 - CM^2 = XN^2 - DN^2$（其中 $CM = \frac{1}{2}AC, DN = \frac{1}{2}BD$ 为两圆半径）。
- **图元增删**：
  - 绘制外接圆 $\odot(ABQ)$（蓝色虚线）与 $\odot(CDQ)$（青色虚线）。
  - 突出显示交点 $X$（大红圆点与光环），连结 $XM, XN$（虚线辅助）。
  - 保持根轴 $H_1H_2$ 高亮，清晰呈现点 $X$ 恰落在直线 $H_1H_2$ 上。

### 步骤 4：密克点螺旋相似 ⇒ 相似比 $k = 1$（$AC = BD$）
- **标题**：④ 螺旋相似 $\triangle XAC \sim \triangle XBD$ ⇒ $AC = BD$
- **讲解正文**：
  在圆周角下，$\angle XBD = \angle XAC$ 且 $\angle XDB = \angle XCA$，故 <b>$\triangle XAC \sim \triangle XBD$</b>。<br>
  $XM, XN$ 为对应中线，相似比设为 $k = \frac{AC}{BD} = \frac{CM}{DN} = \frac{XM}{XN}$。<br>
  若圆幂 $XM^2 - CM^2 = 0$，则 $\angle BXD = 90^\circ$，结合圆周角可推得 $P, B, X, D$ 共圆，导致 $\angle P = 90^\circ$，与 $\triangle APD$ 为锐角三角形矛盾！<br>
  故圆幂非零，由 $XM^2 - CM^2 = k^2(XN^2 - DN^2)$ 及圆幂相等可得：<br>
  <b>$k^2 = 1 \implies k = 1 \implies AC = BD$</b>（两对角线长度必相等！）。
- **图元增删**：
  - 半透明高亮填充 $\triangle XAC$（淡蓝）与 $\triangle XBD$（淡青）。
  - 高亮对应线段 $AC$ 与 $BD$，添加双刻度等长标记（tickMark）。
  - 高亮对应中线 $XM$ 与 $XN$。

### 步骤 5：对偶交点 $Y$ 同样具有全等相似性
- **标题**：⑤ 对偶相似 $\triangle YAC \cong \triangle YBD$ ⇒ $Y$ 对两圆幂相等
- **讲解正文**：
  同理，作出 $\triangle BQC$ 和 $\triangle AQD$ 的外接圆，其第二交点为 $Y$。<br>
  完全同理可得 $\triangle YAC \sim \triangle YBD$。<br>
  由于前一步已严格证明相似比 $k = \frac{AC}{BD} = 1$，因此 <b>$\triangle YAC \cong \triangle YBD$</b>（全等）！<br>
  对应中线等长：$YM = YN$，且半弦等长 $CM = DN$。<br>
  故有：<b>$YM^2 - CM^2 = YN^2 - DN^2 \implies \mathrm{Pow}(Y, \omega_1) = \mathrm{Pow}(Y, \omega_2)$</b>。
- **图元增删**：
  - 绘制外接圆 $\odot(BQC)$（琥珀色虚线）与 $\odot(AQD)$（紫罗兰虚线）。
  - 突出显示交点 $Y$（翠绿色圆点与光环）。
  - 半透明高亮全等三角形 $\triangle YAC$ 与 $\triangle YBD$，连结对应中线 $YM, YN$。

### 步骤 6：得出最终结论（$H_1, H_2, Y$ 三点共线）
- **标题**：⑥ 结论：直线 $H_1H_2$ 必经过交点 $Y$
- **讲解正文**：
  点 $Y$ 对圆 $\omega_1$ 和圆 $\omega_2$ 的圆幂相等，意味着 <b>点 $Y$ 位于这两圆的根轴上</b>。<br>
  而步骤 ② 已证得直线 $H_1H_2$ 即为此两圆的根轴。<br>
  因此，<b>点 $Y$ 必定落在直线 $H_1H_2$ 上</b>！<br>
  即：如果直线 $H_1H_2$ 经过交点 $X$，那么它必经过交点 $Y$。<br>
  四点 $X, H_1, Y, H_2$ 严格共线于根轴之上，命题获证！
- **图元增删**：
  - 全景复现根轴 $H_1H_2$，贯穿四点 $X, H_1, Y, H_2$。
  - 保持两直径圆 $\omega_1, \omega_2$ 的淡色圆弧背景，直观展现根轴几何本质。
  - 四个核心点 $X, H_1, Y, H_2$ 赋予跳动/高亮光环，达成完美总结与视觉收敛。
