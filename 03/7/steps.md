# 例 6：圆内接六边形与对称点构成的相似三角形 — 分步规划

## 题目概述
圆内接六边形 $ABCDEF$ 满足：$AB \cdot CD \cdot EF = BC \cdot DE \cdot AF$。设点 $B$ 关于直线 $AC$ 的对称点为 $B_1$，点 $D$ 关于直线 $CE$ 的对称点为 $D_1$，点 $F$ 关于直线 $EA$ 的对称点为 $F_1$。求证：$\triangle B_1D_1F_1 \sim \triangle BDF$。

---

## 分步详细规划

### Step 0: 题意理解与几何构型
- **标题**：初始构型与轴对称点定义
- **正文**：
  已知圆内接六边形 $ABCDEF$ 满足 $AB \cdot CD \cdot EF = BC \cdot DE \cdot AF$。<br>
  分别作点 $B$ 关于直线 $AC$ 的对称点 $B_1$、点 $D$ 关于直线 $CE$ 的对称点 $D_1$、点 $F$ 关于直线 $EA$ 的对称点 $F_1$。<br>
  目标：证明所形成的三角形 $\triangle B_1D_1F_1 \sim \triangle BDF$。
- **画面图元**：
  - 基础图形：六边形 $ABCDEF$ 及其外接圆 $\odot O$。
  - 对称轴：虚线 $AC, CE, EA$（构成 $\triangle ACE$）。
  - 对称点：$B_1, D_1, F_1$，连接对称线段 $BB_1, DD_1, FF_1$（细虚线）。
  - 目标三角形：弱显 $\triangle BDF$（细灰线）与 $\triangle B_1D_1F_1$（细蓝线）。

### Step 1: 角元塞瓦定理 ⇒ 主对角线共点于 P
- **标题**：角元塞瓦定理导出三对角线共点于 P
- **正文**：
  在 $\triangle ACE$ 中考察对角线 $AD, BE, CF$。由正弦定理与圆周角定理：<br>
  $\frac{\sin \angle ACF}{\sin \angle ECF} = \frac{AF}{EF},\quad \frac{\sin \angle BEC}{\sin \angle BEA} = \frac{BC}{AB},\quad \frac{\sin \angle EAD}{\sin \angle CAD} = \frac{DE}{CD}$。<br>
  三式相乘，代入题设条件 $AB \cdot CD \cdot EF = BC \cdot DE \cdot AF$ 得：<br>
  $\frac{\sin \angle ACF}{\sin \angle ECF} \cdot \frac{\sin \angle BEC}{\sin \angle BEA} \cdot \frac{\sin \angle EAD}{\sin \angle CAD} = \frac{AF \cdot BC \cdot DE}{EF \cdot AB \cdot CD} = 1$。<br>
  由<b>角元塞瓦定理</b>，主对角线 $AD, BE, CF$ 必<b>共点于一点 $P$</b>！
- **画面图元**：
  - 高亮三条主对角线 $AD, BE, CF$（金黄色/橙色高亮），相交于关键交点 $P$（加粗圆点）。
  - 突出参考三角形 $\triangle ACE$（虚线框）。

### Step 2: 轴对称变换与角度等量传递
- **标题**：轴对称与圆周角传递：$\angle PCD_1 = \angle F_1AP$
- **正文**：
  利用轴对称保持角与距离不变的性质：<br>
  $D_1$ 关于 $CE$ 对称于 $D \implies D_1C = DC,\; \angle D_1CE = \angle DCE$；<br>
  $F_1$ 关于 $EA$ 对称于 $F \implies F_1A = FA,\; \angle F_1AE = \angle FAE$。<br>
  由同弧所对圆周角相等：$\angle ECD = \angle EAD,\; \angle FCE = \angle FAE = \angle F_1AE$。<br>
  计算得：<br>
  $\angle PCD_1 = \angle D_1CE - \angle PCE = \angle ECD - \angle FCE = \angle EAD - \angle F_1AE = \angle F_1AP$！
- **画面图元**：
  - 强调对称轴 $CE$ 与 $EA$。
  - 绘制角弧高亮显示 $\angle PCD_1$ 与 $\angle F_1AP$（红色角弧），展现两角相等。
  - 连接线段 $CD_1, AF_1, CP, AP$。

