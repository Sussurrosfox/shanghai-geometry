# 例 9 分步证明规划 (steps.md)

## 题目信息
- **命题**：设 $\omega$ 是一个过 $\triangle ABC$ 的顶点 $A, C$ 的圆，分别与边 $AB, BC$ 交于另一点 $D, E$。圆 $\Gamma$ 与圆 $\omega$ 外切于点 $M$，且 $\Gamma$ 同时与边 $AB, BC$ 相切。证明：$\angle AMC$ 的角平分线过 $\triangle ABC$ 的内心。
- **核心思想**：辅助圆交点构造（点 $I$）+ 弦切角与圆周角转换 + 四点共线（$C', P, Q, A'$）+ 四点共圆（$A, C, A', C'$）+ 内心判定 + 等角平分线。

---

## 色彩规范
- **基准图形（三角形 ABC 与圆 $\omega, \Gamma$）**：深灰蓝 `#334155`，切线/圆边界 `#2563eb`（蓝色）与 `#0891b2`（青色）
- **辅助圆 $\odot(APM)$ / $\odot(AIMP)$**：天青蓝 `#0284c7`
- **辅助圆 $\odot(CQM)$ / $\odot(QMIC)$**：翠绿色 `#059669`
- **共圆 $\odot(ACA'C')$**：优雅紫 `#7c3aed`
- **公切线 $MT$**：金橙色 `#d97706`
- **关键高亮线段与角平分线**：鲜红色 `#dc2626`
- **内心点 $I$ 与切点 $M$**：强对比色高亮标注

---

## 分步规划（共 7 步：Step 0 ~ Step 6）

### Step 0: ✦ 已知条件与几何构形
- **标题**：已知条件与几何图形
- **数学逻辑**：
  给定 $\triangle ABC$。圆 $\omega$ 经过顶点 $A, C$，且与边 $AB, BC$ 分别交于另一点 $D, E$。
  圆 $\Gamma$ 与边 $AB, BC$ 分别相切于点 $P, Q$。
  两圆 $\Gamma$ 与 $\omega$ 外切于点 $M$。
- **新增图元**：
  - $\triangle ABC$（边 $AB, BC, CA$）；
  - 圆 $\omega$（穿过 $A, D, M, E, C$）；
  - 圆 $\Gamma$（切 $AB$ 于 $P$，切 $BC$ 于 $Q$）；
  - 切点 $P, Q, M$ 及交点 $D, E$。
- **擦除图元**：无。

---

### Step 1: ① 引入辅助圆构造交点 $I$
- **标题**：引入辅助圆构造交点 $I$
- **数学逻辑**：
  考虑切点 $P, Q$ 与外切点 $M$。
  作 $\triangle APM$ 的外接圆 $\odot(APM)$ 与 $\triangle CQM$ 的外接圆 $\odot(CQM)$。
  两圆相交于点 $M$，设它们的另一个交点为 $I$。
  连接线段 $MI$。我们将证明 $I$ 恰为 $\triangle ABC$ 的内心，且 $MI$ 平分 $\angle AMC$。
- **新增图元**：
  - 外接圆 $\odot(APM)$（蓝色虚线）；
  - 外接圆 $\odot(CQM)$（绿色虚线）；
  - 点 $I$（深红色高亮圆点）；
  - 线段 $MI$（深蓝色虚线）。
- **擦除图元**：保持基础图形。

---

### Step 2: ② 射线 $CI, AI$ 截出点 $C', A'$
- **标题**：射线 $CI, AI$ 截出点 $C', A'$
- **数学逻辑**：
  延长 $CI$ 交圆 $APM$（即圆 $AIMP$）于异于 $I$ 的点 $C'$；
  延长 $AI$ 交圆 $CQM$（即圆 $QMIC$）于异于 $I$ 的点 $A'$。
  连接弦 $C'P, PM, QM, A'Q$ 以及切点弦 $PQ$。
- **新增图元**：
  - 射线/线段 $C-I-C'$（橙黄色半透明延伸线）；
  - 射线/线段 $A-I-A'$（紫色半透明延伸线）；
  - 点 $C'$ 与点 $A'$；
  - 弦 $C'P, PM, QM, A'Q$ 及切点弦 $PQ$。
- **擦除图元**：Step 1 中的两圆弱化为背景浅色。

---

### Step 3: ③ 弦切角与圆周角 ⇒ $C', P, Q, A'$ 共线
- **标题**：弦切角与圆周角 ⇒ $C', P, Q, A'$ 共线
- **数学逻辑**：
  在圆 $QMIC$ 中，对角互补：$\angle MIC = 180^\circ - \angle MQC$。
  在圆 $AIMP$ 中，同弧所对圆周角相等：$\angle C'PM = \angle MIC = 180^\circ - \angle MQC$。
  由圆 $\Gamma$ 与 $BC$ 切于 $Q$ 的弦切角定理知：$\angle MQC = \angle MPQ$。
  因此 $\angle C'PM = 180^\circ - \angle MPQ \implies \angle C'PM + \angle MPQ = 180^\circ$，这说明 $C', P, Q$ 三点共线！
  同理，$\angle A'QM = \angle MIA = 180^\circ - \angle MPA = 180^\circ - \angle MQP$，得 $P, Q, A'$ 三点共线。
  综合得：$C', P, Q, A'$ 四点共线！
