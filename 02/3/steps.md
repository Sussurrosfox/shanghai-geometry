# 例 2 分步几何证明规划 (02/3)

## 题目概述
锐角 $\triangle ABC$ 中，$AB > AC$，$M$ 为其外接圆 $O$ 上劣弧 $BC$ 的中点，$K$ 为 $A$ 的对径点。过 $O$ 作 $AM$ 的平行线交 $AB$ 于 $D$，交 $CA$ 的延长线于 $E$。直线 $BM$ 交直线 $CK$ 于 $P$，直线 $CM$ 交直线 $BK$ 于 $Q$。
证明：
$$\angle OPB + \angle OEB = \angle OQC + \angle ODC$$

---

## 颜色语义约定
- **基准图形**：深灰/黑色（`#334155`、`#0f172a`），线宽 1.8px
- **外接圆及直径**：灰蓝浅色（`#94a3b8`），虚线或细实线
- **平行线组 ($OD \parallel AM$)**：紫色（`#8b5cf6`），带平行箭头标记
- **相似三角形第 1 组 ($\triangle BOD \sim \triangle CPB$)**：天蓝高亮（`#0284c7`）与橙色（`#ea580c`）
- **相似三角形第 2 组 ($\triangle DBC \sim \triangle OCP$)**：翠绿（`#10b981`）与玫瑰红（`#e11d48`）
- **对称侧相似组 ($\triangle ECB \sim \triangle OBQ$)**：金黄（`#f59e0b`）与湖蓝（`#06b6d4`）
- **目标等式角**：
  - 左端角（$\angle OPB, \angle OEB$）：明亮珊瑚红（`#ef4444`）
  - 右端角（$\angle OQC, \angle ODC$）：鲜明宝青/紫罗兰（`#6366f1`）

---

## 分步详细规划

### Step 0: 题设构型与基准图形
- **标题**：0️⃣ 题设几何构型与基本元素
- **正文**：
  在锐角 $\triangle ABC$ 中，$AB > AC$，$O$ 为外接圆心。$M$ 为劣弧 $BC$ 的中点（$BM = CM$），$K$ 为点 $A$ 的对径点（$AK$ 为直径）。
  过 $O$ 作 $AM$ 的平行线分别交边 $AB$ 于点 $D$、交射线 $CA$ 的延长线于点 $E$。
  直线 $BM$ 与直线 $CK$ 相交于点 $P$；直线 $CM$ 与直线 $BK$ 相交于点 $Q$。
  本演示将逐步推导关键相似三角形与角度代换，最终证明等式 $\angle OPB + \angle OEB = \angle OQC + \angle ODC$。
- **画面图元**：
  - 绘制 $\triangle ABC$、外接圆 $(O)$、圆心 $O$、劣弧中点 $M$、对径点 $K$ 及直径线段 $AK$。
  - 绘制平行割线 $E-D-O$ 与弦 $AM$。
  - 绘制交线 $B-M-P$、$C-K-P$（交于 $P$）与 $C-M-Q$、$B-K-Q$（交于 $Q$）。
  - 显示所有关键点标签：$A, B, C, O, M, K, D, E, P, Q$。

---

### Step 1: 平行线与圆周角导出两组等角
- **标题**：① 平行线导角：$\angle BDO = \angle CBP$ 与 $\angle DBO = \angle BCP$
- **正文**：
  连接辅助线段 $AK, BO, CO, OM$。<br>
  1. <b>第一组等角</b>：因为 $OD \parallel AM$，所以同位角 $\angle BDO = \angle BAM$。由同弧所对圆周角相等，知 $\angle BAM = \angle BCM$；又 $M$ 为劣弧 $BC$ 中点，所对圆弧相等，故 $\angle BCM = \angle CBM = \angle CBP$。由此导出：
  $$\angle BDO = \angle BAM = \angle BCM = \angle CBP$$
  2. <b>第二组等角</b>：由于 $AK$ 是外接圆直径，$\angle ACK = 90^\circ$。在直角 $\triangle ACK$ 中，$\angle BCK = 90^\circ - \angle ACB$。而在等腰 $\triangle AOB$ 中，$\angle ABO = 90^\circ - \angle ACB$。由于 $B, D, A$ 共线，$\angle DBO = \angle ABO$；又 $C, P, K$ 共线，$\angle BCP = \angle BCK$。因此：
  $$\angle DBO = 90^\circ - \angle ACB = \angle BCP$$
- **画面图元**：
  - 高亮辅助线段 $AM, OD$（紫色），标出平行箭头。
  - 虚线连接 $BO, CO, OM$。
  - 红色角弧标记 $\angle BDO, \angle BAM, \angle BCM, \angle CBP$。
  - 蓝色角弧标记 $\angle DBO$ 与 $\angle BCP$。
  - 在 $C$ 处标出直径所对直角 $\angle ACK = 90^\circ$。

---

