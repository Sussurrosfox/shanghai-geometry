# 例 6 分步证明规划与图元清单 (steps.md)

## 题目概述
设 $\bigtriangleup ABC$ 的外心，内心分别为 $O, I$，点 $D, E, F$ 分别在边 $BC, CA, AB$ 上满足 $BD + BF = CA$，$CD + CE = AB$。若 $\bigtriangleup BFD$ 与 $\bigtriangleup CDE$ 的外接圆交于不同于 $D$ 的点 $P$。证明: $OP = OI$。

---

## 步骤规划 (共 7 步，0 ~ 6)

### 步骤 0: 已知条件与几何构形 (基础态)
- **标题**: ✦ 已知条件与几何构形
- **数学逻辑**:
  - 给定 $\triangle ABC$ 及其外心 $O$、内心 $I$、外接圆 $\odot(ABC)$；
  - 点 $D, E, F$ 分别在边 $BC, CA, AB$ 上，满足 $BD + BF = CA = b$，$CD + CE = AB = c$；
  - 作 $\triangle BFD$ 的外接圆 $\odot(BFD)$ 与 $\triangle CDE$ 的外接圆 $\odot(CDE)$，两圆相交于点 $D$ 和第二交点 $P$；
  - **求证**: $OP = OI$。
- **新增图元**:
  - 基础三角形 $\triangle ABC$（深色粗实线），顶点 $A, B, C$ 及标签；
  - 外心 $O$ 与外接圆 $\odot(ABC)$（淡蓝细实线）；
  - 内心 $I$；
  - 边上分点 $D, E, F$；
  - 外接圆 $\odot(BFD)$ 与 $\odot(CDE)$（细虚线/淡色实线）；
  - 焦点 $P$，连结目标线段 $OP, OI$（高亮虚线）。
- **擦除图元**: 无。
- **色彩规划**: $\triangle ABC$ 深色 `#1e293b`，外接圆淡蓝 `#3b82f6`，$\odot(BFD)$ 浅蓝 `#0284c7`，$\odot(CDE)$ 浅青 `#0d9488`，目标线段橙红 `#ea580c`。

---

### 步骤 1: 构造对称点 $I'$ 与投影，得出线段等长 $DD' = EE' = FF'$
- **标题**: ① 构造对称点 $I'$ 与边投影，导出 $DD'=EE'=FF'$
- **数学逻辑**:
  - 作内心 $I$ 关于外心 $O$ 的对称点 $I'$（即 $O$ 为线段 $II'$ 的中点）；
  - 过 $I'$ 分别向边 $BC, CA, AB$ 作垂线，垂足分别为 $D', E', F'$；
  - 考查 $I$ 与 $I'$ 在各边的正交投影：$I$ 到各边垂足为内切圆切点 $T_A, T_B, T_C$；外心 $O$ 到各边垂足为各边中点 $M_A, M_B, M_C$；
  - 因 $O$ 为 $II'$ 中点，由投影线段性质，$M_A$ 为 $T_A$ 与 $D'$ 的中点，知 $BD' = CT_A = s - c$；同理 $BF' = s - a$，$CD' = s - b$，$CE' = s - a$；
  - 从而 $BF' + BD' = (s - a) + (s - c) = b = CA$，$CD' + CE' = (s - b) + (s - a) = c = AB$；
  - 与已知条件 $BD + BF = CA$、$CD + CE = AB$ 相比较，立即导出：
    $$DD' = EE' = FF'$$
- **新增图元**:
  - 对称中心连线 $I-O-I'$，对称点 $I'$ 及其标签；
  - 垂线段 $I'D', I'E', I'F'$（红色虚线）及垂足 $D', E', F'$；
  - 直角标记 $\angle I'D'C = 90^\circ, \angle I'E'A = 90^\circ, \angle I'F'A = 90^\circ$；
  - 高亮等长线段 $DD', EE', FF'$（粗实线橙色）并添加等长双刻度标记。
- **擦除图元**: 步骤 0 的目标线段 $OP, OI$ 及两圆。
- **色彩规划**: 对称轴/垂线红色 `#dc2626`，等长线段与刻度鲜艳橙色 `#ea580c`。

---

