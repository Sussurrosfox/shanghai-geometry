# 例 7：外切四边形的反演与对角线中点距离之比

## 题目背景与结论
设凸四边形 $ABCD$ 外切于圆 $O$，已知各顶点到内切圆心 $O$ 的距离为：
$$OA = 5, \quad OB = 6, \quad OC = 7, \quad OD = 8$$
设对角线 $AC, BD$ 的中点分别为 $M, N$。求 $\frac{OM}{ON}$ 的值。
**核心结论**：$\frac{OM}{ON} = \frac{OA \cdot OC}{OB \cdot OD} = \frac{5 \times 7}{6 \times 8} = \frac{35}{48}$。

---

## 颜色约定
- **基准图形**：四边形 $ABCD$ 为深青灰色（`#334155`），内切圆 $O$ 为浅灰蓝实线（`#64748b`），对角线 $AC, BD$ 为浅虚线。
- **切点与切点四边形**：切点 $E, F, G, H$ 为翠绿色（`#059669`），切点弦及对角线 $EG, HF$ 为绿色虚线。
- **反演平行四边形**：反演点 $A', B', C', D'$ 为紫蓝色（`#7c3aed`），平行四边形 $A'B'C'D'$ 及对角线 $A'C', B'D'$ 为紫色实线。
- **核心待求线段与关键中点**：
  - 中点 $M, N$ 为深蓝色（`#2563eb`），交点 $S$ 为洋红色（`#d946ef`）。
  - $OM$ 高亮为珊瑚红（`#dc2626`），$ON$ 高亮为宝蓝（`#2563eb`），$OS$ 为紫色（`#7c3aed`）。
- **相似三角形对应区域**：
  - $\triangle B'OD'$ 与 $\triangle DOB$ 用琥珀金（`#d97706`）半透明高亮填充。
  - $\triangle A'OC'$ 与 $\triangle COA$ 用翡翠绿（`#059669`）半透明高亮填充。

---

## 分步演示规划

### Step 0: 已知条件与几何构形
- **标题**：0. 外切四边形已知条件与待求线段
- **正文**：
  设凸四边形 $ABCD$ 外切于圆 $O$，四边 $AB, BC, CD, DA$ 与圆 $O$ 分别切于点 $E, F, G, H$。<br>
  已知各顶点到圆心 $O$ 的距离为：
  $$OA = 5, \quad OB = 6, \quad OC = 7, \quad OD = 8$$
  连接对角线 $AC$ 与 $BD$，记它们的中点分别为 $M$ 与 $N$。<br>
  目标：利用圆的外切性质与反演变换，求解线段长度之比 $\frac{OM}{ON}$ 的精确值。
- **画面**：
  - 绘制圆 $O$ 及圆心 $O$。
  - 绘制凸四边形 $ABCD$、对角线 $AC, BD$（深灰色）。
  - 标出对角线中点 $M$（$AC$ 中点）、$N$（$BD$ 中点）。
  - 连接并高亮线段 $OM$（红色）与 $ON$（蓝色）。
  - 连线 $OA, OB, OC, OD$（灰蓝色细线），标出长度 $5, 6, 7, 8$。

---

### Step 1: 构造以 O 为中心、半径 r 的反演变换
- **标题**：1. 建立以 O 为中心、半径 r 的反演变换
- **正文**：
  设圆 $O$ 的半径为 $r$。以 $O$ 为反演中心、圆 $O$ 为基圆（反演幂为 $r^2$）作反演变换。<br>
  设顶点 $A, B, C, D$ 在该反演下的对应点分别为 $A', B', C', D'$。<br>
  由反演变换的定义，反演点落在相应的射线 $OA, OB, OC, OD$ 上，且满足：
  $$OA \cdot OA' = r^2, \quad OB \cdot OB' = r^2, \quad OC \cdot OC' = r^2, \quad OD \cdot OD' = r^2$$
  因为各顶点均在圆外（$OA, OB, OC, OD > r$），故反演点 $A', B', C', D'$ 全部落在圆 $O$ 内部。
- **画面**：
  - 沿射线 $OA, OB, OC, OD$ 标出反演点 $A', B', C', D'$（紫色圆点）。
  - 标出切点 $E, F, G, H$（绿色圆点）。
  - 绘制切点弦 $HE, EF, FG, GH$（虚线），显示 $OA \perp HE, OB \perp EF$ 等垂直关系。

---

### Step 2: 证明 A'B'C'D' 为切点中位线平行四边形
- **标题**：2. 证明 A'B'C'D' 为切点中位线平行四边形
- **正文**：
  考察切线三角形：切线 $AE, AH$ 切圆 $O$ 于 $E, H$。由对称性，$OA \perp HE$ 且 $OA$ 平分弦 $HE$。<br>
  在直角三角形 $\text{Rt}\triangle OEA$ 中，$\angle OEA = 90^\circ$，$OA'$ 为斜边 $OA$ 上的射影。由射影定理：
  $$OE^2 = OA \cdot OA' \implies OA \cdot OA' = r^2$$
  这说明反演点 $A'$ 恰好是 $O$ 在弦 $HE$ 上的垂足，即 **$A'$ 恰为弦 $HE$ 的中点**！<br>
  同理，$B', C', D'$ 分别为切点弦 $EF, FG, GH$ 的中点。<br>
  在圆内接四边形 $EFGH$ 中，顺次连接各边中点 $A', B', C', D'$，由瓦里尼翁（Varignon）定理：
  $$A'B' \parallel \frac{1}{2}HF \parallel C'D', \quad A'D' \parallel \frac{1}{2}EG \parallel B'C'$$
  因此，$A'B'C'D'$ 必为**平行四边形**！其对角线 $A'C'$ 与 $B'D'$ 互相平分于交点 $S$。
