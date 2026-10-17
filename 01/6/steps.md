# 例 5：凸五边形中的三线共点证明分步规划

## 命题内容
已知凸五边形 $ABCDE$ 满足 $AB = BC = CD$，$ \angle EAB = \angle BCD$，$ \angle EDC = \angle CBA$。
证明：过点 $E$ 作 $BC$ 的垂线与 $AC, BD$ 三线共点。

---

## 分步演示总览（共 6 步，Step 0 ~ Step 5）

### Step 0: 题设条件与基础多边形
- **标题**：✦ 题设条件与凸五边形
- **正文**：
  已知凸五边形 $ABCDE$ 满足三边相等：$AB = BC = CD$；
  且对角分别对应相等：$\angle EAB = \angle BCD$，$\angle EDC = \angle CBA$。
  求证：过点 $E$ 作 $BC$ 的垂线与对角线 $AC, BD$ 三线共点。
- **画面图元**：
  - 凸五边形 $ABCDE$（实线轮廓）
  - 等长刻度标记：在边 $AB, BC, CD$ 上标注醒目的双红刻度线
  - 对应角弧标记：在 $\angle EAB$ 与 $\angle BCD$ 处绘制紫色双角弧表示相等；在 $\angle EDC$ 与 $\angle CBA$ 处绘制橙色单角弧表示相等
  - 顶点标签：$A, B, C, D, E$

---

### Step 1: 构造中垂线定点 $I$ 与对角线交点 $H$
- **标题**：① 作中垂线定点 $I$ 与对角线交点 $H$
- **正文**：
  连结对角线 $AC$ 与 $BD$。
  因为 $BA = BC$，由等腰三角形性质，点 $B$ 在 $AC$ 的中垂线上；同理 $CB = CD$，点 $C$ 在 $BD$ 的中垂线上。
  设线段 $AC$ 与 $BD$ 的中垂线交于点 $I$。
  此时中垂线 $BI \perp AC$ 且 $CI \perp BD$。
  设对角线 $AC$ 与 $BD$ 相交于点 $H$。
- **画面图元**：
  - 新增对角线 $AC, BD$（蓝色实线）
  - 新增中垂线 $BI, CI$（绿色虚线/实线射线）
  - 新增交点 $I$（翠绿色圆点）与对角线交点 $H$（深蓝色圆点）
  - 新增直角标记：在 $BI \perp AC$ 以及 $CI \perp BD$ 的交点处标注红色直角符号

---

### Step 2: 垂心性质推导 $IH \perp BC$
- **标题**：② $H$ 为 $\triangle BIC$ 的垂心 $\implies IH \bot BC$
- **正文**：
  在 $\triangle BIC$ 中考察：
  对角线 $AC$ 经过顶点 $C$，且 $AC \perp BI$，因此直线 $AC$ 是边 $BI$ 上的高；
  对角线 $BD$ 经过顶点 $B$，且 $BD \perp CI$，因此直线 $BD$ 是边 $CI$ 上的高。
  对角线交点 $H$ 正是 $\triangle BIC$ 的两条高线的交点，即 **$H$ 为 $\triangle BIC$ 的垂心**！
  由垂心性质，第三条高线必过顶点 $I$ 且垂直于对边 $BC$，故 **$IH \perp BC$**。
- **画面图元**：
  - 高亮 $\triangle BIC$（半透明翠绿浅色填充）
  - 高亮两条高线 $CH$（在 $AC$ 上）与 $BH$（在 $BD$ 上）
  - 绘制连线 $IH$ 并向下延伸至边 $BC$ 的垂足 $K$（深红色高亮线）
  - 标注直角标记：在垂足 $K$ 处标注 $IK \perp BC$ 的直角符号
  - 突出显示垂心 $H$

---

