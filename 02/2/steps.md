# 02/2（例 1）两圆外公切线与垂线证明分步规划

## 题目概述
已知圆 $O_1$ 和圆 $O_2$ 交于 $P, Q$ 两点，两圆的外公切线分别切圆 $O_1$ 和圆 $O_2$ 于点 $A, B$。点 $A, B$ 与 $Q$ 在点 $P$ 两侧。过点 $A$ 作 $AC \perp BP$ 交 $O_1O_2$ 于点 $C$。
证明：$\angle APC = 90^\circ$。

---

## 颜色语义约定
| 语义分类 | 颜色名称 | 16进制色值 | 用途与图元 |
| :--- | :--- | :--- | :--- |
| 圆 $O_1$ 体系 | 经典蓝 | `#2563eb` | 圆 $O_1$、圆心 $O_1$、半径 $O_1A, O_1P$、$\triangle O_1AC$ |
| 圆 $O_2$ 体系 | 森林绿 | `#059669` | 圆 $O_2$、圆心 $O_2$、半径 $O_2B$ |
| 公共弦体系 | 优雅紫 | `#7c3aed` | 公共弦 $PQ$、延长线 $DQ$、$\triangle QAP$ |
| 切线与中点 | 琥珀金/深石板灰 | `#475569` / `#d97706` | 公切线 $AB$、中点 $D$、切线段 $DA, DB$ |
| 垂直与垂足 | 炽热橙红 | `#ea580c` | 垂线 $AC$、直线 $BP$、垂足 $H$、点 $C$ |
| 直角与高亮标记 | 鲜艳红 | `#dc2626` | 直角符号、目标角 $\angle APC$、高亮角弧 |

---

## 分步推演规划

### Step 0: 题目构型与已知条件
- **标题**：✦ 题目构型与已知条件
- **讲解正文**：
  已知两相交圆 $\odot O_1$ 与 $\odot O_2$ 交于点 $P, Q$。直线 $AB$ 为两圆的外公切线，切点分别为 $A, B$。
  点 $P$ 位于切线 $AB$ 与交点 $Q$ 之间。过切点 $A$ 作 $AC \perp BP$，垂足为 $H$，直线 $AC$ 交连心线 $O_1O_2$ 于点 $C$。
  我们需要证明：线段 $AP$ 与 $CP$ 相互垂直，即 $\angle APC = 90^\circ$。
- **图元显隐清单**：
  - **基础图形**：圆 $O_1$、圆 $O_2$、连心线 $O_1O_2$、外公切线 $AB$、弦 $PQ$；
  - **条件图元**：线段 $BP$、垂线 $AC$（交 $O_1O_2$ 于 $C$）、垂足直角标记 $AC \perp BP$；
  - **目标提示**：连结虚线 $AP, CP$，指示待证目标 $\angle APC = 90^\circ$。

---

### Step 1: 延长公共弦交公切线于点 $D$（切割线定理）
- **标题**：① 延长公共弦交公切线于 $D \implies DA = DB$
- **讲解正文**：
  延长公共弦 $QP$ 交外公切线 $AB$ 于点 $D$。
  由圆的切割线定理（圆幂定理）：
  - 对 $\odot O_1$，$DA$ 为切线，$DPQ$ 为割线，故 $DA^2 = DP \cdot DQ$；
  - 对 $\odot O_2$，$DB$ 为切线，$DPQ$ 为割线，故 $DB^2 = DP \cdot DQ$。
  因此 $DA^2 = DB^2$，即 $DA = DB$。
  **结论**：点 $D$ 必为公切线段 $AB$ 的中点。
- **图元显隐清单**：
  - **新增图元**：射线 $QP$ 延长至点 $D$（紫色虚线）；
  - **高亮元素**：线段 $DA$ 与 $DB$ 高亮（橙色），在 $DA, DB$ 上标注等长单刻度线；
  - **割线高亮**：高亮共线线段 $D-P-Q$。

---

### Step 2: 三组对应垂直导出 $\triangle DBP \sim \triangle O_1AC$
- **标题**：② 三组边对应垂直 $\implies \triangle DBP \sim \triangle O_1AC$
- **讲解正文**：
  连接切点半径 $O_1A$。考察 $\triangle DBP$ 与 $\triangle O_1AC$：
  1. $O_1C \perp DP$：连心线 $O_1O_2$ 垂直平分公共弦 $PQ$，即 $O_1C \perp DP$；
  2. $O_1A \perp DB$：外公切线 $AB$ 垂直于切点半径 $O_1A$；
  3. $AC \perp BP$：已知条件。
  因为 $\triangle DBP$ 与 $\triangle O_1AC$ 的三组对应边分别垂直且旋向一致，故对应角相等：
  $$\triangle DBP \sim \triangle O_1AC.$$
  由此得到比例关系：
  $$\frac{DP}{DB} = \frac{O_1C}{O_1A}.$$
