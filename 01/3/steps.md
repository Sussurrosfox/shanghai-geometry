# 例 2：直线 KL 过线段 AJ 的中点 — 分步证明规划

## 题目描述
在 $\triangle ABC$ 中，$\angle C < \angle A < 90^\circ$，$D$ 为边 $AC$ 上一点，使得 $BD = BA$。$\triangle ABC$ 的内切圆分别与边 $AB, AC$ 切于点 $K, L$。设 $J$ 为 $\triangle BCD$ 的内心。证明：直线 $KL$ 过线段 $AJ$ 的中点。

---

## 步骤规划清单（Step 0 ~ Step 6）

### Step 0: 已知条件与图形架构
- **标题**：已知条件与图形架构
- **正文**：
  在 $\triangle ABC$ 中，$\angle C < \angle A < 90^\circ$。点 $D$ 位于边 $AC$ 上且满足 $BD = BA$。<br>
  $\triangle ABC$ 的内切圆分别切边 $AB, AC$ 于点 $K, L$；点 $J$ 为 $\triangle BCD$ 的内心。<br>
  连结直线 $KL$ 与线段 $AJ$，求证：直线 $KL$ 经过线段 $AJ$ 的中点。
- **画面图元**：
  - 基础图形：$\triangle ABC$，内切圆 $\odot I$（淡灰蓝色虚线），切点 $K, L$。
  - 已知线段：$BD$（等长于 $BA$），内心 $J$（及 $\triangle BCD$ 内切圆轻描淡写）。
  - 目标图元：连结线段 $AJ$（实线），直线 $KL$（贯穿延伸线）。
  - 点位：显示 $A, B, C, D, K, L, J$。

### Step 1: ① 作垂线 BS 与 JR，确定 AD 中点 S
- **标题**：① 作垂线 BS 与 JR，确定 AD 中点 S
- **正文**：
  过点 $B$ 作 $BS \perp AC$ 于点 $S$，直线 $BS$ 与 $KL$ 相交于点 $H$。<br>
  过内心 $J$ 作 $JR \perp AC$ 于点 $R$（$R$ 即为 $\triangle BCD$ 内切圆在边 $AC$ 上的切点）。<br>
  在等腰 $\triangle BAD$ 中，$BA = BD$，$BS$ 为底边 $AD$ 上的高，亦为中线，故 $S$ 是 $AD$ 的中点，即 $AS = SD = \frac{1}{2}AD$。
- **画面图元**：
  - 新增图元：垂线段 $BS$（高亮蓝色虚线）、垂线段 $JR$（高亮蓝色虚线）。
  - 标记：垂足 $S, R$ 处的直角标记 $\llcorner$。
  - 等长刻度：线段 $AS$ 与 $SD$ 上标示相同的单横线刻度（表示 $AS = SD$）。
  - 新增点：$S, R, H$。

### Step 2: ② 利用切线长导出 AL = SR 与 SL = DR
- **标题**：② 利用切线长导出 AL = SR 与 SL = DR
- **正文**：
  设 $\triangle ABC$ 与 $\triangle BCD$ 的边长与切线长：<br>
  由内切圆切线长公式，$AL = \frac{AB + AC - BC}{2}$；在 $\triangle BCD$ 中，$R$ 为切点，$DR = \frac{BD + CD - BC}{2}$。<br>
  代入 $BD = BA$ 及 $CD = AC - AD$，得：<br>
  $AL - DR = \frac{AB + AC - BC}{2} - \frac{BA + AC - AD - BC}{2} = \frac{1}{2}AD = AS = SD$。<br>
  在直线上计算线段 $LR = AD + DR - AL = AD - (AL - DR) = AD - \frac{1}{2}AD = \frac{1}{2}AD = AS$。<br>
  从而 $AL = AR - LR = (AS + SR) - AS = SR$；进而由 $AL - AS = SR - SD$ 得 $SL = DR$。
- **画面图元**：
  - 高亮线段组 1：$AL$ 与 $SR$（加粗青蓝色），标示等长刻度。
  - 高亮线段组 2：$SL$ 与 $DR$（加粗橙黄色），标示等长刻度。
  - 底线 $AC$ 上各点相对位置清晰展示：$A - S - L - D - R - C$。