- **画面**：
  - 连线 $EG$ 与 $HF$（浅绿色虚线）。
  - 绘制平行四边形 $A'B'C'D'$（紫色实线，加粗），高亮四边平行与等长。
  - 绘制对角线 $A'C'$ 与 $B'D'$（紫色虚线），交于中心点 $S$。
  - 标出交点 $S$，并在 $B'S, SD'$ 及 $A'S, SC'$ 上显示平分等长标记。

---

### Step 3: 由反演性质导出中线比 ON/OS
- **标题**：3. 反演相似 △B'OD' ~ △DOB 导出中线比 ON/OS
- **正文**：
  考察 $\triangle B'OD'$ 与 $\triangle DOB$：<br>
  它们共用顶角 $\angle B'OD' = \angle DOB$。由反演定义 $OB \cdot OB' = r^2 = OD \cdot OD'$，得：
  $$\frac{OB'}{OD} = \frac{OD'}{OB} = \frac{r^2}{OB \cdot OD}$$
  两边对应成比例且夹角相等，故 **$\triangle B'OD' \sim \triangle DOB$**（反向相似：$B' \leftrightarrow D, D' \leftrightarrow B$）。<br>
  因为 $S$ 是边 $B'D'$ 的中点，而 $N$ 是边 $DB$ 的中点，所以线段 $OS$ 与 $ON$ 分别是这两个相似三角形的**对应中线**！<br>
  相似三角形的对应中线之比等于相似比，由此立得：
  $$\frac{ON}{OS} = \frac{OB}{OD'} = \frac{OB}{\frac{r^2}{OD}} = \frac{OB \cdot OD}{r^2}$$
- **画面**：
  - 琥珀金色半透明填充高亮 $\triangle B'OD'$ 与 $\triangle DOB$。
  - 高亮中线 $ON$（蓝色实线）与中线 $OS$（紫色实线）。
  - 动态显示比例推导卡片 $\frac{ON}{OS} = \frac{OB \cdot OD}{r^2}$。

---

### Step 4: 同理在对角方向导出中线比 OM/OS
- **标题**：4. 反演相似 △A'OC' ~ △COA 导出中线比 OM/OS
- **正文**：
  完全同理，考察另一对反演点形成的三角形 $\triangle A'OC'$ 与 $\triangle COA$：<br>
  由于 $OA \cdot OA' = r^2 = OC \cdot OC'$ 且 $\angle A'OC' = \angle AOC$，有：
  $$\frac{OA'}{OC} = \frac{OC'}{OA} = \frac{r^2}{OA \cdot OC} \implies \triangle A'OC' \sim \triangle COA$$
  顶点反向对应（$A' \leftrightarrow C, C' \leftrightarrow A$）。<br>
  因为平行四边形的对角线互相平分，$S$ 同样是对角线 $A'C'$ 的中点！而 $M$ 为线段 $AC$ 的中点。<br>
  因此 $OS$ 与 $OM$ 分别是这两个相似三角形的**对应中线**，相似比给出：
  $$\frac{OM}{OS} = \frac{OA}{OC'} = \frac{OA}{\frac{r^2}{OC}} = \frac{OA \cdot OC}{r^2}$$
- **画面**：
  - 翠绿色半透明填充高亮 $\triangle A'OC'$ 与 $\triangle COA$。
  - 高亮中线 $OM$（红色实线）与中线 $OS$（紫色实线）。
  - 动态显示比例推导卡片 $\frac{OM}{OS} = \frac{OA \cdot OC}{r^2}$。

---

### Step 5: 两式相比消去参量，得出最终结论
- **标题**：5. 两式相比消去 OS 与 r²，求得 OM/ON = 35/48
- **正文**：
  综合 Step 3 与 Step 4 的中线比例关系式：
  $$\frac{OM}{OS} = \frac{OA \cdot OC}{r^2}, \qquad \frac{ON}{OS} = \frac{OB \cdot OD}{r^2}$$
  将两式直接相比，未知的公共中线长度 $OS$ 与反演半径平方 $r^2$ **完全消去**：
  $$\frac{OM}{ON} = \frac{\frac{OM}{OS}}{\frac{ON}{OS}} = \frac{\frac{OA \cdot OC}{r^2}}{\frac{OB \cdot OD}{r^2}} = \frac{OA \cdot OC}{OB \cdot OD}$$
  代入题目给定的已知距离 $OA = 5, OB = 6, OC = 7, OD = 8$：
  $$\frac{OM}{ON} = \frac{5 \times 7}{6 \times 8} = \frac{35}{48}$$
  这揭示了一个优美的不变量：**外切四边形对角线中点到内心的距离之比，严格等于对应对角顶点到内心距离之积的比值**！
- **画面**：
  - 重点高亮 $OM$（红色光晕加粗）与 $ON$（蓝色光晕加粗）。
  - 显现对角线 $AC$（红色细线）与 $BD$（蓝色细线）。
  - 显现金色结果框，突出展示 $\frac{OM}{ON} = \frac{35}{48}$。