- **图元显隐清单**：
  - **新增图元**：连接线段 $O_1A$；
  - **三角形高亮**：填充半透明高亮 $\triangle DBP$（浅橙色）与 $\triangle O_1AC$（浅青色）；
  - **垂直标记**：显示三组直角标记（$O_1A \perp AB$ 于 $A$，$O_1O_2 \perp PQ$ 于弦心交点，$AC \perp BP$ 于 $H$）；
  - **比例高亮**：高亮边 $DP, DB$ 与 $O_1C, O_1A$。

---

### Step 3: 比例转换导出 $\triangle PO_1C \sim \triangle QAP$
- **标题**：③ 比例代换与弦切角 $\implies \triangle PO_1C \sim \triangle QAP$
- **讲解正文**：
  连接 $O_1P$ 与 $AQ$。
  由 Step 1 知 $DB = DA$，且 $O_1A = O_1P$（同为 $\odot O_1$ 的半径），代换 Step 2 的比例式得：
  $$\frac{O_1C}{O_1P} = \frac{DP}{DA}.$$
  在 $\triangle DAP$ 与 $\triangle DQA$ 中，公共角 $\angle ADP = \angle QDA$，且由弦切角定理 $\angle DAP = \angle DQA$，知 $\triangle DAP \sim \triangle DQA$。
  故有 $\frac{DP}{DA} = \frac{AP}{AQ}$。
  代入上式即得：
  $$\frac{O_1C}{O_1P} = \frac{AP}{AQ} \iff \frac{O_1C}{AP} = \frac{O_1P}{AQ}.$$
  又连心线平分圆心角，得 $\angle PO_1C = \frac{1}{2}\angle PO_1Q$；由圆周角定理，$\angle PAQ = \frac{1}{2}\angle PO_1Q$。
  故夹角相等：$\angle PO_1C = \angle PAQ$。
  两边对应成比例且夹角相等，从而：
  $$\triangle PO_1C \sim \triangle QAP.$$
- **图元显隐清单**：
  - **新增图元**：连接线段 $O_1P, AQ, AP$；
  - **三角形高亮**：高亮 $\triangle PO_1C$（浅绿填充）与 $\triangle QAP$（浅紫填充）；
  - **角弧标记**：绘制对应等角 $\angle PO_1C$ 与 $\angle PAQ$ 的红色同心角弧。

---

### Step 4: 相似对应角相等与弦切角转换
- **标题**：④ 相似对应角相等与弦切角转换
- **讲解正文**：
  由相似三角形 $\triangle PO_1C \sim \triangle QAP$ 的性质，对应角相等：
  $$\angle O_1PC = \angle AQP.$$
  在 $\odot O_1$ 中，$AB$ 为切线，$AP$ 为弦，再次应用弦切角定理：
  弦切角等于其所夹弧所对的圆周角，即：
  $$\angle PAD = \angle AQP.$$
  由等量代换，立即得到关键等角关系：
  $$\angle O_1PC = \angle PAD.$$
- **图元显隐清单**：
  - **高亮角弧**：高亮显示 $\angle O_1PC$、$\angle AQP$ 与 $\angle PAD$ 的角弧（三者均相等，赋予鲜艳标识）；
  - **辅助视线**：虚线强化弦切角边 $AD, AP$ 与圆周角边 $QA, QP$。

---

### Step 5: 角度拆分推导 $\implies \angle APC = 90^\circ$
- **标题**：⑤ 角度拆分推导 $\implies \angle APC = 90^\circ$
- **讲解正文**：
  在等腰 $\triangle O_1AP$ 中，两半径 $O_1A = O_1P$，因此底角相等：
  $$\angle APO_1 = \angle O_1AP.$$
  现在将待求角 $\angle APC$ 沿射线 $PO_1$ 拆分为两部分：
  $$\angle APC = \angle APO_1 + \angle O_1PC.$$
  代入等角关系 $\angle APO_1 = \angle O_1AP$ 以及 $\angle O_1PC = \angle PAD$：
  $$\angle APC = \angle O_1AP + \angle PAD = \angle O_1AD.$$
  由于 $AD$ 是切线，$O_1A$ 是切点半径，切线必垂直于半径：
  $$\angle O_1AD = 90^\circ.$$
  由此最终推得：
  $$\angle APC = 90^\circ.$$
  证毕！
- **图元显隐清单**：
  - **等腰角高亮**：标出等腰 $\triangle O_1AP$ 底角 $\angle APO_1 = \angle O_1AP$；
  - **组合角展示**：展示 $\angle O_1AP + \angle PAD = \angle O_1AD = 90^\circ$；
  - **终局直角标记**：在点 $P$ 处绘制醒目的直角标记 $\angle APC = 90^\circ$，加粗高亮线段 $AP$ 与 $CP$；
  - **达成结论**：页面展现最终证明完成的金色徽标与结论框。