### Step 3: ③ 由外角与角平分线性质导出 ∠SLH = ∠RDJ
- **标题**：③ 由外角与角平分线性质导出 ∠SLH = ∠RDJ
- **正文**：
  在等腰 $\triangle AKL$ 中，因 $AK = AL$（内切圆切线长相等），故 $\angle ALK = 90^\circ - \frac{1}{2}\angle A$。<br>
  又在等腰 $\triangle BAD$ 中，$BA = BD$，其外角 $\angle CDB = \angle DAB + \angle DBA = 180^\circ - \angle A$。<br>
  由于 $J$ 是 $\triangle BCD$ 的内心，$DJ$ 是 $\angle CDB$ 的角平分线，因此：<br>
  $\angle CDJ = \frac{1}{2}\angle CDB = 90^\circ - \frac{1}{2}\angle A$。<br>
  由点 $A, S, L$ 在一条直线上，知 $\angle SLH = \angle ALK = 90^\circ - \frac{1}{2}\angle A$；由点 $D, R, C$ 共线，知 $\angle RDJ = \angle CDJ$。<br>
  因此得到关键角相等：$\angle SLH = \angle RDJ$。
- **画面图元**：
  - 新增连线：辅助线段 $DJ$（虚线）。
  - 角度标记：在 $\angle SLH$ 和 $\angle RDJ$ 处标出醒目的红色双角弧。
  - 等腰三角形底角辅助高亮：淡红色点亮 $\angle ALK$ 与 $\angle AKL$。

### Step 4: ④ △LSH ≌ △DRJ 导出对应边 SH = JR
- **标题**：④ △LSH ≌ △DRJ 导出对应边 SH = JR
- **正文**：
  考察直角三角形 $\triangle LSH$ 与 $\triangle DRJ$：<br>
  1. $\angle LSH = \angle DRJ = 90^\circ$（均为垂直于 $AC$ 的直角）；<br>
  2. 直角边 $SL = DR$（已由步骤 ② 证得）；<br>
  3. 锐角 $\angle SLH = \angle RDJ$（已由步骤 ③ 证得）。<br>
  根据直角三角形的“角边角”（ASA）全等判定定理，得：<br>
  $\triangle LSH \cong \triangle DRJ$。<br>
  由此得出对应直角边相等：$SH = JR$。
- **画面图元**：
  - 区域填充高亮：$\triangle LSH$（半透明翠绿色）与 $\triangle DRJ$（半透明翠绿色）。
  - 高亮对应线段：垂直线段 $SH$ 与 $JR$（加粗翠绿色实线，加等长刻度）。
  - 保留 $SL$ 与 $DR$ 的高亮对比。

### Step 5: ⑤ 判定 HSRJ 为矩形，导出 HJ ∥ AL 且 HJ = AL
- **标题**：⑤ 判定 HSRJ 为矩形，导出 HJ ∥ AL 且 HJ = AL
- **正文**：
  因为 $HS \perp AC$ 且 $JR \perp AC$，所以 $HS \parallel JR$。<br>
  又因为 $SH = JR$（步骤 ④），一组对边平行且相等，故四边形 $HSRJ$ 为平行四边形。<br>
  再由 $HS \perp SR$（$\angle HSR = 90^\circ$），可知 $HSRJ$ 为矩形！<br>
  由矩形性质，对边平行且相等：$HJ \parallel SR$ 且 $HJ = SR$。<br>
  结合步骤 ② 已证的 $SR = AL$ 以及 $A, S, R$ 共线于边 $AC$，立即得出：<br>
  $HJ \parallel AL$ 且 $HJ = AL$。
- **画面图元**：
  - 新增线段：$HJ$（加粗深蓝色）。
  - 区域高亮：矩形 $HSRJ$ 填充半透明天蓝色，高亮四条边界。
  - 平行与等长标记：在对边 $HJ$ 与 $AL$ 上打上平行箭头标记与等长刻度。

### Step 6: ⑥ 判定 ALJH 为平行四边形，KL 平分 AJ
- **标题**：⑥ 判定 ALJH 为平行四边形，KL 平分 AJ
- **正文**：
  连结 $AH$ 与 $LJ$。在四边形 $ALJH$ 中：<br>
  因 $HJ \parallel AL$ 且 $HJ = AL$，有一组对边平行且相等，所以四边形 $ALJH$ 是平行四边形！<br>
  在平行四边形中，对角线互相平分，因此对角线 $HL$ 与 $AJ$ 互相平分。<br>
  记 $HL$ 与 $AJ$ 的交点为 $M$，则 $M$ 为线段 $AJ$ 的中点（同时也是 $HL$ 的中点）。<br>
  由于点 $H$ 与点 $L$ 均在直线 $KL$ 上，直线 $HL$ 即为直线 $KL$。<br>
  由此证明：直线 $KL$ 经过线段 $AJ$ 的中点 $M$。原命题得证！
- **画面图元**：
  - 新增连线：$AH$ 与 $LJ$（深紫色实线）。
  - 区域高亮：平行四边形 $ALJH$ 填充半透明金黄色。
  - 对角线高亮：线段 $HL$（直线 $KL$ 的一部分，鲜艳橙红色）与线段 $AJ$（深紫色），并在交点标注点 $M$。
  - 平分刻度：在 $AM$ 与 $MJ$ 上标示双刻度线，展示 $AM = MJ$。