### Step 3: 全等三角形与角平分线推导
- **标题**：③ 全等三角形 $\implies AI, DI$ 为内角平分线
- **正文**：
  连结 $IA, ID$。
  因为点 $I$ 在 $AC$ 的中垂线上，所以 $IA = IC$；同理 $I$ 在 $BD$ 的中垂线上，所以 $IB = ID$。
  又 $AB = BC = CD$ 且有公共边 $IB, IC$，由三边相等判定定理（SSS）：
  $$\triangle IAB \cong \triangle ICB \cong \triangle ICD$$
  由此可得：
  $\angle IAB = \angle ICB = \frac{1}{2}\angle BCD = \frac{1}{2}\angle EAB$，即 **$AI$ 平分 $\angle EAB$**；
  同理 $\angle IDC = \angle IBC = \frac{1}{2}\angle CBA = \frac{1}{2}\angle EDC$，即 **$DI$ 平分 $\angle EDC$**。
- **画面图元**：
  - 连结虚线 $IA, ID$
  - 用半透明色块分别高亮全等的三个三角形 $\triangle IAB, \triangle ICB, \triangle ICD$
  - 在顶点 $A$ 绘制分角弧线，表明 $\angle IAB = \angle IAE$
  - 在顶点 $D$ 绘制分角弧线，表明 $\angle IDC = \angle IDE$

---

### Step 4: 确立内切圆心并推导 $\angle BIE$
- **标题**：④ 点 $I$ 为内切圆心与 $\angle BIE$ 角度关系
- **正文**：
  由 $IB, IC, IA, ID$ 均为角平分线，可知点 $I$ 到五边形各边 $AB, BC, CD, DE, EA$ 距离均相等！
  因此，**点 $I$ 为凸五边形 $ABCDE$ 的内切圆圆心**，连线 $IE$ 平分 $\angle AED$。
  在四边形 $ABIE$ 中，内角和为 $360^\circ$：
  $$\angle BIE = 360^\circ - \angle EAB - \frac{1}{2}\angle ABC - \frac{1}{2}\angle AED$$
  由五边形内角和 $540^\circ$ 可得：
  $\frac{1}{2}\angle AED = 270^\circ - \angle EAB - \angle ABC$。
  代入化简即得：
  $$\angle BIE = 90^\circ + \frac{1}{2}\angle ABC = 90^\circ + \angle IBC$$
- **画面图元**：
  - 绘制凸五边形的内切圆 $\odot I$（虚线橙色圆）
  - 连结线段 $IE$（橙色实线）
  - 高亮四边形 $ABIE$（淡橙色半透明背景）
  - 绘制角弧标出钝角 $\angle BIE$ 与底角 $\angle IBC$

---

### Step 5: 得出 $EI \bot BC$ 与三线共点结论
- **标题**：⑤ 垂线共线 $\implies$ 过点 $E$ 的垂线与 $AC, BD$ 三线共点
- **正文**：
  在直角 $\triangle IBK$ 中（$IK \perp BC$），$\angle BIK = 90^\circ - \angle IBC$。
  由于 $\angle BIE = 90^\circ + \angle IBC$，故：
  $$\angle BIE + \angle BIK = (90^\circ + \angle IBC) + (90^\circ - \angle IBC) = 180^\circ$$
  这说明点 $E, I, K$ 三点共线，即 **$EI \perp BC$**！
  而在 Step 2 中已由垂心性质证明了 **$IH \perp BC$**（即点 $I, H, K$ 共线）。
  因此，过点 $E$ 作 $BC$ 的垂线必为直线 $EIHK$，同时经过点 $I$ 与点 $H$！
  由于 $H$ 为对角线 $AC$ 与 $BD$ 的交点，所以：
  **过点 $E$ 作 $BC$ 的垂线与 $AC, BD$ 三线共点于点 $H$！** 命题获证。
- **画面图元**：
  - 加粗贯穿高亮垂线 $EIHK$（鲜艳红色实线，从 $E$ 贯穿 $I, H$ 直达垂足 $K$）
  - 在垂足 $K$ 处标注红色直角符号
  - 鲜明高亮对角线 $AC$ 和 $BD$（蓝色实线）
  - 强调三线交点 $H$（带扩散光圈的红/蓝强调标记）
  - 显示完整内切圆与五边形，所有几何关系完美收拢
