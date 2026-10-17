# 例 4：第二交点三角形与中点对称三角形的相似证明

## 题目
设 $A_1, B_1, C_1$ 分别是 $\triangle ABC$ 的边 $BC, CA, AB$ 上的点，$\triangle AB_1C_1, \triangle A_1BC_1, \triangle A_1B_1C$ 的外接圆分别与 $\triangle ABC$ 的外接圆交于另一点 $A_2, B_2, C_2$ ($A_2 \neq A, B_2 \neq B, C_2 \neq C$)，点 $A_3, B_3, C_3$ 分别是 $A_1, B_1, C_1$ 关于边 $BC, CA, AB$ 中点的对称点。证明：$\triangle A_2B_2C_2 \sim \triangle A_3B_3C_3$。

---

## 演示分步规划（6 步）

### Step 0: 已知条件与几何构型
- **标题**：已知条件与几何构型
- **讲解正文**：
  在锐角 $\triangle ABC$ 中，外接圆为 $\odot O$。点 $A_1, B_1, C_1$ 分别在边 $BC, CA, AB$ 上。<br>
  分别作 $\triangle AB_1C_1, \triangle A_1BC_1, \triangle A_1B_1C$ 的外接圆 $\odot O_A, \odot O_B, \odot O_C$（此三圆由密克定理交于密克点 $M$），它们分别与 $\odot O$ 相交于另一点 $A_2, B_2, C_2$。<br>
  同时，取 $A_1, B_1, C_1$ 分别关于边 $BC, CA, AB$ 中点的对称点 $A_3, B_3, C_3$。<br>
  目标：证明 <b>$\triangle A_2B_2C_2 \sim \triangle A_3B_3C_3$</b>。
- **画面元素**：
  - 底层：$\triangle ABC$（深色细线），外接圆 $\odot O$（柔和青蓝细线）。
  - 动态层：小外接圆 $\odot O_A, \odot O_B, \odot O_C$（浅灰色/半透明虚线）；
  - 点位：基准点 $A, B, C$，边上点 $A_1, B_1, C_1$，对称点 $A_3, B_3, C_3$，外接圆交点 $A_2, B_2, C_2$，密克点 $M$；
  - 连线：浅色虚线连接目标三角形 $\triangle A_2B_2C_2$ 与 $\triangle A_3B_3C_3$ 轮廓。

---

### Step 1: 聚焦交点 $A_2$：圆周角与第一组相似
- **标题**：① 圆周角定理与第一组相似 $\triangle B_1A_2C_1 \sim \triangle CA_2B$
- **讲解正文**：
  连接 $A_2A, A_2B_1, A_2C, A_2B, A_2C_1$。<br>
  在圆 $AB_1C_1A_2$ 与圆 $ABC$ 中，弦 $B_1C_1$ 与弦 $BC$ 所对圆周角满足：<br>
  $$\angle C_1A_2B_1 = \angle BAC = \angle BA_2C$$
  同理，在两圆中由同弧圆周角转换可得：<br>
  $$\angle A_2B_1C_1 = \angle A_2AC_1 = \angle A_2CB$$
  两角对应相等，从而导出 <b>$\triangle B_1A_2C_1 \sim \triangle CA_2B$</b>。<br>
  由此得对应边成比例：<br>
  $$\frac{B_1A_2}{CA_2} = \frac{A_2C_1}{A_2B} = \frac{B_1C_1}{CB} \quad \text{①}$$
- **画面元素**：
  - 辅助线：连接 $A_2A, A_2B_1, A_2C, A_2B, A_2C_1$（品蓝/绿色辅助线）；
  - 角弧标记：标出 $\angle C_1A_2B_1$ 与 $\angle BA_2C$ 相等角弧，以及 $\angle A_2B_1C_1$ 与 $\angle A_2CB$ 相等角弧；
  - 面填充：半透明填充相似的 $\triangle B_1A_2C_1$ 和 $\triangle CA_2B$。

---

### Step 2: 托勒密定理与中点对称线段转化
- **标题**：② 托勒密定理与中点对称线段转化
- **讲解正文**：
  在圆内接四边形 $AB_1C_1A_2$ 中应用托勒密定理：<br>
  $$AA_2 \cdot B_1C_1 = B_1A_2 \cdot AC_1 - A_2C_1 \cdot AB_1$$
  在圆内接四边形 $ACBA_2$ 中同理有：<br>
  $$AA_2 \cdot BC = A_2C \cdot AB - A_2B \cdot AC$$
  结合 ① 中的比例式两式相除消去 $AA_2$，化简得：<br>
  $$\frac{A_2C}{A_2B} = \frac{AC - AB_1}{AB - AC_1} = \frac{CB_1}{BC_1}$$
  根据中点对称定义，$B_3$ 是 $B_1$ 关于 $CA$ 中点的对称点，故 $CB_1 = AB_3$；$C_3$ 是 $C_1$ 关于 $AB$ 中点的对称点，故 $BC_1 = AC_3$。<br>
  因此直接导出：<b>$\frac{A_2C}{A_2B} = \frac{AB_3}{AC_3}$</b>。
