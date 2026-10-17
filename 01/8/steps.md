# 圆相交公共弦与垂直分步证明演示规划

## 命题内容
**例 7** 在 $\bigtriangleup ABC$ 中，设 $L$ 是 $BC$ 的中点，$E, F$ 分别是 $L$ 在 $AC, AB$ 上的射影。圆 $ABE$ 与圆 $ACF$ 交于另一点 $P$。求证：$AP \bot BC$。

---

## 步骤规划清单

### Step 0: 已知条件与几何构形
- **标题**：已知条件与几何构形
- **解析正文**：
  在 $\bigtriangleup ABC$ 中：
  - 点 $L$ 是底边 $BC$ 的中点（$BL = CL$）；
  - $E, F$ 分别是 $L$ 在边 $AC, AB$ 上的垂足射影（即 $LE \bot AC, LF \bot AB$）；
  - 圆 $ABE$（记为 $\odot O_1$）与圆 $ACF$（记为 $\odot O_2$）相交于顶点 $A$ 及第二交点 $P$。
  **求证**：公共弦割线 $AP \bot BC$。
- **画面图元**：
  - 绘制 $\triangle ABC$（黑线）；
  - 标注底边中点 $L$，在中点两侧 $BL, CL$ 标注等长刻度线；
  - 绘制垂足线段 $LE, LF$（灰色细线），在 $E, F$ 处标出直角符号；
  - 绘制外接圆 $\odot ABE$（蓝色半透明轮廓）与 $\odot ACF$（绿色半透明轮廓）；
  - 标注两圆交点 $A, P$ 及连线 $AP$；
  - 标注顶点与关键点：$A, B, C, L, E, F, P$。

---

### Step 1: 作辅助直径 $AM, AN$，将垂直转化为平行
- **标题**：① 作直径 $AM, AN$，将垂直转化为平行
- **解析正文**：
  分别作圆 $ABE$ 的直径 $AM$ 与圆 $ACF$ 的直径 $AN$。
  - 因为 $AM$ 是圆 $ABE$ 的直径，$P$ 在圆周上，所以 $\angle APM = 90^\circ$；
  - 同理 $AN$ 是圆 $ACF$ 的直径，$P$ 在圆周上，所以 $\angle APN = 90^\circ$；
  - 从而 $\angle APM + \angle APN = 180^\circ$，这说明 $P, M, N$ 三点共线，且 $AP \bot MN$。
  **核心目标转化**：要证 $AP \bot BC$，只需证明直线 $MN \parallel BC$。
- **画面图元**：
  - 新增圆心 $O_1, O_2$ 与两圆直径 $AM$（蓝色虚线）、$AN$（绿色虚线）；
  - 标出直径端点 $M, N$；
  - 连结直线 $MN$（穿过 $P$ 点，紫色实线/虚线）；
  - 在点 $P$ 处展示 $\angle APM = 90^\circ$ 与 $\angle APN = 90^\circ$ 的直角标记，突出 $AP \bot MN$。

---

### Step 2: 直径与射影共线：$E, L, M$ 与 $F, L, N$ 共线
- **标题**：② 利用直径与射影垂直，发现三点共线
- **解析正文**：
  探寻点 $M, N$ 的位置几何特征：
  - 在圆 $ABE$ 中，直径 $AM$ 所对圆周角 $\angle AEM = 90^\circ$，即 $ME \bot AC$；
  - 又已知 $E$ 为 $L$ 在 $AC$ 上的垂足，所以 $LE \bot AC$（$\angle AEL = 90^\circ$）；
  - 过同一点 $E$ 垂直于 $AC$ 的直线唯一，因此 **$E, L, M$ 三点共线**（$M$ 落在直线 $LE$ 延长线上）！
  - 同理，在圆 $ACF$ 中，$\angle AFN = 90^\circ$，而 $\angle AFL = 90^\circ$，因此 **$F, L, N$ 三点共线**（$N$ 落在直线 $LF$ 延长线上）。
- **画面图元**：
  - 绘制穿过 $M, L, E$ 的延长直线（橙色虚线高亮），在 $E$ 处展示共线垂直标记；
  - 绘制穿过 $N, L, F$ 的延长直线（青色虚线高亮），在 $F$ 处展示共线垂直标记；
  - 闪烁高亮共线点组 $\{E, L, M\}$ 与 $\{F, L, N\}$。