### Step 3: 边比与夹角 ⇒ $\triangle D_1PC \sim \triangle F_1PA$
- **标题**：利用相交弦比值导出 $\triangle D_1PC \sim \triangle F_1PA$
- **正文**：
  在 $\odot O$ 中，相交弦 $AD$ 与 $CF$ 相交于 $P$，易知 $\triangle PCD \sim \triangle PFA$，从而 $\frac{DC}{CP} = \frac{FA}{AP}$。<br>
  代入轴对称等长条件 $D_1C = DC$ 和 $F_1A = FA$，即得：<br>
  $$\frac{D_1C}{CP} = \frac{F_1A}{AP} \iff \frac{D_1C}{F_1A} = \frac{CP}{AP}$$<br>
  结合前一步已证的夹角相等 $\angle PCD_1 = \angle F_1AP$：<br>
  由两边成比例且夹角相等，判定 <b>$\triangle D_1PC \sim \triangle F_1PA$</b>！
- **画面图元**：
  - 浅色半透明填充高亮 $\triangle D_1PC$（青色）与 $\triangle F_1PA$（橙色）。
  - 标注线段对应比例关系。

### Step 4: 相似传递与顶角对顶 ⇒ $\triangle D_1PF_1 \sim \triangle DPF$
- **标题**：相似传递导出 $\triangle D_1PF_1 \sim \triangle DPF$
- **正文**：
  由 $\triangle D_1PC \sim \triangle F_1PA$ 得：<br>
  对应边成比例 $\frac{D_1P}{F_1P} = \frac{PC}{AP}$，且对应角相等 $\angle D_1PC = \angle F_1PA$。<br>
  进而其夹角：$\angle D_1PF_1 = \angle D_1PC + \angle CPF_1 = \angle F_1PA + \angle CPF_1 = \angle CPA = \angle DPF$（对顶角）！<br>
  又圆内接相交弦有 $\triangle CPA \sim \triangle DPF \implies \frac{PC}{AP} = \frac{PD}{PF}$。<br>
  从而 $\frac{D_1P}{F_1P} = \frac{PD}{PF}$，即 $\frac{D_1P}{PD} = \frac{F_1P}{PF}$，夹角 $\angle D_1PF_1 = \angle DPF$。<br>
  由此确立相似关系：<b>$\triangle D_1PF_1 \sim \triangle CPA \sim \triangle DPF$</b>！
- **画面图元**：
  - 高亮 $\triangle D_1PF_1$ 与 $\triangle DPF$（紫色与绿色对比渲染）。
  - 突出对应顶角 $\angle D_1PF_1 = \angle DPF$。

### Step 5: 轮换对称与全图相似 ⇒ $\triangle B_1D_1F_1 \sim \triangle BDF$
- **标题**：三边比例一致，最终得出 $\triangle B_1D_1F_1 \sim \triangle BDF$
- **正文**：
  同理，对点 $B, B_1$ 实施完全相同的轮换对称分析，可得：<br>
  $\triangle B_1PF_1 \sim \triangle BPF \implies \frac{B_1F_1}{BF} = \frac{B_1P}{BP} = \frac{F_1P}{FP}$；<br>
  $\triangle B_1PD_1 \sim \triangle BPD \implies \frac{B_1D_1}{BD} = \frac{B_1P}{BP} = \frac{D_1P}{DP}$。<br>
  综合可知各对应边比值严格恒等：<br>
  $$\frac{B_1D_1}{BD} = \frac{D_1F_1}{DF} = \frac{F_1B_1}{FB} = \lambda$$<br>
  三边对应成比例，最终证得 <b>$\triangle B_1D_1F_1 \sim \triangle BDF$</b>！命题获证。
- **画面图元**：
  - 完整呈现并加粗高亮原三角形 $\triangle BDF$（翡翠绿）与新三角形 $\triangle B_1D_1F_1$（深宝蓝）。
  - 虚线连接各对应顶点的相似放射中心关系，展现出全图浑然一体的和谐几何构图。
