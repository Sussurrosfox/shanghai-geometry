# 例 7 分步证明规划与图元清单 (steps.md)

## 题目概述
设 $I$ 是 $\bigtriangleup ABC$ 的内心, $D$ 是边 $BC$ 上一点, $E$ 是 $BC$ 延长线上点且满足 $\frac{BD}{DC} = \frac{BE}{EC}$. 点 $H$ 在 $IE$ 上且 $DH \bot IE$. 证明: $\angle AHE = \angle IDE$.

---

## 步骤规划 (共 7 步, 0 ~ 6)

### 步骤 0: 已知条件与图形 (基础态)
- **标题**: ✦ 已知条件与几何构形
- **数学逻辑**:
  - 给定 $\triangle ABC$ 及其内心 $I$；
  - $D$ 为边 $BC$ 上内分点, $E$ 为 $BC$ 延长线上外分点, 满足调和分点比 $\frac{BD}{DC} = \frac{BE}{EC} = \lambda$；
  - 连结 $IE$, 过 $D$ 作 $DH \bot IE$ 于 $H$；
  - **求证**: $\angle AHE = \angle IDE$。
- **新增图元**:
  - $\triangle ABC$ (实线), 点 $A, B, C$ 及标签；
  - 内心 $I$ 及角平分线虚线示意；
  - 线段 $BC$ 上的点 $D$ 与延长线上的点 $E$；
  - 线段 $IE$, 垂线 $DH$, 垂足 $H$ 及直角标记 $\angle DHE = 90^\circ$；
  - 虚线标出目标角 $\angle AHE$ 与 $\angle IDE$。
- **擦除图元**: 无。
- **色彩规划**: 基础线深灰 `#334155`, 目标角高亮橙红 `#dc2626`。

---

### 步骤 1: 构造阿氏圆 $\omega$ 与外接圆交点 $P$
- **标题**: ① 构造阿波罗尼斯圆 $\omega$ 与外接圆交点 $P$
- **数学逻辑**:
  - 以线段 $DE$ 为直径作圆 $\omega$. 记 $\frac{BD}{DC} = \frac{BE}{EC} = \lambda$, 则圆 $\omega$ 是平面上到 $B, C$ 距离之比为 $\lambda$ 的点的轨迹 (阿氏圆)；
  - 因 $DH \bot IE$, 即 $\angle DHE = 90^\circ$, 故垂足 $H$ 亦落在圆 $\omega$ 上；
  - 设 $\triangle ABC$ 外接圆与阿氏圆 $\omega$ 的交点为 $P$, 则 $\frac{PB}{PC} = \lambda = \frac{DB}{DC}$, 由内角平分线定理的逆定理, $PD$ 是 $\angle BPC$ 的角平分线。
- **新增图元**:
  - $\triangle ABC$ 外接圆 $\odot(ABC)$ (蓝色虚线/细线)；
  - 阿氏圆 $\omega$ (以 $DE$ 为直径, 绿色虚线)；
  - 交点 $P$, 连结 $PB, PC, PD$, 标注角弧 $\angle BPD = \angle CPD$。
- **擦除图元**: 步骤 0 的目标角高亮。
- **色彩规划**: 外接圆 `BLUE`, 阿氏圆 `GREEN`, 平分角弧 `ORANGE`。

---

### 步骤 2: 引出外接圆弧中点 $M$ 与相似三角形 $\bigtriangleup MCN \sim \bigtriangleup MAC$
- **标题**: ② 引出弧中点 $M$ 与相似比 $MN \cdot MA = MC^2$
- **数学逻辑**:
  - 设 $M$ 为外接圆上弧 $\overset{\frown}{BC}$ (不含 $A$) 的中点. 因 $PD$ 是 $\angle BPC$ 的角平分线, 故射线 $PD$ 必过外接圆弧中点 $M$, 即 $P, D, M$ 三点共线；
  - 射线 $AM$ 为 $\angle BAC$ 的角平分线, 故 $A, I, M$ 共线, 设 $AM$ 与边 $BC$ 交于点 $N$；
  - 由圆周角定理: $\angle MCB = \frac{1}{2}\angle A = \angle MAC$. 考察 $\bigtriangleup MCN$ 与 $\bigtriangleup MAC$, 具有公共角 $\angle CMN = \angle CMA$, 故 $\bigtriangleup MCN \sim \bigtriangleup MAC$, 推得 $\frac{MN}{MC} = \frac{MC}{MA} \implies MN \cdot MA = MC^2$。
- **新增图元**:
  - 弧中点 $M$, 割线 $P-D-M$；
  - 角平分线 $A-I-N-M$, 交点 $N$；
  - 高亮 $\bigtriangleup MCN$ (半透明绿) 与 $\bigtriangleup MAC$ (半透明蓝), 连结 $MC$；
  - 标注等角 $\angle MCB = \angle MAC$。
- **擦除图元**: 步骤 1 中仅用于说明平分的 $PB, PC$ 及角弧。
- **色彩规划**: 相似三角形用浅色高亮填充, $MC$ 强调色 `PURPLE`。

---

### 步骤 3: 相似 $\bigtriangleup MCD \sim \bigtriangleup MPC$ 与鸡爪定理
- **标题**: ③ 相似推导与鸡爪定理: $MN \cdot MA = MC^2 = MD \cdot MP = MI^2$
- **数学逻辑**:
  - 由外接圆同弧圆周角, $\angle MPC = \angle MAC = \angle MCB = \angle MCD$；
  - 在 $\bigtriangleup MCD$ 与 $\bigtriangleup MPC$ 中, 公共角 $\angle CMD = \angle CMP$, 且 $\angle MCD = \angle MPC$, 故 $\bigtriangleup MCD \sim \bigtriangleup MPC$；
  - 由相似比得 $\frac{MD}{MC} = \frac{MC}{MP} \implies MD \cdot MP = MC^2$；
  - 由内心鸡爪定理, 弧中点 $M$ 到内心及端点等距: $MC = MI = MB$, 故 $MC^2 = MI^2$；
  - 从而导出关键等积关系: $MN \cdot MA = MD \cdot MP = MI^2$。
