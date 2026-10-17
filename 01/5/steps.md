# 例 4：角平分线与射影全等证明分步规划

## 题目信息
- **题面**：如图，$\triangle ABC$ 满足 $AB > AC$，其外接圆为 $\Gamma$。$\angle BAC$ 的内、外角平分线与圆 $\Gamma$ 交于点 $M, D$（异于 $A$）。点 $D$ 在边 $AB$ 上的射影为点 $E$，$N$ 为 $AM$ 的中点，$M$ 在 $AC$ 上的射影为点 $K$。证明：$\angle NEA = \angle NCK$。
- **思路概述**：通过外角平分线与垂线构造全等直角三角形 $\triangle AED \cong \triangle ATD$ 及 $\triangle DEB \cong \triangle DTC$，推导出阿基米德折弦性质 $AE = \frac{1}{2}(AB - AC)$；同理在劣弧中点 $M$ 处推导得 $CK = \frac{1}{2}(AB - AC)$，从而 $AE = CK$；再利用 Rt$\triangle AKM$ 的斜边中线性质得到 $NK = NA$ 与 $\angle NKC = \angle EAN$，由 SAS 判定 $\triangle CKN \cong \triangle EAN$，最终导出 $\angle NEA = \angle NCK$。

---

## 颜色约定
- 基础图形（$\triangle ABC$、圆 $\Gamma$、角平分线 $AM, AD$）：深灰/黑色 (`#0f172a`, `#334155`)，圆为细轮廓线 (`#94a3b8`)。
- 辅助垂线与延长线（$DT, AT, CK, MK$）：蓝色/青色虚线 (`#2563eb`, `#0891b2`)。
- 等长线段（$AE, CK$ 及 $NK, NA$）：绿色高亮 (`#059669`) 或 紫色 (`#7c3aed`)。
- 全等三角形填充：柔和半透明色（蓝色 `rgba(37,99,235,0.12)`、橙色 `rgba(234,88,12,0.12)`、紫色 `rgba(124,58,237,0.12)`）。
- 直角标记与角弧高亮：红色 (`#dc2626`)。

---

## 分步规划清单

### Step 0：已知条件与几何构型
- **标题**：已知条件与几何构型
- **正文**：
  在 $\triangle ABC$ 中，$AB > AC$，其外接圆为 $\Gamma$。<br>
  $\angle BAC$ 的内角平分线交圆 $\Gamma$ 于 $M$（劣弧 $BC$ 中点），外角平分线交圆 $\Gamma$ 于 $D$（优弧 $BAC$ 中点）。<br>
  点 $D$ 在边 $AB$ 上的射影为 $E$（$DE \perp AB$）；<br>
  $N$ 为线段 $AM$ 的中点；<br>
  $M$ 在边 $AC$ 上的射影为 $K$（$MK \perp AC$）。<br>
  <b>求证：</b>$\angle NEA = \angle NCK$。
- **画面图元**：
  - 静态底图：圆 $\Gamma$、$\triangle ABC$、内角平分线 $AM$、外角平分线 $AD$、垂线 $DE$、垂线 $MK$。
  - 点集显示：$A, B, C, D, M, E, K, N$。
  - 标记：直角标记 $\angle AED = 90^\circ$、$\angle AKM = 90^\circ$。
  - 辅助提示：虚线连线 $NE, NC$，提示最终待证的两角。

### Step 1：作辅助垂线 $DT \perp AC$，构造 $\triangle AED \cong \triangle ATD$
- **标题**：① 辅助垂线 $DT \implies \triangle AED \cong \triangle ATD$
- **正文**：
  过点 $D$ 作 $DT \perp AC$ 于点 $T$（$T$ 位于边 $CA$ 的延长线上）。<br>
  因为 $AD$ 是 $\angle BAC$ 的外角平分线，根据角平分线性质，平分线上的点到角两边的距离相等，故 $\angle EAD = \angle TAD$。<br>
  又 $\angle AED = \angle ATD = 90^\circ$，$AD$ 为公共斜边，由角角边（AAS）可得：<br>
  $$\triangle AED \cong \triangle ATD$$
  由此得出对应直角边相等：<br>
  <b>$DE = DT$</b> 且 <b>$AE = AT$</b>。
- **画面图元**：
  - 新增图元：$CA$ 延长线至 $T$、辅助垂线 $DT$、垂足 $T$、直角标记 $\angle ATD = 90^\circ$。
  - 高亮图元：高亮直角三角形 $\triangle AED$ 与 $\triangle ATD$（浅蓝填充），线段 $DE, DT$ 与 $AE, AT$ 标记等长。