- **新增图元**：
  - 整条共线直线 $C'-P-Q-A'$ 高亮贯穿显示（亮洋红/紫红色粗线段）；
  - 弦切角弧 $\angle MQC, \angle MPQ, \angle C'PM$ 与补角高亮标记。
- **擦除图元**：擦除 Step 2 中的杂乱连线，保持共线直线与核心角度。

---

### Step 4: ④ 公切线 $MT$ 导角 ⇒ $A, C, A', C'$ 四点共圆
- **标题**：公切线 $MT$ 导角 ⇒ $A, C, A', C'$ 四点共圆
- **数学逻辑**：
  过外切点 $M$ 作两圆 $\Gamma$ 与 $\omega$ 的内公切线 $MT$。
  由弦切角定理：
  $\angle PMT = \angle PQM$（对圆 $\Gamma$ 切于 $M$ 的内公切线与弦 $PM$），
  $\angle AMT = \angle MCA$（对圆 $\omega$ 切于 $M$ 的公切线与弦 $AM$）。
  相加得：$\angle PMA = \angle PMT + \angle AMT = \angle PQM + \angle MCA$。
  在圆 $AIMP$ 中，圆内接四边形对角互补：$180^\circ - \angle AC'A' = 180^\circ - \angle AC'P = \angle PMA$。
  而在圆 $QMIC$ 中，圆内接四边形外角等于内对角：$\angle PQM = \angle MCA'$。
  代入得：$180^\circ - \angle AC'A' = \angle MCA' + \angle MCA = \angle ACA'$，
  即 $\angle AC'A' + \angle ACA' = 180^\circ$！
  因此，四边形 $AC A'C'$ 对角互补，$A, C, A', C'$ 四点共圆！
- **新增图元**：
  - 公切线 $MT$（金色粗虚线）；
  - 辅助圆 $\odot(ACA'C')$（紫色虚线大圆）；
  - 关键角弧标记：$\angle PMT, \angle AMT, \angle PQM, \angle MCA, \angle AC'A', \angle ACA'$；
  - 四边形 $AC A'C'$ 边框高亮。
- **擦除图元**：擦除 Step 3 的补角标记。

---

### Step 5: ⑤ 圆周角传递 ⇒ 点 $I$ 为 $\triangle ABC$ 的内心
- **标题**：圆周角传递 ⇒ 点 $I$ 为 $\triangle ABC$ 的内心
- **数学逻辑**：
  由于 $A, C, A', C'$ 四点共圆：
  同弧 $CA'$ 所对圆周角相等：$\angle CC'A' = \angle CA A' = \angle CAI$。
  又在圆 $AIMP$ 中，同弧 $IP$ 所对圆周角相等：$\angle CC'A' = \angle IC'P = \angle IAP = \angle BAI$。
  由此推得：$\angle BAI = \angle CAI$！这说明射线 $AI$ 是 $\angle BAC$ 的角平分线！
  同理可证：$\angle BCI = \angle QCI = \angle AA'C' = \angle ACI$，说明射线 $CI$ 是 $\angle BCA$ 的角平分线！
  作为两条内角平分线的交点，$I$ 必为 $\triangle ABC$ 的内心！
- **新增图元**：
  - 角平分线 $AI, CI$（鲜亮蓝色与翡翠绿色高亮线段）；
  - 角平分等角标记：$\angle BAI$ 与 $\angle CAI$ 双弧标记；$\angle BCI$ 与 $\angle ACI$ 单弧标记；
  - 点 $I$ 处加上闪亮内心标签与双层光圈。
- **擦除图元**：擦除公切线 $MT$ 与共圆 $\odot(ACA'C')$ 的背景干扰。

---

### Step 6: ⑥ $MI$ 平分 $\angle AMC$ ⇒ 命题得证
- **标题**：$MI$ 平分 $\angle AMC$ ⇒ 命题得证
- **数学逻辑**：
  在圆 $AIMP$ 中，同弧 $AI$ 所对圆周角相等：$\angle AMI = \angle AC'I = \angle AC'C$；
  在圆 $QMIC$ 中，同弧 $CI$ 所对圆周角相等：$\angle CMI = \angle CA'I = \angle CA'A$；
  而在外接圆 $\odot(ACA'C')$ 中，同弦 $AC$ 所对圆周角相等：$\angle AC'C = \angle CA'A$！
  因此：$\angle AMI = \angle CMI$！
  即线段 $MI$ 严格平分 $\angle AMC$！
  既然 $I$ 已经证明是 $\triangle ABC$ 的内心，那么 $\angle AMC$ 的角平分线必然通过 $\triangle ABC$ 的内心 $I$。
  原命题完全得证！Q.E.D.
- **新增图元**：
  - 角两臂 $MA, MC$（深红细线）；
  - 角平分线 $MI$ 高亮（粗红色发光线段，带双侧对称刻度角弧）；
  - 核心等角弧 $\angle AMI = \angle CMI$；
  - 最终结论徽章展示。
- **擦除图元**：清空所有辅助圆，保留最核心的几何骨架、内心 $I$、角平分线 $MI$ 与等角关系。