---

### Step 3: 连结 $BM, CN$，完成角度导引
- **标题**：③ 连结 $BM, CN$，完成角度导引
- **解析正文**：
  连结辅助线段 $BM$ 与 $CN$。
  - 在圆 $ABE$ 中，$AM$ 为直径，故 $\angle ABM = 90^\circ$。因此：
    $$\angle LBM = \angle ABM - \angle ABC = 90^\circ - \angle B$$
    在直角 $\triangle BFL$ 中，$\angle FLB = 90^\circ - \angle B$。由对顶角性质，$\angle CLN = \angle FLB = 90^\circ - \angle B$。
    所以：$$\angle LBM = \angle CLN$$
  - 同理，在圆 $ACF$ 中，$AN$ 为直径，$\angle ACN = 90^\circ$。因此：
    $$\angle LCN = \angle ACN - \angle ACB = 90^\circ - \angle C$$
    在直角 $\triangle CEL$ 中，$\angle ELC = 90^\circ - \angle C$。由对顶角性质，$\angle BLM = \angle ELC = 90^\circ - \angle C$。
    所以：$$\angle BLM = \angle LCN$$
- **画面图元**：
  - 连结辅助线段 $BM$ 和 $CN$（深蓝色与深绿色粗实线）；
  - 在角 $\angle LBM$ 与角 $\angle CLN$ 处标上橙色相同角弧；
  - 在角 $\angle BLM$ 与角 $\angle LCN$ 处标上红色相同角弧；
  - 直观展现两组对顶角与余角的转换关系。

---

### Step 4: 全等三角形判定 $\triangle BLM \cong \triangle CLN$
- **标题**：④ 判定 $\triangle BLM \cong \triangle CLN$，对应高相等
- **解析正文**：
  观察由底边中点衍生出的两个对称三角形 $\triangle BLM$ 与 $\triangle CLN$：
  - $\angle BLM = \angle LCN$（Step 3 已证第一组角相等）
  - $BL = CL$（已知 $L$ 是 $BC$ 的中点，公共等长边）
  - $\angle LBM = \angle CLN$（Step 3 已证第二组角相等）
  由角边角（ASA）全等判定定理：
  $$\triangle BLM \cong \triangle CLN$$
  全等三角形对应高相等：
  因此，点 $M$ 到底边 $BC$ 的垂直距离等于点 $N$ 到底边 $BC$ 的垂直距离！
- **画面图元**：
  - $\triangle BLM$ 填充半透明蓝色，边 $BL, LM, MB$ 高亮；
  - $\triangle CLN$ 填充半透明绿色，边 $CL, LN, NC$ 高亮；
  - 边 $BL, CL$ 上强化等长标记；
  - 分别作点 $M, N$ 到 $BC$ 的垂线段（红色细虚线加直角标记），显示两者等长 $h_M = h_N$。

---

### Step 5: 推得 $MN \parallel BC$，最终得出 $AP \bot BC$
- **标题**：⑤ 推得 $MN \parallel BC$，最终得出 $AP \bot BC$
- **解析正文**：
  - 因为点 $M$ 和点 $N$ 位于直线 $BC$ 的同侧，且到 $BC$ 的垂直距离相等，所以：
    $$MN \parallel BC$$
  - 回顾 Step 1 中已证的公共弦性质：直径所对圆周角互补推出 $P, M, N$ 共线且：
    $$AP \bot MN$$
  - 根据平行线的性质：一条直线垂直于两条平行线中的一条，必垂直于另一条：
    $$MN \parallel BC \quad \text{且} \quad AP \bot MN \implies AP \bot BC$$
  至此，命题得证！
- **画面图元**：
  - 直线 $MN$ 与底边 $BC$ 同时用金色/紫色粗实线高亮，并标注双平行箭头标记；
  - 直线 $AP$ 延长至与底边 $BC$ 相交，并用红色粗实线强烈高亮；
  - 在交点处绘制醒目的红色直角标记，宣告 $AP \bot BC$ 成立；
  - 整体画面达到平衡、严密、完美的证明呈现。
