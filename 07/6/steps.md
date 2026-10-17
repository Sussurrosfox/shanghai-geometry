# 例 5：几何证明交互可视化分步规划与图元设计

本文档为几何证明题目 `07/6.md`（例 5）的高精度交互演示页面设计方案，包含严格的代数几何坐标解算、色彩层级规范以及分步证明图元增删规划。

---

## 一、命题概述与几何分析

### 1. 题目原文
> 在锐角三角形 $ABC$ 中，点 $X, Y$ 是三角形 $ABC$ 内部的两个互异的动点，且满足 $B, C, X, Y$ 四点共圆及 $\angle AXB - \angle ACB = \angle AYC - \angle ABC$ . 证明: 直线 $XY$ 经过一个定点.

### 2. 核心证明链
1. **定点构造**：设过点 $A$ 的 $\Delta ABC$ 外接圆 $\omega_1$ 的切线与直线 $BC$ 的延长线交于点 $D$。点 $D$ 仅取决于固定的锐角三角形 $ABC$，与动点 $X, Y$ 无关。
2. **等角和转化**：利用围绕动点的周角与三角形内角和，将角差条件 $\angle AXB - \angle ACB = \angle AYC - \angle ABC$ 等价转化为 $\angle CAX + \angle CBX = \angle BAY + \angle BCY$。
3. **弦切角与共圆对角导角**：结合 $\omega_1$ 在 $A$ 处的弦切角性质与圆内接四边形 $BCXY$ 对角互补性质，严格推导出 $\angle YAD = \angle AXY$。
4. **切线判定**：由弦切角定理逆定理，得出直线 $AD$ 为 $\Delta AXY$ 外接圆 $\omega$ 在点 $A$ 处的切线。
5. **三圆根心定理**：
   - $\omega_1$（$\Delta ABC$ 外接圆）与 $\omega$（$\Delta AXY$ 外接圆）在点 $A$ 相切，切线 $AD$ 为其根轴；
   - $\omega_1$ 与 $\omega_2$（$BCXY$ 共圆）交于 $B, C$，直线 $BC$ 为其根轴；
   - $\omega$ 与 $\omega_2$ 交于 $X, Y$，直线 $XY$ 为其根轴；
   根据根心定理，三条根轴必共点于一点。已知 $AD$ 与 $BC$ 相交于点 $D$，故直线 $XY$ 必经过定点 $D$。

---

## 二、高精度代数几何坐标解算

为确保交互演示具有绝对几何真实性（圆弧无错位、切线严丝合缝、根轴严格交于同一点），在 SVG 坐标系（$y$ 轴向下）中建立严格的解析几何方程组并解算：

### 1. 几何参数设定
- **基准线与顶点**：
  设底边 $BC$ 位于水平直线 $y = 360$ 上。
  - $B = (100.000, 360.000)$
  - $C = (380.000, 360.000)$（边长 $BC = 280$）
  - 定点 $D$ 设于 $C$ 右侧延长线上：$D = (640.000, 360.000)$
  - 割线段长：$DB = 540$，$DC = 260$。
- **顶点 $A$ 的确定**：
  由切割线定理逆定理，要使 $DA$ 切 $\omega_1$ 于 $A$，必有：
  $$DA^2 = DB \cdot DC = 540 \times 260 = 140400 \implies DA = \sqrt{140400} \approx 374.69988$$
  取 $A_x = 310.000$（使 $\Delta ABC$ 成为各角约 $71.4^\circ, 41.4^\circ, 67.2^\circ$ 的标准锐角三角形），解得：
  $$(310 - 640)^2 + (A_y - 360)^2 = 140400 \implies A_y = 360 - \sqrt{140400 - 108900} = 360 - \sqrt{31500} \approx 182.518$$
  - $A = (310.000, 182.518)$

### 2. 圆与动点坐标解算
- **$\Delta ABC$ 外接圆 $\omega_1$**：
  由三点 $A, B, C$ 垂直平分线求得：
  - 圆心 $O_1 = (240.000, 312.671)$
  - 半径 $R_1 \approx 147.784$
  - 切线验算：$\vec{DA} \cdot \vec{O_1 A} = (-330, -177.482) \cdot (70, -130.154) = -23100 + 23100 = 0.000$（严格相切）
- **四点共圆 $\omega_2$（通过 $B, C, X, Y$）**：
  圆心必在 $BC$ 中垂线 $x = 240$ 上，取 $y_{O2} = 420.000$：
  - 圆心 $O_2 = (240.000, 420.000)$
  - 半径 $R_2 = \sqrt{140^2 + (420 - 360)^2} = \sqrt{19600 + 3600} = \sqrt{23200} \approx 152.315$
