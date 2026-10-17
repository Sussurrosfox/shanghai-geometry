# 题目 04/3（例 2）分步证明与可视化规划

## 命题内容
设 $\Gamma$ 是 $\triangle ABC$ 的外接圆，圆 $\Gamma$ 在 $B, C$ 两点的切线交于 $T$。过 $A$ 且垂直于 $AT$ 的直线与直线 $BC$ 交于 $S$，点 $B_1, C_1$ 在直线 $ST$ 上（$B_1, B$ 在 $BC$ 的垂直平分线的同侧），且 $TB_1 = TC_1 = TB$。
证明：$\triangle AB_1C_1 \sim \triangle ABC$。

---

## 演示步骤规划

### Step 0：已知条件与几何配置
- **标题**：✦ 题设几何构型
- **数学逻辑**：
  给定 $\triangle ABC$ 及其外接圆 $\Gamma$；切线 $TB, TC$ 交于点 $T$；$M$ 为 $BC$ 中点；连接 $AT$；过 $A$ 作 $AS \perp AT$ 交直线 $BC$ 于点 $S$；在割线 $ST$ 上取 $TB_1 = TC_1 = TB$（其中 $B_1, B$ 位于中垂线同侧）。
- **画面图元**：
  - 基础图元：$\triangle ABC$ 外接圆 $\Gamma$、切线 $TB, TC$、直线 $BC$ 及其延长线、线段 $AS$（垂直符号）、直线 $ST$ 及线段 $B_1C_1$。
  - 点：$A, B, C, T, S, M, B_1, C_1$ 及外心 $O$。
- **色彩规划**：
  外接圆与基准线为墨灰 `#475569`，点采用深蓝 `#1e293b`，高亮关键线段。

---

### Step 1：中线与陪位中线的等角性质
- **标题**：① 陪位中线性质 $\angle BAT = \angle MAC$
- **数学逻辑**：
  连接中线 $AM$。因为 $T$ 为外接圆在 $B, C$ 处的切线交点，由陪位中线基本定理，直线 $AT$ 是 $\triangle ABC$ 的 $A$-陪位中线，即 $AM$ 与 $AT$ 关于 $\angle BAC$ 的平分线轴对称。因此：
  $$\angle BAT = \angle MAC$$
- **画面图元**：
  - 新增中线 $AM$（翠绿色虚线 `#059669`）、陪位中线 $AT$（宝石蓝虚线 `#2563eb`）。
  - 角弧标记：在 $\angle BAT$ 与 $\angle MAC$ 处标出同色等角弧（橙色 `#ea580c`）。
- **色彩规划**：
  $AM$ 绿、$AT$ 蓝、角弧橙色。

---

### Step 2：弦切角转化与正弦定理建立边比
- **标题**：② 正弦定理导出边比 $\frac{TC_1}{AT} = \frac{MC}{AM}$
- **数学逻辑**：
  由弦切角定理知 $\angle TBC = \angle BAC$，因此：
  $$\angle TBA = \angle TBC + \angle CBA = \angle BAC + \angle CBA = 180^\circ - \angle ACB$$
  在 $\triangle TAB$ 和 $\triangle AMC$ 中分别运用正弦定理：
  $$\frac{TB}{AT} = \frac{\sin \angle BAT}{\sin \angle TBA} = \frac{\sin \angle MAC}{\sin(180^\circ - \angle ACB)} = \frac{\sin \angle MAC}{\sin \angle ACB} = \frac{MC}{AM}$$
  又题设 $TC_1 = TB$，代入即得：
  $$\frac{TC_1}{AT} = \frac{MC}{AM} \quad \left(\text{即 } \frac{TC_1}{MC} = \frac{AT}{AM}\right)$$
- **画面图元**：
  - 高亮线段 $TB, AT, MC, AM$ 以及 $TC_1$。
  - 等长标记刻度：在 $TB$ 与 $TC_1$ 上加双刻度线。
  - 标记补角 $\angle TBA$ 与 $\angle ACB$。
- **色彩规划**：
  对比高亮线段采用洋紫 `#7c3aed` 与群青 `#2563eb`。

---

### Step 3：直角对顶与四点共圆（$A, M, T, S$）
- **标题**：③ 四点共圆得 $\angle C_1TA = \angle CMA$
- **数学逻辑**：
  因为 $TB = TC$ 且 $M$ 为 $BC$ 中点，故 $TM \perp BC$，即 $\angle TMS = 90^\circ$；
  又由已知过 $A$ 作 $AS \perp AT$，即 $\angle TAS = 90^\circ$。
  在四边形 $AMTS$ 中，对角 $\angle TMS = \angle TAS = 90^\circ$。
  因此，$A, M, T, S$ 四点共圆（以线段 $ST$ 为直径）。
  由同弧所对圆周角相等，立即得出：
  $$\angle STA = \angle SMA \implies \angle C_1TA = \angle CMA$$