- **新增图元**:
  - 高亮 $\bigtriangleup MCD$ 与 $\bigtriangleup MPC$；
  - 连结 $MI, MC$, 标注等长刻度线 $MC = MI$；
  - 标注等角 $\angle MCD = \angle MPC$。
- **擦除图元**: 步骤 2 的 $\bigtriangleup MCN$ 高亮。
- **色彩规划**: 鸡爪定理线段 `RED`, 相似三角形填充 `ORANGE` / `BLUE`。

---

### 步骤 4: 四点共圆 $A, N, D, P$ 与相似 $\bigtriangleup MDI \sim \bigtriangleup MIP$
- **标题**: ④ 四点共圆 $A, N, D, P$ 与相似比 $\bigtriangleup MDI \sim \bigtriangleup MIP$
- **数学逻辑**:
  - 由 $MN \cdot MA = MD \cdot MP$ (相交割线等积逆定理), 立即得到 $A, N, D, P$ 四点共圆；
  - 于是圆周角/外角相等: $\angle PDE = \angle PAN$；
  - 另一方面, 由 $MI^2 = MD \cdot MP \implies \frac{MD}{MI} = \frac{MI}{MP}$, 且夹角 $\angle DMI = \angle IMP$ 为公共角；
  - 故 $\bigtriangleup MDI \sim \bigtriangleup MIP$, 由此得到对应角相等: $\angle MID = \angle MPI$。
- **新增图元**:
  - 过 $A, N, D, P$ 的辅助圆 (紫色细虚线)；
  - 高亮线段 $AD, AN, PD, PN$；
  - 连结 $ID, IP$, 标注等角 $\angle PDE = \angle PAN$ 与 $\angle MID = \angle MPI$。
- **擦除图元**: 步骤 3 的相似三角形高亮与鸡爪标记。
- **色彩规划**: 四点共圆辅助圆 `PURPLE`, 对应角弧 `CYAN` / `ORANGE`。

---

### 步骤 5: 阿氏圆圆周角与导出四点共圆 $A, I, H, P$
- **标题**: ⑤ 阿氏圆圆周角传递, 导出 $A, I, H, P$ 四点共圆
- **数学逻辑**:
  - 注意到 $P, D, H, E$ 四点均在以 $DE$ 为直径的阿氏圆 $\omega$ 上；
  - 弦 $PE$ 所对圆周角相等: $\angle PHE = \angle PDE$；
  - 由步骤 4 可知 $\angle PDE = \angle PAN = \angle PAI$ (因 $A, I, N$ 共线)；
  - 故 $\angle PHE = \angle PAI$；
  - 又因 $E, H, I$ 三点共线, $\angle PHE = \angle PHI$, 故 $\angle PHI = \angle PAI$；
  - 此等角关系说明点 $A, I, H, P$ 对线段 $PI$ 同侧张角相等, 故 $A, I, H, P$ 四点共圆！
- **新增图元**:
  - 高亮阿氏圆 $\omega$ 上的圆内接四边形 $PDHE$ 与弦 $PE$；
  - 标注等角 $\angle PHE = \angle PDE$；
  - 绘制过 $A, I, H, P$ 的辅助圆 (蓝绿色细虚线)；
  - 连结 $AH, AP, IH, IP$。
- **擦除图元**: 步骤 4 的 $A, N, D, P$ 辅助圆。
- **色彩规划**: 共圆圆弧 `CYAN`, 传递等角用 `GREEN` 弧线标注。

---

### 步骤 6: 角度拆分与外角代换, 得出 $\angle AHE = \angle IDE$
- **标题**: ⑥ 倒角代换得出结论: $\angle AHE = \angle IDE$
- **数学逻辑**:
  - 由 $A, I, H, P$ 四点共圆, 有圆周角 $\angle AHI = \angle API$；
  - 拆分角度: $\angle API = \angle APD - \angle IPD$；
  - 在圆内接四边形 $ANDP$ 中, $\angle APD = \angle AND$；由 $\bigtriangleup MDI \sim \bigtriangleup MIP$ 知 $\angle IPD = \angle MID$；
  - 在 $\bigtriangleup IND$ 中, 外角 $\angle AND = \angle BDI + \angle MID$, 故 $\angle APD - \angle IPD = \angle AND - \angle MID = \angle BDI$；
  - 从而 $\angle AHI = \angle BDI$；
  - 两边取补角: $180^\circ - \angle AHI = 180^\circ - \angle BDI$, 因 $E, H, I$ 共线且 $B, D, E$ 共线, 即得 $\angle AHE = \angle IDE$！
  - **结论完全得证！**
- **新增图元**:
  - 高亮目标角 $\angle AHE$ 与 $\angle IDE$ (加粗深红弧线与高亮射线)；
  - 标注中间等角 $\angle AHI = \angle BDI$ 的等角弧线；
  - 视觉强调 $DH \bot IE$ 的垂足直角标记。
- **擦除图元**: 前几步复杂的相似填充与辅助圆, 画面恢复清爽聚焦点。
- **色彩规划**: 最终结论角双色加粗红 `#dc2626`, 辅助分析角 `#2563eb`。
