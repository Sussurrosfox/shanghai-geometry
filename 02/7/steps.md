# 例 6 分步证明演示规划 (steps.md)

## 题目描述
设 $\triangle ABC$ 的外接圆为圆 $O$ ，且 $I$ ， $J$ 分别是 $\triangle ABC$ 的内心和 $A$-旁心， $AJ$ 交圆 $O$ 于点 $U$ ，点 $D$ 在 $BC$ 上且满足 $DA = DJ$ ， $AD$ 交圆 $O$ 于点 $K$ ， $M$ 是 $BC$ 的中点， $IM$ 交 $UK$ 于点 $N$ . 证明: $MI = MN$ .

---

## 颜色约定
- 基础几何元素（三角形边、外接圆）：深灰色 `#334155` / `#94a3b8`
- 关键角平分线与内心、旁心体系：蓝色 `BLUE = #2563eb`
- 对称构造与外心圆体系（点 $A'$、点 $D$）：绿色 `GREEN = #059669`
- 垂径体系与对称点 $U'$、相似三角形：紫色 `PURPLE = #7c3aed`
- 平行线关系（$UN \parallel U'I$）：青色 `CYAN = #0891b2`
- 待证目标与全等三角形（$\triangle MUN \cong \triangle MU'I$、$MI = MN$）：红色 `RED = #dc2626` / 橙色 `ORANGE = #ea580c`

---

## 步骤规划

### Step 0: 几何构型与已知条件
- **标题**：构型引入：外接圆、内心、旁心与已知条件
- **正文**：
  给定 $\triangle ABC$ 与其外接圆 $O$。
  $I$ 为 $\triangle ABC$ 的内心，$J$ 为 $A$-旁心，内角平分线 $AJ$ 交圆 $O$ 于点 $U$（劣弧 $\overset{\frown}{BC}$ 中点）。
  $M$ 是 $BC$ 的中点，$U, M, O$ 三点共线且垂直于 $BC$。
  点 $D$ 在边 $BC$ 上，满足 $DA = DJ$；直线 $AD$ 交圆 $O$ 于点 $K$。
  连接 $IM$ 与 $UK$，两线交于点 $N$。
  **求证**：$MI = MN$。
- **画面图元**：
  - 基础线段：$\triangle ABC$ 边（$AB, BC, CA$），外接圆 $O$；
  - 关键线段：角平分线 $AJ$（贯穿 $A, I, U, J$）、直径延长线 $UV$；
  - 辅助连线：线段 $ADK$、线段 $IMN$、$UK$、线段 $BC$ 中点垂径 $OU$；
  - 显示点：$A, B, C, O, I, J, U, M, D, K, N$。

### Step 1: 对称点 $A'$ 与相似 $\triangle AIO \sim \triangle AA'J$
- **标题**：步骤一：取对称点 $A'$，导出相似 $\triangle AIO \sim \triangle AA'J$
- **正文**：
  作点 $A$ 关于边 $BC$ 的对称点 $A'$。
  由圆周角定理，$\angle AOB = 2\angle ACB = \angle ACA'$，且在直角三角形中易得 $\angle BAO = 90^\circ - \angle ACB = \angle A'AC$。
  因此 $\triangle AOB \sim \triangle ACA'$，得 $\frac{AO}{AB} = \frac{AC}{AA'}$，即：
  $$AO \cdot AA' = AB \cdot AC \quad \text{①}$$
  又根据内心与旁心的经典相似性质，$\triangle AIB \sim \triangle ACJ$，得 $\frac{AI}{AB} = \frac{AC}{AJ}$，即：
  $$AI \cdot AJ = AB \cdot AC \quad \text{②}$$
  由 ① 与 ② 得 $AO \cdot AA' = AI \cdot AJ \iff \frac{AO}{AJ} = \frac{AI}{AA'}$。
  结合夹角 $\angle OAI = \angle JAA' = \frac{|B-C|}{2}$，可判定：
  $$\triangle AIO \sim \triangle AA'J \implies \angle AIO = \angle AA'J$$
- **画面图元**：
  - 高亮/虚线：对称垂线 $AA'$（虚线垂直于 $BC$），连线 $A'J, A'C$；
  - 高亮三角形：$\triangle AIO$（蓝色半透明填充）与 $\triangle AA'J$（绿色半透明填充）；
  - 角弧标记：标出 $\angle OAI$ 与 $\angle JAA'$ 对应角相等；
  - 显示点：新增点 $A'$。

### Step 2: 点 $D$ 转化为 $\triangle AA'J$ 外心与角转移
- **标题**：步骤二：点 $D$ 转化为 $\triangle AA'J$ 外心，建立关键角关系
- **正文**：
  因为点 $A'$ 是 $A$ 关于 $BC$ 的对称点，所以直线 $BC$ 即为线段 $AA'$ 的垂直平分线。
  点 $D$ 在直线 $BC$ 上，必有 $DA = DA'$；
  结合题目已知条件 $DA = DJ$，得到：
  $$DA = DA' = DJ$$
  这表明点 $D$ 到 $\triangle AA'J$ 三顶点等距，故 **$D$ 是 $\triangle AA'J$ 的外心**！
  由外心连线角性质（或圆周角性质），在等腰 $\triangle DAJ$ 中，底角 $\angle DAJ = 90^\circ - \angle AA'J$。
  设 $UV$ 为圆 $O$ 经过 $U$ 的直径，连接 $VA$，则 $\angle VAU = 90^\circ$。
  由圆内接四边形 $VAUK$ 对角互补，得：
  $$\angle VUK = 180^\circ - \angle VAK = 180^\circ - (90^\circ + \angle DAJ) = 90^\circ - \angle DAJ = \angle AA'J$$
  结合步骤一中 $\angle AA'J = \angle AIO$，且 $A, I, U$ 共线（即 $\angle AIO + \angle OIU = 180^\circ$），得到：
  $$\angle VUK + \angle OIU = 180^\circ$$