### 步骤 2: 作 $I'A' \perp IA$，证明全等 $\triangle A'F'F \cong \triangle A'E'E$ 与四点共圆
- **标题**: ② 作 $I'A' \perp IA$，导出全等与四点共圆 $A, E, A', F$
- **数学逻辑**:
  - 连结角平分线 $IA$，过 $I'$ 作 $I'A' \bot IA$ 于点 $A'$；
  - 由 $\angle I'A'A = \angle I'F'A = \angle I'E'A = 90^\circ$，点 $A, F', A', E'$ 四点共圆（以 $AI'$ 为直径）；
  - 因 $AA'$ 是 $\angle F'AE'$ 的平分线，在圆周上平分弧 $\overset{\frown}{F'E'}$，故弦长 $A'F' = A'E'$；
  - 考查直角三角形 $\triangle A'F'F$ 与 $\triangle A'E'E$：
    $A'F' = A'E'$，且由步骤 1 知直角边 $F'F = E'E$，斜边与直角边分别对应相等，因此：
    $$\bigtriangleup A'F'F \cong \bigtriangleup A'E'E$$
  - 由全等得 $\angle A'FF' = \angle A'EE'$，即四边形 $AEA'F$ 的对角互补或外角等于内对角，推得：
    $$A, E, A', F \text{ 四点共圆}$$