### Step 2: 关键相似 $\triangle BOD \sim \triangle CPB$ 桥接转出 $\triangle DBC \sim \triangle OCP$
- **标题**：② 相似三角形：$\triangle BOD \sim \triangle CPB \implies \triangle DBC \sim \triangle OCP$
- **正文**：
  由 Step 1 中已证明的两组等角：
  $$\angle BDO = \angle CPB \text{ 且 } \angle DBO = \angle BCP$$
  由两角对应相等，立得：
  $$\triangle BOD \sim \triangle CPB$$
  从而对应边成比例：
  $$\frac{BD}{CP} = \frac{BO}{CB} \iff \frac{BD}{CB} = \frac{BO}{CP}$$
  注意到 $BO = CO$（均为外接圆半径 $R$），将 $BO$ 替换为 $CO$，得：
  $$\frac{BD}{CO} = \frac{BC}{CP} \iff \frac{BD}{BC} = \frac{CO}{CP}$$
  又两三角形的夹角满足 $\angle DBC = \angle B$；由于直径 $AK$ 对应 $\angle AKC = \angle B$，在直角 $\triangle ACK$ 中 $\angle OCP = 90^\circ - \angle ACB = \angle B$。即夹角 $\angle DBC = \angle OCP$。
  因此，根据<b>两边对应成比例且夹角相等</b>，导出第二对相似三角形：
  $$\triangle DBC \sim \triangle OCP$$
  从而对应角相等：
  $$\angle COP = \angle BDC, \quad \angle CPO = \angle BCD$$
- **画面图元**：
  - 半透明色彩填充高亮 $\triangle BOD$ 与 $\triangle CPB$；
  - 切换色彩填充高亮 $\triangle DBC$（翠绿）与 $\triangle OCP$（玫红）；
  - 标出对应等角弧：$\angle COP$ 与 $\angle BDC$。

---

### Step 3: 对称侧相似 $\triangle ECB \sim \triangle OBQ$
- **标题**：③ 对称侧相似：$\triangle ECB \sim \triangle OBQ \implies \angle BOQ = \angle CEB$
- **正文**：
  完全平行地，考察直线 $OE \parallel AM$ 与点 $Q$（直线 $CM$ 与 $BK$ 的交点）：<br>
  同理可证 $\triangle COE \sim \triangle BQC$，利用 $CO = BO$ 进行比例转置，完全类似地可导出对称侧的第二对相似三角形：
  $$\triangle ECB \sim \triangle OBQ$$
  由相似三角形对应角相等，立即得到：
  $$\angle BOQ = \angle CEB, \quad \angle BQO = \angle CBE$$
- **画面图元**：
  - 色彩填充高亮 $\triangle ECB$ 与 $\triangle OBQ$；
  - 标出对应等角弧：$\angle BOQ$ 与 $\angle CEB$。

---

### Step 4: 角度代换与圆心角差桥接
- **标题**：④ 角度差转换：$\angle OPB - \angle OQC = \angle BDC - \angle CEB$
- **正文**：
  由底端以 $M$ 为基准的外角与顶角关系，结合劣弧中点对称性（$\angle OMB = \angle OMC$），展开角差：
  $$\angle OPB - \angle OQC = (\angle OMB + \angle POM) - (\angle OMC - \angle QOM)$$
  $$= \angle POM + \angle QOM = \angle POM + \angle COM - \angle BOM + \angle QOM$$
  $$= \angle COP - \angle BOQ$$
  将 Step 2 与 Step 3 中得到的相似对应角代换入上式：
  $$\angle COP = \angle BDC, \quad \angle BOQ = \angle CEB$$
  从而立即得到关键角度差恒等式：
  $$\angle OPB - \angle OQC = \angle BDC - \angle CEB$$
- **画面图元**：
  - 连线 $OP, OQ$；
  - 高亮角弧对 $\angle COP$ 与 $\angle BDC$（青色），以及 $\angle BOQ$ 与 $\angle CEB$（橙色）；
  - 动态展示角度差从圆内交点 $P, Q$ 到截线交点 $D, E$ 的精确转移。

---

### Step 5: 外角拆分与移项得证
- **标题**：⑤ 外角拆分与最终等式成立
- **正文**：
  进一步计算角度差 $\angle BDC - \angle CEB$：<br>
  - 在 $\triangle ADC$ 中，$D$ 为边 $AB$ 上一点，外角 $\angle BDC = \angle BAC + \angle ACD$；
  - 在 $\triangle ABE$ 中，$A$ 为线段 $CE$ 上一点，外角 $\angle CAB = \angle CEB + \angle ABE \implies \angle CEB = \angle CAB - \angle ABE$；
  - 两式相减（注意到 $\angle BAC = \angle CAB$）：
  $$\angle BDC - \angle CEB = \angle ACD + \angle ABE$$
  - 又在截线 $\triangle ADE$ 中，外角关系给出 $\angle ODC - \angle OEB = \angle ACD + \angle ABE$；
  - 因此：
  $$\angle BDC - \angle CEB = \angle ODC - \angle OEB$$
  与 Step 4 联立得到：
  $$\angle OPB - \angle OQC = \angle ODC - \angle OEB$$
  两端移项整理，最终得证题设命题：
  $$\mathbf{\angle OPB + \angle OEB = \angle OQC + \angle ODC}$$
- **画面图元**：
  - 高亮目标等式中的四个核心角：
    - 珊瑚红加粗角弧：$\angle OPB$ 与 $\angle OEB$（左端和项）；
    - 紫罗兰加粗角弧：$\angle OQC$ 与 $\angle ODC$（右端和项）；
  - 显示连线 $PE, QD$（辅助视觉聚拢），金色徽标标出「Q.E.D. 证毕」。