- **画面图元**：
  - 辅助圆：以 $D$ 为圆心、$DA$ 为半径的外接圆 $\odot D$（浅绿色虚线，过 $A, A', J$）；
  - 等长标记：线段 $DA, DJ, DA'$ 上的等长刻度；
  - 辅助连线：直径连线 $VA$（直角标记 $\angle VAU = 90^\circ$）；
  - 对应角弧：高亮角 $\angle VUK$ 与角 $\angle AIO$（二者相等且与 $\angle OIU$ 互补）；
  - 显示点：新增点 $V$。

### Step 3: 鸡爪定理与对称点 $U'$ 导出相似 $\triangle UIO \sim \triangle UU'I$
- **标题**：步骤三：鸡爪定理与对称点 $U'$，导出相似 $\triangle UIO \sim \triangle UU'I$
- **正文**：
  取点 $U$ 关于边 $BC$ 的对称点 $U'$。
  由鸡爪定理，弧中点 $U$ 到内心 $I$ 的距离满足 $UI = 2R \sin \frac{A}{2}$。
  又垂径中 $M$ 到弧中点 $U$ 的距离为 $UM = R(1 - \cos A) = 2R \sin^2 \frac{A}{2}$。
  由对称性可知 $UU' = 2UM = 4R \sin^2 \frac{A}{2}$。
  由此建立精确的度量恒等式：
  $$UI^2 = \left(2R \sin \frac{A}{2}\right)^2 = 4R^2 \sin^2 \frac{A}{2} = R \cdot \left(4R \sin^2 \frac{A}{2}\right) = UO \cdot UU'$$
  即 $\frac{UI}{UU'} = \frac{UO}{UI}$。
  又两三角形具有公共角 $\angle OUI = \angle IUU'$，故由边角判定法可得：
  $$\triangle UIO \sim \triangle UU'I \implies \angle UU'I = \angle UIO$$
- **画面图元**：
  - 对称垂线：$UU'$ 沿垂直平分线分布，标注 $M$ 为 $UU'$ 中点；
  - 辅助线：连接 $U'I$ 与 $UI$；
  - 高亮三角形：$\triangle UIO$ 与 $\triangle UU'I$（双色半透明高亮展示公共角与成比例边）；
  - 角弧标记：标出对应角 $\angle UU'I$ 与 $\angle UIO$ 相等；
  - 显示点：新增点 $U'$。

### Step 4: 同旁内角互补导出平行线 $UN \parallel U'I$
- **标题**：步骤四：综合角关系，导出关键平行线 $UN \parallel U'I$
- **正文**：
  在步骤二中已推导：$\angle VUK + \angle OIU = 180^\circ$；
  在步骤三中已推导：$\angle UU'I = \angle UIO$。
  将两式联立代换，即可直接得出：
  $$\angle VUK + \angle UU'I = 180^\circ$$
  注意点 $V, U', M, U$ 均共线于直径 $UV$ 上，射线 $UV$ 即为该直线的正向。
  直线 $UK$（即直线 $UN$）与直线 $U'I$ 被截线 $UV$ 所截：
  其同旁内角 $\angle VUK$ 与 $\angle UU'I$ 严格互补（和为 $180^\circ$）！
  根据平行线判定公理（同旁内角互补，两直线平行），立即得出：
  $$UN \parallel U'I$$
- **画面图元**：
  - 高亮平行线：高亮直线 $UN$（即 $UK$）与线段 $U'I$（青色高亮）；
  - 平行标记：在 $UN$ 与 $U'I$ 上添加平行双箭头标记；
  - 角弧高亮：同时标出截线 $UV$ 两侧互补的角 $\angle VUK$ 与 $\angle UU'I$。

### Step 5: 全等三角形推得最终结论 $MI = MN$
- **标题**：步骤五：中点截线与全等，推得最终结论 $MI = MN$
- **正文**：
  考虑直线 $IMN$ 截平行线 $UN \parallel U'I$ 与垂直轴 $UU'$ 所构成的图形：
  1. 点 $M$ 为线段 $UU'$ 的中点，即 $MU = MU'$；
  2. 直线 $UN \parallel U'I$ 被截线 $UU'$ 所截，内错角相等：$\angle MUN = \angle MU'I$；
  3. 直线 $IN$ 与 $UU'$ 相交于点 $M$，对顶角相等：$\angle UMN = \angle U'MI$。
  由角边角公理（ASA），可判定两三角形全等：
  $$\triangle MUN \cong \triangle MU'I$$
  由此直接得出对应边相等：
  $$MI = MN$$
  至此，命题获证！
- **画面图元**：
  - 高亮全等三角形：$\triangle MUN$ 与 $\triangle MU'I$（双色半透明填充）；
  - 核心等长线段：高亮线段 $MI$ 与线段 $MN$（红色加粗发光）；
  - 等长刻度标记：在 $MI$ 与 $MN$ 上标出双红色等长标记；
  - 中点标记：在 $MU$ 与 $MU'$ 上标出单等长标记。