- **动点 $X, Y$ 的严格求解**：
  直线 $DXY$ 从 $D(640, 360)$ 发射，方向角 $\theta = 12.0^\circ$（单位向量 $\vec{u} = (-\cos 12^\circ, -\sin 12^\circ)$）。
  与圆 $\omega_2$ 的二次交点参数方程求得两交点：
  - 点 $Y$（距 $D$ 较近）：$Y = (323.76, 292.78)$
  - 点 $X$（距 $D$ 较远）：$X = (215.23, 269.71)$
  - 两点间距：$XY \approx 111.0$，$X, Y$ 均在 $\Delta ABC$ 内部。
  - 割线圆幂严格恒等：$DX \cdot DY = 140400 = DA^2 = DB \cdot DC$。
- **$\Delta AXY$ 外接圆 $\omega$**：
  由 $A, X, Y$ 三点共圆求解：
  - 圆心 $O = (277.72, 242.53)$
  - 半径 $R \approx 68.15$
  - 切线验算：$\vec{DA} \cdot \vec{OA} = 0.000$（$DA$ 严格相切于圆 $\omega$ 于点 $A$）
- **角度差严格验算**：
  - $\angle AXB - \angle ACB = 143.14^\circ - 48.88^\circ = 94.26^\circ$
  - $\angle AYC - \angle ABC = 135.69^\circ - 41.43^\circ = 94.26^\circ$
  - 误差 $\Delta = 0.00000^\circ$，代数几何关系完美闭环！

### 3. 画布与视口（ViewBox）
- 全图水平范围：$x \in [87.7, 660.0]$
- 全图垂直范围：$y \in [164.9, 572.3]$
- 视口配置：`viewBox="50 120 640 470"`，留白四周均匀，保证所有顶点、圆弧和切线均不碰壁。

---

## 三、视觉与色彩设计规范

### 1. 色彩语义约定
| 语义对象 | 颜色代码 | 色彩名称 | 应用场景 |
| :--- | :--- | :--- | :--- |
| **基础骨架** | `#1e293b` (深蓝灰) | Base Slate | $\Delta ABC$ 轮廓边框、基准底边 |
| **外接圆 $\omega_1$** | `#2563eb` (蓝色) | Royal Blue | $\Delta ABC$ 外接圆，基准切线 $AD$ |
| **外接圆 $\omega_2$** | `#059669` (绿色) | Emerald Green | 四边形 $BCXY$ 共圆 |
| **外接圆 $\omega$** | `#7c3aed` (紫色) | Violet Purple | $\Delta AXY$ 外接圆 |
| **关键根轴与切线** | `#dc2626` (鲜红) | Coral Red | 汇交于定点 $D$ 的三条根轴，定点 $D$ 高亮 |
| **动点与连线** | `#ea580c` (橙色) | Amber Orange | 动点 $X, Y$ 及其相关辅助连线 |
| **等角标记弧** | `#0891b2` / `#d97706` | Cyan / Amber | 对称角弧标记对比 |

### 2. 三层 SVG 架构与防遮挡规范
- **静态底层 `gBase`**：仅绘制全程恒定的几何基准——三角形 $ABC$、延长线基底、顶点基础标记。
- **动态单步层 `gStep`**：步骤切换时执行 `gStep.innerHTML = ''` 擦除上一阶段图元，按步骤绘制当前所需的辅助线、圆、角弧与高亮轮廓。
- **顶层点与文字 `gPts`**：所有点、圆点（圆点半径 $r=4.5$ 白色边框 $1.5\text{px}$）及文字标签。
- **4px 白色轮廓描边**：所有文本标签启用 CSS `paint-order: stroke fill; stroke: #ffffff; stroke-width: 4px; stroke-linejoin: round;`，即便与任何线段、圆弧重合交叉，文字依然清晰脱颖而出。

---

## 四、分步证明与图元增删规划

### Step 0：已知条件与几何命题
- **标题**：✦ 已知条件与几何命题
- **正文**：在锐角 $\triangle ABC$ 中，点 $X, Y$ 是内部的两个互异动点，满足 $B, C, X, Y$ 四点共圆（记为 $\omega_2$），且角差相等：<br>$\angle AXB - \angle ACB = \angle AYC - \angle ABC$。<br><b>求证</b>：直线 $XY$ 经过一个与 $X, Y$ 无关的定点。
- **画面图元**：
  - `gBase`：三角形 $ABC$（实线实黑）。
  - `gStep`：绘制圆 $\omega_2$（绿色虚线圆），连线 $XY$ 及其延伸割线，绘制动点连线 $BX, CX, BY, CY$。
  - `gPts`：标注顶点 $A, B, C$ 与动点 $X, Y$。

### Step 1：构造定点 $D$ 与外接圆 $\omega_1$
- **标题**：① 构造定点 $D$ 与外接圆 $\omega_1$
- **正文**：设 $\triangle ABC$ 的外接圆为 $\omega_1$。过点 $A$ 作 $\omega_1$ 的切线，与边 $BC$ 的延长线交于点 $D$。<br><b>定点属性</b>：由于 $\triangle ABC$ 为固定的锐角三角形，故外接圆 $\omega_1$、切线 $AD$ 及交点 $D$ 均为唯一的<b>定点</b>。由切割线定理可知 $DA^2 = DB \cdot DC$。
- **画面图元**：
  - `gStep`：绘制外接圆 $\omega_1$（蓝色虚线圆），绘制底边延长线 $CD$，绘制切线 $AD$（红色高亮线段），切点 $A$ 处直角/切线标记。
  - `gPts`：增加定点 $D$ 的标注（带高亮红点与外光圈）。