- **画面元素**：
  - 辅助面：高亮圆内接四边形 $AB_1C_1A_2$ 与 $ACBA_2$；
  - 线段高亮：高亮边上线段 $CB_1$ 与 $AB_3$（等长记号），$BC_1$ 与 $AC_3$（等长记号）；
  - 辅助点：显式标出 $AC$ 中点与 $AB$ 中点，突出对称性。

---

### Step 3: 两边夹角判定相似 $\triangle BA_2C \sim \triangle C_3AB_3$
- **标题**：③ 两边夹角判定相似 $\triangle BA_2C \sim \triangle C_3AB_3$
- **讲解正文**：
  在 $\triangle BA_2C$ 与 $\triangle C_3AB_3$ 中：<br>
  两组对应边成比例：$\frac{A_2C}{A_2B} = \frac{AB_3}{AC_3} \iff \frac{A_2C}{AB_3} = \frac{A_2B}{AC_3}$；<br>
  夹角相等：$\angle CA_2B = \angle BAC = \angle B_3AC_3$。<br>
  由两边成比例且夹角相等，判定 <b>$\triangle BA_2C \sim \triangle C_3AB_3$</b>！<br>
  从而导出关键对应角相等：<b>$\angle A_2CB = \angle AB_3C_3$</b>。<br>
  完全同理，对点 $B_2$ 对称推导可得：<b>$\angle B_2CA = \angle BA_3C_3$</b>。
- **画面元素**：
  - 相似三角形高亮：半透明多边形填充 $\triangle BA_2C$（紫色）与 $\triangle C_3AB_3$（青绿）；
  - 对应夹角弧：$\angle CA_2B$ 与 $\angle B_3AC_3$；
  - 导出底角弧：高亮相等角 $\angle A_2CB$ 与 $\angle AB_3C_3$（红色双弧），以及 $\angle B_2CA$ 与 $\angle BA_3C_3$（橙色双弧）。

---

### Step 4: 圆心角与圆周角转换锁定顶点角相等
- **标题**：④ 圆心角与圆周角转换锁定顶点角相等
- **讲解正文**：
  在圆 $O$ 中，圆心角关系满足：<br>
  $$\angle A_2OB_2 = \angle A_2OB + \angle B_2OA - \angle AOB$$
  对应的圆周角则为：<br>
  $$\angle A_2C_2B_2 = \frac{1}{2}\angle A_2OB_2 = \angle A_2CB + \angle B_2CA - \angle ACB$$
  代入步骤 3 导出的角：<br>
  $$\begin{aligned}
  \angle A_2C_2B_2 &= \angle AB_3C_3 + \angle BA_3C_3 + (\angle BAC + \angle ABC - 180^\circ) \\
  &= 180^\circ - \angle AC_3B_3 - \angle BC_3A_3 = \mathbf{\angle A_3C_3B_3}
  \end{aligned}$$
  成功证明：<b>$\angle A_2C_2B_2 = \angle A_3C_3B_3$</b>。
- **画面元素**：
  - 辅助连线：连线 $C_2A_2, C_2B_2$ 与 $C_3A_3, C_3B_3$；
  - 角弧聚焦：高亮 $\angle A_2C_2B_2$（品红大弧）与 $\angle A_3C_3B_3$（品红大弧）；
  - 背景淡化：淡化其余无关辅助线，突出两角严格一致的几何直观。

---

### Step 5: 轮换对称性得证 $\triangle A_2B_2C_2 \sim \triangle A_3B_3C_3$
- **标题**：⑤ 轮换对称性得证 $\triangle A_2B_2C_2 \sim \triangle A_3B_3C_3$
- **讲解正文**：
  由几何构型的完全轮换对称性，同理可推导其余两对顶点角对应相等：<br>
  $$\angle B_2A_2C_2 = \angle B_3A_3C_3, \quad \angle C_2B_2A_2 = \angle C_3B_3A_3$$
  两个三角形的三组内角均对应相等，从而最终得出结论：<br>
  <div style="text-align:center;font-size:16px;font-weight:700;color:#2563eb;margin-top:8px;">
    $\triangle A_2B_2C_2 \sim \triangle A_3B_3C_3$
  </div>
  原命题得证！
- **画面元素**：
  - 擦除全部干扰线；
  - 目标高亮：$\triangle A_2B_2C_2$（亮橙色轮廓加浅填充）与 $\triangle A_3B_3C_3$（靛蓝色轮廓加浅填充）；
  - 角弧对照：在 $A_2/A_3$、$B_2/B_3$、$C_2/C_3$ 处分别以相同颜色成对绘制三组角弧；
  - 最终完整呈现两个相似三角形的典雅几何构型。