- **新增图元**:
  - 角平分线 $IA$，垂线 $I'A'$，垂足 $A'$ 及直角标记 $\angle I'A'A = 90^\circ$；
  - 以 $AI'$ 为直径的辅助圆 $\odot(AF'A'E')$（细紫色虚线）；
  - 全等三角形 $\triangle A'F'F$ 与 $\triangle A'E'E$（浅青色与浅黄色半透明填充）；
  - 弦 $A'F', A'E'$，四点共圆 $\odot(AEA'F)$（紫色虚线）。
- **擦除图元**: 垂线 $I'D'$ 与点 $D'$，全等无关的刻度标记。
- **色彩规划**: 辅助圆与共圆紫色 `#7c3aed`，全等三角形填充淡青 `#06b6d4` 与淡橙 `#f97316`。

---

### 步骤 3: 作 $I'B' \perp IB$，完全同理得出 $B, D, B', F$ 四点共圆
- **标题**: ③ 同理作 $I'B' \perp IB$，导出四点共圆 $B, D, B', F$
- **数学逻辑**:
  - 连结角平分线 $IB$，过 $I'$ 作 $I'B' \bot IB$ 于点 $B'$；
  - 同理，$\angle I'B'B = \angle I'F'B = \angle I'D'B = 90^\circ$，点 $B, F', B', D'$ 四点共圆（以 $BI'$ 为直径）；
  - $BB'$ 平分 $\angle F'BD'$，故 $B'F' = B'D'$；
  - 结合直角及 $F'F = D'D$，得到直角三角形全等：
    $$\bigtriangleup B'F'F \cong \bigtriangleup B'D'D$$
  - 从而对应角 $\angle B'FF' = \angle B'DD'$，立即导出：
    $$B, D, B', F \text{ 四点共圆}$$
- **新增图元**:
  - 角平分线 $IB$，垂线 $I'B'$，垂足 $B'$ 及直角标记 $\angle I'B'I = 90^\circ$；
  - 全等三角形 $\triangle B'F'F$ 与 $\triangle B'D'D$（浅绿色半透明填充）；
  - 四点共圆 $\odot(BDB'F)$（绿色细虚线）；
  - 点 $B'$ 及标签。
- **擦除图元**: 步骤 2 的 $\triangle A'F'F$ 与 $\triangle A'E'E$ 填充面。
- **色彩规划**: $B$ 端共圆与辅助线采用翡翠绿 `#059669`。

---

### 步骤 4: Miquel 构型与外接圆相交定理，传递得出共圆
- **标题**: ④ Miquel 点 $P$ 传递导出 $A, F, A', P$ 与 $B, F, B', P$ 共圆
- **数学逻辑**:
  - 回顾已知条件：$\triangle BFD$ 与 $\triangle CDE$ 的外接圆交于点 $P$；
  - 由著名的 Miquel 定理：三角形三边分点构成的三圆必共点，故 $\triangle AEF$ 的外接圆 $\odot(AEF)$ 亦必过点 $P$；
  - 且由同弧圆周角性质，Miquel 点满足著名的等角定理：
    $$\angle PFA = \angle PDB = \angle PEC$$
  - 从而 $A, F, P, E$ 四点共圆（即 $P$ 在 $\odot(AEF)$ 上）；
  - 结合步骤 2 证明的 $A, E, A', F$ 四点共圆，可知点 $P, A', A, E, F$ 五点同在圆 $\odot(AFE)$ 上，故：
    $$A, F, A', P \text{ 四点共圆}$$
  - 同理，结合步骤 3 的 $B, D, B', F$ 共圆与 $B, F, P, D$ 共圆，可知 $B, D, F, B', P$ 同圆，故：
    $$B, F, B', P \text{ 四点共圆}$$
- **新增图元**:
  - 重新展现三外接圆 $\odot(BFD), \odot(CDE), \odot(AEF)$（细虚线）；
  - 高亮 Miquel 点 $P$；
  - 共圆 $\odot(AFA'P)$ 与 $\odot(BFB'P)$；
  - 标出等角弧 $\angle PFA = \angle PDB = \angle PEC$。
- **擦除图元**: 步骤 3 的全等三角形填充及垂线细节。
- **色彩规划**: Miquel 圆浅蓝/紫罗兰，交点 $P$ 鲜艳玫瑰红 `#e11d48`。

---

### 步骤 5: 圆周角对角互补，证明 $P, B', I, A'$ 四点共圆
- **标题**: ⑤ 对角互补，导出 $P, B', I, A'$ 四点共圆
- **数学逻辑**:
  - 在圆 $\odot(BFB'P)$ 中，由同弧圆周角性质：$\angle PB'B = \angle PFB$；
  - 在圆 $\odot(AFA'P)$ 中，由同弧圆周角性质：$\angle PA'A = \angle PFA$；
  - 注意到 $B, F, A$ 在同一直线上（三角形的边 $AB$），因此：
    $$\angle PFB + \angle PFA = 180^\circ \text{（邻补角）}$$
  - 又因 $A'$ 在直线 $IA$ 上（$A, A', I$ 共线），$B'$ 在直线 $IB$ 上（$B, B', I$ 共线），故：
    $$\angle PB'I + \angle PA'I = \angle PB'B + \angle PA'A = 180^\circ$$
  - 在四边形 $PA'IB'$ 中，对角 $\angle PB'I$ 与 $\angle PA'I$ 互补，由此证明：
    $$P, B', I, A' \text{ 四点共圆}$$
- **新增图元**:
  - 连结四边形边 $PB', B'I, IA', A'P$（高亮实线）；
  - 标出圆周角 $\angle PB'B$ 与 $\angle PFB$（相同颜色角弧）；
  - 标出圆周角 $\angle PA'A$ 与 $\angle PFA$（相同颜色角弧）；
  - 连结 $PF$，展示在边 $AB$ 上的两互补角。
- **擦除图元**: 冗余的外接圆 $\odot(CDE), \odot(BFD)$。
- **色彩规划**: 互补角对分别采用青色 `#0891b2` 与金黄色 `#d97706`，四边形线段用深靛蓝 `#1d4ed8`。

---

### 步骤 6: 以 $II'$ 为直径的圆收官，得出 $OP = OI$
- **标题**: ⑥ $II'$ 直径圆覆盖点 $P$，得出最终结论 $OP = OI$
- **数学逻辑**:
  - 观察点 $A'$ 与 $B'$ 的构造定义：
    $I'A' \bot IA \implies \angle I'A'I = 90^\circ$；
    $I'B' \bot IB \implies \angle I'B'I = 90^\circ$；
  - 这表明：点 $A'$ 和 $B'$ 均在以线段 $II'$ 为直径的圆上；
  - 由步骤 5 知，点 $P, B', I, A'$ 四点共圆，该外接圆必与过 $A', B', I$ 的以 $II'$ 为直径的圆重合！
  - 因此：**点 $P$ 必落在以线段 $II'$ 为直径的圆上**；
  - 又因 $O$ 是线段 $II'$ 的中点，该直径圆的圆心恰好就是外心 $O$，其半径为 $\frac{1}{2}II' = OI$；
  - 既然 $P$ 在以 $O$ 为圆心、$OI$ 为半径的圆上，立即得出：
    $$OP = OI$$
  - 全题得证！
- **新增图元**:
  - 以 $O$ 为圆心、$OI$ 为半径的完整圆（以 $II'$ 为直径的圆 $\odot(II')$，鲜明紫红细实线）；
  - 直径 $I-O-I'$；
  - 最终目标线段 $OP$ 与 $OI$（加粗红色高亮实线，带等长双刻度标记）；
  - 庆祝高亮与结论印章。
- **擦除图元**: 过渡性的辅助圆周角弧。
- **色彩规划**: 最终圆与目标线段鲜艳红色 `#dc2626`，刻度标记 `#b91c1c`。