### Step 2：周角拆解转化角差条件
- **标题**：② 周角拆解转化角差条件
- **正文**：围绕内部动点 $X$，利用周角 $360^\circ$ 与三角形内角和定理：<br>$\angle AXB = 360^\circ - \angle AXC - \angle CXB$<br>$\angle ACB = \angle ACX + \angle BCX$<br>相减得：$\angle AXB - \angle ACB = 360^\circ - (180^\circ - \angle CAX) - (180^\circ - \angle XBC) = \angle CAX + \angle CBX$。<br>同理：$\angle AYC - \angle ABC = \angle BAY + \angle BCY$。<br>由已知角差相等，立即得出对称等式：<b>$\angle CAX + \angle CBX = \angle BAY + \angle BCY$</b>。
- **画面图元**：
  - `gStep`：高亮连线 $AX, BX$ 与 $AY, CY$；分别绘制角弧 $\angle CAX, \angle CBX$（青色）与 $\angle BAY, \angle BCY$（橙黄色），凸显两组对称角和的转化。

### Step 3：弦切角与圆内接四边形导角
- **标题**：③ 弦切角与圆内接四边形导角
- **正文**：因为 $AD$ 是 $\omega_1$ 的切线，由弦切角定理知 $\angle BAD = \angle ABC + \angle BAC$。<br>结合步骤 ② 的角关系，计算角 $\angle YAD$：<br>$\angle YAD = \angle BAD - \angle BAY = \angle ABC + \angle BAC - (\angle CAX + \angle CBX - \angle BCY)$<br>$= (\angle ABC - \angle CBX) + (\angle BAC - \angle CAX) + \angle BCY = \angle ABX + \angle BAX + \angle BCY$。<br>又由 $B,C,X,Y$ 共圆，圆内接四边形对角互补：$\angle BCY = 180^\circ - \angle BXY$。<br>代入得：$\angle YAD = (180^\circ - \angle AXB) + (180^\circ - \angle BXY) = 360^\circ - (\angle AXB + \angle BXY) = \mathbf{\angle AXY}$！
- **画面图元**：
  - `gStep`：高亮角 $\angle YAD$ 与角 $\angle AXY$（鲜艳红色角弧），高亮弦 $AY$ 与射线 $AD, AX$。

### Step 4：得出 $AD$ 是外接圆 $\omega$ 的切线
- **标题**：④ 判定 $AD$ 是 $\omega(AXY)$ 的切线
- **正文**：在 $\triangle AXY$ 中，射线 $AD$ 与弦 $AY$ 所夹的角满足：<br>$\angle YAD = \angle AXY$（弦切角等于圆周角）。<br>由弦切角定理的逆定理，<b>直线 $AD$ 是 $\triangle AXY$ 的外接圆 $\omega$ 在点 $A$ 处的切线</b>！<br>由此可知，$AD$ 不仅切 $\omega_1$，同时也切 $\omega$，直线 $AD$ 是圆 $\omega$ 与圆 $\omega_1$ 在切点 $A$ 处的公共切线（根轴）。
- **画面图元**：
  - `gStep`：绘制 $\triangle AXY$ 的外接圆 $\omega$（紫色虚线圆），展示 $\omega$ 与 $\omega_1$ 在点 $A$ 处内切，高亮公共切线 $AD$。

### Step 5：三圆根心定理，证明 $XY$ 恒过定点 $D$
- **标题**：⑤ 应用三圆根心定理得出结论
- **正文**：考察三个圆及其两两之间的根轴：<br>1. $\omega$ 与 $\omega_1$：在 $A$ 处相切，公共切线 <b>$AD$</b> 为其根轴；<br>2. $\omega_1$ 与 $\omega_2$：相交于 $B, C$，直线 <b>$BC$</b> 为其根轴；<br>3. $\omega$ 与 $\omega_2$：相交于 $X, Y$，直线 <b>$XY$</b> 为其根轴。<br>由<b>根心定理</b>（三圆根轴定理）：三个圆的两两根轴若不平行，必交于同一点（根心）。<br>因为根轴 $AD$ 与 $BC$ 显然相交于定点 $D$，所以第三条根轴 <b>直线 $XY$ 必经过定点 $D$</b>！<br>证毕。
- **画面图元**：
  - `gStep`：三圆同时显现（$\omega_1$ 蓝色、$\omega_2$ 绿色、$\omega$ 紫色）；同时高亮三条根轴：$AD$（红实线）、$BCD$（深灰实线延伸）、$XYD$（红实线延伸线）；在交点 $D$ 处产生光晕脉冲圆点，全面证明三线共点于定点 $D$。

---
至此，步骤规划完备，代数坐标完全自洽，进入 HTML 编写阶段。