- **画面图元**：
  - 直角标记：顶点 $M$ 处（边指向 $T$ 与 $S$）与顶点 $A$ 处（边指向 $T$ 与 $S$）绘制鲜红直角折线 `#dc2626`。
  - 辅助圆：以 $ST$ 为直径的圆（浅紫虚线 `#a855f7`）。
  - 等角弧：标记 $\angle C_1TA$ 与 $\angle CMA$（金黄色 `#d97706`）。
- **色彩规划**：
  直角红色、辅助圆浅紫、等角金黄。

---

### Step 4：局部三角形相似 $\triangle ATC_1 \sim \triangle AMC$
- **标题**：④ 侧翼相似 $\triangle ATC_1 \sim \triangle AMC$
- **数学逻辑**：
  在 $\triangle ATC_1$ 与 $\triangle AMC$ 中：
  ① 夹边对应成比例：$\frac{TC_1}{AT} = \frac{MC}{AM}$（由 Step 2）；
  ② 夹角对应相等：$\angle C_1TA = \angle CMA$（由 Step 3）。
  根据两边成比例且夹角相等的相似判定定理（SAS）：
  $$\triangle ATC_1 \sim \triangle AMC$$
  由此得出对应边比与对应角：
  $$\frac{AC_1}{AC} = \frac{AT}{AM}, \quad \angle TAC_1 = \angle MAC$$
- **画面图元**：
  - 区域半透明高亮：$\triangle ATC_1$ 填充天蓝 `rgba(37,99,235,0.18)`；$\triangle AMC$ 填充翠绿 `rgba(5,150,105,0.18)`。
  - 高亮对应边 $AC_1$ 与 $AC$。
- **色彩规划**：
  蓝绿双色面域对比。

---

### Step 5：对称性推导与全角合成
- **标题**：⑤ 对称推导 $\triangle AB_1T \sim \triangle ABM$ 与顶角合成
- **数学逻辑**：
  同理，在另一侧：因为 $TB_1 = TB$ 且 $MB = MC$，由完全对称的推导可得：
  $$\triangle AB_1T \sim \triangle ABM$$
  由此得出：
  $$\frac{AB_1}{AB} = \frac{AT}{AM}, \quad \angle B_1AT = \angle BAM$$
  将角相加，得到顶角相等：
  $$\angle B_1AC_1 = \angle B_1AT + \angle TAC_1 = \angle BAM + \angle MAC = \angle BAC$$
  同时对应边成比例：
  $$\frac{AB_1}{AB} = \frac{AC_1}{AC} = \frac{AT}{AM}$$
- **画面图元**：
  - 高亮 $\triangle AB_1T$ 与 $\triangle ABM$ 的对应轮廓。
  - 绘制大角弧：在 $\angle B_1AC_1$ 与 $\angle BAC$ 处绘制醒目同心双角弧（紫红 `#c026d3`）。
  - 高亮线段 $AB_1, AC_1, AB, AC$。
- **色彩规划**：
  紫色与橙色体现对称推导，紫红色双弧标记大角相等。

---

### Step 6：得出最终结论 $\triangle AB_1C_1 \sim \triangle ABC$
- **标题**：✦ 最终结论 $\triangle AB_1C_1 \backsim \triangle ABC$
- **数学逻辑**：
  在 $\triangle AB_1C_1$ 与 $\triangle ABC$ 中：
  ① 顶角相等：$\angle B_1AC_1 = \angle BAC$；
  ② 夹边对应成比例：$\frac{AB_1}{AB} = \frac{AC_1}{AC}$。
  根据两边成比例且夹角相等的相似三角形判定定理，立即得出：
  $$\triangle AB_1C_1 \backsim \triangle ABC$$
  原命题获证！
- **画面图元**：
  - 整体高亮目标三角形 $\triangle AB_1C_1$（深橙红描边 `#ea580c`，半透明橙色填充）与原三角形 $\triangle ABC$（宝石蓝描边 `#2563eb`，半透明蓝色填充）。
  - 擦除所有临时辅助线与局部色块，画面纯净，形成强烈的全局相似对比！
- **色彩规划**：
  橙红与宝石蓝高饱和对比，视觉焦点高度聚焦于最终命题结论。
