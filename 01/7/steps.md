# 凸六边形全等与正三角形分步证明演示规划

## 命题内容
**例 6** 在凸六边形 $ABCDEF$ 中，$AB = CD = EF$，$BC = DE = FA$。证明：若 $\angle FAB + \angle ABC = \angle FAB + \angle EFA = 240^\circ$，则 $\angle FAB + \angle CDE = 240^\circ$。

---

## 步骤规划清单

### Step 0: 已知条件与凸六边形
- **标题**：已知条件与凸六边形
- **解析正文**：
  在凸六边形 $ABCDEF$ 中，已知：
  - 第一组对边相等：$AB = CD = EF$（标记蓝色双刻度线）；
  - 第二组对边相等：$BC = DE = FA$（标记橙色单刻度线）；
  - 顶角和关系：$\angle FAB + \angle ABC = \angle FAB + \angle EFA = 240^\circ$。
  求证：$\angle FAB + \angle CDE = 240^\circ$。
- **画面图元**：
  - 绘制凸六边形 $ABCDEF$ 黑色轮廓线条；
  - 边 $AB, CD, EF$ 标注双刻度线（蓝色）；
  - 边 $BC, DE, FA$ 标注单刻度线（橙色）；
  - 标注所有顶点 $A, B, C, D, E, F$。

---

### Step 1: 连接对角线并导出角相等
- **标题**：① 连接对角线并导出 $\angle ABC = \angle EFA$
- **解析正文**：
  连接对角线 $AC, CE, EA$。
  由已知条件：
  $$\angle FAB + \angle ABC = 240^\circ$$
  $$\angle FAB + \angle EFA = 240^\circ$$
  两式同时减去 $\angle FAB$，立即可得：
  $$\angle ABC = \angle EFA$$
- **画面图元**：
  - 新增虚线对角线 $AC, CE, EA$（紫色虚线）；
  - 顶点 $B$ 处角 $\angle ABC$ 绘制紫色角弧；
  - 顶点 $F$ 处角 $\angle EFA$ 绘制紫色角弧；
  - 高亮显示 $\angle ABC = \angle EFA$。

---

### Step 2: 证明 $\triangle ABC \cong \triangle EFA$
- **标题**：② 证明 $\triangle ABC \cong \triangle EFA$
- **解析正文**：
  在 $\triangle ABC$ 与 $\triangle EFA$ 中：
  - $AB = EF$（已知条件，蓝色边）
  - $\angle ABC = \angle EFA$（Step 1 已证顶角相等）
  - $BC = FA$（已知条件，橙色边）
  由边角边（SAS）全等判定公理，知：
  $$\triangle ABC \cong \triangle EFA$$
  从而得到对应边与对应角分别相等：
  $$AC = AE, \quad \angle BAC = \angle FEA$$
- **画面图元**：
  - $\triangle ABC$ 填充半透明蓝色区域，边 $AB, BC, AC$ 强化；
  - $\triangle EFA$ 填充半透明绿色区域，边 $EF, FA, EA$ 强化；
  - 角 $\angle BAC$ 与 $\angle FEA$ 标注红色角弧；
  - 对角线 $AC$ 与 $AE$ 用粗实线高亮并打上红色等长标记。

---

### Step 3: 角度代换求得 $\angle EAC = 60^\circ$
- **标题**：③ 角度代换求得 $\angle EAC = 60^\circ$
- **解析正文**：
  观察顶点 $A$ 处的内角拆分：
  $$\angle EAC = \angle FAB - \angle FAE - \angle BAC$$
  代入 Step 2 中全等三角形对应角 $\angle BAC = \angle FEA$：
  $$\angle EAC = \angle FAB - (\angle FAE + \angle FEA)$$
  在 $\triangle EFA$ 中，由三角形内角和定理：
  $$\angle FAE + \angle FEA = 180^\circ - \angle EFA$$
  因此：
  $$\angle EAC = \angle FAB - (180^\circ - \angle EFA) = (\angle FAB + \angle EFA) - 180^\circ$$
  代入已知和 $240^\circ$：
  $$\angle EAC = 240^\circ - 180^\circ = 60^\circ$$
- **画面图元**：
  - 保持对角线 $AC, AE$；
  - 在顶点 $A$ 处展示角拆分关系：大角 $\angle FAB$（浅红弧）、$\angle FAE$（绿弧）、$\angle BAC$（蓝弧）；
  - 在夹角 $\angle EAC$ 处醒目标注 $60^\circ$ 红色圆弧与数值标签；
  - 闪烁高亮等腰边 $AC$ 与 $AE$。

---

### Step 4: 判定 $\triangle ACE$ 是正三角形
- **标题**：④ 判定 $\triangle ACE$ 是正三角形
- **解析正文**：
  结合 Step 2 证得的边长关系与 Step 3 算出的夹角：
  - $AC = AE$（两边相等）
  - $\angle EAC = 60^\circ$（顶角为 $60^\circ$）
  有一个角是 $60^\circ$ 的等腰三角形必为正三角形：
  $$\triangle ACE \text{ 是正三角形}$$
  因此对角线三边全部相等：
  $$AC = CE = EA$$
- **画面图元**：
  - $\triangle ACE$ 填充半透明金黄色/淡紫色背景；
  - 三边 $AC, CE, EA$ 统一加粗高亮（绿色或深紫实线）；
  - 三条边 $AC, CE, EA$ 中心均标注醒目的三重刻度线；
  - 展现对称等边三角形的几何形态。

---

### Step 5: $\triangle ABC \cong \triangle CDE \implies$ 结论成立
- **标题**：⑤ $\triangle ABC \cong \triangle CDE \implies \angle FAB + \angle CDE = 240^\circ$
- **解析正文**：
  比较 $\triangle ABC$ 与 $\triangle CDE$ 的三组对应边：
  - $AB = CD$（已知边长条件）
  - $BC = DE$（已知边长条件）
  - $AC = CE$（Step 4 已证正三角形边长）
  由边边边（SSS）全等判定定理，知：
  $$\triangle ABC \cong \triangle CDE$$
  由此得出对应角相等：
  $$\angle ABC = \angle CDE$$
  代入已知关系式 $\angle FAB + \angle ABC = 240^\circ$，最终得出：
  $$\angle FAB + \angle CDE = \angle FAB + \angle ABC = 240^\circ$$
  原命题获证！
- **画面图元**：
  - $\triangle ABC$（浅蓝填充）与 $\triangle CDE$（浅红/珊瑚橙填充）对称高亮对比；
  - 顶角 $\angle ABC$ 与 $\angle CDE$ 标注高亮双角弧（深紫色）；
  - 突出显示整体轮廓与等式结果。