### Step 2：利用圆内接性质，证 Rt$\triangle DEB \cong$ Rt$\triangle DTC$
- **标题**：② 圆内接性质与弦长 $\implies$ Rt$\triangle DEB \cong$ Rt$\triangle DTC$
- **正文**：
  连接 $DB, DC$。<br>
  因为 $D$ 是外角平分线与圆 $\Gamma$ 的交点，由圆周角性质可知 $D$ 为弧 $BAC$ 的中点，因此弦长 <b>$DB = DC$</b>。<br>
  在圆内接四边形 $ABDC$ 中，外角等于内对角，即 $\angle DCT = \angle ABD = \angle EBD$。<br>
  在 Rt$\triangle DEB$ 与 Rt$\triangle DTC$ 中：<br>
  斜边 $DB = DC$，直角边 $DE = DT$。<br>
  由斜边直角边（HL）判定定理可得：<br>
  $$\text{Rt}\triangle DEB \cong \text{Rt}\triangle DTC$$
  由此导出对应边相等：<b>$BE = CT$</b>。
- **画面图元**：
  - 新增图元：连接线段 $DB, DC$（虚线）。
  - 高亮图元：高亮直角三角形 Rt$\triangle DEB$ 与 Rt$\triangle DTC$（橙黄色填充），等长标记 $DB = DC$。

### Step 3：折弦性质推导，得 $AE = CK = \frac{1}{2}(AB - AC)$
- **标题**：③ 折弦推导 $\implies AE = CK = \frac{1}{2}(AB - AC)$
- **正文**：
  由步骤 ② 的全等已知 $BE = CT$。<br>
  因为 $E$ 在线段 $AB$ 上，故 $AB = AE + BE = AE + CT$。<br>
  由于 $T$ 在边 $CA$ 的延长线上，且由步骤 ① 知 $AT = AE$，因此：<br>
  $$CT = AC + AT = AC + AE$$
  代入得：$AB = AE + (AC + AE) = AC + 2AE$，从而解得：<br>
  $$AE = \frac{1}{2}(AB - AC)$$
  同理，点 $M$ 为劣弧 $BC$ 中点，$K$ 为 $M$ 在 $AC$ 上的射影，由对称性与折弦性质同理推导可得：<br>
  $$CK = \frac{1}{2}(AB - AC)$$
  由此得出关键等量关系：<b>$AE = CK$</b>。
- **画面图元**：
  - 移除之前的全等三角形填充；
  - 重点高亮线段 $AE$ 与 $CK$（绿色加粗），并打上单刻度等长标记。

### Step 4：直角三角形斜边中线性质，得 $NK = NA$ 与等角
- **标题**：④ 斜边中线 $\implies NK = NA$ 且 $\angle NKC = \angle EAN$
- **正文**：
  在 Rt$\triangle AKM$ 中，$\angle AKM = 90^\circ$，$N$ 为斜边 $AM$ 的中点。<br>
  由直角三角形斜边中线等于斜边一半定理，可知：<br>
  <b>$NK = NA = NM$</b>。<br>
  因此 $\triangle NAK$ 是等腰三角形，底角 $\angle NKA = \angle NAK$。<br>
  因为点 $C$ 位于线段 $AK$ 上，射线 $KC$ 与 $KA$ 重合，所以 $\angle NKC = \angle NKA = \angle MAC$。<br>
  又因为 $AM$ 平分 $\angle BAC$，故 $\angle MAC = \angle BAM = \angle EAN$。<br>
  由此得出对应夹角相等：<br>
  <b>$\angle NKC = \angle EAN$</b>。
- **画面图元**：
  - 新增图元：连接线段 $NK$（紫色实线）；
  - 高亮图元：高亮线段 $NA$ 与 $NK$（打上双刻度等长标记）；
  - 角弧标记：在 $\angle NKC$ 与 $\angle EAN$ 处绘制红色角弧并标出等角。

### Step 5：SAS 判定全等，导出结论 $\angle NEA = \angle NCK$
- **标题**：⑤ SAS 全等 $\triangle CKN \cong \triangle EAN \implies \angle NEA = \angle NCK$
- **正文**：
  综合以上步骤，在 $\triangle CKN$ 与 $\triangle EAN$ 中：<br>
  1. $CK = AE$（由步骤 ③ 证得）；<br>
  2. $\angle CKN = \angle EAN$（由步骤 ④ 证得）；<br>
  3. $NK = NA$（由步骤 ④ 证得）。<br>
  由边角边（SAS）全等判定定理，可得：<br>
  $$\triangle CKN \cong \triangle EAN$$
  因此对应角相等：<br>
  $$\angle NEA = \angle NCK$$
  原几何命题得证！
- **画面图元**：
  - 绘制连线 $NE$ 和 $NC$（加粗高亮线）；
  - 高亮全等三角形 $\triangle CKN$（紫色高亮填充）与 $\triangle EAN$（蓝色高亮填充）；
  - 在 $\angle NEA$ 与 $\angle NCK$ 处绘制显著的角弧标记并闪烁高亮，宣告结论达成。
